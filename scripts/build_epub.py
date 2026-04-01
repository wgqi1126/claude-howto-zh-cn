#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["ebooklib", "markdown", "beautifulsoup4", "httpx", "pillow", "tenacity"]
# ///
"""
根据 Claude How-To 的 Markdown 文件构建 EPUB。

用法：
    在仓库根目录执行：
        ./scripts/build_epub.py

    或使用 Python/uv 直接运行：
        uv run scripts/build_epub.py
        python scripts/build_epub.py

    命令行选项：
        --root, -r      包含 Markdown 的根目录（默认：仓库根目录）
        --output, -o    输出的 EPUB 文件路径（默认：<root>/claude-howto-guide.epub）
        --verbose, -v   启用详细日志
        --timeout       API 请求超时（秒，默认：30）
        --max-concurrent 最大并发 API 请求数（默认：10）

    本脚本使用内联脚本依赖（PEP 723），uv 会在隔离环境中自动安装所需包。

输出：
    在仓库根目录生成 `claude-howto-guide.epub`。

功能：
    - 按目录结构组织章节（01-slash-commands 等）
    - 通过 Kroki.io API 将 Mermaid 图表渲染为 PNG（异步并发）
    - 根据项目 Logo 生成封面图
    - 将 Markdown 内部链接转换为 EPUB 章节引用
    - 对 SVG 图片使用带样式的占位符替换
    - 严格模式：任一图表无法渲染则失败

依赖：
    - uv（推荐）或已安装依赖的 Python 3.10+
    - 渲染 Mermaid 需要网络连接
    - 仓库内需有 Markdown 文件与 claude-howto-logo.png
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import html
import logging
import os
import re
import sys
import zlib
from dataclasses import dataclass, field
from io import BytesIO
from pathlib import Path

import httpx
import markdown
from bs4 import BeautifulSoup
from ebooklib import epub
from PIL import Image, ImageDraw, ImageFont
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

# =============================================================================
# 自定义异常
# =============================================================================


class EPUBBuildError(Exception):
    """EPUB 构建错误的基类。"""

    pass


class MermaidRenderError(EPUBBuildError):
    """渲染 Mermaid 图表时出错。"""

    pass


class ValidationError(EPUBBuildError):
    """校验输入或输出时出错。"""

    pass


class CoverGenerationError(EPUBBuildError):
    """生成封面图时出错。"""

    pass


# =============================================================================
# 配置与状态
# =============================================================================


@dataclass
class EPUBConfig:
    """EPUB 生成配置。"""

    # 路径
    root_path: Path
    output_path: Path
    logo_path: Path | None = None

    # EPUB 元数据
    identifier: str = "claude-howto-guide"
    title: str = "Claude Code How-To Guide"
    language: str = "en"
    author: str = "Claude Code Community"

    # 封面设置
    cover_width: int = 600
    cover_height: int = 900
    cover_bg_color: tuple[int, int, int] = (26, 26, 46)
    cover_title_color: tuple[int, int, int] = (78, 205, 196)
    cover_subtitle_color: tuple[int, int, int] = (168, 178, 209)

    # 网络设置
    kroki_base_url: str = "https://kroki.io"
    request_timeout: float = 30.0
    max_retries: int = 3
    max_concurrent_requests: int = 10

    # 字体路径（因平台而异）
    title_font_paths: list[str] = field(
        default_factory=lambda: [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux
            "C:\\Windows\\Fonts\\arialbd.ttf",  # Windows
        ]
    )
    subtitle_font_paths: list[str] = field(
        default_factory=lambda: [
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # Linux
            "C:\\Windows\\Fonts\\arial.ttf",  # Windows
        ]
    )


@dataclass
class BuildState:
    """构建过程的可变状态。"""

    mermaid_cache: dict[str, tuple[bytes, str]] = field(default_factory=dict)
    mermaid_counter: int = 0
    mermaid_added_to_book: set[str] = field(default_factory=set)
    path_to_chapter: dict[str, str] = field(default_factory=dict)

    def reset(self) -> None:
        """重置状态，用于全新构建。"""
        self.mermaid_cache.clear()
        self.mermaid_counter = 0
        self.mermaid_added_to_book.clear()
        self.path_to_chapter.clear()


@dataclass
class ChapterInfo:
    """章节处理用信息。"""

    file_path: Path
    display_name: str
    file_title: str
    chapter_filename: str
    is_folder_overview: bool = False
    folder_name: str | None = None


# =============================================================================
# 日志配置
# =============================================================================


def setup_logging(verbose: bool = False) -> logging.Logger:
    """为构建过程配置日志。"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    return logging.getLogger("epub_builder")


