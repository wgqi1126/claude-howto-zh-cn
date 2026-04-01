<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

<h1 id="claude-code-examples---complete-index">Claude Code 示例 — 完整索引</h1>
本文档按功能类型列出全部示例文件的完整索引。

<h2 id="summary-statistics">汇总统计</h2>
- **文件总数**：100+ 个文件
- **分类**：10 个功能分类
- **Plugins**：3 个完整 plugin
- **Skills**：6 个完整 skill
- **Hooks**：8 个示例 hook
- **开箱即用**：所有示例

---

<h2 id="01-slash-commands-10-files">01. Slash Commands（10 个文件）</h2>
面向常见工作流、由用户触发的快捷方式。

| File | Description | Use Case |
|------|-------------|----------|
| `optimize.md` | 代码优化分析器 | 发现性能问题 |
| `pr.md` | Pull request 准备 | PR 工作流自动化 |
| `generate-api-docs.md` | API 文档生成器 | 生成 API 文档 |
| `commit.md` | 提交说明助手 | 规范化提交 |
| `setup-ci-cd.md` | CI/CD 流水线搭建 | DevOps 自动化 |
| `push-all.md` | 推送全部变更 | 快速推送工作流 |
| `unit-test-expand.md` | 扩展单元测试覆盖 | 测试自动化 |
| `doc-refactor.md` | 文档重构 | 文档改进 |
| `pr-slash-command.png` | 截图示例 | 可视化参考 |
| `README.md` | 说明文档 | 安装与使用指南 |

**安装路径**：`.claude/commands/`

**用法**：`/optimize`、`/pr`、`/generate-api-docs`、`/commit`、`/setup-ci-cd`、`/push-all`、`/unit-test-expand`、`/doc-refactor`

---

<h2 id="02-memory-6-files">02. Memory（6 个文件）</h2>
持久化上下文与项目规范。

| File | Description | Scope | Location |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | 团队项目规范 | 项目级 | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | API 相关规则 | 目录级 | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | 个人偏好 | 用户级 | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | 截图：已保存 memory | - | 可视化参考 |
| `memory-ask-claude.png` | 截图：询问 Claude | - | 可视化参考 |
| `README.md` | 说明文档 | - | 参考 |

**安装**：复制到合适位置

**用法**：由 Claude 自动加载

---

<h2 id="03-skills-28-files">03. Skills（28 个文件）</h2>
附带脚本与模板、可被自动调用的能力。

<h3 id="code-review-skill-5-files">Code Review Skill（5 个文件）</h3>
```
code-review/
├── SKILL.md                          # Skill 定义
├── scripts/
│   ├── analyze-metrics.py            # 代码指标分析器
│   └── compare-complexity.py         # 复杂度对比
└── templates/
    ├── review-checklist.md           # 审查清单
    └── finding-template.md           # 问题说明文档
```

**用途**：涵盖安全、性能与质量的全面代码审查

**自动调用时机**：审查代码时

---

<h3 id="brand-voice-skill-4-files">Brand Voice Skill（4 个文件）</h3>
```
brand-voice/
├── SKILL.md                          # Skill 定义
├── templates/
│   ├── email-template.txt            # 邮件格式
│   └── social-post-template.txt      # 社交媒体格式
└── tone-examples.md                  # 示例文案
```

**用途**：在沟通中保持统一的品牌语气

**自动调用时机**：撰写营销文案时

---

<h3 id="documentation-generator-skill-2-files">Documentation Generator Skill（2 个文件）</h3>
```
doc-generator/
├── SKILL.md                          # Skill 定义
└── generate-docs.py                  # Python 文档提取脚本
```

**用途**：从源代码生成完整的 API 文档

**自动调用时机**：创建或更新 API 文档时

---

<h3 id="refactor-skill-5-files">Refactor Skill（5 个文件）</h3>
```
refactor/
├── SKILL.md                          # Skill 定义
├── scripts/
│   ├── analyze-complexity.py         # 复杂度分析器
│   └── detect-smells.py              # 代码异味检测器
├── references/
│   ├── code-smells.md                # 代码异味目录
│   └── refactoring-catalog.md        # 重构模式目录
└── templates/
    └── refactoring-plan.md           # 重构计划模板
```

**用途**：结合复杂度分析进行系统化代码重构

**自动调用时机**：重构代码时

---

<h3 id="claude-md-skill-1-file">Claude MD Skill（1 个文件）</h3>
```
claude-md/
└── SKILL.md                          # Skill 定义
```

