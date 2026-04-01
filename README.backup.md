<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude How To

> 一份面向视觉与示例的 Claude Code 指南——从基础概念到进阶智能体，附带可复制的模板，上手即可用。

<a id="why-this-guide"></a>
## 为什么写本指南？

本项目以另一种方式补充 [Anthropic 官方文档](https://code.claude.com/docs/en/overview)：

| | 官方文档 | 本指南 |
|--|---------------|------------|
| **形式** | 参考型文档 | 配图分步教程 |
| **深度** | 功能说明 | 底层如何运作 |
| **示例** | 基础片段 | 可立即用于生产的模板 |
| **结构** | 按功能组织 | 循序渐进（入门 → 进阶） |
| **上手** | 自行探索 | 带时间估算的路线图 |
| **自我评估** | 无 | 互动测验，发现短板并生成个性化学习路径 |

**在这里你能找到：**
- 用 Mermaid 图解释各功能如何工作
- 可直接复制到项目中的现成配置
- 带上下文与最佳实践的实战示例
- 从 `/help` 到搭建自定义智能体的清晰进阶
- 基于常见问题的排错指南

---

## 目录

- [为什么写本指南？](#why-this-guide)
- [功能目录](#feature-catalog)
- [快速导航](#quick-navigation)
- [学习路径](#learning-path)
- [速查：按场景选功能](#quick-reference-choose-your-features)
- [快速开始](#getting-started)
- **功能模块**
  - [01. Slash Commands](#01-slash-commands)
  - [02. Memory](#02-memory)
  - [03. Skills](#03-skills)
  - [04. Subagents](#04-subagents)
  - [05. MCP Protocol](#05-mcp-protocol)
  - [06. Hooks](#06-hooks)
  - [07. Plugins](#07-plugins)
  - [08. Checkpoints](#08-checkpoints-and-rewind)
  - [09. Advanced Features](#09-advanced-features)
  - [10. CLI Reference](#10-cli-reference)
- [目录结构](#directory-structure)
- [安装速查](#installation-quick-reference)
- [示例工作流](#example-workflows)
- [最佳实践](#best-practices)
- [故障排除](#troubleshooting)
- [测试](#testing)
- [更多资源](#additional-resources)
- [参与贡献](#contributing)
- [EPUB 生成](#epub-generation)
- [贡献者](#contributors)
- [Star 历史](#star-history)

---

<a id="feature-catalog"></a>
## 功能目录

**想快速查阅？** 请查看完整的 **[功能目录](CATALOG.md)**，其中包括：

- 全部 slash commands（内置与自定义）及说明
- Subagents 及其能力
- Skills 及自动触发条件
- Plugins 的组成与安装命令
- 用于外部集成的 MCP 服务器
- 用于事件驱动自动化的 Hooks
- 各功能的一键安装命令

**[查看完整目录](CATALOG.md)**

---

<a id="quick-navigation"></a>
## 快速导航

| 功能 | 说明 | 文件夹 |
|---------|-------------|--------|
| **功能目录** | 含安装命令的完整参考 | [CATALOG.md](CATALOG.md) |
| **Slash Commands** | 用户触发的快捷方式 | [01-slash-commands/](01-slash-commands/) |
| **Memory** | 持久化上下文 | [02-memory/](02-memory/) |
| **Skills** | 可复用能力 | [03-skills/](03-skills/) |
| **Subagents** | 专用 AI 助手 | [04-subagents/](04-subagents/) |
| **MCP Protocol** | 外部工具访问 | [05-mcp/](05-mcp/) |
| **Hooks** | 事件驱动自动化 | [06-hooks/](06-hooks/) |
| **Plugins** | 打包的功能集 | [07-plugins/](07-plugins/) |
| **Checkpoints** | 会话快照与回退 | [08-checkpoints/](08-checkpoints/) |
| **Advanced Features** | 规划、思考、后台任务等 | [09-advanced-features/](09-advanced-features/) |
| **CLI Reference** | 命令、flag 与选项 | [10-cli/](10-cli/) |
| **博客文章** | 实战用法示例 | [Blog Posts](https://medium.com/@luongnv89) |

---

<a id="learning-path"></a>
## 📚 学习路径

**不知从何入手？** 完成 [自我评估测验](LEARNING-ROADMAP.md#-find-your-level) 获取推荐路径，或在 Claude Code 中运行 `/self-assessment` 使用交互版。

> **内置 Skills**：本仓库包含两个可在 Claude Code 中直接使用的交互式 skills：
> - `/self-assessment` — 评估整体 Claude Code 熟练度并生成个性化学习路径
> - `/lesson-quiz [lesson]` — 测验任意一课的理解程度（例如 `/lesson-quiz hooks`）

| 顺序 | 功能 | 难度 | 时间 | 适合人群 |
|-------|---------|-------|------|-----------------|
| **1** | [Slash Commands](01-slash-commands/) | ⭐ 入门 | 30 分钟 | Level 1 起点 |
| **2** | [Memory](02-memory/) | ⭐⭐ 入门+ | 45 分钟 | Level 1 |
| **3** | [Checkpoints](08-checkpoints/) | ⭐⭐ 中级 | 45 分钟 | Level 1 |
| **4** | [CLI 基础](10-cli/) | ⭐⭐ 入门+ | 30 分钟 | Level 1 |
| **5** | [Skills](03-skills/) | ⭐⭐ 中级 | 1 小时 | Level 2 起点 |
| **6** | [Hooks](06-hooks/) | ⭐⭐ 中级 | 1 小时 | Level 2 |
| **7** | [MCP](05-mcp/) | ⭐⭐⭐ 中级+ | 1 小时 | Level 2 |
| **8** | [Subagents](04-subagents/) | ⭐⭐⭐ 中级+ | 1.5 小时 | Level 2 |
| **9** | [Advanced](09-advanced-features/) | ⭐⭐⭐⭐⭐ 进阶 | 2–3 小时 | Level 3 起点 |
| **10** | [Plugins](07-plugins/) | ⭐⭐⭐⭐ 进阶 | 2 小时 | Level 3 |
| **11** | [CLI 精通](10-cli/) | ⭐⭐⭐ 进阶 | 1 小时 | Level 3 |

**合计**：约 11–13 小时 | 📖 **[完整学习路线图 →](LEARNING-ROADMAP.md)**

---

<a id="quick-reference-choose-your-features"></a>
## 🎯 速查：按场景选功能

### 功能对比

| 功能 | 调用方式 | 持久化 | 最适用 |
|---------|-----------|------------|----------|
| **Slash Commands** | 手动（`/cmd`） | 仅当前会话 | 快捷操作 |
| **Memory** | 自动加载 | 跨会话 | 长期积累 |
| **Skills** | 自动触发 | 文件系统 | 自动化工作流 |
| **Subagents** | 自动委派 | 隔离上下文 | 任务拆分 |
| **MCP Protocol** | 自动查询 | 实时 | 访问实时数据 |
| **Hooks** | 事件触发 | 按配置 | 自动化与校验 |
| **Plugins** | 一条命令 | 全功能打包 | 一站式方案 |
| **Checkpoints** | 手动/自动 | 基于会话 | 安全试错 |
| **Planning Mode** | 手动/自动 | 规划阶段 | 复杂实现 |
| **Background Tasks** | 手动 | 任务持续期间 | 长时间运行 |
| **CLI Reference** | 终端命令 | 会话/脚本 | 自动化与脚本 |

### 场景矩阵

| 场景 | 推荐功能组合 |
|----------|---------------------|
| **团队上手** | Memory + Slash Commands + Plugins |
| **代码质量** | Subagents + Skills + Memory + Hooks |
| **文档** | Skills + Subagents + Plugins |
| **DevOps** | Plugins + MCP + Hooks + Background Tasks |
| **安全审查** | Subagents + Skills + Hooks（只读模式） |
| **API 集成** | MCP + Memory |
| **轻量任务** | Slash Commands |
| **复杂项目** | 全部功能 + Planning Mode |
| **重构** | Checkpoints + Planning Mode + Hooks |
| **学习/试验** | Checkpoints + Extended Thinking + Permission Mode |
| **CI/CD 自动化** | CLI Reference + Hooks + Background Tasks |
| **性能优化** | Planning Mode + Checkpoints + Background Tasks |
| **脚本自动化** | CLI Reference + Hooks + MCP |
| **批处理** | CLI Reference + Background Tasks |

---

<a id="getting-started"></a>
## ⚡ 快速开始

### 15 分钟——第一步
```bash
# 复制你的第一条 slash command
cp 01-slash-commands/optimize.md .claude/commands/

# 试一试！
# 在 Claude Code 中：/optimize
```

### 1 小时——必备配置
```bash
# 1. Slash commands（15 分钟）
cp 01-slash-commands/*.md .claude/commands/

# 2. 项目 memory（15 分钟）
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 3. 安装一个 skill（15 分钟）
cp -r 03-skills/code-review ~/.claude/skills/

# 4. 一起试用（15 分钟）
# 看它们如何配合！
```

### 周末——完整配置
- **第 1 天**：Slash Commands、Memory、Skills、Hooks
- **第 2 天**：Subagents、MCP 集成、Plugins
- **结果**：完整的 Claude Code 高阶用户配置

📖 **[详细里程碑与练习 →](LEARNING-ROADMAP.md)**

---

## 01. Slash Commands

**位置**：[01-slash-commands/](01-slash-commands/)

**是什么**：以 Markdown 文件保存、由用户触发的快捷方式

**示例**：
- `optimize.md` - 代码优化分析
- `pr.md` - Pull request 准备
- `generate-api-docs.md` - API 文档生成

**安装**：
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**用法**：
```
/optimize
/pr
/generate-api-docs
```

**延伸阅读**：[Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

---

## 02. Memory

**位置**：[02-memory/](02-memory/)

**是什么**：跨会话持久化的上下文

**示例**：
- `project-CLAUDE.md` - 团队级项目规范
- `directory-api-CLAUDE.md` - 目录级规则
- `personal-CLAUDE.md` - 个人偏好

**安装**：
```bash
# 项目 memory
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# 目录 memory
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# 个人 memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**用法**：由 Claude 自动加载

---

## 03. Skills

**位置**：[03-skills/](03-skills/)

**是什么**：可复用、可自动触发，包含说明与脚本

**示例**：
- `code-review/` - 带脚本的全面代码审查
- `brand-voice/` - 品牌语气一致性检查
- `doc-generator/` - API 文档生成

**安装**：
```bash
# 个人 skills
cp -r 03-skills/code-review ~/.claude/skills/

# 项目 skills
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**用法**：在相关场景下自动触发

---

## 04. Subagents

**位置**：[04-subagents/](04-subagents/)

**是什么**：带隔离上下文与自定义提示词的专用 AI 助手

**示例**：
- `code-reviewer.md` - 全面代码质量分析
- `test-engineer.md` - 测试策略与覆盖率
- `documentation-writer.md` - 技术文档
- `secure-reviewer.md` - 安全向审查（只读）
- `implementation-agent.md` - 完整功能实现

**安装**：
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**用法**：由主智能体自动委派

---

## 05. MCP Protocol

**位置**：[05-mcp/](05-mcp/)

**是什么**：Model Context Protocol，用于访问外部工具与 API

**示例**：
- `github-mcp.json` - GitHub 集成
- `database-mcp.json` - 数据库查询
- `filesystem-mcp.json` - 文件操作
- `multi-mcp.json` - 多个 MCP 服务器

**安装**：
```bash
# 设置环境变量
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 通过 CLI 添加 MCP 服务器
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 或手动编辑项目 .mcp.json（示例见 05-mcp/）
```

**用法**：配置完成后，MCP 工具会自动对 Claude 可用

---

## 06. Hooks

**位置**：[06-hooks/](06-hooks/)

**是什么**：在 Claude Code 事件发生时自动执行的事件驱动 shell 命令

**示例**：
- `format-code.sh` - 写入前自动格式化代码
- `pre-commit.sh` - 提交前运行测试
- `security-scan.sh` - 安全扫描
- `log-bash.sh` - 记录所有 bash 命令
- `validate-prompt.sh` - 校验用户提示
- `notify-team.sh` - 事件发生时通知团队

**安装**：
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

在 `~/.claude/settings.json` 中配置 hooks：
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/security-scan.sh"]
    }]
  }
}
```

**用法**：Hooks 在事件发生时自动执行

**Hook 类型**：
- **Tool Hooks**：`PreToolUse:*`、`PostToolUse:*`
- **Session Hooks**：`Stop`、`SubagentStop`、`SubagentStart`
- **Lifecycle Hooks**：`Notification`、`ConfigChange`、`WorktreeCreate`、`WorktreeRemove`

---

## 07. Plugins

**位置**：[07-plugins/](07-plugins/)

**是什么**：将命令、agents、MCP 与 hooks 等打包在一起

**示例**：
- `pr-review/` - 完整 PR 审查工作流
- `devops-automation/` - 部署与监控
- `documentation/` - 文档生成

**安装**：
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**用法**：使用打包的 slash commands 与功能

---

## 08. Checkpoints and Rewind

**位置**：[08-checkpoints/](08-checkpoints/)

**是什么**：保存对话状态并回退到较早节点，以尝试不同方案

**核心概念**：
- **Checkpoint**：对话状态的快照
- **Rewind**：回到某一 checkpoint
- **Branch Point**：从同一 checkpoint 分叉尝试多种做法

**用法**：
```
# 每次用户输入都会自动创建 Checkpoints
# 若要回退，连按两次 Esc 或使用：
/rewind

# 随后可从下列五项中选择：
# 1. 恢复代码与对话
# 2. 仅恢复对话
# 3. 仅恢复代码
# 4. 从此处摘要
# 5. 取消
```

**适用场景**：
- 尝试不同实现路径
- 从错误中恢复
- 安全试验
- 对比备选方案
- 对不同设计做 A/B 对比

**示例工作流**：
```
1. 照常工作（checkpoints 会自动创建）
2. 尝试实验性方案
3. 若成功：继续
4. 若失败：连按 Esc+Esc 或 /rewind 返回
```

---

## 09. Advanced Features

**位置**：[09-advanced-features/](09-advanced-features/)

**是什么**：面向复杂工作流与自动化的高级能力

### Planning Mode

在写代码前生成详细实现计划：
```
User: /plan Implement user authentication system

Claude: [生成完整的分步计划]

User: Approve and proceed
```

**收益**：清晰路线图、时间估算、风险评估

### Extended Thinking

用于复杂问题的深度推理。可用 `Alt+T` / `Option+T` 切换，或设置环境变量 `MAX_THINKING_TOKENS`：
```bash
# 会话内切换：按 Alt+T（macOS 上为 Option+T）

# 或通过环境变量设置
MAX_THINKING_TOKENS=10000 claude

# 然后提出复杂问题
User: Should we use microservices or monolith?
Claude: [结合 Extended Thinking 系统分析利弊]
```

**收益**：更稳妥的架构决策、更充分的分析

### Background Tasks

长时间操作不阻塞当前工作：
```
User: 在后台运行测试

Claude: 已启动 bg-1234，你可继续其他工作

[稍后] 测试结果：245 通过，3 失败
```

**收益**：并行开发、无需干等

### Permission Modes

控制 Claude 可执行的操作：
- **`default`**：标准权限，敏感操作会确认
- **`acceptEdits`**：自动接受文件编辑，其他操作仍确认
- **`plan`**：仅分析与规划，不修改
- **`dontAsk`**：不经确认接受所有操作
- **`bypassPermissions`**：跳过全部权限检查（危险）

```bash
claude --permission-mode plan          # 代码审查模式
claude --permission-mode acceptEdits   # 学习模式
claude --permission-mode default       # 标准模式
```

### Headless Mode

在 CI/CD 与自动化场景运行 Claude Code：
```bash
claude -p "Run tests and generate report"
```

**适用场景**：CI/CD、自动审查、批处理

### Session Management

管理多个工作会话：
```bash
/resume                          # 交互式恢复先前会话
/rename                          # 重命名当前会话
/fork                            # 分叉当前会话
claude -c                        # 继续最近一次会话
claude -r "session"              # 按查询条件恢复会话
```

### Interactive Features

**快捷键**：Ctrl+R（搜索）、Tab（补全）、↑/↓（历史）

**命令历史**：访问先前命令

**多行输入**：跨多行的复杂提示

### Configuration

在 `~/.claude/settings.json` 中自定义 Claude Code 行为：
```json
{
  "permissions": {
    "allow": ["Read", "Glob", "Grep", "Bash(git *)"],
    "deny": ["Bash(rm -rf *)"]
  },
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }]
  },
  "env": {
    "MAX_THINKING_TOKENS": "10000"
  }
}
```

完整配置见 [config-examples.json](09-advanced-features/config-examples.json)。

---

## 10. CLI Reference

**位置**：[10-cli/](10-cli/)

**是什么**：Claude Code 命令行接口的完整参考

**主要板块**：
- CLI 命令（`claude`、`claude -p`、`claude -c`、`claude -r`）
- 核心 flag（print 模式、continue、resume、version）
- 模型与配置（`--model`、`--agents`）
- 系统提示词定制
- 工具与权限管理
- 输出格式（text、JSON、stream-JSON）
- MCP 配置
- 会话管理

**简短示例**：
```bash
# 交互模式
claude "explain this project"

# Print 模式（非交互）
claude -p "review this code"

# 处理文件内容
cat error.log | claude -p "explain this error"

# 供脚本使用的 JSON 输出
claude -p --output-format json "list functions"

# 恢复会话
claude -r "feature-auth" "continue implementation"
```

**适用场景**：
- 接入 CI/CD 流水线
- 脚本自动化与管道
- 批处理
- 多会话工作流
- 自定义 agent 配置

---

<a id="directory-structure"></a>
## 目录结构

```

├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md（本文件）
```

---

<a id="installation-quick-reference"></a>
## 安装速查

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Plugins
/plugin install pr-review

# Checkpoints（默认开启，在 settings 中配置）
# 见 08-checkpoints/README.md

# Advanced Features（在 settings 中配置）
# 见 09-advanced-features/config-examples.json

# CLI Reference（无需安装）
# 用法示例见 10-cli/README.md
```

---

<a id="example-workflows"></a>
## 示例工作流

### 1. 完整代码审查工作流

```markdown
# 使用：Slash Commands + Subagents + Memory + MCP

User: /review-pr

Claude:
1. 加载项目 memory（编码规范）
2. 通过 GitHub MCP 拉取 PR
3. 委派给 code-reviewer subagent
4. 委派给 test-engineer subagent
5. 汇总结论
6. 给出完整审查意见
```

### 2. 自动化文档

```markdown
# 使用：Skills + Subagents + Memory

User: "Generate API documentation for the auth module"

Claude:
1. 加载项目 memory（文档规范）
2. 识别文档生成请求
3. 自动调用 doc-generator skill
4. 委派给 api-documenter subagent
5. 生成含示例的完整文档
```

### 3. DevOps 部署

```markdown
# 使用：Plugins + MCP + Hooks

User: /deploy production

Claude:
1. 运行 pre-deploy hook（校验环境）
2. 委派给 deployment-specialist subagent
3. 通过 Kubernetes MCP 执行部署
4. 监控进度
5. 运行 post-deploy hook（健康检查）
6. 汇报状态
```

---

<a id="best-practices"></a>
## 最佳实践

### 建议做法 ✅
- 从 slash commands 简单起步
- 逐步增加功能
- 用 memory 固化团队规范
- 先在本地验证配置
- 为自定义实现写文档
- 将项目配置纳入版本控制
- 与团队共享 plugins

### 避免做法 ❌
- 不要重复造轮子
- 不要硬编码凭据
- 不要省略文档
- 不要把简单任务过度复杂化
- 不要忽视安全最佳实践
- 不要提交敏感数据

---

<a id="troubleshooting"></a>
## 故障排除

### 功能未加载
1. 检查文件位置与命名
2. 校验 YAML frontmatter 语法
3. 检查文件权限
4. 核对 Claude Code 版本兼容性

### MCP 连接失败
1. 确认环境变量
2. 检查 MCP 服务器是否已安装
3. 测试凭据
4. 检查网络连通性

### Subagent 未委派
1. 检查工具权限
2. 确认 agent 描述是否清晰
3. 评估任务复杂度
4. 单独测试该 agent

---

<a id="testing"></a>
## 测试

本仓库包含较完整的自动化测试，用于保障代码质量与可靠性。

### 测试概览

- **单元测试**：使用 pytest 的 Python 测试（Python 3.10、3.11、3.12）
- **代码质量**：使用 Ruff 做 lint 与格式化
- **安全**：使用 Bandit 做漏洞扫描
- **类型检查**：使用 mypy 做静态类型分析
- **构建验证**：EPUB 生成测试
- **覆盖率**：Codecov 集成

### 本地运行测试

```bash
# 安装开发依赖
uv pip install -r requirements-dev.txt

# 运行全部单元测试
pytest scripts/tests/ -v

# 运行测试并生成覆盖率报告
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 代码质量检查
ruff check scripts/
ruff format --check scripts/

# 安全扫描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 类型检查
mypy scripts/ --ignore-missing-imports
```

### GitHub 上的自动化测试

在以下情况会自动运行测试：
- 推送到 `main` 或 `develop` 分支
- 向 `main` 提交 Pull Request

在 GitHub Actions 标签页查看结果，或阅读 [TESTING.md](.github/TESTING.md) 了解详情。

### 编写测试

参与贡献时，请为新功能补充测试：

1. **在** `scripts/tests/test_*.py` **中编写测试**
2. **在本地运行测试** 确认通过
3. **使用** `pytest --cov=scripts` **查看覆盖率**
4. **随 PR 一并提交** — 所有贡献均需包含测试

更细的测试指南见 [TESTING.md](.github/TESTING.md)。

---

<a id="additional-resources"></a>
## 更多资源

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) - 可复用的 skills 合集
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny's Claude Code Workflow](https://x.com/bcherny/status/2007179832300581177) - Claude Code 创造者分享的体系化工作流：并行 agents、共享 CLAUDE.md、Plan 模式、slash commands、subagents，以及用于长时间自主会话的校验 hooks。要点包括把重复工作流沉淀为可复用命令，以及将 Claude 接入团队工具（GitHub、Slack、BigQuery、Sentry），形成端到端闭环与反馈。

---

<a id="contributing"></a>
## 参与贡献

发现问题或想贡献示例？欢迎参与！

**请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，其中说明：**
- 可贡献的类型（示例、文档、功能、缺陷、反馈）
- 如何搭建开发环境
- 目录结构与内容添加方式
- 写作规范与最佳实践
- 提交与 PR 流程

**社区准则：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 彼此如何协作
- [SECURITY.md](SECURITY.md) - 安全政策与漏洞报告

### 报告安全问题

若发现安全漏洞，请负责任地披露：

1. **使用 GitHub Private Vulnerability Reporting**：https://github.com/luongnv89/claude-howto/security/advisories
2. **或阅读** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) 获取详细说明
3. **请勿** 就安全问题公开发帖

安全问题会认真对待并及时处理。完整政策见 [SECURITY.md](SECURITY.md)。

快速上手：
1. Fork 并克隆仓库
2. 创建有意义的分支（`add/feature-name`、`fix/bug`、`docs/improvement`）
3. 按指南修改内容
4. 提交 Pull Request 并写清说明

**需要帮助？** 请开 issue 或 discussion，我们会协助你完成流程。

---

<a id="license"></a>
## 许可证

本项目采用 MIT License，详见 [LICENSE](LICENSE)。

你可以：
- 在项目中使用本指南与示例
- 修改与改编内容
- 分享与分发
- 用于商业用途

唯一要求：保留许可证与版权声明副本。

---

<a id="epub-generation"></a>
## EPUB 生成

希望离线阅读？可生成 EPUB 电子书：

```bash
uv run scripts/build_epub.py
```

会生成 `claude-howto-guide.epub`，包含全部内容及已渲染的 Mermaid 图。

更多选项见 [scripts/README.md](scripts/README.md)。

---

<a id="contributors"></a>
## 贡献者

感谢每一位贡献者！

| 贡献者 | PR |
|--------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - add a tool to create an epub](https://github.com/luongnv89/claude-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): Use tilde fences for nested code blocks in concepts guide](https://github.com/luongnv89/claude-howto/pull/7) |

---

<a id="star-history"></a>
## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

**最近更新**：2026 年 3 月  
**Claude Code 版本**：2.1+  
**兼容模型**：Claude Sonnet 4.6、Claude Opus 4.6、Claude Haiku 4.5