# =============================================================================
# 输入校验
# =============================================================================


def validate_inputs(config: EPUBConfig, logger: logging.Logger) -> None:
    """在开始构建前校验所有输入。"""
    errors = []

    # 检查根路径是否存在
    if not config.root_path.exists():
        errors.append(f"Root path does not exist: {config.root_path}")
    elif not config.root_path.is_dir():
        errors.append(f"Root path is not a directory: {config.root_path}")

    # 检查输出路径是否可写
    output_dir = config.output_path.parent
    if not output_dir.exists():
        errors.append(f"Output directory does not exist: {output_dir}")
    elif not os.access(output_dir, os.W_OK):
        errors.append(f"Output directory is not writable: {output_dir}")

    # 若指定了 Logo 则检查
    logo_path = config.logo_path or (config.root_path / "claude-howto-logo.png")
    if not logo_path.exists():
        logger.warning(
            f"未找到 Logo 文件：{logo_path}。将生成不含 Logo 的封面。"
        )

    # 至少应存在若干 Markdown 文件
    md_files = list(config.root_path.glob("**/*.md"))
    if not md_files:
        errors.append(f"No markdown files found in {config.root_path}")

    if errors:
        for error in errors:
            logger.error(error)
        raise ValidationError("\n".join(errors))


# =============================================================================
# Mermaid 渲染（异步 + 重试）
# =============================================================================


def sanitize_mermaid(mermaid_code: str) -> str:
    """清理 mermaid 代码，减轻 Markdown 解析问题。

    Mermaid 在节点内的 markdown 特性会把编号列表（如 "1. Item"）
    误解析；此处对句点转义以避免该问题。
    """
    # 对方括号内的编号列表转义：[1. Text] -> [1\. Text]
    sanitized = re.sub(r'\[(["\']?)(\d+)\.(\s)', r"[\1\2\\.\3", mermaid_code)
    return sanitized


