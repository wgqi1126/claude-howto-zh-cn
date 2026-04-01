---
name: self-assessment
version: 2.2.0
description: 全面的 Claude Code 自我评估与学习路径顾问。运行覆盖 10 个功能领域的多类别测验，生成带各主题得分的详细技能画像，识别具体短板，并生成带优先下一步的个性化学习路径。在用户说「评估我的水平」「参加测验」「看看我什么水平」「该从哪里开始」「接下来该学什么」「检查一下我的技能」「技能检查」或「提升水平」时使用。
---

<a id="self-assessment--learning-path-advisor"></a>
# 自我评估与学习路径顾问

全面的交互式评估，用于衡量你在 10 个 Claude Code 功能领域上的熟练度，识别具体技能缺口，并生成个性化学习路径以提升水平。

<a id="instructions"></a>
## 使用说明

<a id="step-1-welcome--choose-assessment-mode"></a>
### 第 1 步：欢迎并选择评估深度

向用户提供评估深度选项：

使用 AskUserQuestion，选项如下：
- **快速评估** — 「8 道题，约 2 分钟。判断你的整体水平（初级/中级/高级）并给出学习路径。」
- **深度评估** — 「5 个类别、题目更细，约 5 分钟。给出各主题技能分、识别具体短板，并构建带优先级的学习路径。」

若用户选择 **快速评估**，进入第 2A 步。
若用户选择 **深度评估**，进入第 2B 步。

---

<a id="step-2a-quick-assessment"></a>
### 第 2A 步：快速评估

展示两道多选题（AskUserQuestion 每题最多 4 个选项）：

**问题 1**（标题：「基础」）：
「第 1/2 部分：以下哪些 Claude Code 技能你已经具备？」
选项：
1. 「启动 Claude Code 并对话」— 我会运行 `claude` 并与它交互
2. 「创建/编辑过 CLAUDE.md」— 我已配置项目或用户 memory
3. 「用过 3 个以上 slash commands」— 例如 /help、/compact、/model、/clear
4. 「创建过自定义 command/skill」— 写过 SKILL.md 或自定义 command 文件

**问题 2**（标题：「进阶」）：
「第 2/2 部分：以下哪些进阶技能你已经具备？」
选项：
1. 「配置过 MCP 服务器」— 例如 GitHub、数据库或其他外部数据源
2. 「设置过 Hooks」— 在 ~/.claude/settings.json 中配置过 hooks
3. 「创建/使用过 Subagents」— 使用过 .claude/agents/ 进行任务委派
4. 「使用过 print 模式（claude -p）」— 使用 `claude -p` 做非交互或 CI/CD

**计分：**
- 合计 0–2 项 = 等级 1：初级
- 合计 3–5 项 = 等级 2：中级
- 合计 6–8 项 = 等级 3：高级

带着等级结果进入第 3 步，并列出**未勾选**的具体项作为缺口。

---

<a id="step-2b-deep-assessment"></a>
### 第 2B 步：深度评估

分 5 轮提问，每轮调用一次 AskUserQuestion。每轮覆盖 2 个相关功能领域。所有轮次均使用多选。

**重要**：AskUserQuestion 每题最多 4 个选项。每轮恰好 1 道题、4 个选项，覆盖 2 个主题（每个主题 2 个选项）。

---

**第 1 轮 — Slash Commands 与 Memory**（标题：「命令」）

「以下哪些你已经做过？请选择所有符合项。」
选项：
1. 「创建过自定义 slash command 或 skill」— 写过带 frontmatter 的 SKILL.md，或创建过 .claude/commands/ 下的文件
2. 「在 command 中使用过动态上下文」— 在 skill/command 文件中使用过 `$ARGUMENTS`、`$0`/`$1`、反引号 `!command` 语法，或 `@file` 引用
3. 「同时配置过项目与个人 memory」— 既创建项目 CLAUDE.md，也有个人 ~/.claude/CLAUDE.md（或 CLAUDE.local.md）
4. 「使用过 memory 层级相关能力」— 理解 7 级优先级顺序，使用过 .claude/rules/ 目录、路径专属规则，或 @import 语法

**第 1 轮计分：**
- 选项 1–2 计入 **Slash Commands**（0–2 分）
- 选项 3–4 计入 **Memory**（0–2 分）

---

**第 2 轮 — Skills 与 Hooks**（标题：「自动化」）

