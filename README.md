<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

[![GitHub Stars](https://img.shields.io/github/stars/wgqi1126/claude-howto-zh-cn?style=flat&color=gold)](https://github.com/wgqi1126/claude-howto-zh-cn/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/wgqi1126/claude-howto-zh-cn?style=flat)](https://github.com/wgqi1126/claude-howto-zh-cn/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.2.0-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

# 周末掌握 Claude Code

从输入 `claude` 开始，进阶到编排 agents、hooks、skills 和 MCP 服务器，并配合可视化教程、可直接复制的模板以及循序渐进的学习路径。

**[15 分钟快速上手](#-get-started-in-15-minutes)** | **[找到你的当前水平](#-not-sure-where-to-start)** | **[浏览功能目录](CATALOG.md)**

---

## 目录

- [问题所在](#the-problem)
- [Claude How To 如何解决这个问题](#how-claude-how-to-fixes-this)
- [它是如何工作的](#how-it-works)
- [不知道从哪里开始？](#-not-sure-where-to-start)
- [15 分钟快速上手](#-get-started-in-15-minutes)
- [你可以用它构建什么？](#what-can-you-build-with-this)
- [常见问题](#faq)
- [参与贡献](#contributing)
- [许可证](#license)

---

<a id="the-problem"></a>

## 问题所在

你已经安装了 Claude Code，也试了几个提示词。然后呢？

- **官方文档会介绍功能，但不会告诉你如何把这些功能组合起来用。** 你知道有 slash commands，却不知道怎么把它和 hooks、memory、subagents 串起来，组成真正能节省数小时的工作流。
- **没有清晰的学习路径。** 应该先学 MCP 还是 hooks？先学 skills 还是 subagents？结果往往是什么都看过一点，但什么都没真正掌握。
- **示例过于基础。** 一个 “hello world” 级别的 slash command，并不能帮你搭建生产级代码审查流水线，更别提结合 memory、委派给专门 agent、再自动执行安全扫描了。

Claude Code 90% 的能力你都还没真正用上，而且你甚至不知道自己错过了什么。

---

<a id="how-claude-how-to-fixes-this"></a>

## Claude How To 如何解决这个问题

这不是另一份功能参考手册，而是一套**结构化、可视化、示例驱动**的指南。它会用可直接复制到项目中的真实模板，教你掌握 Claude Code 的全部核心能力。

| | 官方文档 | 本指南 |
|--|----------|--------|
| **形式** | 参考文档 | 带 Mermaid 图的可视化教程 |
| **深度** | 功能描述 | 解释底层工作方式 |
| **示例** | 基础片段 | 可立即上手的生产级模板 |
| **结构** | 按功能分类 | 渐进式学习路径（从入门到高级） |
| **上手方式** | 自主摸索 | 带时间估算的引导式路线图 |
| **自我评估** | 无 | 交互式测验，帮你定位短板并生成个性化学习路径 |

### 你将获得：

- **10 个教程模块**，覆盖 Claude Code 的全部核心功能，从 slash commands 到自定义 agent 团队
- **可复制即用的配置**，包括 slash commands、`CLAUDE.md` 模板、hook 脚本、MCP 配置、subagent 定义，以及完整插件包
- **Mermaid 图示**，帮助你理解每个功能在内部是如何工作的，做到不仅知道“怎么做”，也知道“为什么”
- **一条引导式学习路径**，帮助你在 11 到 13 小时内从新手成长为高阶用户
- **内置自测能力**，直接在 Claude Code 中运行 `/self-assessment` 或 `/lesson-quiz hooks` 即可发现知识盲区

**[开始学习路径 ->](LEARNING-ROADMAP.md)**

---

<a id="how-it-works"></a>

## 它是如何工作的

### 1. 先找到你的水平

完成 [自我评估测验](LEARNING-ROADMAP.md#-find-your-level)，或者直接在 Claude Code 中运行 `/self-assessment`。系统会根据你已经掌握的内容生成个性化路线图。

### 2. 按引导路径逐步学习

按顺序学习 10 个模块，每个模块都建立在前一个模块之上。边学边把模板直接复制进你的项目。

### 3. 把多个功能组合成工作流

真正的威力来自功能组合。你会学会如何把 slash commands、memory、subagents、hooks 连接起来，形成自动化流水线，处理代码审查、部署、文档生成等任务。

### 4. 验证你的理解

每学完一个模块，就运行 `/lesson-quiz [topic]`。测验会精确指出你遗漏的知识点，帮助你快速补齐短板。

**[15 分钟快速上手](#-get-started-in-15-minutes)**

---

## 已被 5,900+ 开发者采用

- **5,900+ GitHub Stars**，来自日常使用 Claude Code 的开发者
- **690+ Forks**，很多团队已在此基础上改造成自己的工作流
- **持续维护中**，会随每次 Claude Code 发布同步更新（最新版本：v2.2.0，2026 年 3 月）
- **社区驱动**，贡献者会持续分享自己在真实项目中的配置与经验

[![Star History Chart](https://api.star-history.com/svg?repos=wgqi1126/claude-howto-zh-cn&type=Date)](https://star-history.com/#wgqi1126/claude-howto-zh-cn&Date)

---

<a id="-not-sure-where-to-start"></a>

## 不知道从哪里开始？

先做自我评估，或者直接按你的水平开始：

| 水平 | 你已经可以…… | 从这里开始 | 预计时间 |
|------|----------------|------------|----------|
| **初学者** | 启动 Claude Code 并对话 | [Slash Commands](01-slash-commands/) | 约 2.5 小时 |
| **中级** | 使用 `CLAUDE.md` 和自定义命令 | [Skills](03-skills/) | 约 3.5 小时 |
| **高级** | 配置 MCP 服务器和 hooks | [Advanced Features](09-advanced-features/) | 约 5 小时 |

**完整 10 模块学习路径：**

| 顺序 | 模块 | 难度 | 时间 |
|------|------|------|------|
| 1 | [Slash Commands](01-slash-commands/) | 初学者 | 30 分钟 |
| 2 | [Memory](02-memory/) | 初学者+ | 45 分钟 |
| 3 | [Checkpoints](08-checkpoints/) | 中级 | 45 分钟 |
| 4 | [CLI Basics](10-cli/) | 初学者+ | 30 分钟 |
| 5 | [Skills](03-skills/) | 中级 | 1 小时 |
| 6 | [Hooks](06-hooks/) | 中级 | 1 小时 |
| 7 | [MCP](05-mcp/) | 中级+ | 1 小时 |
| 8 | [Subagents](04-subagents/) | 中级+ | 1.5 小时 |
| 9 | [Advanced Features](09-advanced-features/) | 高级 | 2-3 小时 |
| 10 | [Plugins](07-plugins/) | 高级 | 2 小时 |

**[查看完整学习路线图 ->](LEARNING-ROADMAP.md)**

---

<a id="-get-started-in-15-minutes"></a>

## 15 分钟快速上手

```bash
# 1. 克隆本指南
git clone https://github.com/wgqi1126/claude-howto-zh-cn.git
cd claude-howto-zh-cn

# 2. 复制你的第一个 slash command
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. 试试看，在 Claude Code 中输入：
# /optimize

# 4. 想继续？先配置项目 memory：
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. 安装一个 skill：
cp -r 03-skills/code-review ~/.claude/skills/
```

想要完整一些的初始化配置？下面是 **1 小时核心安装方案**：

```bash
# Slash commands（15 分钟）
cp 01-slash-commands/*.md .claude/commands/

# 项目 memory（15 分钟）
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 安装一个 skill（15 分钟）
cp -r 03-skills/code-review ~/.claude/skills/

# 周末目标：继续加入 hooks、subagents、MCP 和 plugins
# 按学习路径逐步完成配置
```

**[查看完整安装速查](#installation-quick-reference)**

---

<a id="what-can-you-build-with-this"></a>

## 你可以用它构建什么？

| 使用场景 | 你会组合使用的功能 |
|----------|--------------------|
| **自动化代码审查** | Slash Commands + Subagents + Memory + MCP |
| **团队入职引导** | Memory + Slash Commands + Plugins |
| **CI/CD 自动化** | CLI Reference + Hooks + Background Tasks |
| **文档生成** | Skills + Subagents + Plugins |
| **安全审计** | Subagents + Skills + Hooks（只读模式） |
| **DevOps 流水线** | Plugins + MCP + Hooks + Background Tasks |
| **复杂重构** | Checkpoints + Planning Mode + Hooks |

---

<a id="faq"></a>

## 常见问题

**这是免费的吗？**  
是的。项目采用 MIT 许可证，永久免费。你可以将它用于个人项目、工作场景或团队内部，只需保留许可证声明即可。

**这个项目还在维护吗？**  
是的，而且是持续维护。指南会随着 Claude Code 每次发布同步更新。当前版本为 v2.2.0（2026 年 3 月），兼容 Claude Code 2.1+。

**它和官方文档有什么区别？**  
官方文档更偏功能参考；这份指南则是教程，提供图示、生产级模板和渐进式学习路径。两者是互补关系：先用这里学会怎么用，再去官方文档查具体细节。

**完整学完要多久？**  
完整路径约需 11 到 13 小时。但你在 15 分钟内就能获得实际收益，只要复制一个 slash command 模板并亲手试一遍即可。

**我可以搭配 Claude Sonnet / Haiku / Opus 使用吗？**  
可以。所有模板都适用于 Claude Sonnet 4.6、Claude Opus 4.6 和 Claude Haiku 4.5。

**我可以参与贡献吗？**  
当然可以。请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 中的说明。我们欢迎新的示例、bug 修复、文档改进和社区模板。

**我可以离线阅读吗？**  
可以。运行 `uv run scripts/build_epub.py` 即可生成包含全部内容与渲染后图示的 EPUB 电子书。

---

## 现在开始真正掌握 Claude Code

你已经安装好了 Claude Code。你与 10 倍效率之间，差的只是知道如何把它真正用起来。这份指南提供了结构化的路径、可视化解释和可直接复制的模板，帮助你快速到达那个状态。

MIT 许可证，永久免费。你可以直接 clone、fork，然后按自己的方式继续演化。

**[开始学习路径 ->](LEARNING-ROADMAP.md)** | **[浏览功能目录](CATALOG.md)** | **[15 分钟快速上手](#-get-started-in-15-minutes)**

---

<details>
<summary>快速导航：全部功能</summary>

| 功能 | 说明 | 目录 |
|------|------|------|
| **Feature Catalog** | 带安装命令的完整参考目录 | [CATALOG.md](CATALOG.md) |
| **Slash Commands** | 用户主动触发的快捷命令 | [01-slash-commands/](01-slash-commands/) |
| **Memory** | 持久化上下文 | [02-memory/](02-memory/) |
| **Skills** | 可复用能力 | [03-skills/](03-skills/) |
| **Subagents** | 专用 AI 助手 | [04-subagents/](04-subagents/) |
| **MCP Protocol** | 外部工具访问能力 | [05-mcp/](05-mcp/) |
| **Hooks** | 事件驱动自动化 | [06-hooks/](06-hooks/) |
| **Plugins** | 打包好的功能集合 | [07-plugins/](07-plugins/) |
| **Checkpoints** | 会话快照与回退 | [08-checkpoints/](08-checkpoints/) |
| **Advanced Features** | 规划、深度思考、后台任务 | [09-advanced-features/](09-advanced-features/) |
| **CLI Reference** | 命令、参数与选项 | [10-cli/](10-cli/) |
| **Blog Posts** | 真实使用场景案例 | [Blog Posts](https://medium.com/@luongnv89) |

</details>

<details>
<summary>功能对比</summary>

| 功能 | 触发方式 | 持久性 | 最适合 |
|------|----------|--------|--------|
| **Slash Commands** | 手动（`/cmd`） | 仅当前会话 | 快速捷径 |
| **Memory** | 自动加载 | 跨会话 | 长期上下文积累 |
| **Skills** | 自动触发 | 文件系统级 | 自动化工作流 |
| **Subagents** | 自动委派 | 隔离上下文 | 任务分发 |
| **MCP Protocol** | 自动查询 | 实时 | 获取在线数据 |
| **Hooks** | 事件触发 | 配置式 | 自动化与校验 |
| **Plugins** | 一条命令安装 | 覆盖全部功能 | 完整解决方案 |
| **Checkpoints** | 手动/自动 | 会话级 | 安全试验 |
| **Planning Mode** | 手动/自动 | 计划阶段 | 复杂实现 |
| **Background Tasks** | 手动 | 任务持续期间 | 长时间运行操作 |
| **CLI Reference** | 终端命令 | 会话/脚本 | 自动化与脚本编排 |

</details>

<a id="installation-quick-reference"></a>

<details>
<summary>安装速查</summary>

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

# Checkpoints（默认自动启用，可在 settings 中配置）
# 参见 08-checkpoints/README.md

# Advanced Features（在 settings 中配置）
# 参见 09-advanced-features/config-examples.json

# CLI Reference（无需安装）
# 使用示例参见 10-cli/README.md
```

</details>

<details>
<summary>01. Slash Commands</summary>

**位置**: [01-slash-commands/](01-slash-commands/)

**是什么**: 以 Markdown 文件形式存储、由用户主动调用的快捷命令

**示例**:
- `optimize.md` - 代码优化分析
- `pr.md` - 准备 Pull Request
- `generate-api-docs.md` - API 文档生成器

**安装**:
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**用法**:
```
/optimize
/pr
/generate-api-docs
```

**延伸阅读**: [Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. Memory</summary>

**位置**: [02-memory/](02-memory/)

**是什么**: 跨会话持久化的上下文

**示例**:
- `project-CLAUDE.md` - 团队级项目规范
- `directory-api-CLAUDE.md` - 目录级规则
- `personal-CLAUDE.md` - 个人偏好

**安装**:
```bash
# 项目 memory
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# 目录 memory
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# 个人 memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**用法**: Claude 会自动加载

</details>

<details>
<summary>03. Skills</summary>

**位置**: [03-skills/](03-skills/)

**是什么**: 可复用、可自动触发的能力包，通常包含说明与脚本

**示例**:
- `code-review/` - 带脚本的完整代码审查能力
- `brand-voice/` - 品牌语气一致性检查器
- `doc-generator/` - API 文档生成器

**安装**:
```bash
# 个人 skills
cp -r 03-skills/code-review ~/.claude/skills/

# 项目 skills
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**用法**: 当请求相关时会被自动调用

</details>

<details>
<summary>04. Subagents</summary>

**位置**: [04-subagents/](04-subagents/)

**是什么**: 带隔离上下文和自定义提示的专门 AI 助手

**示例**:
- `code-reviewer.md` - 全面的代码质量分析
- `test-engineer.md` - 测试策略与覆盖率建议
- `documentation-writer.md` - 技术文档编写
- `secure-reviewer.md` - 偏安全方向的审查（只读）
- `implementation-agent.md` - 完整功能实现 agent

**安装**:
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**用法**: 由主 agent 自动委派

</details>

<details>
<summary>05. MCP Protocol</summary>

**位置**: [05-mcp/](05-mcp/)

**是什么**: 用于访问外部工具和 API 的 Model Context Protocol

**示例**:
- `github-mcp.json` - GitHub 集成
- `database-mcp.json` - 数据库查询
- `filesystem-mcp.json` - 文件系统操作
- `multi-mcp.json` - 多个 MCP 服务器组合

**安装**:
```bash
# 设置环境变量
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 通过 CLI 添加 MCP 服务器
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 或手动写入项目 .mcp.json（示例见 05-mcp/）
```

**用法**: 一旦配置完成，Claude 会自动可用这些 MCP 工具

</details>

<details>
<summary>06. Hooks</summary>

**位置**: [06-hooks/](06-hooks/)

**是什么**: 针对 Claude Code 事件自动执行的事件驱动 shell 命令

**示例**:
- `format-code.sh` - 写入前自动格式化代码
- `pre-commit.sh` - 提交前运行测试
- `security-scan.sh` - 扫描安全问题
- `log-bash.sh` - 记录所有 bash 命令
- `validate-prompt.sh` - 校验用户提示词
- `notify-team.sh` - 事件发生时发送通知

**安装**:
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

**用法**: hooks 会在对应事件发生时自动执行

**Hook 类型**（4 大类，25 个事件）：
- **工具类 Hooks**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`
- **会话类 Hooks**: `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
- **任务类 Hooks**: `UserPromptSubmit`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`
- **生命周期 Hooks**: `ConfigChange`, `CwdChanged`, `FileChanged`, `PreCompact`, `PostCompact`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

</details>

<details>
<summary>07. Plugins</summary>

**位置**: [07-plugins/](07-plugins/)

**是什么**: 将 commands、agents、MCP 与 hooks 打包在一起的功能集合

**示例**:
- `pr-review/` - 完整 PR 审查工作流
- `devops-automation/` - 部署与监控
- `documentation/` - 文档生成

**安装**:
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**用法**: 直接使用打包好的 slash commands 与配套功能

</details>

<details>
<summary>08. Checkpoints and Rewind</summary>

**位置**: [08-checkpoints/](08-checkpoints/)

**是什么**: 保存会话状态，并回退到之前的时间点以尝试不同方案

**核心概念**:
- **Checkpoint**: 会话状态快照
- **Rewind**: 回退到之前的检查点
- **Branch Point**: 从同一检查点分叉出多个方案

**用法**:
```
# 每次用户提交提示时都会自动创建 checkpoint
# 要回退，按两次 Esc，或使用：
/rewind

# 然后从五个选项中选择：
# 1. 恢复代码和对话
# 2. 仅恢复对话
# 3. 仅恢复代码
# 4. 从这里开始总结
# 5. 取消
```

**使用场景**:
- 尝试不同实现方案
- 从错误中恢复
- 安全实验
- 比较不同备选解
- 对设计方案做 A/B 测试

</details>

<details>
<summary>09. Advanced Features</summary>

**位置**: [09-advanced-features/](09-advanced-features/)

**是什么**: 面向复杂工作流与自动化的高级能力

**包含**:
- **Planning Mode** - 编码前先生成详细实现计划
- **Extended Thinking** - 处理复杂问题时进行更深层推理（`Alt+T` / `Option+T` 切换）
- **Background Tasks** - 在不阻塞当前对话的情况下运行长任务
- **Permission Modes** - `default`, `acceptEdits`, `plan`, `dontAsk`, `bypassPermissions`
- **Headless Mode** - 在 CI/CD 中运行 Claude Code：`claude -p "Run tests and generate report"`
- **Session Management** - `/resume`, `/rename`, `/fork`, `claude -c`, `claude -r`
- **Configuration** - 在 `~/.claude/settings.json` 中自定义行为

完整配置示例见 [config-examples.json](09-advanced-features/config-examples.json)。

</details>

<details>
<summary>10. CLI Reference</summary>

**位置**: [10-cli/](10-cli/)

**是什么**: Claude Code 命令行界面的完整参考

**快速示例**:
```bash
# 交互模式
claude "explain this project"

# 打印模式（非交互）
claude -p "review this code"

# 处理文件内容
cat error.log | claude -p "explain this error"

# 为脚本输出 JSON
claude -p --output-format json "list functions"

# 恢复会话
claude -r "feature-auth" "continue implementation"
```

**适用场景**: CI/CD 集成、脚本自动化、批处理、多会话工作流、自定义 agent 配置

</details>

<details>
<summary>示例工作流</summary>

### 完整代码审查工作流

```markdown
# 使用：Slash Commands + Subagents + Memory + MCP

User: /review-pr

Claude:
1. 加载项目 memory（编码规范）
2. 通过 GitHub MCP 获取 PR
3. 委派给 code-reviewer subagent
4. 委派给 test-engineer subagent
5. 汇总发现的问题
6. 给出完整审查结果
```

### 自动化文档生成

```markdown
# 使用：Skills + Subagents + Memory

User: "为 auth 模块生成 API 文档"

Claude:
1. 加载项目 memory（文档规范）
2. 识别出文档生成请求
3. 自动调用 doc-generator skill
4. 委派给 api-documenter subagent
5. 生成包含示例的完整文档
```

### DevOps 部署

```markdown
# 使用：Plugins + MCP + Hooks

User: /deploy production

Claude:
1. 运行部署前 hook（校验环境）
2. 委派给 deployment-specialist subagent
3. 通过 Kubernetes MCP 执行部署
4. 监控进度
5. 运行部署后 hook（健康检查）
6. 报告状态
```

</details>

<details>
<summary>目录结构</summary>

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
└── README.md（当前文件）
```

</details>

<details>
<summary>最佳实践</summary>

### 推荐做法
- 从简单的 slash commands 开始
- 按增量方式逐步添加功能
- 用 memory 维护团队规范
- 先在本地测试配置
- 记录自定义实现方式
- 将项目配置纳入版本控制
- 在团队内共享 plugins

### 不建议的做法
- 不要创建重复功能
- 不要硬编码凭据
- 不要跳过文档
- 不要把简单任务设计得过于复杂
- 不要忽略安全最佳实践
- 不要提交敏感数据

</details>

<details>
<summary>故障排查</summary>

### 功能未加载
1. 检查文件位置和命名
2. 确认 YAML frontmatter 语法正确
3. 检查文件权限
4. 确认 Claude Code 版本兼容性

### MCP 连接失败
1. 确认环境变量
2. 检查 MCP 服务器是否正确安装
3. 测试凭据是否有效
4. 检查网络连通性

### Subagent 没有被委派
1. 检查工具权限
2. 确认 agent 描述是否足够清晰
3. 评估任务复杂度是否合适
4. 独立测试该 agent

</details>

<details>
<summary>测试</summary>

本项目包含较完整的自动化测试体系：

- **单元测试**: 基于 pytest 的 Python 测试（Python 3.10、3.11、3.12）
- **代码质量**: 使用 Ruff 进行 lint 与格式检查
- **安全性**: 使用 Bandit 扫描漏洞
- **类型检查**: 使用 mypy 进行静态类型分析
- **构建验证**: 验证 EPUB 生成功能
- **覆盖率跟踪**: 集成 Codecov

```bash
# 安装开发依赖
uv pip install -r requirements-dev.txt

# 运行全部单元测试
pytest scripts/tests/ -v

# 运行测试并生成覆盖率报告
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 运行代码质量检查
ruff check scripts/
ruff format --check scripts/

# 运行安全扫描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 运行类型检查
mypy scripts/ --ignore-missing-imports
```

每次向 `main`/`develop` 推送，以及每次向 `main` 提交 PR 时，测试都会自动运行。详细信息见 [TESTING.md](.github/TESTING.md)。

</details>

<details>
<summary>EPUB 生成</summary>

想离线阅读这份指南？可以生成 EPUB 电子书：

```bash
uv run scripts/build_epub.py
```

这会生成 `claude-howto-guide.epub`，包含全部内容以及已渲染的 Mermaid 图表。

更多选项见 [scripts/README.md](scripts/README.md)。

</details>

<details>
<summary>参与贡献</summary>

发现问题，或者想补充一个示例？非常欢迎你的帮助。

**请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，其中详细说明了：**
- 可贡献的内容类型（示例、文档、功能、缺陷、反馈）
- 如何搭建开发环境
- 目录结构以及如何添加内容
- 写作规范与最佳实践
- Commit 与 PR 流程

**我们的社区规范：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 社区行为准则
- [SECURITY.md](SECURITY.md) - 安全策略与漏洞报告方式

### 报告安全问题

如果你发现了安全漏洞，请负责任地进行报告：

1. **使用 GitHub 私有漏洞报告**: https://github.com/wgqi1126/claude-howto-zh-cn/security/advisories
2. **或者阅读** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) 获取详细说明
3. **不要** 为安全漏洞创建公开 issue

快速开始：
1. Fork 并克隆仓库
2. 创建一个清晰描述用途的分支（`add/feature-name`、`fix/bug`、`docs/improvement`）
3. 按照指南完成修改
4. 提交带有清晰说明的 Pull Request

**需要帮助？** 直接创建 issue 或 discussion，我们会引导你完成流程。

</details>

<details>
<summary>补充资源</summary>

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) - 可直接使用的 skills 集合
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny's Claude Code Workflow](https://x.com/bcherny/status/2007179832300581177) - Claude Code 的作者分享了他系统化的工作流：并行 agents、共享 `CLAUDE.md`、Plan 模式、slash commands、subagents，以及用于自治长任务的校验 hooks。

</details>

---

<a id="contributing"></a>

## 参与贡献

欢迎贡献内容。开始前请先阅读我们的 [贡献指南](CONTRIBUTING.md)。

## 贡献者

感谢所有为这个项目做出贡献的人。

| 贡献者 | PR |
|--------|----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - add a tool to create an epub](https://github.com/wgqi1126/claude-howto-zh-cn/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): Use tilde fences for nested code blocks in concepts guide](https://github.com/wgqi1126/claude-howto-zh-cn/pull/7) |

---

<a id="license"></a>

## 许可证

MIT 许可证，详见 [LICENSE](LICENSE)。你可以自由使用、修改和分发，唯一要求是保留许可证声明。

---

**最后更新**: 2026 年 3 月  
**Claude Code 版本**: 2.1+  
**兼容模型**: Claude Sonnet 4.6、Claude Opus 4.6、Claude Haiku 4.5
