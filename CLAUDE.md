# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在此代码库中工作时提供指导。

## 项目概述

这是一个 Claude Code 功能的文档/教程项目。仓库包含 Claude Code 功能的指南、模板和示例，包括斜杠命令、skills、subagents、hooks、MCP 服务器和插件。主要内容是 markdown 文件，按编号模块组织（01-slash-commands 到 10-cli）。

**本项目是 [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto) 的中文化版本，目标是将原项目的文档和教程翻译成中文，帮助中文用户更好地学习和使用 Claude Code。**

`scripts/` 中的 Python 脚本用于 EPUB 电子书生成和测试。

## 开发命令

### Python 环境设置
```bash
# 安装 uv（快速 Python 包管理器）
brew install uv  # macOS
pip install uv   # 或通过 pip 安装

# 创建虚拟环境并安装依赖
cd scripts
uv venv
source .venv/bin/activate
uv pip install -r requirements-dev.txt
```

### 测试
```bash
# 运行所有单元测试
pytest scripts/tests/ -v

# 运行测试并生成覆盖率报告
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 运行特定测试文件
pytest scripts/tests/test_build_epub.py -v

# 运行特定测试函数
pytest scripts/tests/test_build_epub.py::test_function_name -v
```

### 代码质量
```bash
# 检查格式
ruff format --check scripts/

# 自动修复格式问题
ruff format scripts/

# 运行 linter
ruff check scripts/

# 自动修复 linter 问题
ruff check --fix scripts/
```

### 安全与类型检查
```bash
# 安全扫描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 类型检查
mypy scripts/ --ignore-missing-imports --no-implicit-optional
```

### EPUB 构建
```bash
# 构建 EPUB 电子书
uv run scripts/build_epub.py

# 详细输出模式构建
uv run scripts/build_epub.py --verbose
```

### Pre-commit Hooks
```bash
# 安装 hooks
pre-commit install

# 手动运行所有 hooks
pre-commit run --all-files
```

## 架构

### 目录结构
```
├── 01-slash-commands/     # 用户调用的快捷命令模板（.md 文件）
├── 02-memory/             # CLAUDE.md 模板，用于持久化上下文
├── 03-skills/             # 自动调用的能力（SKILL.md + scripts/ + templates/）
├── 04-subagents/          # 专业智能体定义（.md 文件）
├── 05-mcp/                # Model Context Protocol 服务器配置（.json 文件）
├── 06-hooks/              # 事件驱动的自动化脚本（.sh 文件）
├── 07-plugins/            # 打包的功能集合
├── 08-checkpoints/        # 会话快照文档
├── 09-advanced-features/  # 规划模式、后台任务、权限
├── 10-cli/                # CLI 参考文档
├── scripts/              # Python 工具（build_epub.py、tests/）
└── resources/             # Logo、设计系统资源
```

### Python 脚本（`scripts/`）
- `build_epub.py` - 从 markdown 内容生成 EPUB 电子书（使用 ebooklib、markdown、httpx、pillow）
- `tests/` - build_epub.py 功能的 pytest 测试套件

### 模块命名约定
每个编号模块包含：
- `README.md` - 概述和索引
- 功能特定文件（命令/智能体用 `.md`、skills 用目录、MCP 配置用 `.json`）
- 每个功能的复制粘贴安装命令

## Git 工作流

### 分支命名
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 提交格式
```
类型(范围): 描述
```

**重要：所有 git 提交必须使用中文，包括类型、范围和描述。**

类型对照表：
- `新增` (feat) - 新功能
- `修复` (fix) - Bug 修复
- `文档` (docs) - 文档变更
- `重构` (refactor) - 代码重构
- `样式` (style) - 格式调整
- `测试` (test) - 测试相关
- `杂项` (chore) - 构建、依赖等

示例：
```bash
git commit -m "新增(文档): 添加中文化说明"
git commit -m "修复(脚本): 修复 EPUB 生成错误"
git commit -m "文档(README): 更新安装指南"
```

## CI/CD

GitHub Actions（`.github/workflows/test.yml`）在以下情况触发：
- 当 `scripts/**` 变化时推送到 `main`/`develop`
- 当 `scripts/**` 变化时拉取请求到 `main`

任务：pytest（Python 3.10-3.12）、ruff lint/format、bandit 安全扫描、mypy 类型检查、EPUB 构建验证