「以下哪些你已经做过？请选择所有符合项。」
选项：
1. 「安装并使用过自动调用的 skill」— 根据描述自动触发、无需手动输入 /command 的 skill
2. 「控制过 skill 的调用行为」— 在 SKILL.md frontmatter 中使用过 `disable-model-invocation`、`user-invocable`，或带 agent 字段的 `context: fork`
3. 「配置过 PreToolUse 或 PostToolUse hook」— 配置在工具执行前/后运行的 hook（例如命令校验器、自动格式化）
4. 「使用过 hook 的高级能力」— 配置过 prompt 类 hook、SKILL.md 中的组件级 hook、HTTP hook，或带自定义 JSON 输出（updatedInput、systemMessage）的 hook

**第 2 轮计分：**
- 选项 1–2 计入 **Skills**（0–2 分）
- 选项 3–4 计入 **Hooks**（0–2 分）

---

**第 3 轮 — MCP 与 Subagents**（标题：「集成」）

「以下哪些你已经做过？请选择所有符合项。」
选项：
1. 「连接过 MCP 服务器并使用其工具」— 例如用于 PR/issue 的 GitHub MCP、用于查询的数据库 MCP，或任意外部数据源
2. 「使用过 MCP 的高级能力」— 项目级 .mcp.json、OAuth 认证、带 @ 提及的 MCP 资源、Tool Search，或 `claude mcp serve`
3. 「创建或配置过自定义 Subagents」— 在 .claude/agents/ 中定义 agent，并配置自定义 tools、model 或 permissions
4. 「使用过 Subagents 的高级能力」— Worktree 隔离、持久 agent memory、Ctrl+B 后台任务、带 `Task(agent_name)` 的 agent 允许列表，或 agent 团队

**第 3 轮计分：**
- 选项 1–2 计入 **MCP**（0–2 分）
- 选项 3–4 计入 **Subagents**（0–2 分）

---

**第 4 轮 — Checkpoints 与 Advanced Features**（标题：「高级用户」）

「以下哪些你已经做过？请选择所有符合项。」
选项：
1. 「使用 Checkpoints 做安全实验」— 创建过 checkpoint，用过 Esc+Esc 或 /rewind，恢复过代码和/或对话，或使用过 Summarize 选项
2. 「使用过 planning mode 或 extended thinking」— 通过 /plan、Shift+Tab 或 --permission-mode plan 启用 planning；用 Alt+T/Option+T 切换 extended thinking
3. 「配置过 permission modes」— 通过 CLI 标志、快捷键或设置使用 acceptEdits、plan、dontAsk 或 bypassPermissions 模式
4. 「使用过 remote/desktop/web 相关能力」— 使用过 `claude remote-control`、`claude --remote`、`/teleport`、`/desktop`，或配合 `claude -w` 使用 worktrees

**第 4 轮计分：**
- 选项 1 计入 **Checkpoints**（0–1 分）
- 选项 2–4 计入 **Advanced Features**（0–3 分，上限计 2 分）

---

**第 5 轮 — Plugins 与 CLI**（标题：「精通」）

「以下哪些你已经做过？请选择所有符合项。」
选项：
1. 「安装或创建过 plugin」— 使用市场里的捆绑 plugin，或创建含 plugin.json 清单的 .claude-plugin/ 目录
2. 「使用过 plugin 的高级能力」— Plugin hooks、plugin MCP 服务器、LSP 配置、带命名空间的 plugin 命令，或用于测试的 --plugin-dir 标志
3. 「在脚本或 CI/CD 中使用过 print 模式」— 使用带 --output-format json、--max-turns 的 `claude -p`、管道输入，或集成到 GitHub Actions / CI 流水线
4. 「使用过 CLI 的高级能力」— 会话恢复（-c/-r）、--agents 标志、用于结构化输出的 --json-schema、--fallback-model、--from-pr，或批处理循环

**第 5 轮计分：**
- 选项 1–2 计入 **Plugins**（0–2 分）
- 选项 3–4 计入 **CLI**（0–2 分）

---

<a id="step-3-calculate--present-results"></a>
### 第 3 步：计算并展示结果

#### 3A：快速评估

统计总勾选数并确定等级。然后展示：

```markdown
## Claude Code 技能评估结果

### 你的等级：[等级 1：初级 / 等级 2：中级 / 等级 3：高级]

你勾选了 **N/8** 项。

[根据等级写一句鼓励性总结]

### 技能画像

| 领域 | 状态 |
|------|------|
| 基础 CLI 与对话 | [已勾选/缺口] |
| CLAUDE.md 与 Memory | [已勾选/缺口] |
| Slash Commands（内置） | [已勾选/缺口] |
| 自定义 Commands 与 Skills | [已勾选/缺口] |
| MCP 服务器 | [已勾选/缺口] |
| Hooks | [已勾选/缺口] |
| Subagents | [已勾选/缺口] |
| Print 模式与 CI/CD | [已勾选/缺口] |

### 已识别缺口

[对每个未勾选项，用一行说明要学什么，并附上教程链接]

### 个性化学习路径

[输出对应等级的学习路径 — 见第 4 步]
```