class MermaidRenderer:
    """通过 Kroki.io API 异步渲染 Mermaid 图表。"""

    def __init__(
        self, config: EPUBConfig, state: BuildState, logger: logging.Logger
    ) -> None:
        self.config = config
        self.state = state
        self.logger = logger
        self._semaphore: asyncio.Semaphore | None = None

    async def _fetch_single(
        self, client: httpx.AsyncClient, mermaid_code: str, index: int
    ) -> tuple[str, tuple[bytes, str]]:
        """获取单个 Mermaid 图表（含重试逻辑）。"""
        cache_key = mermaid_code.strip()

        # 先查缓存
        if cache_key in self.state.mermaid_cache:
            self.logger.debug(f"图表 {index} 缓存命中")
            return cache_key, self.state.mermaid_cache[cache_key]

        # 用信号量限流
        assert self._semaphore is not None
        async with self._semaphore:
            result = await self._fetch_with_retry(client, mermaid_code, index)
            if result is None:
                raise MermaidRenderError(
                    f"在 {self.config.max_retries} 次尝试后仍无法渲染 Mermaid 图表 {index}"
                )
            return cache_key, result

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type((httpx.TimeoutException, httpx.NetworkError)),
        reraise=True,
    )
    async def _fetch_with_retry(
        self, client: httpx.AsyncClient, mermaid_code: str, index: int
    ) -> tuple[bytes, str] | None:
        """带重试逻辑获取图表。"""
        try:
            compressed = zlib.compress(mermaid_code.encode("utf-8"), level=9)
            encoded = base64.urlsafe_b64encode(compressed).decode("ascii")
            url = f"{self.config.kroki_base_url}/mermaid/png/{encoded}"

            self.logger.debug(f"正在获取图表 {index}...")
            response = await client.get(url, timeout=self.config.request_timeout)

            if response.status_code == 200:
                self.state.mermaid_counter += 1
                img_name = f"mermaid_{self.state.mermaid_counter}.png"
                result = (response.content, img_name)
                cache_key = mermaid_code.strip()
                self.state.mermaid_cache[cache_key] = result
                self.logger.info(f"已渲染图表 {index} -> {img_name}")
                return result
            else:
                self.logger.warning(
                    f"Kroki API 对图表 {index} 返回状态码 {response.status_code}"
                )
                raise MermaidRenderError(
                    f"Kroki API 对图表 {index} 返回状态码 {response.status_code}"
                )

        except httpx.TimeoutException:
            self.logger.warning(f"获取图表 {index} 超时，将重试...")
            raise
        except httpx.NetworkError as e:
            self.logger.warning(
                f"图表 {index} 网络错误：{e}，将重试..."
            )
            raise

    async def render_all(
        self, diagrams: list[tuple[int, str]]
    ) -> dict[str, tuple[bytes, str]]:
        """并发渲染全部 Mermaid 图表。"""
        self._semaphore = asyncio.Semaphore(self.config.max_concurrent_requests)
        results: dict[str, tuple[bytes, str]] = {}

        async with httpx.AsyncClient(
            follow_redirects=True,
            limits=httpx.Limits(max_connections=self.config.max_concurrent_requests),
            timeout=httpx.Timeout(self.config.request_timeout),
        ) as client:
            tasks = [
                self._fetch_single(client, sanitize_mermaid(code), idx)
                for idx, code in diagrams
            ]

            self.logger.info(f"正在并发获取 {len(tasks)} 个 Mermaid 图表...")

            # 使用 gather 且 return_exceptions=False，保持严格模式
            completed = await asyncio.gather(*tasks)

            for cache_key, data in completed:
                results[cache_key] = data

        success_count = len(results)
        self.logger.info(
            f"成功渲染 {success_count}/{len(diagrams)} 个图表"
        )
        return results


def extract_all_mermaid_blocks(
    md_files: list[tuple[Path, str]], logger: logging.Logger
) -> list[tuple[int, str]]:
    """从 Markdown 文件中提取全部不重复的 Mermaid 代码块。"""
    pattern = r"```mermaid\n(.*?)```"
    seen: set[str] = set()
    diagrams: list[tuple[int, str]] = []
    counter = 0

    for file_path, _ in md_files:
        try:
            content = file_path.read_text(encoding="utf-8")
            for match in re.finditer(pattern, content, flags=re.DOTALL):
                code = match.group(1).strip()
                if code not in seen:
                    seen.add(code)
                    counter += 1
                    diagrams.append((counter, code))
        except UnicodeDecodeError as e:
            logger.warning(f"无法读取 {file_path}：{e}")

    logger.info(f"共发现 {len(diagrams)} 个不重复的 Mermaid 图表")
    return diagrams


# =============================================================================
# 章节收集（单次遍历）
# =============================================================================


def get_chapter_order() -> list[tuple[str, str]]:
    """按目录结构定义章节顺序。"""
    return [
        ("README.md", "Introduction"),
        ("LEARNING-ROADMAP.md", "Learning Roadmap"),
        ("QUICK_REFERENCE.md", "Quick Reference"),
        ("claude_concepts_guide.md", "Claude Concepts Guide"),
        ("01-slash-commands", "Slash Commands"),
        ("02-memory", "Memory"),
        ("03-skills", "Skills"),
        ("04-subagents", "Subagents"),
        ("05-mcp", "MCP Protocol"),
        ("06-hooks", "Hooks"),
        ("07-plugins", "Plugins"),
        ("08-checkpoints", "Checkpoints"),
        ("09-advanced-features", "Advanced Features"),
        ("resources.md", "Resources"),
    ]