**用途**：管理与优化 CLAUDE.md 文件

---

<h3 id="blog-draft-skill-3-files">Blog Draft Skill（3 个文件）</h3>
```
blog-draft/
├── SKILL.md                          # Skill 定义
└── templates/
    ├── draft-template.md             # 博文草稿模板
    └── outline-template.md           # 博文大纲模板
```

**用途**：按统一结构撰写博文草稿

**另含**：`README.md` — Skills 概览与使用说明

**安装路径**：`~/.claude/skills/` 或 `.claude/skills/`

---

<h2 id="04-subagents-9-files">04. Subagents（9 个文件）</h2>
具备自定义能力的专业 AI 助手。

| File | Description | Tools | Use Case |
|------|-------------|-------|----------|
| `code-reviewer.md` | 代码质量分析 | read, grep, diff, lint_runner | 全面审查 |
| `test-engineer.md` | 测试覆盖分析 | read, write, bash, grep | 测试自动化 |
| `documentation-writer.md` | 文档撰写 | read, write, grep | 文档生成 |
| `secure-reviewer.md` | 安全审查（只读） | read, grep | 安全审计 |
| `implementation-agent.md` | 完整实现 | read, write, bash, grep, edit, glob | 功能开发 |
| `debugger.md` | 调试专项 | read, bash, grep | 问题排查 |
| `data-scientist.md` | 数据分析专项 | read, write, bash | 数据工作流 |
| `clean-code-reviewer.md` | Clean code 规范 | read, grep | 代码质量 |
| `README.md` | 说明文档 | - | 安装与使用指南 |

**安装路径**：`.claude/agents/`

**用法**：由主 agent 自动委派

---

<h2 id="05-mcp-protocol-5-files">05. MCP Protocol（5 个文件）</h2>
外部工具与 API 集成。

| File | Description | Integrates With | Use Case |
|------|-------------|-----------------|----------|
| `github-mcp.json` | GitHub 集成 | GitHub API | PR/issue 管理 |
| `database-mcp.json` | 数据库查询 | PostgreSQL/MySQL | 实时数据查询 |
| `filesystem-mcp.json` | 文件操作 | 本地文件系统 | 文件管理 |
| `multi-mcp.json` | 多服务器 | GitHub + DB + Slack | 完整集成 |
| `README.md` | 说明文档 | - | 安装与使用指南 |

**安装路径**：`.mcp.json`（项目级）或 `~/.claude.json`（用户级）

**用法**：`/mcp__github__list_prs` 等

---

<h2 id="06-hooks-9-files">06. Hooks（9 个文件）</h2>
事件驱动的自动化脚本，会自动执行。

| File | Description | Event | Use Case |
|------|-------------|-------|----------|
| `format-code.sh` | 自动格式化代码 | PreToolUse:Write | 代码格式化 |
| `pre-commit.sh` | 提交前运行测试 | PreToolUse:Bash | 测试自动化 |
| `security-scan.sh` | 安全扫描 | PostToolUse:Write | 安全检查 |
| `log-bash.sh` | 记录 bash 命令 | PostToolUse:Bash | 命令日志 |
| `validate-prompt.sh` | 校验提示 | PreToolUse | 输入校验 |
| `notify-team.sh` | 发送通知 | Notification | 团队通知 |
| `context-tracker.py` | 跟踪上下文窗口用量 | PostToolUse | 上下文监控 |
| `context-tracker-tiktoken.py` | 基于 token 的上下文跟踪 | PostToolUse | 精确 token 计数 |
| `README.md` | 说明文档 | - | 安装与使用指南 |

**安装路径**：在 `~/.claude/settings.json` 中配置

**用法**：在设置中配置后自动执行

**Hook 类型**（4 类，25 个事件）：
- Tool Hooks：PreToolUse、PostToolUse、PostToolUseFailure、PermissionRequest
- Session Hooks：SessionStart、SessionEnd、Stop、StopFailure、SubagentStart、SubagentStop
- Task Hooks：UserPromptSubmit、TaskCompleted、TaskCreated、TeammateIdle
- Lifecycle Hooks：ConfigChange、CwdChanged、FileChanged、PreCompact、PostCompact、WorktreeCreate、WorktreeRemove、Notification、InstructionsLoaded、Elicitation、ElicitationResult

---

<h2 id="07-plugins-3-complete-plugins-40-files">07. Plugins（3 个完整 plugin，40 个文件）</h2>
打包的功能集合。

