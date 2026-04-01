<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

<a id="claude-code-examples---quick-reference-card"></a>

# Claude Code 示例 · 速查卡

<a id="installation-quick-commands"></a>

## 🚀 安装速用命令

### Slash Commands
```bash
# 全部安装
cp 01-slash-commands/*.md .claude/commands/

# 安装指定项
cp 01-slash-commands/optimize.md .claude/commands/
```

### Memory
```bash
# 项目 memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 个人 memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills
```bash
# 个人 skills
cp -r 03-skills/code-review ~/.claude/skills/

# 项目 skills
cp -r 03-skills/code-review .claude/skills/
```

### Subagents
```bash
# 全部安装
cp 04-subagents/*.md .claude/agents/

# 安装指定项
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# 设置凭据
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 安装配置（项目作用域）
cp 05-mcp/github-mcp.json .mcp.json

# 或用户作用域：写入 ~/.claude.json
```

### Hooks
```bash
# 安装 hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 在 settings 中配置（~/.claude/settings.json）
```

### Plugins
```bash
# 从示例安装（若已发布）
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints
```bash
# 每次用户提示都会自动创建 Checkpoints
# 若要回退，连按两次 Esc 或使用：
/rewind

# 然后选择：恢复代码与会话、仅恢复会话、仅恢复代码、
# 从此处起摘要，或取消
```

### Advanced Features
```bash
# 在 settings 中配置（.claude/settings.json）
# 参见 09-advanced-features/config-examples.json

# Planning mode
/plan Task description

# Permission modes（使用 --permission-mode 标志）
# default        - 有风险的操作会请求批准
# acceptEdits    - 自动接受文件编辑，其余仍询问
# plan           - 只读分析，不修改
# dontAsk        - 接受除有风险操作外的所有动作
# auto           - 后台分类器自动决定权限
# bypassPermissions - 接受所有动作（需要 --dangerously-skip-permissions）

# Session management
/resume                # 恢复先前会话
/rename "name"         # 为当前会话命名
/fork                  # 分叉当前会话
claude -c              # 继续最近一次会话
claude -r "session"    # 按名称/ID 恢复会话
```

---

<a id="feature-cheat-sheet"></a>

## 📋 功能一览

| 功能 | 安装路径 | 用法 |
|---------|-------------|-------|
| **Slash Commands（55+）** | `.claude/commands/*.md` | `/command-name` |
| **Memory** | `./CLAUDE.md` | 自动加载 |
| **Skills** | `.claude/skills/*/SKILL.md` | 自动调用 |
| **Subagents** | `.claude/agents/*.md` | 自动委派 |
| **MCP** | `.mcp.json`（项目）或 `~/.claude.json`（用户） | `/mcp__server__action` |
| **Hooks（25 个事件）** | `~/.claude/hooks/*.sh` | 事件触发（4 种类型） |
| **Plugins** | 通过 `/plugin install` | 打包全部 |
| **Checkpoints** | 内置 | `Esc+Esc` 或 `/rewind` |
| **Planning Mode** | 内置 | `/plan <task>` |
| **Permission Modes（6 种）** | 内置 | `--allowedTools`、`--permission-mode` |
| **Sessions** | 内置 | `/session <command>` |
| **Background Tasks** | 内置 | 在后台运行 |
| **Remote Control** | 内置 | WebSocket API |
| **Web Sessions** | 内置 | `claude web` |
| **Git Worktrees** | 内置 | `/worktree` |
| **Auto Memory** | 内置 | 自动保存到 CLAUDE.md |
| **Task List** | 内置 | `/task list` |
| **Bundled Skills（5）** | 内置 | `/simplify`、`/loop`、`/claude-api`、`/voice`、`/browse` |

---

<a id="common-use-cases"></a>

## 🎯 常见用法

### 代码审查
```bash
# 方式 1：Slash command
cp 01-slash-commands/optimize.md .claude/commands/
# 使用：/optimize

# 方式 2：Subagent
cp 04-subagents/code-reviewer.md .claude/agents/
# 使用：自动委派

# 方式 3：Skill
cp -r 03-skills/code-review ~/.claude/skills/
# 使用：自动调用

# 方式 4：Plugin（推荐）
/plugin install pr-review
# 使用：/review-pr
```

### 文档
```bash
# Slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# Skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Plugin（完整方案）
/plugin install documentation
```

### DevOps
```bash
# 完整 plugin
/plugin install devops-automation

# 命令：/deploy、/rollback、/status、/incident
```

### 团队规范
```bash
# 项目 memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 按团队需要编辑
vim CLAUDE.md
```

### 自动化与 Hooks
```bash
# 安装 hooks（25 个事件，4 种类型：command、http、prompt、agent）
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 示例：
# - 提交前测试：pre-commit.sh
# - 自动格式化：format-code.sh
# - 安全扫描：security-scan.sh

# Auto Mode：全流程自主执行
claude --enable-auto-mode -p "Refactor and test the auth module"
# 或用 Shift+Tab 在交互中循环切换模式
```

### 安全重构
```bash
# 每次提示前会自动创建 Checkpoints
# 尝试重构
# 若成功：继续
# 若失败：连按 Esc+Esc 或使用 /rewind 回退
```

### 复杂实现
```bash
# 使用 planning mode
/plan Implement user authentication system

# Claude 会生成详细计划
# 审阅并批准
# Claude 再按步骤实现
```

### CI/CD 集成
```bash
# 无界面模式（非交互）
claude -p "Run all tests and generate report"

# CI 中配合 permission mode
claude -p "Run tests" --permission-mode dontAsk

# Auto Mode：CI 任务全自动
claude --enable-auto-mode -p "Run tests and fix failures"

# 配合 hooks 做自动化
# 参见 09-advanced-features/README.md
```

### 学习与试验
```bash
# 使用 plan 模式做安全分析
claude --permission-mode plan

# 安全实验——Checkpoints 会自动创建
# 需要回退时：连按 Esc+Esc 或使用 /rewind
```

### Agent Teams
```bash
# 启用 agent teams
export CLAUDE_AGENT_TEAMS=1

# 或在 settings.json 中
{ "agentTeams": { "enabled": true } }

# 可从类似提示开始：「用团队方式实现功能 X」
```

<a id="scheduled-tasks"></a>

### 定时任务
```bash
# 每 5 分钟执行一次命令
/loop 5m /check-status

# 一次性提醒
/loop 30m "remind me to check the deploy"
```

---

<a id="file-locations-reference"></a>

## 📁 文件位置参考

```
Your Project/
├── .claude/
│   ├── commands/              # Slash commands 放这里
│   ├── agents/                # Subagents 放这里
│   ├── skills/                # 项目 skills 放这里
│   └── settings.json          # 项目设置（hooks 等）
├── .mcp.json                  # MCP 配置（项目作用域）
├── CLAUDE.md                  # 项目 memory
└── src/
    └── api/
        └── CLAUDE.md          # 目录级 memory

User Home/
├── .claude/
│   ├── commands/              # 个人 commands
│   ├── agents/                # 个人 agents
│   ├── skills/                # 个人 skills
│   ├── hooks/                 # Hook 脚本
│   ├── settings.json          # 用户设置
│   ├── managed-settings.d/    # 托管设置（企业/组织）
│   └── CLAUDE.md              # 个人 memory
└── .claude.json               # 个人 MCP 配置（用户作用域）
```

---

<a id="finding-examples"></a>

## 🔍 查找示例

<a id="by-category"></a>

### 按类别
- **Slash Commands**：`01-slash-commands/`
- **Memory**：`02-memory/`
- **Skills**：`03-skills/`
- **Subagents**：`04-subagents/`
- **MCP**：`05-mcp/`
- **Hooks**：`06-hooks/`
- **Plugins**：`07-plugins/`
- **Checkpoints**：`08-checkpoints/`
- **Advanced Features**：`09-advanced-features/`
- **CLI**：`10-cli/`

<a id="by-use-case"></a>

### 按场景
- **性能**：`01-slash-commands/optimize.md`
- **安全**：`04-subagents/secure-reviewer.md`
- **测试**：`04-subagents/test-engineer.md`
- **文档**：`03-skills/doc-generator/`
- **DevOps**：`07-plugins/devops-automation/`

<a id="by-complexity"></a>

### 按复杂度
- **简单**：Slash commands
- **中等**：Subagents、Memory
- **进阶**：Skills、Hooks
- **完整**：Plugins

---

<a id="learning-path"></a>

## 🎓 学习路径

<a id="day-1"></a>

### 第 1 天
```bash
# 阅读概览
cat README.md

# 安装一条 command
cp 01-slash-commands/optimize.md .claude/commands/

# 试用
/optimize
```

<a id="day-2-3"></a>

### 第 2–3 天
```bash
# 配置 memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# 安装 subagent
cp 04-subagents/code-reviewer.md .claude/agents/
```

<a id="day-4-5"></a>

### 第 4–5 天
```bash
# 配置 MCP
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# 试用 MCP 命令
/mcp__github__list_prs
```

<a id="week-2"></a>

### 第 2 周
```bash
# 安装 skill
cp -r 03-skills/code-review ~/.claude/skills/

# 让其自动调用
# 只需说：「Review this code for issues」
```

<a id="week-3"></a>

### 第 3 周及以后
```bash
# 安装完整 plugin
/plugin install pr-review

# 使用打包功能
/review-pr
/check-security
/check-tests
```

---

<a id="new-features-march-2026"></a>

## 新功能（2026 年 3 月）

| 功能 | 说明 | 用法 |
|---------|-------------|-------|
| **Auto Mode** | 后台分类器驱动的全自动运行 | `--enable-auto-mode` 标志，`Shift+Tab` 循环模式 |
| **Channels** | Discord 与 Telegram 集成 | `--channels` 标志，Discord/Telegram 机器人 |
| **Voice Dictation** | 语音输入命令与上下文 | `/voice` 命令 |
| **Hooks（25 个事件）** | 扩展后的 hook 系统，含 4 种类型 | command、http、prompt、agent 等 hook 类型 |
| **MCP Elicitation** | MCP 服务器可在运行时请求用户输入 | 服务器需要澄清时会自动提示 |
| **WebSocket MCP** | MCP 连接的 WebSocket 传输 | 在 `.mcp.json` 中用 `ws://` URL 配置 |
| **Plugin LSP** | 插件的 Language Server Protocol 支持 | `userConfig`、`${CLAUDE_PLUGIN_DATA}` 变量 |
| **Remote Control** | 通过 WebSocket API 控制 Claude Code | `claude --remote`，用于外部集成 |
| **Web Sessions** | 浏览器版 Claude Code 界面 | `claude web` 启动 |
| **Desktop App** | 原生桌面应用 | 从 claude.ai/download 下载 |
| **Task List** | 管理后台任务 | `/task list`、`/task status <id>` |
| **Auto Memory** | 从对话自动保存 memory | Claude 将关键上下文自动写入 CLAUDE.md |
| **Git Worktrees** | 并行开发的隔离工作区 | `/worktree` 创建隔离工作区 |
| **Model Selection** | 在 Sonnet 4.6 与 Opus 4.6 间切换 | `/model` 或 `--model` 标志 |
| **Agent Teams** | 多智能体协作完成任务 | 用环境变量 `CLAUDE_AGENT_TEAMS=1` 启用 |
| **Scheduled Tasks** | 使用 `/loop` 的周期性任务 | `/loop 5m /command` 或 CronCreate 工具 |
| **Chrome Integration** | 浏览器自动化 | `--chrome` 标志或 `/chrome` 命令 |
| **Keyboard Customization** | 自定义快捷键 | `/keybindings` 命令 |

---

<a id="tips--tricks"></a>

## 技巧与提示

<a id="customization"></a>

### 定制
- 先按示例原样使用
- 再按需求修改
- 与团队共享前先自测
- 对配置做版本管理

<a id="best-practices"></a>

### 最佳实践
- 团队规范用 memory
- 完整工作流用 plugins
- 复杂任务用 subagents
- 快捷操作用 slash commands

<a id="troubleshooting"></a>

### 故障排查
```bash
# 检查文件位置
ls -la .claude/commands/
ls -la .claude/agents/

# 核对 YAML 语法
head -20 .claude/agents/code-reviewer.md

# 测试 MCP 连接
echo $GITHUB_TOKEN
```

---

<a id="feature-matrix"></a>

## 📊 功能对照表

| 需求 | 使用方式 | 示例 |
|------|----------|---------|
| 快捷操作 | Slash Command（55+） | `01-slash-commands/optimize.md` |
| 团队规范 | Memory | `02-memory/project-CLAUDE.md` |
| 自动工作流 | Skill | `03-skills/code-review/` |
| 专项任务 | Subagent | `04-subagents/code-reviewer.md` |
| 外部数据 | MCP（含 Elicitation、WebSocket） | `05-mcp/github-mcp.json` |
| 事件自动化 | Hook（25 个事件，4 种类型） | `06-hooks/pre-commit.sh` |
| 完整方案 | Plugin（含 LSP 支持） | `07-plugins/pr-review/` |
| 安全试错 | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| 全自动 | Auto Mode | `--enable-auto-mode` 或 `Shift+Tab` |
| 聊天集成 | Channels | `--channels`（Discord、Telegram） |
| CI/CD 流水线 | CLI | `10-cli/README.md` |

---

<a id="quick-links"></a>

## 🔗 快速链接

- **主指南**：`README.md`
- **完整索引**：`INDEX.md`
- **摘要**：`EXAMPLES_SUMMARY.md`
- **原始指南**：`claude_concepts_guide.md`

---

<a id="common-questions"></a>

## 📞 常见问题

**问：该用哪一种？**  
答：从 slash commands 开始，再按需叠加其他能力。

**问：能混用吗？**  
答：可以。它们可以协同工作。Memory + Commands + MCP 很强。

**问：怎么和团队共享？**  
答：把 `.claude/` 目录提交到 git。

**问：密钥怎么办？**  
答：用环境变量，不要硬编码。

**问：能改示例吗？**  
答：当然可以。它们就是给你定制用的模板。

---

<a id="checklist"></a>

## ✅ 清单

入门检查清单：

- [ ] 阅读 `README.md`
- [ ] 安装 1 条 slash command
- [ ] 试用该命令
- [ ] 创建项目 `CLAUDE.md`
- [ ] 安装 1 个 subagent
- [ ] 配置 1 个 MCP 集成
- [ ] 安装 1 个 skill
- [ ] 试用一个完整 plugin
- [ ] 按需求定制
- [ ] 与团队共享

---

**快速开始**：`cat README.md`

**完整索引**：`cat INDEX.md`

**本速查卡**：随手备查即可。