def collect_folder_files(folder_path: Path) -> list[tuple[Path, str]]:
    """收集文件夹内全部 Markdown，README 优先。"""
    files: list[tuple[Path, str]] = []

    # 若存在则先加入 README
    readme = folder_path / "README.md"
    if readme.exists():
        files.append((readme, "概述"))

    # 其余 .md 文件
    for md_file in sorted(folder_path.glob("*.md")):
        if md_file.name != "README.md":
            title = md_file.stem.replace("-", " ").replace("_", " ").title()
            files.append((md_file, title))

    # 递归子目录
    for subfolder in sorted(folder_path.iterdir()):
        if subfolder.is_dir() and not subfolder.name.startswith("."):
            subfiles = collect_folder_files(subfolder)
            for sf, st in subfiles:
                rel_path = sf.relative_to(folder_path)
                if len(rel_path.parts) > 1:
                    prefix = (
                        rel_path.parts[0].replace("-", " ").replace("_", " ").title()
                    )
                    files.append((sf, f"{prefix}: {st}"))
                else:
                    files.append((sf, st))

    return files


class ChapterCollector:
    """单次遍历收集并整理章节信息。"""

    def __init__(self, root_path: Path, state: BuildState) -> None:
        self.root_path = root_path
        self.state = state

    def collect_all_chapters(
        self, chapter_order: list[tuple[str, str]]
    ) -> list[ChapterInfo]:
        """一次遍历收集全部章节并建立路径映射。"""
        chapters: list[ChapterInfo] = []
        chapter_num = 0

        for item, display_name in chapter_order:
            item_path = self.root_path / item

            if item_path.is_file() and item_path.suffix == ".md":
                chapter_num += 1
                chapter_filename = f"chap_{chapter_num:02d}.xhtml"
                self.state.path_to_chapter[item] = chapter_filename

                chapters.append(
                    ChapterInfo(
                        file_path=item_path,
                        display_name=display_name,
                        file_title=display_name,
                        chapter_filename=chapter_filename,
                    )
                )

            elif item_path.is_dir():
                folder_chapters = self._collect_folder(
                    item_path, item, display_name, chapter_num
                )
                if folder_chapters:
                    chapter_num += 1
                    chapters.extend(folder_chapters)

        return chapters

    def _collect_folder(
        self, folder_path: Path, item: str, display_name: str, base_chapter_num: int
    ) -> list[ChapterInfo]:
        """从目录收集章节。"""
        folder_files = collect_folder_files(folder_path)
        if not folder_files:
            return []

        chapter_num = base_chapter_num + 1
        chapters: list[ChapterInfo] = []

        # 映射目录本身
        first_filename = f"chap_{chapter_num:02d}_00.xhtml"
        self.state.path_to_chapter[item] = first_filename
        self.state.path_to_chapter[item.rstrip("/")] = first_filename

        for i, (file_path, file_title) in enumerate(folder_files):
            chapter_filename = f"chap_{chapter_num:02d}_{i:02d}.xhtml"
            rel_path = str(file_path.relative_to(self.root_path))
            self.state.path_to_chapter[rel_path] = chapter_filename

            chapters.append(
                ChapterInfo(
                    file_path=file_path,
                    display_name=display_name if i == 0 else file_title,
                    file_title=file_title,
                    chapter_filename=chapter_filename,
                    is_folder_overview=(i == 0),
                    folder_name=display_name,
                )
            )

        return chapters


# =============================================================================
# 封面图生成
# =============================================================================