<h3 id="pr-review-plugin-10-files">PR Review Plugin（10 个文件）</h3>
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # Plugin 清单
├── commands/
│   ├── review-pr.md                  # 全面审查
│   ├── check-security.md             # 安全检查
│   └── check-tests.md                # 测试覆盖检查
├── agents/
│   ├── security-reviewer.md          # 安全专项
│   ├── test-checker.md               # 测试专项
│   └── performance-analyzer.md       # 性能专项
├── mcp/
│   └── github-config.json            # GitHub 集成
├── hooks/
│   └── pre-review.js                 # 审查前校验
└── README.md                         # Plugin 说明
```

**功能**：安全分析、测试覆盖、性能影响

**命令**：`/review-pr`、`/check-security`、`/check-tests`

**安装**：`/plugin install pr-review`

---

<h3 id="devops-automation-plugin-15-files">DevOps Automation Plugin（15 个文件）</h3>
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin 清单
├── commands/
│   ├── deploy.md                     # 部署
│   ├── rollback.md                   # 回滚
│   ├── status.md                     # 系统状态
│   └── incident.md                   # 事件响应
├── agents/
│   ├── deployment-specialist.md      # 部署专家
│   ├── incident-commander.md         # 事件协调
│   └── alert-analyzer.md             # 告警分析
├── mcp/
│   └── kubernetes-config.json        # Kubernetes 集成
├── hooks/
│   ├── pre-deploy.js                 # 部署前检查
│   └── post-deploy.js                # 部署后任务
├── scripts/
│   ├── deploy.sh                     # 部署自动化
│   ├── rollback.sh                   # 回滚自动化
│   └── health-check.sh               # 健康检查
└── README.md                         # Plugin 说明
```

**功能**：Kubernetes 部署、回滚、监控、事件响应

**命令**：`/deploy`、`/rollback`、`/status`、`/incident`

**安装**：`/plugin install devops-automation`

---

