<a id="changelog"></a>

# 更新日志

## v2.2.0 — 2026-03-26

<a id="documentation"></a>

### 文档

- 同步所有教程与参考文档至 Claude Code v2.1.84（f78c094）@luongnv89
  - 更新 slash commands：55+ 内置 + 5 个捆绑 skills，标记 3 个已弃用
  - 将 hook 事件从 18 个扩展至 25 个，新增 `agent` hook 类型（现为 4 种类型）
  - 在高级功能中加入 Auto Mode、Channels、Voice Dictation
  - 新增 `effort`、`shell` 等 skill frontmatter 字段；`initialPrompt`、`disallowedTools` 等 agent 字段
  - 新增 WebSocket MCP 传输、elicitation、2KB 工具上限
  - 新增 plugin LSP 支持、`userConfig`、`${CLAUDE_PLUGIN_DATA}`
  - 更新全部参考文档（CATALOG、QUICK_REFERENCE、LEARNING-ROADMAP、INDEX）
- 将 README 改写为落地页式指南结构（32a0776）@luongnv89

<a id="bug-fixes"></a>

### 问题修复

- 补充缺失的 cSpell 词条与 README 章节以符合 CI 要求（93f9d51）@luongnv89
- 将 `Sandboxing` 加入 cSpell 词典（b80ce6f）@luongnv89

**完整变更记录**：https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

<a id="bug-fixes-1"></a>

### 问题修复

- 移除导致 CI 链接检查失败的失效 marketplace 链接（3fdf0d6）@luongnv89
- 将 `sandboxed` 与 `pycache` 加入 cSpell 词典（dc64618）@luongnv89

**完整变更记录**：https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

<a id="features"></a>

### 新功能

- 新增自适应学习路径，含 self-assessment 与 lesson quiz skills（1ef46cd）@luongnv89
  - `/self-assessment` — 覆盖 10 个功能领域的交互式能力测验，并生成个性化学习路径
  - `/lesson-quiz [lesson]` — 按课时知识检测，每课 8–10 道针对性题目

<a id="bug-fixes-2"></a>

### 问题修复

- 更新失效 URL、弃用说明与过时引用（8fe4520）@luongnv89
- 修复 resources 与 self-assessment skill 中的断链（7a05863）@luongnv89
- 在概念指南中对嵌套代码块使用波浪线围栏（5f82719）@VikalpP
- 向 cSpell 词典补充缺失词条（8df7572）@luongnv89

<a id="documentation-1"></a>

### 文档

- Phase 5 质量保证 — 统一文档一致性、URL 与术语（00bbe4c）@luongnv89
- 完成 Phase 3–4 — 新功能覆盖与参考文档更新（132de29）@luongnv89
- 在 MCP 上下文膨胀一节加入 MCPorter 运行时说明（ef52705）@luongnv89
- 在 6 份指南中补充缺失命令、功能与设置（4bc8f15）@luongnv89
- 依据仓库既有约定新增样式指南（84141d0）@luongnv89
- 在指南对比表中新增 self-assessment 一行（8fe0c96）@luongnv89
- 因 PR #7 将 VikalpP 列入贡献者名单（d5b4350）@luongnv89
- 在 README 与路线图中加入 self-assessment 与 lesson-quiz skill 引用（d5a6106）@luongnv89

<a id="new-contributors"></a>

### 新贡献者

- @VikalpP 在 #7 中首次贡献

**完整变更记录**：https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

<a id="features-1"></a>

### 新功能

- 将全部文档同步至 Claude Code 2026 年 2 月功能（487c96d）
  - 更新 10 个教程目录与 7 份参考文档中的共 26 个文件
  - 新增 **Auto Memory** 文档 — 按项目持久保存所学内容
  - 新增 **Remote Control**、**Web Sessions** 与 **Desktop App** 文档
  - 新增 **Agent Teams** 文档（实验性多智能体协作）
  - 新增 **MCP OAuth 2.0**、**Tool Search** 与 **Claude.ai Connectors** 文档
  - 新增 **Persistent Memory** 与 **Worktree Isolation**（面向 subagents）文档
  - 新增 **Background Subagents**、**Task List**、**Prompt Suggestions** 文档
  - 新增 **Sandboxing** 与 **Managed Settings**（Enterprise）文档
  - 新增 **HTTP Hooks** 与 7 个新 hook 事件文档
  - 新增 **Plugin Settings**、**LSP Servers** 与 Marketplace 更新文档
  - 新增 **Summarize from Checkpoint** 回退选项文档
  - 记录 17 条新 slash commands（`/fork`、`/desktop`、`/teleport`、`/tasks`、`/fast` 等）
  - 记录新 CLI 标志（`--worktree`、`--from-pr`、`--remote`、`--teleport`、`--teammate-mode` 等）
  - 记录与 auto memory、effort 级别、agent teams 等相关的环境变量

<a id="design"></a>

### 设计

- 将 Logo 重设计为指南针括号标识，采用极简配色（20779db）

<a id="bug-fixes--corrections"></a>

### 问题修复 / 更正

- 更新模型名称：Sonnet 4.5 → **Sonnet 4.6**，Opus 4.5 → **Opus 4.6**
- 修正权限模式名称：将虚构的「Unrestricted/Confirm/Read-only」替换为实际的 `default`/`acceptEdits`/`plan`/`dontAsk`/`bypassPermissions`
- 修正 hook 事件：删除虚构的 `PreCommit`/`PostCommit`/`PrePush`，补充真实事件（`SubagentStart`、`WorktreeCreate`、`ConfigChange` 等）
- 修正 CLI 语法：将 `claude-code --headless` 替换为 `claude -p`（print 模式）
- 修正 checkpoint 相关说明：将虚构的 `/checkpoint save/list/rewind/diff` 替换为实际的 `Esc+Esc` / `/rewind` 界面
- 修正会话管理说明：将虚构的 `/session list/new/switch/save` 替换为真实的 `/resume`/`/rename`/`/fork`
- 修正 plugin 清单格式：`plugin.yaml` → `.claude-plugin/plugin.json`
- 修正 MCP 配置路径：`~/.claude/mcp.json` → `.mcp.json`（项目）/ `~/.claude.json`（用户）
- 修正文档 URL：`docs.claude.com` → `docs.anthropic.com`；删除虚构的 `plugins.claude.com`
- 删除多份文件中的虚构配置字段
- 将所有「Last Updated」日期更新为 2026 年 2 月

**完整变更记录**：https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