def load_font(
    font_paths: list[str], size: int, logger: logging.Logger
) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """从候选路径列表加载字体，失败则回退到默认字体。"""
    for font_path in font_paths:
        try:
            font = ImageFont.truetype(font_path, size)
            logger.debug(f"已加载字体：{font_path}")
            return font
        except OSError:
            continue

    logger.warning("未找到自定义字体，使用默认字体")
    return ImageFont.load_default()


def _add_logo_to_cover(
    cover: Image.Image, logo_path: Path, config: EPUBConfig, logger: logging.Logger
) -> None:
    """将 Logo 绘制到封面上。"""
    with Image.open(logo_path) as logo:
        target_width = config.cover_width - 60
        scale_factor = target_width / logo.width
        new_height = int(logo.height * scale_factor)
        logo_scaled = logo.resize((target_width, new_height), Image.Resampling.LANCZOS)

        if logo_scaled.mode == "RGBA":
            logo_bg = Image.new("RGB", logo_scaled.size, config.cover_bg_color)
            logo_bg.paste(logo_scaled, mask=logo_scaled.split()[3])
            logo_scaled = logo_bg
        elif logo_scaled.mode != "RGB":
            logo_scaled = logo_scaled.convert("RGB")

        logo_x = (config.cover_width - logo_scaled.width) // 2
        logo_y = config.cover_height - logo_scaled.height - 80
        cover.paste(logo_scaled, (logo_x, logo_y))
        logger.debug(f"已从 {logo_path} 添加 Logo")


def _draw_text_centered(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    color: tuple[int, int, int],
    canvas_width: int,
    y_start: int,
    line_spacing: int,
) -> int:
    """绘制居中多行文本，返回最终 y 坐标。"""
    y_offset = y_start
    for line in text.split("\n"):
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (canvas_width - text_width) // 2
        draw.text((x, y_offset), line, font=font, fill=color)
        y_offset += line_spacing
    return y_offset


def create_cover_image(
    config: EPUBConfig,
    logger: logging.Logger,
    title: str = "Claude Code\nHow-To 指南",
    subtitle: str = "Claude Code 功能完整指南",
) -> bytes:
    """生成封面图，含错误处理。"""
    try:
        cover = Image.new(
            "RGB", (config.cover_width, config.cover_height), config.cover_bg_color
        )
        draw = ImageDraw.Draw(cover)

        # 字体只加载一次
        title_font = load_font(config.title_font_paths, 72, logger)
        subtitle_font = load_font(config.subtitle_font_paths, 24, logger)

        # 若有 Logo 则添加
        logo_path = config.logo_path or (config.root_path / "claude-howto-logo.png")
        if logo_path.exists():
            _add_logo_to_cover(cover, logo_path, config, logger)
        else:
            logger.warning("未找到 Logo，生成纯文字封面")

        # 标题
        y_after_title = _draw_text_centered(
            draw,
            title,
            title_font,
            config.cover_title_color,
            config.cover_width,
            y_start=120,
            line_spacing=90,
        )

        # 副标题
        _draw_text_centered(
            draw,
            subtitle,
            subtitle_font,
            config.cover_subtitle_color,
            config.cover_width,
            y_start=y_after_title + 20,
            line_spacing=30,
        )

        buffer = BytesIO()
        cover.save(buffer, format="PNG", optimize=True)
        logger.info("封面图生成成功")
        return buffer.getvalue()

    except Exception as e:
        logger.error(f"创建封面图失败：{e}")
        raise CoverGenerationError(f"封面生成失败：{e}") from e


# =============================================================================
# HTML 生成
# =============================================================================


def create_chapter_html(
    display_name: str, file_title: str, html_content: str, is_overview: bool = False
) -> str:
    """生成章节 HTML，并做适当转义。"""
    safe_display = html.escape(display_name)
    safe_title = html.escape(file_title)

    if is_overview:
        return f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
    <meta charset="utf-8"/>
    <title>{safe_display}</title>
</head>
<body>
    <h1>{safe_display}</h1>
    {html_content}
</body>
</html>"""
    else:
        return f"""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en">
