"""EPUB 构建器测试的 Pytest 配置与共享 fixtures。"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import pytest

# 将父目录加入路径以便导入
sys.path.insert(0, str(Path(__file__).parent.parent))

from build_epub import BuildState, EPUBConfig, setup_logging


@pytest.fixture
def tmp_project(tmp_path: Path) -> Path:
    """创建用于测试的最小项目结构。"""
    # 创建根目录 Markdown 文件
    readme = tmp_path / "README.md"
    readme.write_text("# 测试项目\n\n这是测试内容。")

    # 创建章节目录
    chapter_dir = tmp_path / "01-test-chapter"
    chapter_dir.mkdir()
    (chapter_dir / "README.md").write_text("# 章节概览\n\n概览正文。")
    (chapter_dir / "section.md").write_text("# 小节\n\n小节正文。")

    # 使用 PIL 创建有效的 PNG logo
    from PIL import Image as PILImage

    logo_path = tmp_path / "claude-howto-logo.png"
    img = PILImage.new("RGB", (100, 100), color=(26, 26, 46))
    img.save(logo_path, "PNG")

    return tmp_path


@pytest.fixture
def config(tmp_project: Path) -> EPUBConfig:
    """创建测试用配置。"""
    return EPUBConfig(
        root_path=tmp_project,
        output_path=tmp_project / "test.epub",
    )


@pytest.fixture
def state() -> BuildState:
    """创建全新的构建状态。"""
    return BuildState()


@pytest.fixture
def logger() -> logging.Logger:
    """创建测试用 logger。"""
    return setup_logging(verbose=False)
