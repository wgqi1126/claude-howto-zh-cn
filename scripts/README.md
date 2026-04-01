<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# EPUB 构建脚本

根据 Claude How-To 的 Markdown 文件构建 EPUB 电子书。

## 功能

- 按目录结构组织章节（`01-slash-commands`、`02-memory` 等）
- 通过 Kroki.io API 将 Mermaid 图表渲染为 PNG
- 异步并发获取——并行渲染全部图表
- 根据项目 Logo 生成封面图
- 将内部 Markdown 链接转换为 EPUB 章节引用
- 严格错误模式——任一图表无法渲染即失败

## 环境要求

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- 渲染 Mermaid 图表需要联网

## 快速开始

```bash
# 最简单：由 uv 处理一切
uv run scripts/build_epub.py
```

## 开发环境

```bash
# 创建虚拟环境
uv venv

# 激活并安装依赖
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# 运行测试
pytest scripts/tests/ -v

# 运行脚本
python scripts/build_epub.py
```

## 命令行选项

```
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--timeout TIMEOUT] [--max-concurrent MAX_CONCURRENT]

options:
  -h, --help            show this help message and exit
  --root, -r ROOT       Root directory (default: repo root)
  --output, -o OUTPUT   Output path (default: claude-howto-guide.epub)
  --verbose, -v         Enable verbose logging
  --timeout TIMEOUT     API timeout in seconds (default: 30)
  --max-concurrent N    Max concurrent requests (default: 10)
```

## 示例

```bash
# 详细输出构建
uv run scripts/build_epub.py --verbose

# 自定义输出位置
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# 限制并发请求（如遇限流）
uv run scripts/build_epub.py --max-concurrent 5
```

## 输出

在仓库根目录生成 `claude-howto-guide.epub`。

EPUB 包含：
- 带项目 Logo 的封面
- 含嵌套层级的目录
- 全部 Markdown 内容转换为兼容 EPUB 的 HTML
- Mermaid 图表渲染为 PNG 图片

## 运行测试

```bash
# 使用虚拟环境
source .venv/bin/activate
pytest scripts/tests/ -v

# 或直接用 uv
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with httpx --with pillow --with tenacity \
    pytest scripts/tests/ -v
```

## 依赖

通过 PEP 723 内联脚本元数据管理：

| 包名 | 用途 |
|---------|------|
| `ebooklib` | 生成 EPUB |
| `markdown` | Markdown 转 HTML |
| `beautifulsoup4` | 解析 HTML |
| `httpx` | 异步 HTTP 客户端 |
| `pillow` | 封面图生成 |
| `tenacity` | 重试逻辑 |

## 故障排除

**构建因网络错误失败**：检查网络连接与 Kroki.io 可用性。可尝试 `--timeout 60`。

**限流**：使用 `--max-concurrent 3` 降低并发请求数。

**缺少 Logo**：若找不到 `claude-howto-logo.png`，脚本会生成仅含文字的封面。