<head>
    <meta charset="utf-8"/>
    <title>{safe_title}</title>
</head>
<body>
    <h2>{safe_title}</h2>
    {html_content}
</body>
</html>"""


def handle_svg_image(src: str, alt: str, logger: logging.Logger) -> str:
    """用带样式的占位符处理 SVG 图片。"""
    placeholder = f"""
    <div class="svg-placeholder" style="
        border: 1px dashed #ccc;
        padding: 1em;
        text-align: center;
        background: #f9f9f9;
        border-radius: 4px;
        margin: 1em 0;
    ">
        <p><em>[SVG 图片：{html.escape(alt)}]</em></p>
        <p style="font-size: 0.8em; color: #666;">
            原始地址：{html.escape(src)}
        </p>
    </div>
    """
    logger.debug(f"已替换 SVG 图片：{src}")
    return placeholder


# =============================================================================
# Markdown 处理
# =============================================================================


def process_mermaid_blocks(
    md_content: str, book: epub.EpubBook, state: BuildState, logger: logging.Logger
) -> str:
    """查找 mermaid 代码块并替换为图片引用。"""
    pattern = r"```mermaid\n(.*?)```"

    def replace_mermaid(match: re.Match[str]) -> str:
        mermaid_code = sanitize_mermaid(match.group(1))
        cache_key = mermaid_code.strip()

        if cache_key in state.mermaid_cache:
            img_data, img_name = state.mermaid_cache[cache_key]
            # 仅在尚未加入电子书时再添加图片
            if img_name not in state.mermaid_added_to_book:
                img_item = epub.EpubItem(
                    uid=img_name.replace(".", "_"),
                    file_name=f"images/{img_name}",
                    media_type="image/png",
                    content=img_data,
                )
                book.add_item(img_item)
                state.mermaid_added_to_book.add(img_name)
            return f"\n![图表](images/{img_name})\n"
        else:
            # 严格模式下预先拉取全部图表后不应出现
            logger.error("缓存中未找到 Mermaid 图表")
            raise MermaidRenderError("缓存中未找到 Mermaid 图表")

    return re.sub(pattern, replace_mermaid, md_content, flags=re.DOTALL)


def convert_internal_links(
    html_content: str, current_file: Path, root_path: Path, state: BuildState
) -> str:
    """将 Markdown 链接转为 EPUB 内部章节链接。"""
    soup = BeautifulSoup(html_content, "html.parser")

    for link in soup.find_all("a"):
        href = link.get("href", "")
        if not href or href.startswith(("http://", "https://", "mailto:", "#")):
            continue

        # 解析路径时去掉锚点
        anchor = ""
        if "#" in href:
            href, anchor = href.split("#", 1)
            anchor = "#" + anchor

        # 从当前文件所在目录解析相对路径
        if href:
            resolved = (current_file.parent / href).resolve()
            try:
                rel_to_root = resolved.relative_to(root_path)
            except ValueError:
                # 链接指向仓库外
                continue

            # 规范化路径以便查找
            lookup_path = str(rel_to_root)

            # 尝试多种路径形式以匹配
            paths_to_try = [
                lookup_path,
                lookup_path.rstrip("/"),
                lookup_path + "/README.md"
                if not lookup_path.endswith(".md")
                else lookup_path,
            ]

            for path in paths_to_try:
                if path in state.path_to_chapter:
                    link["href"] = state.path_to_chapter[path] + anchor
                    break

    return str(soup)


def md_to_html(
    md_content: str,
    current_file: Path,
    root_path: Path,
    book: epub.EpubBook,
    state: BuildState,
    logger: logging.Logger,
) -> str:
    """将 Markdown 转为带样式的 HTML。

    处理内容：
    - Mermaid 图表（渲染为 PNG）
    - SVG 图片（替换为样式占位符）
    - 内部链接（转为 EPUB 章节引用）
    - 常规 Markdown 特性
    """
    # 先于 Markdown 转换处理 mermaid 块
    md_content = process_mermaid_blocks(md_content, book, state, logger)

    # Markdown -> HTML
    html_content = markdown.markdown(
        md_content,
        extensions=[
            "tables",
            "fenced_code",
            "codehilite",
            "toc",
        ],
    )

    # 清理 SVG 引用（EPUB 中无法直接使用）
    soup = BeautifulSoup(html_content, "html.parser")
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if src.endswith(".svg"):
            alt = img.get("alt", "图片")
            placeholder = handle_svg_image(src, alt, logger)
            img.replace_with(BeautifulSoup(placeholder, "html.parser"))

    html_content = str(soup)

    # 内部链接 -> EPUB 章节引用
    html_content = convert_internal_links(html_content, current_file, root_path, state)

    return html_content


# =============================================================================
# EPUB 生成
# =============================================================================


def create_stylesheet() -> epub.EpubItem:
    """创建 EPUB 样式表。"""
    style = """
    body { font-family: Georgia, serif; line-height: 1.6; padding: 1em; }
    h1 { color: #333; border-bottom: 2px solid #e67e22; padding-bottom: 0.3em; }
    h2 { color: #444; margin-top: 1.5em; }
    h3 { color: #555; }
    code { background: #f4f4f4; padding: 0.2em 0.4em; border-radius: 3px; font-family: monospace; }
    pre { background: #f4f4f4; padding: 1em; overflow-x: auto; border-radius: 5px; }
    pre code { background: none; padding: 0; }
    table { border-collapse: collapse; width: 100%; margin: 1em 0; }
    th, td { border: 1px solid #ddd; padding: 0.5em; text-align: left; }
    th { background: #f4f4f4; }
    blockquote { border-left: 4px solid #e67e22; margin: 1em 0; padding-left: 1em; color: #666; }
    a { color: #e67e22; }
    img { max-width: 100%; height: auto; display: block; margin: 1em auto; }
    .diagram { text-align: center; margin: 1.5em 0; }
    .svg-placeholder { border: 1px dashed #ccc; padding: 1em; text-align: center; background: #f9f9f9; border-radius: 4px; margin: 1em 0; }
    """
    return epub.EpubItem(
        uid="style_nav",
        file_name="style/nav.css",
        media_type="text/css",
        content=style,
    )


async def build_epub_async(
    config: EPUBConfig,
    logger: logging.Logger,
    state: BuildState | None = None,
) -> Path:
    """异步构建 EPUB，并并发获取图表。"""
    state = state or BuildState()
    state.reset()  # 确保从干净状态开始

    # 校验输入
    validate_inputs(config, logger)

    # 初始化电子书
    book = epub.EpubBook()
    book.set_identifier(config.identifier)
    book.set_title(config.title)
    book.set_language(config.language)
    book.add_author(config.author)

    # 封面
    logger.info("正在生成封面图...")
    cover_data = create_cover_image(config, logger)
    book.set_cover("cover.png", cover_data)

    # CSS
    nav_css = create_stylesheet()
    book.add_item(nav_css)

    # 单次遍历收集章节
    logger.info("正在收集章节...")
    collector = ChapterCollector(config.root_path, state)
    chapter_infos = collector.collect_all_chapters(get_chapter_order())

    # 提取并预取全部 Mermaid 图表
    logger.info("正在提取 Mermaid 图表...")
    md_files = [(ch.file_path, ch.file_title) for ch in chapter_infos]
    all_diagrams = extract_all_mermaid_blocks(md_files, logger)

    if all_diagrams:
        renderer = MermaidRenderer(config, state, logger)
        await renderer.render_all(all_diagrams)

    # 处理各章
    logger.info("正在处理章节...")
    chapters: list[epub.EpubHtml] = []
    toc: list[epub.EpubHtml | tuple[epub.Section, list[epub.EpubHtml]]] = []

    current_folder: str | None = None
    current_folder_chapters: list[epub.EpubHtml] = []

    for chapter_info in chapter_infos:
        try:
            content = chapter_info.file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError as e:
            logger.error(f"无法读取 {chapter_info.file_path}：{e}")
            raise ValidationError(
                f"Failed to read {chapter_info.file_path}: {e}"
            ) from e

        logger.debug(
            f"处理中：{chapter_info.file_path.relative_to(config.root_path)}"
        )
        html_content = md_to_html(
            content, chapter_info.file_path, config.root_path, book, state, logger
        )

        chapter = epub.EpubHtml(
            title=chapter_info.file_title,
            file_name=chapter_info.chapter_filename,
            lang="en",
        )

        chapter.content = create_chapter_html(
            chapter_info.display_name,
            chapter_info.file_title,
            html_content,
            is_overview=chapter_info.is_folder_overview
            or chapter_info.folder_name is None,
        )
        chapter.add_item(nav_css)
        book.add_item(chapter)
        chapters.append(chapter)

        # 构建目录结构
        if chapter_info.folder_name is None:
            # 单文件章节
            if current_folder is not None:
                # 结束上一目录分组
                toc.append(
                    (epub.Section(current_folder), current_folder_chapters.copy())
                )
                current_folder_chapters.clear()
                current_folder = None
            toc.append(chapter)
        else:
            # 目录下的章节
            if current_folder != chapter_info.folder_name:
                if current_folder is not None:
                    # 结束上一目录分组
                    toc.append(
                        (epub.Section(current_folder), current_folder_chapters.copy())
                    )
                    current_folder_chapters.clear()
                current_folder = chapter_info.folder_name
            current_folder_chapters.append(chapter)

    # 处理最后一个目录分组
    if current_folder is not None and current_folder_chapters:
        toc.append((epub.Section(current_folder), current_folder_chapters))

    # 设置目录
    book.toc = toc

    # 导航文件
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # spine
    book.spine = ["nav"] + chapters

    # 写入 EPUB
    logger.info(f"正在写入 EPUB：{config.output_path}...")
    epub.write_epub(str(config.output_path), book, {})

    logger.info(f"EPUB 已成功创建：{config.output_path}")
    return config.output_path


def create_epub(root_path: Path, output_path: Path, verbose: bool = False) -> Path:
    """同步封装，保持向后兼容。"""
    logger = setup_logging(verbose)
    config = EPUBConfig(root_path=root_path, output_path=output_path)
    return asyncio.run(build_epub_async(config, logger))


# =============================================================================
# 命令行
# =============================================================================


def main() -> int:
    """命令行入口与参数解析。"""
    parser = argparse.ArgumentParser(
        description="根据 Claude How-To 的 Markdown 文件构建 EPUB。"
    )
    parser.add_argument(
        "--root",
        "-r",
        type=Path,
        default=None,
        help="包含 Markdown 的根目录（默认：仓库根目录）",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="输出的 EPUB 文件路径（默认：<root>/claude-howto-guide.epub）",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="启用详细日志"
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="API 请求超时（秒）（默认：30）",
    )
    parser.add_argument(
        "--max-concurrent",
        type=int,
        default=10,
        help="最大并发 API 请求数（默认：10）",
    )

    args = parser.parse_args()

    # 确定根路径
    root = args.root
    if root is None:
        # 默认为 scripts 的上一级（仓库根目录）
        root = Path(__file__).parent.parent

    root = root.resolve()
    output = args.output or (root / "claude-howto-guide.epub")
    output = output.resolve()

    logger = setup_logging(args.verbose)
    config = EPUBConfig(
        root_path=root,
        output_path=output,
        request_timeout=args.timeout,
        max_concurrent_requests=args.max_concurrent,
    )

    try:
        result = asyncio.run(build_epub_async(config, logger))
        print(f"已成功创建：{result}")
        return 0
    except EPUBBuildError as e:
        logger.error(f"构建失败：{e}")
        return 1
    except KeyboardInterrupt:
        logger.warning("用户中断了构建")
        return 130


if __name__ == "__main__":
    sys.exit(main())