#### 3B：深度评估

根据 5 轮结果计算各主题得分。每个主题 0–2 分。然后展示：

```markdown
## Claude Code 技能评估结果

### 整体等级：[等级 1 / 等级 2 / 等级 3]

**总分：N/20 分**

[一句鼓励性总结]

### 技能画像

| 功能领域 | 得分 | 掌握度 | 状态 |
|----------|------|--------|------|
| Slash Commands | N/2 | [无/基础/熟练] | [待学/复习/已掌握] |
| Memory | N/2 | [无/基础/熟练] | [待学/复习/已掌握] |
| Skills | N/2 | [无/基础/熟练] | [待学/复习/已掌握] |
| Hooks | N/2 | [无/基础/熟练] | [待学/复习/已掌握] |
| MCP | N/2 | [无/基础/熟练] | [待学/复习/已掌握] |
| Subagents | N/2 | [无/基础/熟练] | [待学/复习/已掌握] |
| Checkpoints | N/1 | [无/熟练] | [待学/已掌握] |
| Advanced Features | N/2 | [无/基础/熟练] | [待学/复习/已掌握] |
| Plugins | N/2 | [无/基础/熟练] | [待学/复习/已掌握] |
| CLI | N/2 | [无/基础/熟练] | [待学/复习/已掌握] |

**掌握度说明：** 0 = 无，1 = 基础，2 = 熟练

### 优势领域
[列出得分为 2/2 的主题 — 视为已掌握]

### 优先缺口（下一步学习）
[列出得分为 0 的主题 — 需优先补强，按依赖顺序排列]

### 待复习领域
[列出得分为 1/2 的主题 — 基础已会，进阶能力尚未使用]

### 个性化学习路径

[按缺口输出学习路径 — 见第 4 步]
```

**深度评估的整体等级计算：**
- 总分 0–6 = 等级 1：初级
- 总分 7–13 = 等级 2：中级
- 总分 14–20 = 等级 3：高级

---

<a id="step-4-generate-personalized-learning-path"></a>
### 第 4 步：生成个性化学习路径

根据评估结果生成针对用户缺口的学习路径。不要只重复通用等级路径——要因人调整。

#### 路径生成规则

1. **跳过已掌握主题**：某主题得 2/2 分时，不要把它放进路径。
2. **按依赖顺序优先**：Slash Commands 先于 Skills，Memory 先于 Subagents，等。依赖顺序为：
   - Slash Commands（无依赖）→ Skills（依赖 Slash Commands）
   - Memory（无依赖）→ Subagents（依赖 Memory）
   - CLI 基础（无依赖）→ CLI 进阶（依赖前述全部）
   - Checkpoints（无依赖）
   - Hooks（依赖 Slash Commands）
   - MCP（无依赖）→ Plugins（依赖 MCP、Skills、Hooks）
   - Advanced Features（依赖前述全部）
3. **对 1/2 分主题**：推荐「深入」——链接到对方尚未覆盖的具体进阶小节。
4. **估算时间**：只累加对方需要学习/复习的主题所需时间。
5. **分阶段**：将剩余主题按逻辑每阶段 2–3 个主题组织。

#### 路径输出格式

```markdown
### 个性化学习路径

**预计耗时**：约 N 小时（按当前技能情况调整）

#### 阶段 1：[阶段名称]（约 N 小时）
[仅当对方在这些领域存在缺口时填写]

**[主题名称]** — [从零学习 / 进阶深挖]
- 教程：[教程目录链接]
- 重点：[对方需要的具体章节/概念]
- 关键练习：[一道具体练习]
- 完成标志：[可验证的成功标准]

**[主题名称]** — …

---

#### 阶段 2：[阶段名称]（约 N 小时）
…

---

### 推荐练习项目

结合你的缺口，可尝试下列贴近实际的练习以巩固学习：

1. **[项目名称]**：[一行说明，组合 2–3 个缺口主题]
2. **[项目名称]**：[一行说明]
3. **[项目名称]**：[一行说明]
```

#### 各主题专项建议

某主题为缺口时使用下列具体建议：