<h3 id="documentation-plugin-14-files">Documentation Plugin（14 个文件）</h3>
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # Plugin 清单
├── commands/
│   ├── generate-api-docs.md          # 生成 API 文档
│   ├── generate-readme.md            # 创建 README
│   ├── sync-docs.md                  # 文档同步
│   └── validate-docs.md              # 文档校验
├── agents/
│   ├── api-documenter.md             # API 文档专项
│   ├── code-commentator.md           # 代码注释专项
│   └── example-generator.md          # 示例生成
├── mcp/
│   └── github-docs-config.json       # GitHub 集成
├── templates/
│   ├── api-endpoint.md               # API 端点模板
│   ├── function-docs.md              # 函数文档模板
│   └── adr-template.md               # ADR 模板
└── README.md                         # Plugin 说明
```

**功能**：API 文档、README 生成、文档同步与校验

**命令**：`/generate-api-docs`、`/generate-readme`、`/sync-docs`、`/validate-docs`

**安装**：`/plugin install documentation`

**另含**：`README.md` — Plugins 概览与使用说明

---

<h2 id="08-checkpoints-and-rewind-2-files">08. Checkpoints and Rewind（2 个文件）</h2>
保存对话状态并探索不同方案。

| File | Description | Content |
|------|-------------|---------|
| `README.md` | 说明文档 | 完整的 checkpoint 指南 |
| `checkpoint-examples.md` | 真实场景示例 | 数据库迁移、性能优化、UI 迭代、调试 |
| | | |

**核心概念**：
- **Checkpoint**：对话状态的快照
- **Rewind**：回到先前的 checkpoint
- **Branch Point**：并行尝试多种方案

**用法**：
```
# 每次用户输入都会自动创建 checkpoint
# 若要回退，连按两次 Esc 或使用：
/rewind
# 然后选择：恢复代码与对话、仅恢复对话、
# 仅恢复代码、从此处摘要，或取消
```

**适用场景**：
- 尝试不同实现
- 从错误中恢复
- 安全地做实验
- 对比方案
- A/B 测试

---

<h2 id="09-advanced-features-3-files">09. Advanced Features（3 个文件）</h2>
面向复杂工作流的高级能力。

| File | Description | Features |
|------|-------------|----------|
| `README.md` | 完整指南 | 全部高级功能说明 |
| `config-examples.json` | 配置示例 | 10+ 种场景化配置 |
| `planning-mode-examples.md` | 规划示例 | REST API、数据库迁移、重构 |
| Scheduled Tasks | 使用 `/loop` 与 cron 工具的周期性任务 | 自动化周期性工作流 |
| Chrome Integration | 通过无头 Chromium 的浏览器自动化 | Web 测试与抓取 |
| Remote Control (expanded) | 连接方式、安全与对比表 | 远程会话管理 |
| Keyboard Customization | 自定义快捷键、和弦、上下文 | 个性化快捷操作 |
| Desktop App (expanded) | Connectors、launch.json、企业功能 | 桌面端集成 |
| | | |

**涵盖的高级功能**：

<h3 id="planning-mode">规划模式（Planning Mode）</h3>
- 编写详细实现计划
- 时间估算与风险评估
- 系统化任务拆分

<h3 id="extended-thinking">扩展思考（Extended Thinking）</h3>
- 针对复杂问题的深度推理
- 架构决策分析
- 权衡评估

<h3 id="background-tasks">后台任务（Background Tasks）</h3>
- 长时间运行而不阻塞
- 并行开发工作流
- 任务管理与监控

<h3 id="permission-modes">权限模式（Permission Modes）</h3>
- **default**：有风险的操作需确认
- **acceptEdits**：自动接受文件编辑，其余仍询问
- **plan**：只读分析，不修改
- **auto**：自动批准安全操作，有风险时提示
- **dontAsk**：除高风险外全部接受
- **bypassPermissions**：全部接受（需 `--dangerously-skip-permissions`）

<h3 id="headless-mode-claude--p">Headless Mode（`claude -p`）</h3>
- CI/CD 集成
- 自动化任务执行
- 批处理

<h3 id="session-management">会话管理（Session Management）</h3>
- 多个工作会话
- 会话切换与保存
- 会话持久化

<h3 id="interactive-features">交互功能（Interactive Features）</h3>
- 键盘快捷键
- 命令历史
- Tab 补全
- 多行输入

<h3 id="configuration">配置（Configuration）</h3>
- 全面的设置管理
- 按环境的配置
- 按项目定制

<h3 id="scheduled-tasks">定时任务（Scheduled Tasks）</h3>
- 使用 `/loop` 的周期性任务
- Cron 工具：CronCreate、CronList、CronDelete
- 自动化周期性工作流

<h3 id="chrome-integration">Chrome 集成（Chrome Integration）</h3>
- 通过无头 Chromium 进行浏览器自动化
- Web 测试与抓取能力
- 页面交互与数据提取

<h3 id="remote-control-expanded">远程控制（扩展说明）（Remote Control）</h3>
- 连接方式与协议
- 安全考量与最佳实践
- 远程访问选项对比表

<h3 id="keyboard-customization">键盘自定义（Keyboard Customization）</h3>
- 自定义快捷键配置
- 多键和弦支持
- 按上下文激活快捷键

<h3 id="desktop-app-expanded">桌面应用（扩展说明）（Desktop App）</h3>
- IDE 集成用 Connectors
- launch.json 配置
- 企业功能与部署

---

<h2 id="10-cli-usage-1-file">10. CLI Usage（1 个文件）</h2>
命令行用法模式与参考。

| File | Description | Content |
|------|-------------|---------|
| `README.md` | CLI 文档 | 标志位、选项与用法模式 |

**主要 CLI 功能**：
- `claude` — 启动交互式会话
- `claude -p "prompt"` — 无头/非交互模式
- `claude web` — 启动 Web 会话
- `claude --model` — 选择模型（Sonnet 4.6、Opus 4.6）
- `claude --permission-mode` — 设置权限模式
- `claude --remote` — 通过 WebSocket 启用远程控制

---

<h2 id="documentation-files-13-files">Documentation Files（13 个文件）</h2>
| File | Location | Description |
|------|----------|-------------|
| `README.md` | `/` | 示例总览 |
| `INDEX.md` | `/` | 本完整索引 |
| `QUICK_REFERENCE.md` | `/` | 速查卡 |
| `README.md` | `/01-slash-commands/` | Slash Commands 指南 |
| `README.md` | `/02-memory/` | Memory 指南 |
| `README.md` | `/03-skills/` | Skills 指南 |
| `README.md` | `/04-subagents/` | Subagents 指南 |
| `README.md` | `/05-mcp/` | MCP 指南 |
| `README.md` | `/06-hooks/` | Hooks 指南 |
| `README.md` | `/07-plugins/` | Plugins 指南 |
| `README.md` | `/08-checkpoints/` | Checkpoints 指南 |
| `README.md` | `/09-advanced-features/` | 高级功能指南 |
| `README.md` | `/10-cli/` | CLI 指南 |

---

<h2 id="complete-file-tree">完整文件树</h2>
```
claude-howto/
├── README.md                                    # 总览
├── INDEX.md                                     # 本文件
├── QUICK_REFERENCE.md                           # 速查卡
├── claude_concepts_guide.md                     # 原始指南
│
├── 01-slash-commands/                           # Slash Commands
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # Memory
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # Skills
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # Subagents
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # MCP Protocol
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # Hooks
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # Plugins
│   ├── pr-review/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── review-pr.md
│   │   │   ├── check-security.md
│   │   │   └── check-tests.md
│   │   ├── agents/
│   │   │   ├── security-reviewer.md
│   │   │   ├── test-checker.md
│   │   │   └── performance-analyzer.md
│   │   ├── mcp/
│   │   │   └── github-config.json
│   │   ├── hooks/
│   │   │   └── pre-review.js
│   │   └── README.md
│   ├── devops-automation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── deploy.md
│   │   │   ├── rollback.md
│   │   │   ├── status.md
│   │   │   └── incident.md
│   │   ├── agents/
│   │   │   ├── deployment-specialist.md
│   │   │   ├── incident-commander.md
│   │   │   └── alert-analyzer.md
│   │   ├── mcp/
│   │   │   └── kubernetes-config.json
│   │   ├── hooks/
│   │   │   ├── pre-deploy.js
│   │   │   └── post-deploy.js
│   │   ├── scripts/
│   │   │   ├── deploy.sh
│   │   │   ├── rollback.sh
│   │   │   └── health-check.sh
│   │   └── README.md
│   ├── documentation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── generate-api-docs.md
│   │   │   ├── generate-readme.md
│   │   │   ├── sync-docs.md
│   │   │   └── validate-docs.md
│   │   ├── agents/
│   │   │   ├── api-documenter.md
│   │   │   ├── code-commentator.md
│   │   │   └── example-generator.md
│   │   ├── mcp/
│   │   │   └── github-docs-config.json
│   │   ├── templates/
│   │   │   ├── api-endpoint.md
│   │   │   ├── function-docs.md
│   │   │   └── adr-template.md
│   │   └── README.md
│   └── README.md
│
├── 08-checkpoints/                              # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # Advanced Features
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # CLI Usage
    └── README.md
