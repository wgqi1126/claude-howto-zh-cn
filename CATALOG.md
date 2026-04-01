<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

<a id="claude-code-feature-catalog"></a>

# Claude Code 功能目录

> Claude Code 全部功能的简明参考：命令、智能体、Skills、Plugins 与 Hooks。

**导航**：[命令](#slash-commands) | [权限模式](#permission-modes) | [Subagents](#subagents) | [Skills](#skills) | [Plugins](#plugins) | [MCP 服务器](#mcp-servers) | [Hooks](#hooks) | [Memory 文件](#memory-files) | [新功能](#new-features-march-2026)

---

## 概要

| 功能 | 内置 | 示例 | 合计 | 参考 |
|---------|----------|----------|-------|-----------|
| **Slash Commands** | 55+ | 8 | 63+ | [01-slash-commands/](01-slash-commands/) |
| **Subagents** | 6 | 10 | 16 | [04-subagents/](04-subagents/) |
| **Skills** | 5 个捆绑 | 4 | 9 | [03-skills/](03-skills/) |
| **Plugins** | - | 3 | 3 | [07-plugins/](07-plugins/) |
| **MCP 服务器** | 1 | 8 | 9 | [05-mcp/](05-mcp/) |
| **Hooks** | 25 个事件 | 7 | 7 | [06-hooks/](06-hooks/) |
| **Memory** | 7 种类型 | 3 | 3 | [02-memory/](02-memory/) |
| **合计** | **99** | **43** | **117** | |

---

<a id="slash-commands"></a>

## Slash Commands

命令是用户调用的快捷方式，用于执行特定操作。

### 内置命令

| 命令 | 说明 | 适用场景 |
|---------|-------------|-------------|
| `/help` | 显示帮助信息 | 入门、了解命令 |
| `/btw` | 附带提问且不写入上下文 | 快速岔开话题 |
| `/chrome` | 配置 Chrome 集成 | 浏览器自动化 |
| `/clear` | 清空对话历史 | 重新开始、减少上下文 |
| `/diff` | 交互式 diff 查看器 | 审阅变更 |
| `/config` | 查看/编辑配置 | 自定义行为 |
| `/status` | 显示会话状态 | 查看当前状态 |
| `/agents` | 列出可用智能体 | 查看可委托选项 |
| `/skills` | 列出可用 skills | 查看自动调用能力 |
| `/hooks` | 列出已配置的 hooks | 调试自动化 |
| `/insights` | 分析会话模式 | 优化会话 |
| `/install-slack-app` | 安装 Claude Slack 应用 | Slack 集成 |
| `/keybindings` | 自定义键盘快捷键 | 快捷键定制 |
| `/mcp` | 列出 MCP 服务器 | 检查外部集成 |
| `/memory` | 查看已加载的 memory 文件 | 调试上下文加载 |
| `/mobile` | 生成移动端二维码 | 移动端访问 |
| `/passes` | 查看使用 passes | 订阅信息 |
| `/plugin` | 管理 plugins | 安装/移除扩展 |
| `/plan` | 进入规划模式 | 复杂实现 |
| `/rewind` | 回退到检查点 | 撤销变更、尝试其他方案 |
| `/checkpoint` | 管理检查点 | 保存/恢复状态 |
| `/cost` | 显示 token 使用费用 | 监控支出 |
| `/context` | 显示上下文窗口使用情况 | 管理对话长度 |
| `/export` | 导出对话 | 留存备查 |
| `/extra-usage` | 配置额外用量上限 | 速率限制管理 |
| `/feedback` | 提交反馈或缺陷报告 | 上报问题 |
| `/login` | 使用 Anthropic 身份登录 | 使用相关功能 |
| `/logout` | 退出登录 | 切换账号 |
| `/sandbox` | 切换沙箱模式 | 安全执行命令 |
| `/vim` | 切换 vim 模式 | 类 vim 编辑 |
| `/doctor` | 运行诊断 | 排查问题 |
| `/reload-plugins` | 重新加载已安装的 plugins | 管理 plugin |
| `/release-notes` | 显示发行说明 | 查看新功能 |
| `/remote-control` | 启用远程控制 | 远程访问 |
| `/permissions` | 管理权限 | 控制访问 |
| `/session` | 管理会话 | 多会话工作流 |
| `/rename` | 重命名当前会话 | 整理会话 |
| `/resume` | 恢复先前会话 | 继续工作 |
| `/todo` | 查看/管理待办列表 | 跟踪任务 |
| `/tasks` | 查看后台任务 | 监控异步操作 |
| `/copy` | 将上一条回复复制到剪贴板 | 快速分享输出 |
| `/teleport` | 将会话转移到另一台机器 | 远程继续工作 |
| `/desktop` | 打开 Claude Desktop 应用 | 切换到桌面界面 |
| `/theme` | 更改配色主题 | 自定义外观 |
| `/usage` | 显示 API 使用统计 | 监控配额与费用 |
| `/fork` | 分叉当前对话 | 探索其他方案 |
| `/stats` | 显示会话统计 | 回顾会话指标 |
| `/statusline` | 配置状态栏 | 自定义状态显示 |
| `/stickers` | 查看会话贴纸 | 趣味奖励 |
| `/fast` | 切换快速输出模式 | 加快响应 |
| `/terminal-setup` | 配置终端集成 | 设置终端相关功能 |
| `/upgrade` | 检查更新 | 版本管理 |

### 自定义命令（示例）

| 命令 | 说明 | 适用场景 | 范围 | 安装 |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | 分析代码以优化 | 性能改进 | Project | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | 准备 pull request | 提交 PR 前 | Project | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | 生成 API 文档 | 编写 API 文档 | Project | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | 带上下文的 git commit | 提交变更 | User | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | 暂存、提交并推送 | 快速部署 | User | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | 重构文档结构 | 改进文档 | Project | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | 搭建 CI/CD 流水线 | 新项目 | Project | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | 扩大测试覆盖 | 改进测试 | Project | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **范围**：`User` = 个人工作流（`~/.claude/commands/`），`Project` = 团队共享（`.claude/commands/`）

**参考**：[01-slash-commands/](01-slash-commands/) | [官方文档](https://code.claude.com/docs/en/interactive-mode)

**快速安装（全部自定义命令）**：
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

<a id="permission-modes"></a>

## 权限模式

Claude Code 支持 6 种权限模式，用于控制如何授权工具使用。

| 模式 | 说明 | 适用场景 |
|------|-------------|-------------|
| `default` | 每次工具调用都提示 | 标准交互使用 |
| `acceptEdits` | 自动接受文件编辑，其余仍提示 | 可信的编辑工作流 |
| `plan` | 只读工具，不写入 | 规划与探索 |
| `auto` | 接受全部工具且不提示 | 完全自主运行（Research Preview） |
| `bypassPermissions` | 跳过全部权限检查 | CI/CD、无界面环境 |
| `dontAsk` | 跳过需要权限提示的工具 | 非交互脚本 |

> **说明**：`auto` 模式为 Research Preview 功能（2026 年 3 月）。仅在可信、已沙箱化的环境中使用 `bypassPermissions`。

**参考**：[官方文档](https://code.claude.com/docs/en/permissions)

---

<a id="subagents"></a>

## Subagents

面向特定任务、具有隔离上下文的专用 AI 助手。

### 内置 Subagents

| 智能体 | 说明 | 工具 | 模型 | 适用场景 |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | 多步任务、研究 | 全部工具 | 继承主模型 | 复杂研究、多文件任务 |
| **Plan** | 实现规划 | Read、Glob、Grep、Bash | 继承主模型 | 架构设计、规划 |
| **Explore** | 代码库探索 | Read、Glob、Grep | Haiku 4.5 | 快速检索、理解代码 |
| **Bash** | 命令执行 | Bash | 继承主模型 | Git 操作、终端任务 |
| **statusline-setup** | 状态栏配置 | Bash、Read、Write | Sonnet 4.6 | 配置状态栏显示 |
| **Claude Code Guide** | 帮助与文档 | Read、Glob、Grep | Haiku 4.5 | 获取帮助、了解功能 |

### Subagent 配置字段

| 字段 | 类型 | 说明 |
|-------|------|-------------|
| `name` | string | 智能体标识 |
| `description` | string | 智能体职责 |
| `model` | string | 模型覆盖（例如 `haiku-4.5`） |
| `tools` | array | 允许使用的工具列表 |
| `effort` | string | 推理强度（`low`、`medium`、`high`） |
| `initialPrompt` | string | 智能体启动时注入的系统提示 |
| `disallowedTools` | array | 明确禁止该智能体使用的工具 |

### 自定义 Subagents（示例）

| 智能体 | 说明 | 适用场景 | 范围 | 安装 |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | 全面代码质量审查 | 代码评审会话 | Project | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | 功能架构设计 | 新功能规划 | Project | `cp 04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | 深度代码库分析 | 理解既有功能 | Project | `cp 04-subagents/code-explorer.md .claude/agents/` |
| `clean-code-reviewer` | Clean Code 原则评审 | 可维护性评审 | Project | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | 测试策略与覆盖 | 测试规划 | Project | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | 技术文档 | API 文档、指南 | Project | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | 安全向评审 | 安全审计 | Project | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | 完整功能实现 | 功能开发 | Project | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | 根因分析 | 缺陷调查 | User | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL 查询、数据分析 | 数据相关任务 | User | `cp 04-subagents/data-scientist.md .claude/agents/` |

> **范围**：`User` = 个人（`~/.claude/agents/`），`Project` = 团队共享（`.claude/agents/`）

**参考**：[04-subagents/](04-subagents/) | [官方文档](https://code.claude.com/docs/en/sub-agents)

**快速安装（全部自定义智能体）**：
```bash
cp 04-subagents/*.md .claude/agents/
```

---

<a id="skills"></a>

## Skills

带说明、脚本与模板的自动调用能力。

### 示例 Skills

| Skill | 说明 | 何时自动调用 | 范围 | 安装 |
|-------|-------------|-------------------|-------|--------------|
| `code-review` | 全面代码评审 | 「评审这段代码」「检查质量」 | Project | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | 品牌一致性检查 | 撰写营销文案 | Project | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | API 文档生成 | 「生成文档」「编写 API 文档」 | Project | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | 系统化重构（Martin Fowler） | 「重构这段」「整理代码」 | User | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **范围**：`User` = 个人（`~/.claude/skills/`），`Project` = 团队共享（`.claude/skills/`）

### Skill 目录结构

```
~/.claude/skills/skill-name/
├── SKILL.md          # Skill 定义与说明
├── scripts/          # 辅助脚本
└── templates/        # 输出模板
```

### Skill Frontmatter 字段

Skills 在 `SKILL.md` 中支持 YAML frontmatter 配置：

| 字段 | 类型 | 说明 |
|-------|------|-------------|
| `name` | string | Skill 显示名称 |
| `description` | string | Skill 作用 |
| `autoInvoke` | array | 自动调用的触发短语 |
| `effort` | string | 推理强度（`low`、`medium`、`high`） |
| `shell` | string | 脚本使用的 shell（`bash`、`zsh`、`sh`） |

**参考**：[03-skills/](03-skills/) | [官方文档](https://code.claude.com/docs/en/skills)

**快速安装（全部 Skills）**：
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### 捆绑 Skills

| Skill | 说明 | 何时自动调用 |
|-------|-------------|-------------------|
| `/simplify` | 审阅代码质量 | 编写代码之后 |
| `/batch` | 对多个文件运行提示 | 批量操作 |
| `/debug` | 调试失败测试/错误 | 调试会话 |
| `/loop` | 按间隔运行提示 | 周期性任务 |
| `/claude-api` | 使用 Claude API 构建应用 | API 开发 |

---

<a id="plugins"></a>

## Plugins

命令、智能体、MCP 服务器与 hooks 的打包集合。

### 示例 Plugins

| Plugin | 说明 | 组件 | 适用场景 | 范围 | 安装 |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | PR 评审工作流 | 3 个命令、3 个智能体、GitHub MCP | 代码评审 | Project | `/plugin install pr-review` |
| `devops-automation` | 部署与监控 | 4 个命令、3 个智能体、K8s MCP | DevOps 任务 | Project | `/plugin install devops-automation` |
| `documentation` | 文档生成套件 | 4 个命令、3 个智能体、模板 | 文档工作 | Project | `/plugin install documentation` |

> **范围**：`Project` = 团队共享，`User` = 个人工作流

### Plugin 结构

```
.claude-plugin/
├── plugin.json       # 清单文件
├── commands/         # Slash commands
├── agents/           # Subagents
├── skills/           # Skills
├── mcp/              # MCP 配置
├── hooks/            # Hook 脚本
└── scripts/          # 工具脚本
```

**参考**：[07-plugins/](07-plugins/) | [官方文档](https://code.claude.com/docs/en/plugins)

**Plugin 管理命令**：
```bash
/plugin list              # 列出已安装的 plugins
/plugin install <name>    # 安装 plugin
/plugin remove <name>     # 移除 plugin
/plugin update <name>     # 更新 plugin
```

---

<a id="mcp-servers"></a>

## MCP 服务器

用于外部工具与 API 访问的 Model Context Protocol 服务器。

### 常用 MCP 服务器

| 服务器 | 说明 | 适用场景 | 范围 | 安装 |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | PR、议题、代码管理 | GitHub 工作流 | Project | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | SQL 查询、数据访问 | 数据库操作 | Project | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | 高级文件操作 | 复杂文件任务 | User | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | 团队沟通 | 通知、更新 | Project | 在设置中配置 |
| **Google Docs** | 文档访问 | 编辑、审阅文档 | Project | 在设置中配置 |
| **Asana** | 项目管理 | 任务跟踪 | Project | 在设置中配置 |
| **Stripe** | 支付数据 | 财务分析 | Project | 在设置中配置 |
| **Memory** | 持久化 memory | 跨会话回忆 | User | 在设置中配置 |
| **Context7** | 库文档 | 查阅最新文档 | Built-in | 内置 |

> **范围**：`Project` = 团队（`.mcp.json`），`User` = 个人（`~/.claude.json`），`Built-in` = 预装

### MCP 配置示例

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**参考**：[05-mcp/](05-mcp/) | [MCP 协议文档](https://modelcontextprotocol.io)

**快速安装（GitHub MCP）**：
```bash
export GITHUB_TOKEN="your_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

<a id="hooks"></a>

## Hooks

在 Claude Code 事件上执行 shell 命令的事件驱动自动化。

### Hook 事件

| 事件 | 说明 | 触发时机 | 用例 |
|-------|-------------|----------------|-----------|
| `SessionStart` | 会话开始/恢复 | 会话初始化 | 设置任务 |
| `InstructionsLoaded` | 说明已加载 | 加载 CLAUDE.md 或规则文件 | 自定义说明处理 |
| `UserPromptSubmit` | 处理提示之前 | 用户发送消息 | 输入校验 |
| `PreToolUse` | 工具执行之前 | 任意工具运行前 | 校验、日志 |
| `PermissionRequest` | 显示权限对话框 | 敏感操作之前 | 自定义审批流 |
| `PostToolUse` | 工具成功之后 | 任意工具完成后 | 格式化、通知 |
| `PostToolUseFailure` | 工具执行失败 | 工具报错之后 | 错误处理、日志 |
| `Notification` | 发送通知 | Claude 发送通知时 | 外部提醒 |
| `SubagentStart` | 启动 Subagent | Subagent 任务开始 | 初始化子智能体上下文 |
| `SubagentStop` | Subagent 结束 | Subagent 任务完成 | 串联后续动作 |
| `Stop` | Claude 完成回复 | 回复结束 | 清理、报告 |
| `StopFailure` | API 错误结束本轮 | 发生 API 错误 | 错误恢复、日志 |
| `TeammateIdle` | Teammate 智能体空闲 | 智能体团队协作 | 分配工作 |
| `TaskCompleted` | 任务标记完成 | 任务完成 | 任务后处理 |
| `TaskCreated` | 通过 TaskCreate 创建任务 | 新任务创建 | 任务跟踪、日志 |
| `ConfigChange` | 配置已更新 | 修改设置时 | 响应配置变更 |
| `CwdChanged` | 工作目录变更 | 目录切换时 | 按目录初始化 |
| `FileChanged` | 监视的文件变更 | 文件被修改 | 文件监视、重建 |
| `PreCompact` | 压缩操作之前 | 上下文压缩 | 状态保留 |
| `PostCompact` | 压缩完成之后 | 压缩结束 | 压缩后动作 |
| `WorktreeCreate` | 正在创建工作树 | 创建 Git worktree | 初始化 worktree 环境 |
| `WorktreeRemove` | 正在移除工作树 | 移除 Git worktree | 清理 worktree 资源 |
| `Elicitation` | MCP 服务器请求输入 | MCP elicitation | 输入校验 |
| `ElicitationResult` | 用户对 elicitation 的响应 | 用户响应 | 响应处理 |
| `SessionEnd` | 会话结束 | 会话终止 | 清理、保存状态 |

### 示例 Hooks

| Hook | 说明 | 事件 | 范围 | 安装 |
|------|-------------|-------|-------|--------------|
| `validate-bash.py` | 命令校验 | PreToolUse:Bash | Project | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | 安全扫描 | PostToolUse:Write | Project | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | 自动格式化 | PostToolUse:Write | User | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | 提示校验 | UserPromptSubmit | Project | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | Token 用量跟踪 | Stop | User | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | 提交前校验 | PreToolUse:Bash | Project | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | 命令日志 | PostToolUse:Bash | User | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |

> **范围**：`Project` = 团队（`.claude/settings.json`），`User` = 个人（`~/.claude/settings.json`）

### Hook 配置

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "~/.claude/hooks/validate-bash.py"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "command": "~/.claude/hooks/format-code.sh"
      }
    ]
  }
}
```

**参考**：[06-hooks/](06-hooks/) | [官方文档](https://code.claude.com/docs/en/hooks)

**快速安装（全部 Hooks）**：
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

<a id="memory-files"></a>

## Memory 文件

跨会话自动加载的持久化上下文。

### Memory 类型

| 类型 | 位置 | 范围 | 适用场景 |
|------|----------|-------|-------------|
| **Managed Policy** | 组织托管策略 | Organization | 落实组织级标准 |
| **Project** | `./CLAUDE.md` | Project（团队） | 团队规范、项目上下文 |
| **Project Rules** | `.claude/rules/` | Project（团队） | 模块化项目规则 |
| **User** | `~/.claude/CLAUDE.md` | User（个人） | 个人偏好 |
| **User Rules** | `~/.claude/rules/` | User（个人） | 模块化个人规则 |
| **Local** | `./CLAUDE.local.md` | Local（不纳入 git） | 本机覆盖（截至 2026 年 3 月未在官方文档中列出；可能为遗留） |
| **Auto Memory** | 自动 | Session | 自动捕获的洞见与修正 |

> **范围**：`Organization` = 管理员托管，`Project` = 通过 git 与团队共享，`User` = 个人偏好，`Local` = 不提交，`Session` = 自动管理

**参考**：[02-memory/](02-memory/) | [官方文档](https://code.claude.com/docs/en/memory)

**快速安装**：
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

<a id="new-features-march-2026"></a>

## 新功能（2026 年 3 月）

| 功能 | 说明 | 用法 |
|---------|-------------|------------|
| **Remote Control** | 通过 API 远程控制 Claude Code 会话 | 使用 remote control API 以编程方式发送提示并接收回复 |
| **Web Sessions** | 在浏览器环境中运行 Claude Code | 通过 `claude web` 或 Anthropic Console 访问 |
| **Desktop App** | Claude Code 原生桌面应用 | 使用 `/desktop` 或从 Anthropic 网站下载 |
| **Agent Teams** | 协调多个智能体处理相关任务 | 配置协作并共享上下文的 teammate 智能体 |
| **Task List** | 后台任务管理与监控 | 使用 `/tasks` 查看和管理后台操作 |
| **Prompt Suggestions** | 上下文感知的命令建议 | 根据当前上下文自动显示建议 |
| **Git Worktrees** | 用于并行开发的隔离 git worktree | 使用 worktree 相关命令安全地并行处理分支 |
| **Sandboxing** | 隔离执行环境以提高安全性 | 使用 `/sandbox` 切换；在受限环境中运行命令 |
| **MCP OAuth** | MCP 服务器的 OAuth 认证 | 在 MCP 服务器设置中配置 OAuth 凭据以实现安全访问 |
| **MCP Tool Search** | 动态搜索与发现 MCP 工具 | 使用工具搜索查找已连接服务器上的可用 MCP 工具 |
| **Scheduled Tasks** | 使用 `/loop` 与 cron 工具设置周期性任务 | 使用 `/loop 5m /command` 或 CronCreate 工具 |
| **Chrome Integration** | 使用无头 Chromium 进行浏览器自动化 | 使用 `--chrome` 标志或 `/chrome` 命令 |
| **Keyboard Customization** | 自定义快捷键（含和弦键） | 使用 `/keybindings` 或编辑 `~/.claude/keybindings.json` |
| **Auto Mode** | 无权限提示的完全自主运行（Research Preview） | 使用 `--mode auto` 或 `/permissions auto`；2026 年 3 月 |
| **Channels** | 多渠道通信（Telegram、Slack 等）（Research Preview） | 配置 channel 插件；2026 年 3 月 |
| **Voice Dictation** | 语音输入提示 | 使用麦克风图标或语音快捷键 |
| **Agent Hook Type** | 生成 Subagent 而非执行 shell 的 Hook | 在 hook 配置中设置 `"type": "agent"` |
| **Prompt Hook Type** | 向对话注入提示文本的 Hook | 在 hook 配置中设置 `"type": "prompt"` |
| **MCP Elicitation** | MCP 服务器可在工具执行期间请求用户输入 | 通过 `Elicitation` 与 `ElicitationResult` hook 事件处理 |
| **WebSocket MCP Transport** | 基于 WebSocket 的 MCP 服务器连接传输 | 在 MCP 服务器配置中使用 `"transport": "websocket"` |
| **Plugin LSP Support** | 通过 plugins 集成语言服务器协议 | 在 `plugin.json` 中配置 LSP 服务器以获得编辑器功能 |
| **Managed Drop-ins** | 组织托管的 drop-in 配置（v2.1.83） | 通过托管策略由管理员配置；自动应用于所有用户 |

---

## 速查矩阵

### 功能选择指南

| 需求 | 推荐功能 | 原因 |
|------|---------------------|-----|
| 快捷操作 | Slash Command | 手动、即时 |
| 持久上下文 | Memory | 自动加载 |
| 复杂自动化 | Skill | 自动调用 |
| 专项任务 | Subagent | 隔离上下文 |
| 外部数据 | MCP 服务器 | 实时访问 |
| 事件自动化 | Hook | 事件触发 |
| 完整方案 | Plugin | 一站式打包 |

### 安装优先级

| 优先级 | 功能 | 命令 |
|----------|---------|---------|
| 1. 必备 | Memory | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. 日常使用 | Slash Commands | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. 质量 | Subagents | `cp 04-subagents/*.md .claude/agents/` |
| 4. 自动化 | Hooks | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. 外部 | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. 进阶 | Skills | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. 完整 | Plugins | `/plugin install pr-review` |

---

## 一条命令完整安装

从本仓库安装全部示例：

```bash
# 创建目录
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# 安装全部功能
cp 01-slash-commands/*.md .claude/commands/ && \
cp 02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r 03-skills/* ~/.claude/skills/ && \
cp 04-subagents/*.md .claude/agents/ && \
cp 06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## 其他资源

- [Claude Code 官方文档](https://code.claude.com/docs/en/overview)
- [MCP 协议规范](https://modelcontextprotocol.io)
- [学习路线图](LEARNING-ROADMAP.md)
- [主 README](README.md)

---

**最后更新**：2026 年 3 月