**Slash Commands（0 分）**：
- 教程：[01-slash-commands/](../../../01-slash-commands/)
- 重点：内置命令参考、创建第一个 SKILL.md、`$ARGUMENTS` 语法
- 关键练习：创建 `/optimize` 命令并测试
- 完成标志：能创建带参数与动态上下文的自定义 skill

**Slash Commands（1 分 — 复习）**：
- 重点：反引号 `!command` 语法的动态上下文、`@file` 引用、`disable-model-invocation` 与 `user-invocable` 的控制差异
- 完成标志：能创建可注入实时命令输出并自主控制调用行为的 skill

**Memory（0 分）**：
- 教程：[02-memory/](../../../02-memory/)
- 重点：创建 CLAUDE.md、`/init` 与 `/memory` 命令、用 `#` 前缀快速更新
- 关键练习：按你的代码规范创建项目 CLAUDE.md
- 完成标志：Claude 能在多次会话间记住你的偏好

**Memory（1 分 — 复习）**：
- 重点：7 级层级与优先级顺序、带路径专属规则的 .claude/rules/ 目录、`@import` 语法（最大深度 5）、Auto Memory MEMORY.md（200 行上限）
- 完成标志：对不同目录有模块化规则，并理解完整层级

**Skills（0 分）**：
- 教程：[03-skills/](../../../03-skills/)
- 重点：SKILL.md 格式、通过 description 字段自动调用、渐进式披露（3 级加载）
- 关键练习：安装 code-review skill 并确认会自动触发
- 完成标志：skill 能根据对话上下文自动激活

**Skills（1 分 — 复习）**：
- 重点：带 `agent` 字段的 `context: fork` 以在 Subagent 中执行、`disable-model-invocation` 与 `user-invocable`、2% 上下文预算、捆绑资源（scripts/、references/、assets/）
- 完成标志：能创建在 fork 上下文中于 Subagent 内运行的 skill

**Hooks（0 分）**：
- 教程：[06-hooks/](../../../06-hooks/)
- 重点：配置结构（matcher + hooks 数组）、PreToolUse/PostToolUse 事件、退出码（0=成功，2=拦截）、JSON 输入/输出格式
- 关键练习：编写在工具执行前校验 Bash 命令的 PreToolUse hook
- 完成标志：hook 能在执行前拦截危险命令

**Hooks（1 分 — 复习）**：
- 重点：全部 25 种 hook 事件（含 PostToolUseFailure、StopFailure、TaskCreated、CwdChanged、FileChanged、PostCompact、Elicitation、ElicitationResult）、4 种 hook 类型（command、http、prompt、agent）、SKILL.md frontmatter 中的组件级 hook、带 allowedEnvVars 的 HTTP hook、SessionStart/CwdChanged/FileChanged 用的 `CLAUDE_ENV_FILE`
- 完成标志：能创建基于 prompt 的 Stop hook，以及 skill 中的组件级 hook

**MCP（0 分）**：
- 教程：[05-mcp/](../../../05-mcp/)
- 重点：`claude mcp add` 命令、传输类型（推荐 HTTP）、GitHub MCP 搭建、环境变量展开
- 关键练习：添加 GitHub MCP 服务器并查询 PR
- 完成标志：能通过 MCP 从外部服务查询实时数据

**MCP（1 分 — 复习）**：
- 重点：项目级 .mcp.json（需团队审批）、OAuth 2.0 认证、带 `@server:resource` 提及的 MCP 资源、Tool Search（ENABLE_TOOL_SEARCH）、`claude mcp serve`、输出上限（10k/25k/50k）
- 完成标志：有项目 .mcp.json，并理解 Tool Search 自动模式