```

---

<h2 id="quick-start-by-use-case">按场景快速上手</h2>
<h3 id="code-quality--reviews">代码质量与审查</h3>
```bash
# 安装 slash command
cp 01-slash-commands/optimize.md .claude/commands/

# 安装 subagent
cp 04-subagents/code-reviewer.md .claude/agents/

# 安装 skill
cp -r 03-skills/code-review ~/.claude/skills/

# 或安装完整 plugin
/plugin install pr-review
```

<h3 id="devops--deployment">DevOps 与部署</h3>
```bash
# 安装 plugin（包含全部内容）
/plugin install devops-automation
```

<h3 id="documentation">文档</h3>
```bash
# 安装 slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# 安装 subagent
cp 04-subagents/documentation-writer.md .claude/agents/

# 安装 skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# 或安装完整 plugin
/plugin install documentation
```

<h3 id="team-standards">团队规范</h3>
```bash
# 设置项目 memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 按团队规范编辑
```

<h3 id="external-integrations">外部集成</h3>
```bash
# 设置环境变量
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 安装 MCP 配置（项目级）
cp 05-mcp/multi-mcp.json .mcp.json
```

<h3 id="automation--validation">自动化与校验</h3>
```bash
# 安装 hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 在设置中配置 hooks（~/.claude/settings.json）
# 参见 06-hooks/README.md
```

<h3 id="safe-experimentation">安全实验</h3>
```bash
# 每次用户输入都会自动创建 checkpoint
# 回退：按 Esc+Esc 或使用 /rewind
# 然后在 rewind 菜单中选择要恢复的内容

# 示例见 08-checkpoints/README.md
```

<h3 id="advanced-workflows">高级工作流</h3>
```bash
# 配置高级功能
# 参见 09-advanced-features/config-examples.json

# 使用 planning mode
/plan Implement feature X

# 使用权限模式
claude --permission-mode plan          # 代码审查（只读）
claude --permission-mode acceptEdits   # 自动接受编辑
claude --permission-mode auto          # 自动批准安全操作

# 以无头模式运行（CI/CD）
claude -p "Run tests and report results"

# 后台任务
Run tests in background

