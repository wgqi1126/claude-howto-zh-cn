<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

<a id="advanced-features"></a>
# 高级功能

Claude Code 高级能力全面指南，涵盖 Planning Mode（规划模式）、Extended Thinking（扩展思考）、Auto Mode（自动模式）、后台任务、权限模式、Print mode（`claude -p`，非交互）、会话管理、交互功能、Channels、语音听写、Remote Control、Web Sessions、Desktop App、任务列表、提示建议、Git worktrees、沙箱、托管设置与配置。

<a id="table-of-contents"></a>
## 目录

1. [概述](#overview)
2. [Planning Mode（规划模式）](#planning-mode)
3. [Extended Thinking（扩展思考）](#extended-thinking)
4. [Auto Mode（自动模式）](#auto-mode)
5. [后台任务](#background-tasks)
6. [定时任务](#scheduled-tasks)
7. [权限模式](#permission-modes)
8. [Headless Mode / Print mode（无头与打印模式）](#headless-mode)
9. [会话管理](#session-management)
10. [交互功能](#interactive-features)
11. [语音听写](#voice-dictation)
12. [Channels（通道）](#channels)
13. [Chrome 集成](#chrome-integration)
14. [Remote Control（远程控制）](#remote-control)
15. [Web Sessions（网页会话）](#web-sessions)
16. [Desktop App（桌面应用）](#desktop-app)
17. [任务列表](#task-list)
18. [提示建议](#prompt-suggestions)
19. [Git Worktrees（Git 工作树）](#git-worktrees)
20. [沙箱](#sandboxing)
21. [托管设置（企业版）](#managed-settings-enterprise)
22. [配置与设置](#configuration-and-settings)
23. [最佳实践](#best-practices)
24. [相关资源](#related-concepts)

---

<a id="overview"></a>
## 概述

Claude Code 的高级功能在核心能力之上扩展了规划、推理、自动化与控制机制，便于在复杂开发任务、代码审查、自动化与多会话管理等场景下使用更精细的工作流。

**主要高级功能包括：**
- **Planning Mode**：在写代码前先产出可审阅、可批准的详细实现计划
- **Extended Thinking**：对复杂问题做更深入推理
- **Auto Mode**：后台安全分类器在每次执行前审查动作（Research Preview）
- **后台任务**：长时间操作不阻塞对话
- **权限模式**：控制 Claude 可执行的操作（`default`、`acceptEdits`、`plan`、`auto`、`dontAsk`、`bypassPermissions`）
- **Print mode**：以非交互方式运行 Claude Code，用于自动化与 CI/CD（`claude -p`）
- **会话管理**：管理多个工作会话
- **交互功能**：快捷键、多行输入、命令历史
- **语音听写**：按住说话，支持 20 种语言的 STT
- **Channels**：MCP 服务器向运行中的会话推送消息（Research Preview）
- **Remote Control**：在 Claude.ai 或 Claude 应用中控制本机的 Claude Code
- **Web Sessions**：在 claude.ai/code 浏览器中运行 Claude Code
- **Desktop App**：独立应用，支持可视化 diff、多会话等
- **任务列表**：在上下文压缩后仍保留任务跟踪
- **提示建议**：根据上下文智能建议命令
- **Git Worktrees**：隔离的 worktree 分支并行开发
- **沙箱**：操作系统级文件系统与网络隔离
- **托管设置**：通过 plist、注册表或托管文件进行企业部署
- **配置**：通过 JSON 配置文件自定义行为

---

<a id="planning-mode"></a>
## Planning Mode（规划模式）

Planning Mode 让 Claude 在实现前先梳理复杂任务，生成你可审阅并批准的详细计划。

### Planning Mode 是什么？

Planning Mode 分为两阶段：
1. **规划阶段**：Claude 分析任务并生成详细实现计划
2. **实现阶段**：你批准后，Claude 按计划执行

### 何时使用 Planning Mode

✅ 适合使用 Planning Mode 的场景：
- 复杂的多文件重构
- 新功能实现
- 架构调整
- 数据库迁移
- 大型 API 改版

❌ 不必使用 Planning Mode 的场景：
- 简单 bug 修复
- 仅格式调整
- 单文件小改
- 快速问答

### 如何启用 Planning Mode

**Slash command**：
```bash
/plan Implement user authentication system
```

**CLI 参数**：
```bash
claude --permission-mode plan
```

**设为默认**：
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**快捷键**：
- `Shift + Tab` — 在权限模式间切换（含 plan）
- `Alt + M` — 在权限模式间切换（Windows/Linux）

### Planning Mode 的优势

- **结构化实现**：把实现步骤拆细
- **审阅与批准**：执行前可批准或调整计划
- **风险识别**：在动手前发现潜在问题
- **阶段清晰**：分阶段与里程碑组织实现

### 示例：功能实现

```
User: /plan Add a real-time notification system

Claude: 我会为实时通知功能制定实现计划。

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Install WebSocket libraries (socket.io)
2. Set up WebSocket server
3. Configure connection management

### Phase 2: Backend Implementation
4. Create notification service
5. Implement notification queue
6. Add database schema for notifications
7. Create API endpoints

### Phase 3: Frontend Integration
8. Set up WebSocket client
9. Create notification UI components
10. Implement notification state management
11. Add notification permissions

### Phase 4: Testing & Deployment
12. Write unit tests
13. Write integration tests
14. Update documentation
15. Deploy to staging

预计时间：3–4 小时
需修改文件：12
需新建文件：8

是否继续？(yes/no/modify plan)

User: yes

Claude: [按计划开始实现]
```

### 修改计划

```
User: 修改计划 — 暂时跳过队列，以后再补

Claude: 已更新计划：
[展示去掉队列后的修改版计划]

User: 可以，继续

Claude: [按修改后的计划实现]
```

### Planning Mode 配置

通过 CLI 参数或 slash command 启用 Planning Mode：

```bash
# 通过 CLI 激活 plan 模式
claude --permission-mode plan

# 或在 REPL 内使用 /plan
/plan Implement user authentication system
```

**规划用模型别名**：使用 `opusplan` 作为模型别名，规划用 Opus、执行用 Sonnet：

```bash
claude --model opusplan "design and implement the new API"
```

**在外部编辑器中编辑计划**：按 `Ctrl+G` 可在系统默认编辑器中打开当前计划，便于细改。

---

<a id="extended-thinking"></a>
## Extended Thinking（扩展思考）

Extended Thinking 让 Claude 在给出答案前花更多时间推理复杂问题。

### Extended Thinking 是什么？

Extended Thinking 是一种有意识的逐步推理过程，Claude 会：
- 拆解复杂问题
- 比较多种方案
- 权衡取舍
- 推演边界情况

### 如何启用 Extended Thinking

**快捷键**：
- `Option + T`（macOS）/ `Alt + T`（Windows/Linux）— 开关 Extended Thinking

**自动启用**：
- 默认对所有模型开启（Opus 4.6、Sonnet 4.6、Haiku 4.5）
- Opus 4.6：自适应推理，力度档位：`low`（○）、`medium`（◐）、`high`（●）、`max`（仅 Opus 4.6）
- 其他模型：固定预算，最高 31,999 tokens

**配置方式**：
- 开关：`Alt+T` / `Option+T`，或通过 `/config`
- 查看推理：`Ctrl+O`（verbose 模式）
- 设置力度：`/effort` 命令或 `--effort` 参数

**自定义预算**：
```bash
export MAX_THINKING_TOKENS=1024
```

**力度档位**（仅 Opus 4.6）：
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○), medium (◐), high (●), or max (Opus 4.6 only)
```

**CLI 参数**：
```bash
claude --effort high "complex architectural review"
```

**Slash command**：
```
/effort high
```

> **说明：** 提示词中的关键词 `ultrathink` 会触发深度推理模式。力度 `low`、`medium`、`high`、`max`（仅 Opus 4.6）控制 Claude 进行推理的量级。

### Extended Thinking 的优势

- **深度推理**：在复杂问题上投入更多思考
- **更好的架构决策**：充分评估后再做选择
- **考虑边界情况**：预先想到潜在问题与场景
- **分析更完整**：结构化处理复杂问题

### 示例：架构决策

```
User: /think Should we use microservices or a monolith for our e-commerce platform?

Claude: 让我仔细推演这项架构决策……

<extended_thinking>
## Context Analysis
- 团队规模：5 名开发者
- 预期流量：初期约 1 万日活
- 需扩展至 10 万+ 用户
- DevOps 资源有限
- MVP 时间线 6 个月

## Approach 1: Microservices
优点：
+ 可独立扩缩
+ 技术栈灵活
+ 团队可并行
+ 故障隔离

缺点：
- 运维复杂度高
- 网络开销
- 需要分布式追踪
- 需要 DevOps 能力
- 初期开发较慢

## Approach 2: Monolith
优点：
+ 部署更简单
+ 初期开发更快
+ 调试更容易
+ 运维负担更低
+ 单一代码库

缺点：
- 后期扩展难
- 全量部署
- 技术栈锁定
- 易出现紧耦合

## Decision Factors
1. 团队规模（5 人）→ 倾向单体
2. DevOps 资源（有限）→ 倾向单体
3. 时间线（6 个月）→ 倾向单体
4. 未来规模（10 万用户）→ 单体 + 缓存可达标
5. 复杂度预算 → 有限

## Recommendation
从 **模块化单体（modular monolith）** 起步：
- 单一部署单元
- 清晰的模块边界
- 模块间接口干净
- 若需要可再拆出微服务

这样可获得：
✓ 初期开发快
✓ 运维复杂度低
✓ 日后可再拆服务
✓ 架构清晰

迁移路径：当用户达 5 万+ 或某模块需独立扩缩时，再将对应模块拆为微服务。
</extended_thinking>

**Recommendation**：采用边界清晰的模块化单体。

该方案在团队规模、时间线与 DevOps 约束下兼顾未来扩展；有明确业务需要时，可再将部分模块迁到微服务。
```

### Extended Thinking 配置

通过环境变量、快捷键与 CLI 参数控制 Extended Thinking：

```bash
# 设置思考 token 预算
export MAX_THINKING_TOKENS=16000

# 设置力度档位（仅 Opus 4.6）：low (○)、medium (◐)、high (●) 或 max（仅 Opus 4.6）
export CLAUDE_CODE_EFFORT_LEVEL=high
```

会话中可用 `Alt+T` / `Option+T` 切换，用 `/effort` 设置力度，或通过 `/config` 配置。

---

<a id="auto-mode"></a>
## Auto Mode（自动模式）

Auto Mode 是一种 Research Preview 权限模式（2026 年 3 月），使用后台安全分类器在每次执行前审查动作；在允许 Claude 自主工作的同时拦截危险操作。

### 要求

- **套餐**：Team plan（Enterprise 与 API 逐步推出）
- **模型**：Claude Sonnet 4.6 或 Opus 4.6
- **分类器**：在 Claude Sonnet 4.6 上运行（会产生额外 token 成本）

### 启用 Auto Mode

```bash
# 用 CLI 标志解锁 auto 模式
claude --enable-auto-mode

# 然后在 REPL 中用 Shift+Tab 切到该模式
```

或将其设为默认权限模式：

```bash
claude --permission-mode auto
```

通过配置设置：

```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### 分类器如何工作

后台分类器按以下顺序决策：

1. **允许/拒绝规则** — 先检查显式权限规则
2. **只读/编辑自动通过** — 读文件与编辑自动通过
3. **分类器** — 后台分类器审查该动作
4. **回退** — 连续 3 次或累计 20 次被拦截后，回退为向用户确认

### 默认拦截的操作

Auto Mode 默认会拦截：

| 被拦截的操作 | 示例 |
|----------------|---------|
| 管道到 shell 的安装 | `curl \| bash` |
| 向外发送敏感数据 | API 密钥、凭据经网络外发 |
| 生产环境部署 | 指向生产的部署命令 |
| 大批量删除 | 对大目录执行 `rm -rf` |
| IAM 变更 | 权限与角色修改 |
| 向 main 强推 | `git push --force origin main` |

### 默认允许的操作

| 允许的操作 | 示例 |
|----------------|---------|
| 本地文件操作 | 读、写、编辑项目文件 |
| 声明式依赖安装 | 按清单执行 `npm install`、`pip install` |
| 只读 HTTP | 用 `curl` 拉取文档 |
| 推送到当前分支 | `git push origin feature-branch` |

### 配置 Auto Mode

**以 JSON 打印默认规则**：
```bash
claude auto-mode defaults
```

**配置可信基础设施**：企业部署可通过托管设置 `autoMode.environment` 定义可信 CI/CD 环境、部署目标与基础设施模式。

### 回退行为

分类器不确定时，Auto Mode 会改为提示用户：
- **连续 3 次**被分类器拦截后
- 或会话内分类器累计拦截 **20 次**后

从而在分类器无法自信批准时，仍由你保留控制权。

### 种子化与 Auto Mode 等效的权限（无需 Team plan）

若没有 Team plan，或希望不用后台分类器、采用更简单的方式，可在 `~/.claude/settings.json` 中写入偏保守的安全权限规则作为基线。脚本从只读与本地检查类规则开始，再按需让你选择是否加入编辑、测试、本地 git 写入、包安装与 GitHub 写入等能力。

**文件：** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# 预览将添加的内容（不写文件）
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# 应用偏保守的基线
python3 09-advanced-features/setup-auto-mode-permissions.py

# 仅在需要时增加更多能力
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

脚本会在以下类别下添加规则：

| 类别 | 示例 |
|----------|---------|
| 核心只读工具 | `Read(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)`, `WebFetch(*)` |
| 本地检查 | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)`, `Bash(cat:*)` |
| 可选编辑 | `Edit(*)`, `Write(*)`, `NotebookEdit(*)` |
| 可选测试/构建 | `Bash(pytest:*)`, `Bash(python3 -m pytest:*)`, `Bash(cargo test:*)` |
| 可选 git 写入 | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git stash:*)` |
| Git（本地写入） | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| 包管理器 | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| 构建与测试 | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| 常用 shell | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

危险操作（`rm -rf`、`sudo`、强推、`DROP TABLE`、`terraform destroy` 等）有意不包含。脚本具有幂等性 — 多次运行不会产生重复规则。

---

<a id="background-tasks"></a>
## 后台任务

后台任务让长时间运行的操作在后台执行，不阻塞当前对话。

### 后台任务是什么？

后台任务异步运行，你仍可继续操作：
- 长时间测试套件
- 构建流程
- 数据库迁移
- 部署脚本
- 分析工具

**基本用法：**
```bash
User: Run tests in background

Claude: 已启动任务 bg-1234

/task list           # 列出所有任务
/task status bg-1234 # 查看进度
/task show bg-1234   # 查看输出
/task cancel bg-1234 # 取消任务
```

### 启动后台任务

```
User: Run the full test suite in the background

Claude: 正在后台运行测试（task-id: bg-1234）
测试运行期间你可以继续工作。

[可继续对话]

User: Meanwhile, let's refactor the auth module

Claude: [在后台跑测试的同时处理 auth 模块]

[测试完成后]

Claude: 📢 后台任务 bg-1234 已完成：
✅ 245 个测试通过
❌ 3 个测试失败
查看结果：/task show bg-1234
```

### 管理后台任务

**列出活动任务**：
```
User: /task list

活动后台任务：
1. [bg-1234] 运行测试中（约 50% 完成，剩余约 2 分钟）
2. [bg-1235] 构建 Docker 镜像中（约 25% 完成，剩余约 8 分钟）
3. [bg-1236] 部署到 staging 中（约 90% 完成，剩余约 30 秒）
```

**查看任务状态**：
```
User: /task status bg-1234

Task bg-1234: Running tests
Status: In progress
Progress: 120/245 tests (49%)
Started: 2025-11-08 10:30:15
Estimated completion: 2025-11-08 10:34:22
```

**查看任务输出**：
```
User: /task show bg-1234

[Shows live output from the test run]
```

**取消任务**：
```
User: /task cancel bg-1234

Cancelled background task bg-1234
```

### 示例：并行开发

```
User: Run the build in the background

Claude: Starting build... (task-id: bg-5001)

User: Also run the linter in background

Claude: Starting linter... (task-id: bg-5002)

User: While those run, let's implement the new API endpoint

Claude: [Implements API endpoint while build and linter run]

[10 minutes later]

Claude: 📢 Build completed successfully (bg-5001)
📢 Linter found 12 issues (bg-5002)

User: Show me the linter issues

Claude: [Shows linter output from bg-5002]
```

### 配置

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

<a id="scheduled-tasks"></a>
## 定时任务

定时任务可按固定间隔或一次性提醒自动执行提示。任务与会话绑定 — 仅在 Claude Code 活跃时运行，会话结束即清除。自 v2.1.72+ 起提供。

### `/loop` 命令

```bash
# Explicit interval
/loop 5m check if the deployment finished

# Natural language
/loop check build status every 30 minutes
```

也支持标准 5 字段 cron 表达式以实现精确调度。

### 一次性提醒

在指定时间只触发一次的提醒：

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### 管理定时任务

| 工具 | 说明 |
|------|-------------|
| `CronCreate` | 创建新的定时任务 |
| `CronList` | 列出所有活动定时任务 |
| `CronDelete` | 移除定时任务 |

**限制与行为**：
- 每个会话最多 **50** 个定时任务
- 与会话绑定 — 会话结束即清除
- 重复任务在 **3 天**后自动过期
- 仅在 Claude Code 运行时触发 — 错过的执行不会补跑

### 行为细节

| 方面 | 说明 |
|--------|--------|
| **重复任务抖动** | 间隔的最多 10%（最长 15 分钟） |
| **单次抖动** | 在整点/:30 边界最多 90 秒 |
| **错过触发** | 不补跑 — 若当时未运行 Claude Code 则跳过 |
| **持久化** | 重启后不保留 |

### Cloud 定时任务

使用 `/schedule` 创建在 Anthropic 基础设施上运行的 Cloud 定时任务：

```
/schedule daily at 9am run the test suite and report failures
```

Cloud 定时任务在重启后仍保留，且不要求本机一直运行 Claude Code。

### 禁用定时任务

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

### 示例：监控部署

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **提示**：定时任务与会话绑定。若需要重启后仍存在的自动化，请改用 CI/CD、GitHub Actions 或 Desktop App 中的定时任务。

---

<a id="permission-modes"></a>
## 权限模式

权限模式控制 Claude 在无需你逐项确认时可执行哪些操作。

### 可用权限模式

| 模式 | 行为 |
|---|---|
| `default` | 仅读文件；其他操作均需确认 |
| `acceptEdits` | 读并编辑文件；命令仍需确认 |
| `plan` | 仅读文件（调研模式，不编辑） |
| `auto` | 所有动作经后台安全分类器检查（Research Preview） |
| `bypassPermissions` | 所有动作，不做权限检查（危险） |
| `dontAsk` | 仅预先批准的工具会执行；其余拒绝 |

在 CLI 中用 `Shift+Tab` 循环切换。用 `--permission-mode` 或 `permissions.defaultMode` 设置默认模式。

### 启用方式

**快捷键**：
```bash
Shift + Tab  # Cycle through all 6 modes
```

**Slash command**：
```bash
/plan                  # Enter plan mode
```

**CLI 参数**：
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**设置**：
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### 权限模式示例

#### default 模式
重要操作会请求确认：

```
User: Fix the bug in auth.ts

Claude: I need to modify src/auth.ts to fix the bug.
The change will update the password validation logic.

Approve this change? (yes/no/show)
```

#### plan 模式
执行前先审阅实现计划：

```
User: /plan Implement user authentication system

Claude: I'll create a plan for implementing authentication.

## Implementation Plan
[Detailed plan with phases and steps]

Ready to proceed? (yes/no/modify)
```

#### acceptEdits 模式
自动接受文件修改：

```
User: acceptEdits
User: Fix the bug in auth.ts

Claude: [Makes changes without asking]
```

### 使用场景

**代码审查**：
```
User: claude --permission-mode plan
User: Review this PR and suggest improvements

Claude: [Reads code, provides feedback, but cannot modify]
```

**结对编程**：
```
User: claude --permission-mode default
User: Let's implement the feature together

Claude: [Asks for approval before each change]
```

**自动化任务**：
```
User: claude --permission-mode acceptEdits
User: Fix all linting issues in the codebase

Claude: [Auto-accepts file edits without asking]
```

---

<a id="headless-mode"></a>
## Headless Mode / Print mode（无头与打印模式）

Print mode（`claude -p`）让 Claude Code 在无交互输入下运行，适合自动化与 CI/CD。这是非交互模式，取代较早的 `--headless` 参数。

### Print mode 是什么？

Print mode 适用于：
- 自动化脚本执行
- 接入 CI/CD
- 批处理
- 定时任务

### 以 Print mode 运行（非交互）

```bash
# Run specific task
claude -p "Run all tests"

# Process piped content
cat error.log | claude -p "Analyze these errors"

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### Print mode 更多示例

```bash
# Run a specific task with output capture
claude -p "Run all tests and generate coverage report"

# With structured output
claude -p --output-format json "Analyze code quality"

# With input from stdin
echo "Analyze code quality" | claude -p "explain this"
```

### 示例：CI/CD 集成

**GitHub Actions**：
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for:
            - Code quality issues
            - Security vulnerabilities
            - Performance concerns
            - Test coverage
            Output results as JSON" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: JSON.stringify(review, null, 2)
            });
```

### Print mode 配置

Print mode（`claude -p`）支持多种自动化相关参数：

```bash
# Limit autonomous turns
claude -p --max-turns 5 "refactor this module"

# Structured JSON output
claude -p --output-format json "analyze this codebase"

# With schema validation
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# Disable session persistence
claude -p --no-session-persistence "one-off analysis"
```

---

<a id="session-management"></a>
## 会话管理

高效管理多个 Claude Code 会话。

### 会话管理命令

| 命令 | 说明 |
|---------|-------------|
| `/resume` | 按 ID 或名称恢复对话 |
| `/rename` | 为当前会话命名 |
| `/fork` | 将当前会话分叉为新分支 |
| `claude -c` | 继续最近一次对话 |
| `claude -r "session"` | 按名称或 ID 恢复会话 |

### 恢复会话

**继续上一次对话**：
```bash
claude -c
```

**按名称恢复会话**：
```bash
claude -r "auth-refactor" "finish this PR"
```

**重命名当前会话**（在 REPL 内）：
```
/rename auth-refactor
```

### 分叉会话

分叉会话可在不丢失原会话的前提下尝试其他方案：

```
/fork
```

或从 CLI：
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### 会话持久化

会话会自动保存，并可恢复：

```bash
# Continue last conversation
claude -c

# Resume specific session by name or ID
claude -r "auth-refactor"

# Resume and fork for experimentation
claude --resume auth-refactor --fork-session "alternative approach"
```

---

<a id="interactive-features"></a>
## 交互功能

### 快捷键

Claude Code 提供多种快捷键以提高效率。以下为官方文档中的完整参考：

| 快捷键 | 说明 |
|----------|-------------|
| `Ctrl+C` | 取消当前输入/生成 |
| `Ctrl+D` | 退出 Claude Code |
| `Ctrl+G` | 在外部编辑器中编辑计划 |
| `Ctrl+L` | 清屏 |
| `Ctrl+O` | 切换 verbose 输出（查看推理） |
| `Ctrl+R` | 反向搜索历史 |
| `Ctrl+T` | 切换任务列表视图 |
| `Ctrl+B` | 后台运行中的任务 |
| `Esc+Esc` | 回退代码/对话 |
| `Shift+Tab` / `Alt+M` | 切换权限模式 |
| `Option+P` / `Alt+P` | 切换模型 |
| `Option+T` / `Alt+T` | 开关 Extended Thinking |

**行编辑（标准 readline 快捷键）：**

| 快捷键 | 作用 |
|----------|--------|
| `Ctrl + A` | 光标移到行首 |
| `Ctrl + E` | 光标移到行尾 |
| `Ctrl + K` | 剪切到行尾 |
| `Ctrl + U` | 剪切到行首 |
| `Ctrl + W` | 向后删除一词 |
| `Ctrl + Y` | 粘贴（yank） |
| `Tab` | 自动补全 |
| `↑ / ↓` | 命令历史 |

### 自定义键位

运行 `/keybindings` 可打开 `~/.claude/keybindings.json` 进行编辑（v2.1.18+）。

**配置格式**：

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    },
    {
      "context": "Confirmation",
      "bindings": {
        "ctrl+a": "confirmation:yes"
      }
    }
  ]
}
```

将绑定设为 `null` 可解除默认快捷键。

### 可用 Context

键位按界面 Context 划分作用域：

| Context | 键动作 |
|---------|-------------|
| **Chat** | `submit`, `cancel`, `cycleMode`, `modelPicker`, `thinkingToggle`, `undo`, `externalEditor`, `stash`, `imagePaste` |
| **Confirmation** | `yes`, `no`, `previous`, `next`, `nextField`, `cycleMode`, `toggleExplanation` |
| **Global** | `interrupt`, `exit`, `toggleTodos`, `toggleTranscript` |
| **Autocomplete** | `accept`, `dismiss`, `next`, `previous` |
| **HistorySearch** | `search`, `previous`, `next` |
| **Settings** | 设置页内导航 |
| **Tabs** | 标签切换与管理 |
| **Help** | 帮助面板导航 |

共 18 个 context，另含 `Transcript`、`Task`、`ThemePicker`、`Attachments`、`Footer`、`MessageSelector`、`DiffDialog`、`ModelPicker`、`Select` 等。

### 组合键（Chord）

键位支持 chord（多键序列）：

```
"ctrl+k ctrl+s"   → Two-key sequence: press ctrl+k, then ctrl+s
"ctrl+shift+p"    → Simultaneous modifier keys
```

**按键语法**：
- **修饰键**：`ctrl`、`alt`（或 `opt`）、`shift`、`meta`（或 `cmd`）
- **大写表示含 Shift**：`K` 等价于 `shift+k`
- **特殊键**：`escape`、`enter`、`return`、`tab`、`space`、`backspace`、`delete`、方向键等

### 保留与冲突按键

| 键 | 状态 | 说明 |
|-----|--------|-------|
| `Ctrl+C` | 保留 | 不可改绑（中断） |
| `Ctrl+D` | 保留 | 不可改绑（退出） |
| `Ctrl+B` | 终端冲突 | tmux 前缀键 |
| `Ctrl+A` | 终端冲突 | GNU Screen 前缀键 |
| `Ctrl+Z` | 终端冲突 | 进程挂起 |

> **提示**：若快捷键无效，请检查是否与终端模拟器或多路复用器冲突。

### Tab 补全

Claude Code 提供智能 Tab 补全：

```
User: /rew<TAB>
→ /rewind

User: /plu<TAB>
→ /plugin

User: /plugin <TAB>
→ /plugin install
→ /plugin enable
→ /plugin disable
```

### 命令历史

访问先前命令：

```
User: <↑>  # Previous command
User: <↓>  # Next command
User: Ctrl+R  # Search history

(reverse-i-search)`test': run all tests
```

### 多行输入

复杂查询可使用多行模式：

```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

**示例：**

```
User: \
> Implement a user authentication system
> with the following requirements:
> - JWT tokens
> - Email verification
> - Password reset
> - 2FA support
> \end

Claude: [Processes the multi-line request]
```

### 行内编辑

发送前可编辑命令：

```
User: Deploy to prodcution<Backspace><Backspace>uction

[Edit in-place before sending]
```

### Vim 模式

可为文本编辑启用 Vi/Vim 键位：

**启用**：
- 使用 `/vim` 或 `/config` 开启
- 用 `Esc` 进入 NORMAL，用 `i`/`a`/`o` 进入 INSERT

**移动**：
- `h` / `l` — 左/右
- `j` / `k` — 下/上
- `w` / `b` / `e` — 按词移动
- `0` / `$` — 行首/行尾
- `gg` / `G` — 文首/文末

**文本对象**：
- `iw` / `aw` — 词内/含空格
- `i"` / `a"` — 引号内/含引号
- `i(` / `a(` — 括号内/含括号

### Bash 模式

使用 `!` 前缀直接执行 shell 命令：

```bash
! npm test
! git status
! cat src/index.js
```

用于快速执行命令而无需切换上下文。

---

<a id="voice-dictation"></a>
## 语音听写

语音听写为 Claude Code 提供按住说话的语音输入，可用语音代替打字输入提示。

### 启用语音听写

```
/voice
```

### 功能

| 功能 | 说明 |
|---------|-------------|
| **Push-to-talk** | 按住键录音，松开发送 |
| **20 languages** | 语音转文字支持 20 种语言 |
| **Custom keybinding** | 通过 `/keybindings` 配置按住说话键 |
| **Account requirement** | STT 处理需要 Claude.ai 账号 |

### 配置

在键位文件（`/keybindings`）中自定义按住说话键。语音听写使用你的 Claude.ai 账号进行语音转文字处理。

---

<a id="channels"></a>
## Channels（通道）

Channels（Research Preview）允许 MCP 服务器向运行中的 Claude Code 会话推送消息，便于与外部服务实时集成。

### 订阅 Channels

```bash
# Subscribe to channel plugins at startup
claude --channels discord,telegram
```

### 支持的集成

| 集成 | 说明 |
|-------------|-------------|
| **Discord** | 在会话中接收并回复 Discord 消息 |
| **Telegram** | 在会话中接收并回复 Telegram 消息 |

### 配置

企业部署的**托管设置**：

```json
{
  "allowedChannelPlugins": ["discord", "telegram"]
}
```

`allowedChannelPlugins` 托管设置控制组织内允许使用的 channel 插件。

### 工作原理

1. MCP 服务器作为 channel 插件连接外部服务
2. 入站消息被推入当前活动的 Claude Code 会话
3. Claude 可在会话上下文中阅读并回复消息
4. Channel 插件须通过 `allowedChannelPlugins` 托管设置批准

---

<a id="chrome-integration"></a>
## Chrome 集成

Chrome 集成将 Claude Code 连接到你的 Chrome 或 Microsoft Edge 浏览器，用于实时网页自动化与调试。自 v2.0.73+ 起为 beta 功能（Edge 支持自 v1.0.36+）。

### 启用 Chrome 集成

**启动时**：

```bash
claude --chrome      # Enable Chrome connection
claude --no-chrome   # Disable Chrome connection
```

**会话内**：

```
/chrome
```

选择「Enabled by default」可在后续会话默认启用 Chrome 集成。Claude Code 会共享浏览器的登录状态，因此可操作需登录的 Web 应用。

### 能力

| 能力 | 说明 |
|------------|-------------|
| **Live debugging** | 读控制台、检查 DOM、实时调试 JavaScript |
| **Design verification** | 将渲染结果与设计稿对比 |
| **Form validation** | 测表单提交、输入校验与错误处理 |
| **Web app testing** | 操作已登录应用（Gmail、Google Docs、Notion 等） |
| **Data extraction** | 抓取并处理网页内容 |
| **Session recording** | 将浏览器操作录为 GIF |

### 站点级权限

Chrome 扩展按站点管理访问权限。可随时在扩展弹窗中为各站点授予或撤销权限。Claude Code 仅会操作你明确允许的站点。

### 工作原理

Claude Code 在可见窗口中控制浏览器 — 你可实时看到操作。遇到登录页或验证码时，Claude 会暂停并等待你手动处理后再继续。

### 已知限制

- **浏览器支持**：仅 Chrome 与 Edge — Brave、Arc 等 Chromium 变体不支持
- **WSL**：Windows Subsystem for Linux 中不可用
- **第三方提供商**：与 Bedrock、Vertex 或 Foundry API 提供商不兼容
- **Service worker 空闲**：长时间会话中 Chrome 扩展的 service worker 可能进入空闲

> **提示**：Chrome 集成为 beta 功能，后续版本可能扩大浏览器支持范围。

---

<a id="remote-control"></a>
## Remote Control（远程控制）

Remote Control 让你在手机、平板或任意浏览器上继续本机正在运行的 Claude Code 会话。会话仍在你的机器上运行 — 不会迁到云端。适用于 Pro、Max、Team 与 Enterprise 套餐（v2.1.51+）。

### 启动 Remote Control

**从 CLI**：

```bash
# Start with default session name
claude remote-control

# Start with a custom name
claude remote-control --name "Auth Refactor"
```

**在会话内**：

```
/remote-control
/remote-control "Auth Refactor"
```

**可用参数**：

| 参数 | 说明 |
|------|-------------|
| `--name "title"` | 自定义会话标题，便于识别 |
| `--verbose` | 输出详细连接日志 |
| `--sandbox` | 启用文件系统与网络隔离 |
| `--no-sandbox` | 关闭沙箱（默认） |

### 连接会话

从其他设备连接有三种方式：

1. **会话 URL** — 会话启动时打印在终端；可在任意浏览器打开
2. **二维码** — 启动后按空格显示可扫描的二维码
3. **按名称查找** — 在 claude.ai/code 或 Claude 移动应用（iOS/Android）中浏览会话

### 安全

- **不开放入站端口** 到本机
- **仅出站 HTTPS**，经 TLS
- **限定凭据** — 多个短时、窄范围 token
- **会话隔离** — 各远程会话相互独立

### Remote Control 与网页版 Claude Code

| 方面 | Remote Control | Claude Code on Web |
|--------|---------------|-------------------|
| **执行位置** | 在你本机运行 | 在 Anthropic 云端运行 |
| **本地工具** | 可完整使用本机 MCP、文件与 CLI | 无本地依赖 |
| **适用场景** | 从其他设备继续本机工作 | 在任意浏览器从零开始 |

### 限制

- 每个 Claude Code 实例仅一个远程会话
- 主机上终端须保持打开
- 网络不可达约 10 分钟后会话超时

### 使用场景

- 离开座位时用手机或平板控制 Claude Code
- 使用更丰富的 claude.ai 界面，同时保留本机工具执行
- 在完整本地开发环境下随时做代码审查

---

<a id="web-sessions"></a>
## Web Sessions（网页会话）

Web Sessions 让你在浏览器 claude.ai/code 中直接运行 Claude Code，也可从 CLI 创建网页会话。

### 创建 Web Session

```bash
# Create a new web session from the CLI
claude --remote "implement the new API endpoints"
```

这会在 claude.ai 上启动可通过任意浏览器访问的 Claude Code 会话。

### 在本地恢复 Web Session

若在网页上启动了会话并想在本地终端继续：

```bash
# Resume a web session in the local terminal
claude --teleport
```

或在交互式 REPL 中：
```
/teleport
```

### 使用场景

- 在一台机器上开始工作，在另一台继续
- 与团队成员共享会话 URL
- 在网页 UI 中做可视化 diff，再切回终端执行

---

<a id="desktop-app"></a>
## Desktop App（桌面应用）

Claude Code Desktop App 为独立应用，提供可视化 diff、并行会话与集成连接器。支持 macOS 与 Windows（Pro、Max、Team、Enterprise 套餐）。

### 安装

在 [claude.ai](https://claude.ai) 下载对应平台安装包：
- **macOS**：Universal（Apple Silicon 与 Intel）
- **Windows**：提供 x64 与 ARM64 安装程序

设置步骤见 [Desktop Quickstart](https://code.claude.com/docs/en/desktop-quickstart)。

### 从 CLI 交接

将当前 CLI 会话转到 Desktop App：

```
/desktop
```

### 核心功能

| 功能 | 说明 |
|---------|-------------|
| **Diff view** | 按文件可视化审阅并内联评论；Claude 会阅读评论并修改 |
| **App preview** | 自动启动开发服务器并内嵌浏览器做实时验证 |
| **PR monitoring** | 集成 GitHub CLI，CI 失败可自动修复、检查通过可自动合并 |
| **Parallel sessions** | 侧栏多会话，自动 Git worktree 隔离 |
| **Scheduled tasks** | 应用打开时运行的重复任务（每小时、每天、工作日、每周） |
| **Rich rendering** | 代码、Markdown、图表渲染与语法高亮 |

### App preview 配置

在 `.claude/launch.json` 中配置开发服务器行为：

```json
{
  "command": "npm run dev",
  "port": 3000,
  "readyPattern": "ready on",
  "persistCookies": true
}
```

<a id="connectors"></a>
### Connectors（连接器）

连接外部服务以获取更丰富上下文：

| Connector | 能力 |
|-----------|------------|
| **GitHub** | PR 监控、Issue、代码审查 |
| **Slack** | 通知、频道上下文 |
| **Linear** | Issue、冲刺管理 |
| **Notion** | 文档与知识库 |
| **Asana** | 任务与项目跟踪 |
| **Calendar** | 日程与会议上下文 |

> **说明**：远程（云端）会话不可用 Connectors。

### 远程与 SSH 会话

- **远程会话**：在 Anthropic 云端运行；关闭应用后仍可继续。可通过 claude.ai/code 或 Claude 移动应用访问
- **SSH 会话**：通过 SSH 连接远程机器，可完整使用远程文件系统与工具。远程机器须安装 Claude Code

### Desktop 中的权限模式

Desktop App 支持与 CLI 相同的 4 种权限模式：

| 模式 | 行为 |
|------|----------|
| **Ask permissions**（默认） | 每次编辑与命令都需审阅批准 |
| **Auto accept edits** | 文件编辑自动通过；命令仍需手动批准 |
| **Plan mode** | 做任何改动前先审阅方案 |
| **Bypass permissions** | 自动执行（仅沙箱内，由管理员控制）

### 企业功能

- **Admin console**：管理组织的 Code 标签页访问与权限设置
- **MDM deployment**：macOS 通过 MDM 部署，Windows 可通过 MSIX
- **SSO integration**：要求组织成员使用单点登录
- **Managed settings**：集中管理团队配置与可用模型

---

<a id="task-list"></a>
## 任务列表

任务列表在上下文压缩（为适配上下文窗口而裁剪对话历史）后仍能持久跟踪任务。

### 开关任务列表

会话中按 `Ctrl+T` 可打开或关闭任务列表视图。

### 持久任务

任务在上下文压缩后仍保留，避免长周期、多步骤工作中重要事项丢失。

### 命名任务目录

使用环境变量 `CLAUDE_CODE_TASK_LIST_ID` 可创建跨会话共享的命名任务目录：

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

便于团队工作流或多会话项目共用同一任务列表。

---

<a id="prompt-suggestions"></a>
## 提示建议

提示建议会根据 git 历史与当前对话上下文，在输入框下方以灰色显示示例命令。

### 工作原理

- 建议以灰色文字显示在输入提示下方
- 按 `Tab` 接受建议
- 按 `Enter` 接受并立即发送
- 建议具上下文感知，结合 git 历史与会话状态

### 关闭提示建议

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

<a id="git-worktrees"></a>
## Git Worktrees（Git 工作树）

Git Worktrees 让你在隔离的 worktree 中启动 Claude Code，从而在不同分支上并行工作而无需 stash 或频繁切换。

### 在 Worktree 中启动

```bash
# Start Claude Code in an isolated worktree
claude --worktree
# or
claude -w
```

### Worktree 位置

Worktree 创建在：

```
<repo>/.claude/worktrees/<name>
```

### 单体仓库的稀疏检出

使用 `worktree.sparsePaths` 可在单体仓库中做 sparse-checkout，减少磁盘占用与克隆时间：

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### Worktree 工具与 Hooks

| 项 | 说明 |
|------|-------------|
| `ExitWorktree` | 退出并清理当前 worktree 的工具 |
| `WorktreeCreate` | 创建 worktree 时触发的 Hook 事件 |
| `WorktreeRemove` | 移除 worktree 时触发的 Hook 事件 |

### 自动清理

若 worktree 中无任何改动，会话结束时会自动清理。

### 使用场景

- 在功能分支上开发同时保持 main 干净
- 隔离运行测试而不影响工作区
- 在可丢弃环境中尝试实验性改动
- 在单体仓库中对特定包做稀疏检出以加快启动

---

<a id="sandboxing"></a>
## 沙箱

沙箱为 Claude Code 执行的 Bash 命令提供操作系统级文件系统与网络隔离，与权限规则互补，多一层安全防护。

### 启用沙箱

**Slash command**：
```
/sandbox
```

**CLI 参数**：
```bash
claude --sandbox       # Enable sandboxing
claude --no-sandbox    # Disable sandboxing
```

### 配置项

| 设置 | 说明 |
|---------|-------------|
| `sandbox.enabled` | 启用或关闭沙箱 |
| `sandbox.failIfUnavailable` | 若无法启用沙箱则失败 |
| `sandbox.filesystem.allowWrite` | 允许写入的路径 |
| `sandbox.filesystem.allowRead` | 允许读取的路径 |
| `sandbox.filesystem.denyRead` | 拒绝读取的路径 |
| `sandbox.enableWeakerNetworkIsolation` | 在 macOS 上启用较弱网络隔离 |

### 配置示例

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    },
    "enableWeakerNetworkIsolation": true
  }
}
```

### 工作原理

- Bash 在受限文件系统访问的沙箱环境中运行
- 可隔离网络访问，避免意外外连
- 与权限规则配合，形成纵深防御
- 在 macOS 上可使用 `sandbox.enableWeakerNetworkIsolation` 限制网络（macOS 上无法做到完整网络隔离）

### 使用场景

- 安全运行不受信任或生成的代码
- 防止意外修改项目目录外的文件
- 在自动化任务中限制网络访问

---

<a id="managed-settings-enterprise"></a>
## 托管设置（企业版）

托管设置让企业管理员通过各平台原生管理工具在组织内统一部署 Claude Code 配置。

### 部署方式

| 平台 | 方式 | 起始版本 |
|----------|--------|-------|
| macOS | 托管 plist（MDM） | v2.1.51+ |
| Windows | Windows 注册表 | v2.1.51+ |
| 跨平台 | 托管配置文件 | v2.1.51+ |
| 跨平台 | 托管 drop-in（`managed-settings.d/` 目录） | v2.1.83+ |

### 托管 Drop-in

自 v2.1.83 起，管理员可将多份托管设置文件放入 `managed-settings.d/`。文件按字母顺序合并，便于跨团队模块化配置：

```
~/.claude/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### 可用托管设置

| 设置 | 说明 |
|---------|-------------|
| `disableBypassPermissionsMode` | 禁止用户启用 bypass 权限模式 |
| `availableModels` | 限制用户可选模型 |
| `allowedChannelPlugins` | 控制允许的 channel 插件 |
| `autoMode.environment` | 为 Auto Mode 配置可信基础设施 |
| Custom policies | 组织级权限与工具策略 |

### 示例：macOS Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>disableBypassPermissionsMode</key>
  <true/>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

<a id="configuration-and-settings"></a>
## 配置与设置

### 配置文件位置

1. **全局配置**：`~/.claude/config.json`
2. **项目配置**：`./.claude/config.json`
3. **用户配置**：`~/.config/claude-code/settings.json`

### 完整配置示例

**核心高级功能配置：**

```json
{
  "permissions": {
    "mode": "default"
  },
  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh"
  },
  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"]
      }
    }
  }
}
```

**扩展配置示例：**

```json
{
  "permissions": {
    "mode": "default",
    "allowedTools": ["Bash(git log:*)", "Read"],
    "disallowedTools": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": ["eslint --fix ${file_path}"] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": ["~/.claude/hooks/security-scan.sh"] }],
    "Stop": [{ "hooks": ["~/.claude/hooks/notify.sh"] }]
  },

  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

### 环境变量

可用环境变量覆盖配置：

```bash
# Model selection
export ANTHROPIC_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# API configuration
export ANTHROPIC_API_KEY=sk-ant-...

# Thinking configuration
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high

# Feature toggles
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=true
export CLAUDE_CODE_SIMPLE=true              # Set by --bare flag

# MCP configuration
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# Task management
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Agent teams (experimental)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=true

# Subagent and plugin configuration
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=true

# Subprocess and streaming
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000
```

### 配置管理命令

```
User: /config
[Opens interactive configuration menu]
```

`/config` 提供交互菜单，可切换例如：
- Extended Thinking 开/关
- Verbose 输出
- 权限模式
- 模型选择

### 按项目配置

在项目根目录创建 `.claude/config.json`：

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": ["npm test && npm run lint"] }]
  },
  "permissions": {
    "mode": "default"
  },
  "mcp": {
    "servers": {
      "project-db": {
        "command": "mcp-postgres",
        "env": {
          "DATABASE_URL": "${PROJECT_DB_URL}"
        }
      }
    }
  }
}
```

---

<a id="best-practices"></a>
## 最佳实践

### Planning Mode（规划模式）实践要点
- ✅ 用于复杂多步骤任务
- ✅ 批准前审阅计划
- ✅ 需要时修改计划
- ❌ 不要用于简单任务

### Extended Thinking（扩展思考）实践要点
- ✅ 用于架构决策
- ✅ 用于复杂问题解决
- ✅ 审阅推理过程
- ❌ 不要用于简单问答

### 后台任务
- ✅ 用于长时间操作
- ✅ 关注任务进度
- ✅ 妥善处理任务失败
- ❌ 不要同时启动过多并发任务

### 权限
- ✅ 代码审查用 `plan`（只读）
- ✅ 交互开发用 `default`
- ✅ 自动化工作流用 `acceptEdits`
- ✅ 需自主执行且带安全护栏时用 `auto`
- ❌ 除非万不得已，不要使用 `bypassPermissions`

### 会话
- ✅ 不同任务使用不同会话
- ✅ 保存重要会话状态
- ✅ 清理旧会话
- ❌ 不要在同一会话混无关工作

---

<a id="related-concepts"></a>
## 相关资源

更多关于 Claude Code 及相关功能的信息：

- [Official Interactive Mode Documentation](https://code.claude.com/docs/en/interactive-mode)
- [Official Headless Mode Documentation](https://code.claude.com/docs/en/headless)
- [CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Checkpoints 指南](../08-checkpoints/) — 会话管理与回退
- [Slash Commands](../01-slash-commands/) — 命令参考
- [Memory 指南](../02-memory/) — 持久上下文
- [Skills 指南](../03-skills/) — 自主能力
- [Subagents 指南](../04-subagents/) — 委托执行任务
- [MCP 指南](../05-mcp/) — 外部数据访问
- [Hooks 指南](../06-hooks/) — 事件驱动自动化
- [Plugins 指南](../07-plugins/) — 打包扩展
- [Official Scheduled Tasks Documentation](https://code.claude.com/docs/en/scheduled-tasks)
- [Official Chrome Integration Documentation](https://code.claude.com/docs/en/chrome)
- [Official Remote Control Documentation](https://code.claude.com/docs/en/remote-control)
- [Official Keybindings Documentation](https://code.claude.com/docs/en/keybindings)
- [Official Desktop App Documentation](https://code.claude.com/docs/en/desktop)