**Subagents（0 分）**：
- 教程：[04-subagents/](../../../04-subagents/)
- 重点：Agent 文件格式（.claude/agents/*.md）、内置 agents（general-purpose、Plan、Explore）、tools/model/permissionMode 配置
- 关键练习：创建 code-reviewer Subagent 并测试委派
- 完成标志：Claude 会把代码审查委派给你的自定义 agent

**Subagents（1 分 — 复习）**：
- 重点：Worktree 隔离（`isolation: worktree`）、持久 agent memory（带 scopes 的 `memory` 字段）、后台 agent（Ctrl+B/Ctrl+F）、配合 `Task(agent_name)` 的 agent 允许列表、agent 团队（`--teammate-mode`）
- 完成标志：有在 worktree 隔离下运行且带持久 memory 的 Subagent

**Checkpoints（0 分）**：
- 教程：[08-checkpoints/](../../../08-checkpoints/)
- 重点：Esc+Esc 与 /rewind 入口、5 种 rewind 选项（恢复代码+对话、仅对话、仅代码、摘要、取消）、限制（bash 文件系统操作未跟踪）
- 关键练习：做实验性修改后 rewind 恢复
- 完成标志：能放心实验，知道可以回退

**Advanced Features（0 分）**：
- 教程：[09-advanced-features/](../../../09-advanced-features/)
- 重点：Planning 模式（/plan 或 Shift+Tab）、permission modes（5 种）、extended thinking（Alt+T 切换）
- 关键练习：用 planning 模式设计功能再实现
- 完成标志：能在规划与实现模式间流畅切换

**Advanced Features（1 分 — 复习）**：
- 重点：Remote control（`claude remote-control`）、web 会话（`claude --remote`）、desktop 交接（`/desktop`）、worktrees（`claude -w`）、任务列表（Ctrl+T）、企业托管设置
- 完成标志：能在 CLI、web、desktop 之间交接会话

**Plugins（0 分）**：
- 教程：[07-plugins/](../../../07-plugins/)
- 重点：Plugin 结构（.claude-plugin/plugin.json）、plugin 打包内容（commands、agents、MCP、hooks、settings）、从市场安装
- 关键练习：安装一个 plugin 并浏览其组件
- 完成标志：能判断何时用 plugin、何时用独立组件

**Plugins（1 分 — 复习）**：
- 重点：编写 plugin.json 清单、plugin hooks（hooks/hooks.json）、LSP 配置（.lsp.json）、`${CLAUDE_PLUGIN_ROOT}` 变量、测试用 --plugin-dir、市场上架
- 完成标志：能为团队创建并测试 plugin

**CLI（0 分）**：
- 教程：[10-cli/](../../../10-cli/)
- 重点：交互模式与 print 模式、管道配合 `claude -p`、`--output-format json`、会话管理（-c/-r）
- 关键练习：将文件管道到 `claude -p` 并得到 JSON 输出
- 完成标志：能在脚本中非交互使用 Claude

**CLI（1 分 — 复习）**：
- 重点：带 JSON 配置的 --agents 标志、用于结构化输出的 --json-schema、--fallback-model、--from-pr、--strict-mcp-config、for 循环批处理、`claude mcp serve`
- 完成标志：有在 CI/CD 中使用 Claude 并输出结构化 JSON 的脚本

---

<a id="step-5-offer-follow-up-actions"></a>
### 第 5 步：提供后续操作

展示结果后，询问用户接下来想做什么：

使用 AskUserQuestion，选项如下：
- **开始学习** — 「现在就帮我从学习路径里的第一个主题开始」
- **深挖某个缺口** — 「详细讲解我的一个缺口领域，让我在这里学会」
- **练习项目** — 「帮我设计一个覆盖我缺口领域的练习项目」
- **重新测评** — 「我想重新做测验（也许换另一种模式）」

若选 **开始学习**：阅读第一个缺口教程的 README.md，并带用户完成第一道练习。
若选 **深挖某个缺口**：询问是哪个缺口主题，然后阅读对应教程 README.md，用示例讲解要点。
若选 **练习项目**：设计一个小项目，组合 2–3 个缺口主题并给出具体步骤。
若选 **重新测评**：回到第 1 步。

<a id="error-handling"></a>
## 错误处理

### 用户在某一轮未选任何项
该轮对应主题按 0 分处理。继续下一轮。

### 用户在所有轮次都未选任何项
定为等级 1：初级。鼓励从头开始，并输出完整初级路径。

### 用户想重做
从第 1 步重新开始一次全新评估。

### 用户不认同自己的等级
尊重对方判断。询问对方自认哪一等级。按对方选择的等级展示路径，并对可能遗漏的主题做前置条件检查。

### 用户询问某个具体主题
若评估过程中用户说类似「讲讲 hooks」或「我想学 MCP」，先记下来。展示结果后，无论得分如何，在学习路径中突出该主题。

<a id="validation"></a>
## 校验

### 触发测试用例

**应触发：**
- "assess my level"
- "take the quiz"
- "find my level"
- "where should I start"
- "what level am I"
- "learning path quiz"
- "self-assessment"
- "what should I learn next"
- "check my skills"
- "skill check"
- "level up"
- "how good am I at Claude Code"
- "evaluate my Claude Code knowledge"

**不应触发：**
- "review my code"
- "create a skill"
- "help me with MCP"
- "explain slash commands"
- "what is a checkpoint"