# 完整指南见 09-advanced-features/README.md
```

---

<h2 id="feature-coverage-matrix">功能覆盖矩阵</h2>
| Category | Commands | Agents | MCP | Hooks | Scripts | Templates | Docs | Images | Total |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **01 Slash Commands** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 Memory** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 Skills** | - | - | - | - | 5 | 9 | 1 | - | **28** |
| **04 Subagents** | - | 8 | - | - | - | - | 1 | - | **9** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 Hooks** | - | - | - | 8 | - | - | 1 | - | **9** |
| **07 Plugins** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **40** |
| **08 Checkpoints** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 Advanced** | - | - | - | - | - | - | 1 | 2 | **3** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

<h2 id="learning-path">学习路径</h2>
<h3 id="beginner-week-1">入门（第 1 周）</h3>
1. ✅ 阅读 `README.md`
2. ✅ 安装 1–2 个 slash command
3. ✅ 创建项目 memory 文件
4. ✅ 试用基础命令

<h3 id="intermediate-week-2-3">进阶（第 2–3 周）</h3>
1. ✅ 配置 GitHub MCP
2. ✅ 安装一个 subagent
3. ✅ 尝试委派任务
4. ✅ 安装一个 skill

<h3 id="advanced-week-4">高级（第 4 周起）</h3>
1. ✅ 安装完整 plugin
2. ✅ 创建自定义 slash command
3. ✅ 创建自定义 subagent
4. ✅ 创建自定义 skill
5. ✅ 构建自己的 plugin

<h3 id="expert-week-5">专家（第 5 周起）</h3>
1. ✅ 配置 hooks 实现自动化
2. ✅ 使用 checkpoint 做实验
3. ✅ 配置 planning mode
4. ✅ 有效使用权限模式
5. ✅ 为 CI/CD 配置无头模式
6. ✅ 掌握会话管理

---

<h2 id="search-by-keyword">按关键词检索</h2>
<h3 id="performance">性能</h3>
- `01-slash-commands/optimize.md` — 性能分析
- `04-subagents/code-reviewer.md` — 性能审查
- `03-skills/code-review/` — 性能指标
- `07-plugins/pr-review/agents/performance-analyzer.md` — 性能专项

<h3 id="security">安全</h3>
- `04-subagents/secure-reviewer.md` — 安全审查
- `03-skills/code-review/` — 安全分析
- `07-plugins/pr-review/` — 安全检查

<h3 id="testing">测试</h3>
- `04-subagents/test-engineer.md` — 测试工程师
- `07-plugins/pr-review/commands/check-tests.md` — 测试覆盖

<h3 id="documentation-1">文档</h3>
- `01-slash-commands/generate-api-docs.md` — API 文档命令
- `04-subagents/documentation-writer.md` — 文档撰写 agent
- `03-skills/doc-generator/` — 文档生成 skill
- `07-plugins/documentation/` — 完整文档 plugin

<h3 id="deployment">部署</h3>
- `07-plugins/devops-automation/` — 完整 DevOps 方案

<h3 id="automation">自动化</h3>
- `06-hooks/` — 事件驱动自动化
- `06-hooks/pre-commit.sh` — 提交前自动化
- `06-hooks/format-code.sh` — 自动格式化
- `09-advanced-features/` — 用于 CI/CD 的无头模式

<h3 id="validation">校验</h3>
- `06-hooks/security-scan.sh` — 安全校验
- `06-hooks/validate-prompt.sh` — 提示校验

<h3 id="experimentation">实验</h3>
- `08-checkpoints/` — 通过 rewind 安全实验
- `08-checkpoints/checkpoint-examples.md` — 真实场景示例

<h3 id="planning">规划</h3>
- `09-advanced-features/planning-mode-examples.md` — Planning mode 示例
- `09-advanced-features/README.md` — Extended Thinking

<h3 id="configuration-1">配置</h3>
- `09-advanced-features/config-examples.json` — 配置示例

---

<h2 id="notes">说明</h2>
- 所有示例均可直接使用
- 请按实际需求修改
- 示例遵循 Claude Code 最佳实践
- 每个分类都有独立的 README，含详细说明
- 脚本包含适当的错误处理
- 模板可自定义

---

<h2 id="contributing">参与贡献</h2>
希望补充更多示例？请遵循以下结构：
1. 创建合适的子目录
2. 附带含用法的 README.md
3. 遵循命名约定
4. 充分测试
5. 更新本索引

---

**最后更新**：2026 年 3 月  
**示例总数**：100+ 个文件  
**分类**：10 项功能  
**Hooks**：8 个自动化脚本  
**配置示例**：10+ 种场景  
**开箱即用**：所有示例
