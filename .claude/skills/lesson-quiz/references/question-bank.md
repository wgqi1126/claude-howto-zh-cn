<a id="lesson-quiz-question-bank"></a>
# 课程测验 — 题库

每课 10 道题。每道题包含：类别、题干、选项（3–4 个）、正确答案、解析，以及复习指向。

---

<a id="lesson-01-slash-commands"></a>
## 第 01 课：Slash Commands

### Q1
- **类别**：概念
- **题干**：Claude Code 中的 slash commands 有哪四种类型？
- **选项**：A) 内置、Skills、插件命令、MCP 提示 | B) 内置、自定义、Hook 命令、API 提示 | C) 系统、用户、插件、终端命令 | D) 核心、扩展、宏、脚本命令
- **正确答案**：A
- **解析**：Claude Code 包含内置命令（如 /help、/compact）、Skills（SKILL.md 文件）、插件命令（带命名空间的 plugin-name:command），以及 MCP 提示（/mcp__server__prompt）。
- **复习**：Types of Slash Commands 一节

### Q2
- **类别**：实践
- **题干**：如何把用户提供的全部参数传给某个 Skill？
- **选项**：A) 使用 `${args}` | B) 使用 `$ARGUMENTS` | C) 使用 `$@` | D) 使用 `$INPUT`
- **正确答案**：B
- **解析**：`$ARGUMENTS` 会捕获命令名之后的全部文本。若需位置参数，使用 `$0`、`$1` 等。
- **复习**：Argument handling 一节

### Q3
- **类别**：概念
- **题干**：当 Skill（.claude/skills/name/SKILL.md）与旧版命令（.claude/commands/name.md）同名并存时，谁优先？
- **选项**：A) 旧版命令 | B) Skill | C) 谁先创建谁优先 | D) Claude 请用户选择
- **正确答案**：B
- **解析**：同名时 Skill 优先于旧版命令。Skill 体系会取代较早的命令体系。
- **复习**：Skill precedence 一节

### Q4
- **类别**：实践
- **题干**：如何把实时的 shell 输出注入到 Skill 的提示中？
- **选项**：A) 使用 `$(command)` 语法 | B) 使用 `!`command``（带 ! 的反引号）语法 | C) 使用 `@shell:command` 语法 | D) 使用 `{command}` 语法
- **正确答案**：B
- **解析**：`!`command`` 语法会执行 shell 命令，并在 Claude 看到提示之前将其输出注入 Skill 提示。
- **复习**：Dynamic context injection 一节

### Q5
- **类别**：概念
- **题干**：Skill 的 frontmatter 中 `disable-model-invocation: true` 起什么作用？
- **选项**：A) 完全禁止该 Skill 运行 | B) 仅允许用户调用（Claude 不能自动调用） | C) 在 /help 菜单中隐藏 | D) 关闭该 Skill 的 AI 处理
- **正确答案**：B
- **解析**：`disable-model-invocation: true` 表示仅用户可通过 `/command-name` 触发。Claude 永远不会自动调用，适用于有副作用（如部署）的 Skills。
- **复习**：Controlling invocation 一节

### Q6
- **类别**：实践
- **题干**：希望创建一个仅 Claude 能自动调用、对用户 / 菜单隐藏（不在用户 slash 菜单中显示）的 Skill，应设置哪个 frontmatter 字段？
- **选项**：A) `disable-model-invocation: true` | B) `user-invocable: false` | C) `hidden: true` | D) `auto-only: true`
- **正确答案**：B
- **解析**：`user-invocable: false` 会在用户的 slash 菜单中隐藏该 Skill，但仍允许 Claude 根据上下文自动调用。
- **复习**：Invocation control matrix

### Q7
- **类别**：实践
- **题干**：名为「deploy」的新自定义 Skill，正确的目录结构是？
- **选项**：A) `.claude/commands/deploy.md` | B) `.claude/skills/deploy/SKILL.md` | C) `.claude/skills/deploy.md` | D) `.claude/deploy/SKILL.md`
- **正确答案**：B
- **解析**：Skills 位于 `.claude/skills/` 下的目录中，内含 `SKILL.md`。目录名与命令名一致。
- **复习**：Skill types and locations 一节

### Q8
- **类别**：概念
- **题干**：插件命令如何避免与用户命令重名冲突？
- **选项**：A) 使用 `plugin-name:command-name` 命名空间 | B) 使用特殊 .plugin 扩展名 | C) 使用 `p/` 前缀 | D) 自动覆盖用户命令
- **正确答案**：A
- **解析**：插件命令使用如 `pr-review:check-security` 的命名空间，避免与独立用户命令冲突。
- **复习**：Plugin commands 一节

### Q9
- **类别**：实践
- **题干**：希望限制某个 Skill 可调用的工具，应添加哪个 frontmatter 字段？
- **选项**：A) `tools: [Read, Grep]` | B) `allowed-tools: [Read, Grep]` | C) `permissions: [Read, Grep]` | D) `restrict-tools: [Read, Grep]`
- **正确答案**：B
- **解析**：SKILL.md frontmatter 中的 `allowed-tools` 用于限定该命令可调用的工具范围。
- **复习**：Frontmatter fields reference

### Q10
- **类别**：概念
- **题干**：Skill 中的 `@file` 语法用于什么？
- **选项**：A) 导入另一个 Skill | B) 引用文件并将其内容纳入提示 | C) 创建符号链接 | D) 设置文件权限
- **正确答案**：B
- **解析**：Skill 中的 `@path/to/file` 语法会把被引用文件的内容纳入提示，便于拉入模板或上下文文件。
- **复习**：File references 一节

---

<a id="lesson-02-memory"></a>
## 第 02 课：Memory

### Q1
- **类别**：概念
- **题干**：Claude Code 的 memory 层级有几级？哪一级优先级最高？
- **选项**：A) 5 级，User Memory 最高 | B) 7 级，Managed Policy 最高 | C) 3 级，Project Memory 最高 | D) 7 级，Auto Memory 最高
- **正确答案**：B
- **解析**：层级共 7 级：Managed Policy > Project Memory > Project Rules > User Memory > User Rules > Local Project Memory > Auto Memory。Managed Policy（由管理员设置）优先级最高。
- **复习**：Memory hierarchy 一节

### Q2
- **类别**：实践
- **题干**：在对话中如何快速向 memory 添加一条新规则？
- **选项**：A) 输入 `/memory add "rule text"` | B) 在消息前加 `#`（例如 `# always use TypeScript`） | C) 输入 `/rule "rule text"` | D) 使用 `@add-memory "rule text"`
- **正确答案**：B
- **解析**：`#` 前缀模式可在对话中快速追加单条规则。Claude 会询问保存到哪一级 memory。
- **复习**：Quick memory updates 一节

### Q3
- **类别**：概念
- **题干**：CLAUDE.md 中 `@path/to/file` 导入的最大深度是多少？
- **选项**：A) 3 层 | B) 5 层 | C) 10 层 | D) 无限制
- **正确答案**：B
- **解析**：`@import` 语法支持递归导入，最大深度为 5，以防无限循环。
- **复习**：Import syntax 一节

### Q4
- **类别**：实践
- **题干**：如何让规则文件仅作用于 `src/api/` 下的文件？
- **选项**：A) 把规则放在 `src/api/CLAUDE.md` | B) 在 `.claude/rules/*.md` 的 YAML frontmatter 中加 `paths: src/api/**` | C) 将文件命名为 `.claude/rules/api.md` | D) 在规则文件中使用 `@scope: src/api`
- **正确答案**：B
- **解析**：`.claude/rules/` 下的文件支持 `paths:` frontmatter 字段，可用 glob 将规则限定到特定目录。
- **复习**：Path-specific rules 一节

### Q5
- **类别**：概念
- **题干**：会话开始时，Auto Memory 的 MEMORY.md 会加载多少行？
- **选项**：A) 全部行 | B) 前 100 行 | C) 前 200 行 | D) 前 500 行
- **正确答案**：C
- **解析**：会话开始时会自动加载 MEMORY.md 的前 200 行。从 MEMORY.md 引用的主题文件按需加载。
- **复习**：Auto Memory 一节

### Q6
- **类别**：实践
- **题干**：希望个人项目偏好不提交到 git，应使用哪个文件？
- **选项**：A) `~/.claude/CLAUDE.md` | B) `CLAUDE.local.md` | C) `.claude/rules/personal.md` | D) `.claude/memory/personal.md`
- **正确答案**：B
- **解析**：项目根目录的 `CLAUDE.local.md` 用于个人、项目级偏好，应加入 .gitignore。
- **复习**：Memory locations comparison

### Q7
- **类别**：概念
- **题干**：`/init` 命令做什么？
- **选项**：A) 从零初始化新的 Claude Code 项目 | B) 根据项目结构生成模板 CLAUDE.md | C) 将所有 memory 重置为默认 | D) 创建新会话
- **正确答案**：B
- **解析**：`/init` 会分析项目并生成带建议规则与标准的模板 CLAUDE.md，属于一次性引导工具。
- **复习**：/init command 一节

### Q8
- **类别**：实践
- **题干**：如何完全关闭 Auto Memory？
- **选项**：A) 删除 ~/.claude/projects 目录 | B) 设置 `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` | C) 在 CLAUDE.md 中加 `auto-memory: false` | D) 使用 `/memory disable auto`
- **正确答案**：B
- **解析**：设置 `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` 可关闭 auto memory。值为 `0` 会强制开启。未设置 = 默认开启。
- **复习**：Auto Memory configuration 一节

### Q9
- **类别**：概念
- **题干**：较低优先级的 memory 层能否覆盖较高优先级层的规则？
- **选项**：A) 能，最近的规则总赢 | B) 不能，较高层级始终优先 | C) 能，若较低层使用 `!important` 标记 | D) 视规则类型而定
- **正确答案**：B
- **解析**：优先级从 Managed Policy 向下传递。较低层（如 Auto Memory）不能覆盖较高层（如 Project Memory）。
- **复习**：Memory hierarchy 一节

### Q10
- **类别**：实践
- **题干**：跨两个仓库工作，希望 Claude 同时加载两边的 CLAUDE.md，应使用什么参数？
- **选项**：A) `--multi-repo` | B) `--add-dir /path/to/other` | C) `--include /path/to/other` | D) `--merge-context /path/to/other`
- **正确答案**：B
- **解析**：`--add-dir` 会从额外目录加载 CLAUDE.md，实现多仓库上下文。
- **复习**：Additional directories 一节

---

<a id="lesson-03-skills"></a>
## 第 03 课：Skills

### Q1
- **类别**：概念
- **题干**：Skill 体系中渐进式披露分哪三个层级？
- **选项**：A) 元数据、说明、资源 | B) 名称、正文、附件 | C) 页眉、内容、脚本 | D) 摘要、详情、数据
- **正确答案**：A
- **解析**：第 1 层：元数据（约 100 token，始终加载）；第 2 层：SKILL.md 正文（少于 5k token，触发时加载）；第 3 层：打包资源（scripts/references/assets，按需加载）。
- **复习**：Progressive disclosure architecture 一节

### Q2
- **类别**：实践
- **题干**：Skill 被 Claude 自动调用的最关键因素是什么？
- **选项**：A) Skill 的文件名 | B) frontmatter 中带「何时使用」关键词的 `description` 字段 | C) Skill 的目录位置 | D) `auto-invoke: true` frontmatter 字段
- **正确答案**：B
- **解析**：Claude 是否自动调用 Skill 仅依据其 `description` 字段，其中需包含具体触发短语与场景。
- **复习**：Auto-invocation 一节

### Q3
- **类别**：概念
- **题干**：SKILL.md 文件建议的最大长度是多少？
- **选项**：A) 100 行 | B) 250 行 | C) 500 行 | D) 1000 行
- **正确答案**：C
- **解析**：SKILL.md 宜控制在 500 行以内。更大篇幅的参考资料应放在 `references/` 子目录文件中。
- **复习**：Content guidelines 一节

### Q4
- **类别**：实践
- **题干**：如何让 Skill 在隔离的 Subagent 中运行并拥有独立上下文？
- **选项**：A) 在 frontmatter 中设 `isolation: true` | B) 在 frontmatter 中设 `context: fork` 并配合 `agent` 字段 | C) 在 frontmatter 中设 `subagent: true` | D) 把 Skill 放在 `.claude/agents/`
- **正确答案**：B
- **解析**：`context: fork` 在独立上下文中运行 Skill，`agent` 字段指定使用的智能体类型（如 `Explore`、`Plan` 或自定义 agent）。
- **复习**：Running skills in subagents 一节

### Q5
- **类别**：概念
- **题干**：Skill 元数据（第 1 层）大约占用多少上下文预算？
- **选项**：A) 上下文窗口的 0.5% | B) 上下文窗口的 2% | C) 上下文窗口的 5% | D) 上下文窗口的 10%
- **正确答案**：B
- **解析**：Skill 元数据约占上下文窗口的 2%（回退：16,000 字符）。可通过 `SLASH_COMMAND_TOOL_CHAR_BUDGET` 配置。
- **复习**：Context budget 一节

### Q6
- **类别**：实践
- **题干**：Skill 需要引用大型 API 规范，应放在哪里？
- **选项**：A) 直接写在 SKILL.md 内 | B) 放在 Skill 目录下的 `references/api-spec.md` | C) 放在项目的 CLAUDE.md | D) 放在单独的 `.claude/rules/` 文件
- **正确答案**：B
- **解析**：大型参考资料应放在 `references/` 子目录。Claude 按需加载第 3 层资源，保持 SKILL.md 精简。
- **复习**：Supporting files structure 一节

### Q7
- **类别**：概念
- **题干**：Skill 中 Reference Content 与 Task Content 有何区别？
- **选项**：A) Reference 只读，Task 读写 | B) Reference 向上下文补充知识，Task 提供分步操作说明 | C) Reference 用于文档，Task 用于代码 | D) 没有区别
- **正确答案**：B
- **解析**：Reference Content 向 Claude 上下文补充领域知识（如品牌规范）。Task Content 为工作流提供可执行的分步说明。
- **复习**：Skill content types 一节

### Q8
- **类别**：实践
- **题干**：Skill frontmatter 的 `name` 字段允许哪些字符？
- **选项**：A) 任意字符 | B) 仅小写字母、数字和连字符（最多 64 字符） | C) 字母与下划线 | D) 仅字母数字
- **正确答案**：B
- **解析**：名称须为 kebab-case（小写、连字符），最长 64 字符，且不能包含 "anthropic" 或 "claude"。
- **复习**：SKILL.md format 一节

### Q9
- **类别**：概念
- **题干**：Claude 按什么顺序查找 Skills？
- **选项**：A) User > Project > Enterprise | B) Enterprise > Personal > Project（插件使用命名空间） | C) Project > User > Enterprise | D) 按字母顺序
- **正确答案**：B
- **解析**：优先级为：Enterprise > Personal > Project。插件 Skills 使用命名空间（plugin-name:skill）避免冲突。
- **复习**：Skill types and locations 一节

### Q10
- **类别**：实践
- **题干**：如何阻止 Claude 自动调用某个 Skill，同时仍允许用户手动使用？
- **选项**：A) 设 `user-invocable: false` | B) 设 `disable-model-invocation: true` | C) 删除 description 字段 | D) 设 `auto-invoke: false`
- **正确答案**：B
- **解析**：`disable-model-invocation: true` 阻止 Claude 自动调用，但 Skill 仍保留在用户的 `/` 菜单中供手动使用。
- **复习**：Controlling invocation 一节

---

<a id="lesson-04-subagents"></a>
## 第 04 课：Subagents

### Q1
- **类别**：概念
- **题干**：与内联对话相比，Subagents 的主要优势是什么？
- **选项**：A) 更快 | B) 在独立、干净的上下文窗口中运行，避免上下文污染 | C) 可使用更多工具 | D) 错误处理更好
- **正确答案**：B
- **解析**：Subagents 获得全新上下文窗口，只接收主智能体传入的内容，避免主对话被任务细节污染。
- **复习**：Overview 一节

### Q2
- **类别**：实践
- **题干**：agent 定义的优先级顺序是什么？
- **选项**：A) Project > User > CLI | B) CLI > User > Project | C) User > Project > CLI | D) 完全同等
- **正确答案**：B
- **解析**：CLI 定义的 agent（`--agents` 标志）覆盖用户级（`~/.claude/agents/`），用户级又覆盖项目级（`.claude/agents/`）。
- **复习**：File locations 一节

### Q3
- **类别**：概念
- **题干**：哪个内置 Subagent 使用 Haiku 模型并针对只读代码库探索优化？
- **选项**：A) general-purpose | B) Plan | C) Explore | D) Bash
- **正确答案**：C
- **解析**：Explore Subagent 使用 Haiku 做快速、只读的代码库探索。支持三种 thoroughness：quick、medium、very thorough。
- **复习**：Built-in subagents 一节

### Q4
- **类别**：实践
- **题干**：如何限制协调型 agent 可派生的 Subagents？
- **选项**：A) 使用 `allowed-agents:` 字段 | B) 在 `tools` 字段中使用 `Task(agent_name)` 语法 | C) 设 `spawn-limit: 2` | D) 使用 `restrict-agents: [name1, name2]`
- **正确答案**：B
- **解析**：在 tools 字段中加入 `Task(worker, researcher)` 会形成白名单——该 agent 只能派生名为 "worker" 或 "researcher" 的 Subagents。
- **复习**：Restrict spawnable subagents 一节

### Q5
- **类别**：概念
- **题干**：对 Subagent 而言，`isolation: worktree` 做什么？
- **选项**：A) 在 Docker 容器中运行 | B) 为 agent 提供独立 git worktree，改动不影响主工作树 | C) 禁止读取任何文件 | D) 在沙箱中运行
- **正确答案**：B
- **解析**：Worktree 隔离会创建独立 git worktree。若无改动会自动清理；若有改动会返回 worktree 路径与分支。
- **复习**：Worktree isolation 一节

### Q6
- **类别**：实践
- **题干**：如何让 Subagent 在后台运行？
- **选项**：A) 在 agent 配置中设 `background: true` | B) 在 agent 配置中设 `async: true` | C) 启动后按 Ctrl+D | D) 使用 `--background` CLI 标志
- **正确答案**：A
- **解析**：agent 配置中的 `background: true` 使 Subagent 始终以后台任务运行。用户也可用 Ctrl+B 将前台任务送入后台。
- **复习**：Background subagents 一节

### Q7
- **类别**：概念
- **题干**：`memory` 字段在作用域为 `project` 时对 Subagent 起什么作用？
- **选项**：A) 授予项目 CLAUDE.md 的读权限 | B) 创建绑定当前项目的持久 memory 目录 | C) 共享主 agent 的对话历史 | D) 加载项目的 git 历史
- **正确答案**：B
- **解析**：`memory` 字段为 Subagent 创建持久目录。`project` 作用域表示 memory 绑定当前项目。agent 的 MEMORY.md 前 200 行会自动加载。
- **复习**：Persistent memory 一节

### Q8
- **类别**：实践
- **题干**：如何在 Subagent 的 description 中加入措辞，促使 Claude 自动把任务委派给它？
- **选项**：A) 加 "priority: high" | B) 在 description 中包含 "use PROACTIVELY" 或 "MUST BE USED" | C) 设 `auto-delegate: true` | D) 加 "trigger: always"
- **正确答案**：B
- **解析**：在 description 中加入 "use PROACTIVELY" 或 "MUST BE USED" 等短语，会强烈鼓励 Claude 自动将匹配任务委派给该 Subagent。
- **复习**：Automatic delegation 一节

### Q9
- **类别**：概念
- **题干**：Subagent 合法的 `permissionMode` 取值有哪些？
- **选项**：A) read, write, admin | B) default, acceptEdits, bypassPermissions, plan, dontAsk, auto | C) safe, normal, dangerous | D) restricted, standard, elevated
- **正确答案**：B
- **解析**：Subagents 支持六种权限模式：default（逐项询问）、acceptEdits（自动接受编辑）、bypassPermissions（跳过全部）、plan（只读）、dontAsk（除非预先批准否则自动拒绝）、auto（后台分类器决定）。
- **复习**：Configuration fields 一节

### Q10
- **类别**：实践
- **题干**：如何恢复先前运行返回了 agentId 的 Subagent？
- **选项**：A) 使用 `/resume agent-id` | B) 调用 Task 工具时传入带 agentId 的 `resume` 参数 | C) 使用 `claude -r agent-id` | D) Subagent 无法恢复
- **正确答案**：B
- **解析**：传入此前返回的 agentId 作为 `resume` 参数即可恢复 Subagent，完整上下文会保留。
- **复习**：Resumable agents 一节

---

<a id="lesson-05-mcp"></a>
## 第 05 课：MCP

### Q1
- **类别**：概念
- **题干**：三种 MCP 传输协议是什么？推荐哪一种？
- **选项**：A) HTTP（推荐）、Stdio、SSE（已弃用） | B) WebSocket（推荐）、REST、gRPC | C) TCP、UDP、HTTP | D) Stdio（推荐）、HTTP、SSE
- **正确答案**：A
- **解析**：远程服务器推荐 HTTP。Stdio 用于本地进程（目前最常见）。SSE 已弃用但仍支持。
- **复习**：Transport protocols 一节

### Q2
- **类别**：实践
- **题干**：如何通过 CLI 添加 GitHub MCP 服务器？
- **选项**：A) `claude mcp install github` | B) `claude mcp add --transport http github https://api.github.com/mcp` | C) `claude plugin add github-mcp` | D) `claude connect github`
- **正确答案**：B
- **解析**：使用 `claude mcp add` 并带上 `--transport`、名称与服务器 URL。Stdio 示例：`claude mcp add github -- npx -y @modelcontextprotocol/server-github`。
- **复习**：MCP configuration management 一节

### Q3
- **类别**：概念
- **题干**：当 MCP 工具描述超过上下文窗口的 10% 时会发生什么？
- **选项**：A) 被截断 | B) Tool Search 自动启用，动态选取相关工具 | C) Claude 报错 | D) 额外工具被禁用
- **正确答案**：B
- **解析**：工具超过上下文 10% 时 MCP Tool Search 会自动启用。至少需要 Sonnet 4 或 Opus 4（不支持 Haiku）。
- **复习**：MCP Tool Search 一节

### Q4
- **类别**：实践
- **题干**：如何在 MCP 配置中使用环境变量回退？
- **选项**：A) `${VAR || "default"}` | B) `${VAR:-default}` | C) `${VAR:default}` | D) `${VAR ? "default"}`
- **正确答案**：B
- **解析**：`${VAR:-default}` 在环境变量未设置时提供默认值。无回退的 `${VAR}` 在未设置时会报错。
- **复习**：Environment variable expansion 一节

### Q5
- **类别**：概念
- **题干**：就数据访问而言，MCP 与 Memory 有何区别？
- **选项**：A) MCP 更快，Memory 更慢 | B) MCP 面向实时/变化的外部数据，Memory 面向持久/静态的偏好 | C) MCP 面向代码，Memory 面向文本 | D) 二者可互换
- **正确答案**：B
- **解析**：MCP 连接实时、变化的外部数据源（API、数据库等）。Memory 存储持久、静态的项目上下文与偏好。
- **复习**：MCP vs Memory 一节

### Q6
- **类别**：实践
- **题干**：团队成员首次遇到项目级 `.mcp.json` 时会发生什么？
- **选项**：A) 自动加载 | B) 出现审批提示，要求信任项目的 MCP 服务器 | C) 除非在设置中主动启用否则忽略 | D) Claude 请管理员批准
- **正确答案**：B
- **解析**：项目级 `.mcp.json` 在每位成员首次使用时会触发安全审批提示，用于防止不可信的 MCP 服务器。
- **复习**：MCP Scopes 一节

### Q7
- **类别**：概念
- **题干**：`claude mcp serve` 做什么？
- **选项**：A) 启动 MCP 服务器面板 | B) 让 Claude Code 自身作为 MCP 服务器供其他应用连接 | C) 提供 MCP 文档 | D) 测试 MCP 服务器连接
- **正确答案**：B
- **解析**：`claude mcp serve` 将 Claude Code 变为 MCP 服务器，支持多智能体编排——一个 Claude 实例可被另一个控制。
- **复习**：Claude as MCP Server 一节

### Q8
- **类别**：实践
- **题干**：MCP 工具的默认最大输出大小是多少？
- **选项**：A) 5,000 token | B) 10,000 token | C) 25,000 token | D) 50,000 token
- **正确答案**：C
- **解析**：默认最大为 25,000 token（`MAX_MCP_OUTPUT_TOKENS`）。10k token 时会警告。磁盘持久化上限为 50,000 字符。
- **复习**：MCP Output Limits 一节

### Q9
- **类别**：概念
- **题干**：在托管配置中，若某服务器同时匹配 `allowedMcpServers` 与 `deniedMcpServers`，谁生效？
- **选项**：A) 允许优先 | B) 拒绝优先 | C) 后配置的优先 | D) 二者独立同时应用
- **正确答案**：B
- **解析**：在托管 MCP 配置中，拒绝规则始终优先于允许规则。
- **复习**：Managed MCP Configuration 一节

### Q10
- **类别**：实践
- **题干**：如何在对话中引用 MCP resource？
- **选项**：A) 使用 `/mcp resource-name` | B) 使用 `@server-name:protocol://resource/path` 提及语法 | C) 使用 `mcp.get("resource")` | D) 资源自动加载
- **正确答案**：B
- **解析**：通过对话中的 `@server-name:protocol://resource/path` 提及语法访问 MCP resources。
- **复习**：MCP Resources 一节

---

<a id="lesson-06-hooks"></a>
## 第 06 课：Hooks

### Q1
- **类别**：概念
- **题干**：Claude Code 中的 Hooks 有哪四种类型？
- **选项**：A) Pre、Post、Error、Filter hooks | B) Command、HTTP、Prompt、Agent hooks | C) Before、After、Around、Through hooks | D) Input、Output、Filter、Transform hooks
- **正确答案**：B
- **解析**：Command hooks 运行 shell 脚本，HTTP hooks 调用 webhook，Prompt hooks 使用单轮 LLM 评估，Agent hooks 使用基于 Subagent 的校验。
- **复习**：Hook types 一节

### Q2
- **类别**：实践
- **题干**：某 hook 脚本以退出码 2 结束，会发生什么？
- **选项**：A) 显示非阻塞警告 | B) 阻塞性错误——stderr 作为错误展示给 Claude，并阻止工具使用 | C) Hook 会重试 | D) 会话结束
- **正确答案**：B
- **解析**：退出码 0 = 成功/继续；退出码 2 = 阻塞性错误（stderr 作为错误）；其他非零 = 非阻塞（stderr 仅在 verbose 中显示）。
- **复习**：Exit codes 一节

### Q3
- **类别**：概念
- **题干**：PreToolUse hook 在 stdin 上接收哪些 JSON 字段？
- **选项**：A) `tool_name` 与 `tool_output` | B) `session_id`、`tool_name`、`tool_input`、`hook_event_name`、`cwd` 等 | C) 仅 `tool_name` | D) 完整对话历史
- **正确答案**：B
- **解析**：Hooks 在 stdin 上接收 JSON，包含：session_id、transcript_path、hook_event_name、tool_name、tool_input、tool_use_id、cwd、permission_mode 等。
- **复习**：JSON input structure 一节

### Q4
- **类别**：实践
- **题干**：PreToolUse hook 如何在执行前修改工具的输入参数？
- **选项**：A) 在 stderr 返回修改后的 JSON | B) 在 stdout 返回带 `updatedInput` 字段的 JSON（退出码 0） | C) 写入临时文件 | D) Hooks 不能修改输入
- **正确答案**：B
- **解析**：PreToolUse hook 可在 stdout 输出含 `"updatedInput": {...}` 的 JSON（退出码 0），在 Claude 使用工具前修改参数。
- **复习**：PreToolUse output 一节

### Q5
- **类别**：概念
- **题干**：哪个 hook 事件支持 `CLAUDE_ENV_FILE`，用于将环境变量持久化到会话？
- **选项**：A) PreToolUse | B) UserPromptSubmit | C) SessionStart | D) 所有事件
- **正确答案**：C
- **解析**：仅 SessionStart hooks 可使用 `CLAUDE_ENV_FILE` 将环境变量持久化到会话。
- **复习**：SessionStart 一节

### Q6
- **类别**：实践
- **题干**：希望 hook 仅在 Skill 首次加载时运行一次，而非每次工具调用都运行，应添加什么字段？
- **选项**：A) `run-once: true` | B) 在组件 hook 定义中加 `once: true` | C) `single: true` | D) `max-runs: 1`
- **正确答案**：B
- **解析**：组件级 hooks（定义在 SKILL.md 或 agent frontmatter 中）支持 `once: true`，仅在首次激活时运行。
- **复习**：Component-scoped hooks 一节

### Q7
- **类别**：概念
- **题干**：Stop hook 定义在 Subagent 的 frontmatter 中时会自动转换成什么？
- **选项**：A) PostToolUse hook | B) SubagentStop hook | C) SessionEnd hook | D) 仍为 Stop hook
- **正确答案**：B
- **解析**：Stop hook 放在 Subagent frontmatter 时会自动转为 SubagentStop，以便在该 Subagent 结束时运行。
- **复习**：Component-scoped hooks 一节

### Q8
- **类别**：实践
- **题干**：如何将 hook 匹配到来自某服务器的全部 MCP 工具？
- **选项**：A) `matcher: "mcp_github"` | B) `matcher: "mcp__github__.*"`（正则） | C) `matcher: "mcp:github:*"` | D) `matcher: "github-mcp"`
- **正确答案**：B
- **解析**：matcher 使用正则模式。MCP 工具遵循 `mcp__server__tool` 命名，故 `mcp__github__.*` 可匹配全部 GitHub MCP 工具。
- **复习**：Matcher patterns 一节

### Q9
- **类别**：概念
- **题干**：Claude Code 共支持多少个 hook 事件？
- **选项**：A) 10 | B) 16 | C) 25 | D) 30
- **正确答案**：C
- **解析**：Claude Code 支持 25 个 hook 事件：PreToolUse、PostToolUse、PostToolUseFailure、UserPromptSubmit、Stop、StopFailure、SubagentStop、SubagentStart、PermissionRequest、Notification、PreCompact、PostCompact、SessionStart、SessionEnd、WorktreeCreate、WorktreeRemove、ConfigChange、CwdChanged、FileChanged、TeammateIdle、TaskCompleted、TaskCreated、Elicitation、ElicitationResult、InstructionsLoaded。
- **复习**：Hook events table

### Q10
- **类别**：实践
- **题干**：要调试某 hook 未触发的原因，最佳做法是什么？
- **选项**：A) 在 hook 脚本中加 print | B) 使用 `--debug` 标志，并用 `Ctrl+O` 进入 verbose 模式 | C) 查看系统日志 | D) Hooks 没有调试手段
- **正确答案**：B
- **解析**：`--debug` 与 `Ctrl+O` verbose 模式会显示 hook 执行详情，包括哪些 hook 触发及其输入输出。
- **复习**：Debugging 一节

---

<a id="lesson-07-plugins"></a>
## 第 07 课：Plugins

### Q1
- **类别**：概念
- **题干**：插件的核心清单文件是什么？放在哪里？
- **选项**：A) 根目录的 `plugin.yaml` | B) `.claude-plugin/plugin.json` | C) 带 "claude" 键的 `package.json` | D) `.claude/plugin.md`
- **正确答案**：B
- **解析**：插件清单位于 `.claude-plugin/plugin.json`，必填字段包括：name、description、version、author。
- **复习**：Plugin definition structure 一节

### Q2
- **类别**：实践
- **题干**：发布前如何在本地测试插件？
- **选项**：A) 使用 `/plugin test ./my-plugin` | B) 使用 `claude --plugin-dir ./my-plugin` | C) 使用 `claude plugin validate ./my-plugin` | D) 复制到 ~/.claude/plugins/
- **正确答案**：B
- **解析**：`--plugin-dir` 从本地目录加载插件以供测试，可重复用于加载多个插件。
- **复习**：Testing 一节

### Q3
- **类别**：概念
- **题干**：插件内的 Hooks 与 MCP 配置中，哪个环境变量可用于引用插件安装目录？
- **选项**：A) `$PLUGIN_HOME` | B) `${CLAUDE_PLUGIN_ROOT}` | C) `$PLUGIN_DIR` | D) `${CLAUDE_PLUGIN_PATH}`
- **正确答案**：B
- **解析**：`${CLAUDE_PLUGIN_ROOT}` 解析为插件安装目录，便于在 hooks 与 MCP 配置中使用可移植路径。
- **复习**：Plugin directory structure 一节

### Q4
- **类别**：实践
- **题干**：「pr-review」插件中有名为「check-security」的命令，用户如何调用？
- **选项**：A) `/check-security` | B) `/pr-review:check-security` | C) `/plugin pr-review check-security` | D) `/pr-review/check-security`
- **正确答案**：B
- **解析**：插件命令使用 `plugin-name:command-name` 命名空间，避免与用户命令及其他插件冲突。
- **复习**：Plugin commands 一节

### Q5
- **类别**：概念
- **题干**：插件可以打包哪些组件？
- **选项**：A) 仅命令与设置 | B) 命令、agents、skills、hooks、MCP 服务器、LSP 配置、设置、模板、脚本 | C) 仅命令、hooks 与 MCP 服务器 | D) 仅 skills 与 agents
- **正确答案**：B
- **解析**：插件可打包：commands/、agents/、skills/、hooks/hooks.json、.mcp.json、.lsp.json、settings.json、templates/、scripts/、docs/、tests/。
- **复习**：Plugin directory structure 一节

### Q6
- **类别**：实践
- **题干**：如何从 GitHub 安装插件？
- **选项**：A) `claude plugin add github:username/repo` | B) `/plugin install github:username/repo` | C) `npm install @claude/username-repo` | D) `git clone` 后 `claude plugin register`
- **正确答案**：B
- **解析**：使用 `/plugin install github:username/repo` 可直接从 GitHub 仓库安装。
- **复习**：Installation methods 一节

### Q7
- **类别**：概念
- **题干**：插件中 `settings.json` 的 `agent` 键做什么？
- **选项**：A) 指定认证凭据 | B) 设置插件的主线程 agent | C) 列出可用 Subagents | D) 配置 agent 权限
- **正确答案**：B
- **解析**：插件 settings.json 中的 `agent` 键指定插件激活时作为主线程使用的 agent 定义。
- **复习**：Plugin Settings 一节

### Q8
- **类别**：实践
- **题干**：如何管理插件生命周期（启用/禁用/更新）？
- **选项**：A) 手动编辑配置文件 | B) 使用 `/plugin enable`、`/plugin disable`、`/plugin update plugin-name` | C) 使用 `claude plugin-manager` | D) 重新安装插件
- **正确答案**：B
- **解析**：Claude Code 提供 slash 命令管理完整生命周期：启用、禁用、更新、卸载。
- **复习**：Installation methods 一节

### Q9
- **类别**：概念
- **题干**：与独立的 skills/hooks/MCP 相比，插件的主要优势是什么？
- **选项**：A) 插件更快 | B) 一条命令安装、版本化、市场分发、一站式打包 | C) 插件权限更多 | D) 插件可离线工作
- **正确答案**：B
- **解析**：插件将多种组件打成一个可安装单元，支持版本与市场分发及自动更新——相对手动拼装独立组件。
- **复习**：Standalone vs Plugin comparison 一节

### Q10
- **类别**：实践
- **题干**：插件目录内插件 Hooks 配置放在哪里？
- **选项**：A) `.claude-plugin/hooks.json` | B) `hooks/hooks.json` | C) `plugin.json` 的 hooks 段 | D) `.claude/settings.json`
- **正确答案**：B
- **解析**：插件 hooks 在插件目录结构的 `hooks/hooks.json` 中配置。
- **复习**：Plugin hooks 一节

---

<a id="lesson-08-checkpoints"></a>
## 第 08 课：Checkpoints

### Q1
- **类别**：概念
- **题干**：Checkpoints 会捕获哪四类内容？
- **选项**：A) Git commit、分支、tag、stash | B) 消息、文件修改、工具使用历史、会话上下文 | C) 代码、测试、日志、配置 | D) 输入、输出、错误、耗时
- **正确答案**：B
- **解析**：Checkpoints 捕获对话消息、Claude 工具造成的文件修改、工具使用历史以及会话上下文。
- **复习**：Overview 一节

### Q2
- **类别**：实践
- **题干**：如何打开 checkpoint 浏览器？
- **选项**：A) 使用 `/checkpoints` 命令 | B) 连按 `Esc + Esc`（双 Esc）或使用 `/rewind` | C) 使用 `/history` 命令 | D) 按 `Ctrl+Z`
- **正确答案**：B
- **解析**：双 Esc（Esc+Esc）或 `/rewind` 命令可打开 checkpoint 浏览器以选择恢复点。
- **复习**：Accessing checkpoints 一节

### Q3
- **类别**：概念
- **题干**：有多少种 rewind 选项？分别是什么？
- **选项**：A) 3 种：撤销、重做、重置 | B) 5 种：恢复代码+对话、仅恢复对话、仅恢复代码、从此处摘要、取消 | C) 2 种：完全恢复、部分恢复 | D) 4 种：代码、消息、两者、取消
- **正确答案**：B
- **解析**：5 个选项为：Restore code and conversation（完全回滚）、仅恢复对话、仅恢复代码、Summarize from here（压缩）、Never mind（取消）。
- **复习**：Rewind options 一节

### Q4
- **类别**：实践
- **题干**：在 Claude Code 中通过 Bash 执行了 `rm -rf temp/`，之后想 rewind，checkpoint 会恢复这些文件吗？
- **选项**：A) 会，checkpoint 捕获一切 | B) 不会，Bash 文件系统操作（rm、mv、cp）不在 checkpoint 跟踪范围内 | C) 仅当使用 Edit 工具时才会 | D) 仅当启用了 autoCheckpoint 时才会
- **正确答案**：B
- **解析**：Checkpoints 仅跟踪 Claude 工具（Write、Edit）造成的文件变更。rm、mv、cp 等 Bash 命令不在 checkpoint 跟踪范围内。
- **复习**：Limitations 一节

### Q5
- **类别**：概念
- **题干**：Checkpoints 保留多久？
- **选项**：A) 直到会话结束 | B) 7 天 | C) 30 天 | D) 永久
- **正确答案**：C
- **解析**：Checkpoints 可跨会话保留最多 30 天，之后自动清理。
- **复习**：Checkpoint persistence 一节

### Q6
- **类别**：实践
- **题干**：rewind 时「Summarize from here」做什么？
- **选项**：A) 从该点删除对话 | B) 将对话压缩为 AI 生成摘要，同时在 transcript 中保留原文 | C) 生成变更要点列表 | D) 将对话导出到文件
- **正确答案**：B
- **解析**：Summarize 将对话压缩为较短的 AI 摘要。完整原文仍保留在 transcript 文件中。
- **复习**：Summarize option 一节

### Q7
- **类别**：概念
- **题干**：何时自动创建 checkpoint？
- **选项**：A) 每 5 分钟 | B) 每次用户提示 | C) 仅手动保存时 | D) 每次工具使用后
- **正确答案**：B
- **解析**：每次用户提示都会自动创建 checkpoint，在 Claude 处理请求之前捕获状态。
- **复习**：Automatic checkpoints 一节

### Q8
- **类别**：实践
- **题干**：如何关闭自动创建 checkpoint？
- **选项**：A) 使用 `--no-checkpoints` 标志 | B) 在设置中设 `autoCheckpoint: false` | C) 删除 checkpoints 目录 | D) 无法关闭 checkpoint
- **正确答案**：B
- **解析**：在配置中设置 `autoCheckpoint: false` 可关闭自动创建 checkpoint（默认为 true）。
- **复习**：Configuration 一节

### Q9
- **类别**：概念
- **题干**：Checkpoints 能否替代 git commit？
- **选项**：A) 能，功能更强 | B) 不能，二者互补——checkpoint 面向会话且会过期，git 永久且可共享 | C) 小项目可以替代 | D) 仅单人开发可以
- **正确答案**：B
- **解析**：Checkpoints 是临时性的（保留 30 天）、会话范围且不可共享。Git commit 永久、可审计、可共享。建议二者配合使用。
- **复习**：Integration with git 一节

### Q10
- **类别**：实践
- **题干**：想比较两种不同做法，推荐的 checkpoint 工作流是什么？
- **选项**：A) 开两个独立会话 | B) 在做法 A 前打 checkpoint，尝试 A，rewind 到同一 checkpoint，再尝试 B，比较结果 | C) 改用 git 分支 | D) 没有好的比较方式
- **正确答案**：B
- **解析**：分支策略：在干净状态打 checkpoint，尝试做法 A 并记录结果，rewind 到同一 checkpoint 再尝试做法 B，比较两种结果。
- **复习**：Workflow patterns 一节

---

<a id="lesson-09-advanced-features"></a>
## 第 09 课：高级功能

### Q1
- **类别**：概念
- **题干**：Claude Code 有哪六种权限模式？
- **选项**：A) read、write、execute、admin、root、sudo | B) default、acceptEdits、plan、auto、dontAsk、bypassPermissions | C) safe、normal、elevated、admin、unrestricted、god | D) view、edit、run、deploy、full、bypass
- **正确答案**：B
- **解析**：六种模式：default（逐项询问）、acceptEdits（自动接受编辑）、plan（只读分析）、auto（后台分类器决定）、dontAsk（除非预先批准否则自动拒绝）、bypassPermissions（跳过全部检查）。
- **复习**：Permission Modes 一节

### Q2
- **类别**：实践
- **题干**：如何激活 planning mode？
- **选项**：A) 仅能通过 `/plan` 命令 | B) 通过 `/plan`、`Shift+Tab`/`Alt+M`、`--permission-mode plan` 标志或默认配置 | C) 仅通过 `--planning` 标志 | D) planning 始终开启
- **正确答案**：B
- **解析**：可通过多种方式激活 planning mode：/plan 命令、Shift+Tab/Alt+M 快捷键、`--permission-mode plan` CLI 标志，或配置中的默认值。
- **复习**：Planning Mode 一节

### Q3
- **类别**：概念
- **题干**：`opusplan` 模型别名做什么？
- **选项**：A) 全部使用 Opus | B) 规划阶段用 Opus，实现阶段用 Sonnet | C) 使用特殊规划优化模型 | D) 自动启用 plan mode
- **正确答案**：B
- **解析**：`opusplan` 是模型别名：规划阶段用 Opus（更高质量分析），执行阶段用 Sonnet（更快实现）。
- **复习**：Planning Mode 一节

### Q4
- **类别**：实践
- **题干**：如何在会话中切换 extended thinking？
- **选项**：A) 输入 `/think` | B) 按 `Option+T`（macOS）或 `Alt+T` | C) 使用 `--thinking` 标志 | D) 始终开启且无法切换
- **正确答案**：B
- **解析**：Option+T（macOS）或 Alt+T 可切换 extended thinking。默认对所有模型开启。Opus 4.6 支持自适应 effort 级别。
- **复习**：Extended Thinking 一节

### Q5
- **类别**：概念
- **题干**：「think」或「ultrathink」是否为激活增强思考的特殊关键词？
- **选项**：A) 是，会触发更深推理 | B) 否，视为普通提示文本，无特殊行为 | C) 仅「ultrathink」特殊 | D) 仅与 Opus 配合有效
- **正确答案**：B
- **解析**：文档明确说明这些是普通提示指令，不是特殊激活词。Extended thinking 由 Alt+T 开关与环境变量控制。
- **复习**：Extended Thinking 一节

### Q6
- **类别**：实践
- **题干**：如何在 CI/CD 管道中运行 Claude，输出结构化 JSON 并限制轮次？
- **选项**：A) `claude --ci --json --limit 3` | B) `claude -p --output-format json --max-turns 3 "review code"` | C) `claude --pipeline --format json` | D) `claude run --json --turns 3`
- **正确答案**：B
- **解析**：Print 模式（`-p`）配合 `--output-format json` 与 `--max-turns` 是常见的 CI/CD 集成方式。
- **复习**：Headless/Print Mode 一节

### Q7
- **类别**：概念
- **题干**：Task List 功能（Ctrl+T）提供什么？
- **选项**：A) 后台进程列表 | B) 跨上下文压缩仍保留的持久待办，可通过 `CLAUDE_CODE_TASK_LIST_ID` 共享 | C) 历史会话列表 | D) 待处理工具调用队列
- **正确答案**：B
- **解析**：Task List（Ctrl+T）在上下文压缩后仍持久，可通过命名任务目录与 `CLAUDE_CODE_TASK_LIST_ID` 跨会话共享。
- **复习**：Task List 一节

### Q8
- **类别**：实践
- **题干**：在 planning mode 下如何用常用编辑器在外部编辑计划？
- **选项**：A) 从终端复制粘贴 | B) 按 `Ctrl+G` 在外部编辑器中打开计划 | C) 使用 `/export-plan` 命令 | D) 计划不能在外部编辑
- **正确答案**：B
- **解析**：Ctrl+G 会在配置的外部编辑器中打开当前计划以供修改。
- **复习**：Planning Mode 一节

### Q9
- **类别**：概念
- **题干**：`dontAsk` 与 `bypassPermissions` 模式有何区别？
- **选项**：A) 相同 | B) `dontAsk` 默认拒绝除非预先批准；`bypassPermissions` 完全跳过检查 | C) `dontAsk` 用于文件；`bypassPermissions` 用于命令 | D) `bypassPermissions` 更安全
- **正确答案**：B
- **解析**：dontAsk 对权限请求默认拒绝，除非匹配预先批准的模式。bypassPermissions 完全跳过安全检查——日常使用中很危险。
- **复习**：Permission Modes 一节

### Q10
- **类别**：实践
- **题干**：如何将 CLI 会话交给桌面应用？
- **选项**：A) 使用 `/export` 命令 | B) 使用 `/desktop` 命令 | C) 复制会话 ID 粘贴到应用 | D) CLI 与桌面间无法转移会话
- **正确答案**：B
- **解析**：`/desktop` 命令将当前 CLI 会话交给原生桌面应用，便于可视化 diff 审查与多会话管理。
- **复习**：Desktop App 一节

---

<a id="lesson-10-cli-reference"></a>
## 第 10 课：CLI 参考

### Q1
- **类别**：概念
- **题干**：Claude CLI 的两种主要模式是什么？
- **选项**：A) 在线与离线模式 | B) 交互式 REPL（`claude`）与 Print 模式（`claude -p`） | C) GUI 与终端模式 | D) 单次与批处理模式
- **正确答案**：B
- **解析**：交互式 REPL 为默认对话模式。Print 模式（-p）非交互、可脚本化、可管道传输——单次响应后退出。
- **复习**：CLI architecture 一节

### Q2
- **类别**：实践
- **题干**：如何将文件通过管道传入 Claude 并得到 JSON 输出？
- **选项**：A) `claude --file error.log --json` | B) `cat error.log | claude -p --output-format json "explain this"` | C) `claude < error.log --format json` | D) `claude -p --input error.log --json`
- **正确答案**：B
- **解析**：通过 stdin 将内容传入 print 模式（-p），并使用 --output-format json 得到结构化输出。
- **复习**：Interactive vs Print Mode 一节

### Q3
- **类别**：概念
- **题干**：`-c` 与 `-r` 标志有何区别？
- **选项**：A) 完全相同 | B) `-c` 继续最近会话；`-r` 按名称或 ID 恢复 | C) `-c` 新建会话；`-r` 恢复 | D) `-c` 用于代码；`-r` 用于审查
- **正确答案**：B
- **解析**：`-c/--continue` 恢复最近一次对话。`-r/--resume "name"` 按名称或会话 ID 恢复指定会话。
- **复习**：Session management 一节

### Q4
- **类别**：实践
- **题干**：如何保证 Claude 输出符合 JSON Schema 的有效 JSON？
- **选项**：A) 仅用 `--output-format json` | B) 使用 `--output-format json --json-schema '{"type":"object",...}'` | C) 使用 `--strict-json` 标志 | D) JSON 输出始终符合 schema
- **正确答案**：B
- **解析**：单独使用 `--output-format json` 为尽力而为的 JSON。加上带 JSON Schema 定义的 `--json-schema` 可保证输出符合 schema。
- **复习**：Output and format 一节

### Q5
- **类别**：概念
- **题干**：哪个标志仅在 print 模式（-p）下有效，在交互模式下无效？
- **选项**：A) `--model` | B) `--system-prompt-file` | C) `--verbose` | D) `--max-turns`
- **正确答案**：B
- **解析**：`--system-prompt-file` 从文件加载 system prompt，但仅在 print 模式下有效。交互会话请使用 `--system-prompt`（内联字符串）。
- **复习**：System prompt flags comparison table

### Q6
- **类别**：实践
- **题干**：如何做安全审计时仅允许 Claude 使用只读工具？
- **选项**：A) `claude --read-only "audit code"` | B) `claude --permission-mode plan --tools "Read,Grep,Glob" "audit code"` | C) `claude --safe-mode "audit code"` | D) `claude --no-write "audit code"`
- **正确答案**：B
- **解析**：将 `--permission-mode plan`（只读分析）与 `--tools`（工具白名单）组合，可将 Claude 限制为只读操作。
- **复习**：Tool and permission management 一节

### Q7
- **类别**：概念
- **题干**：agent 定义的优先级顺序是什么？
- **选项**：A) Project > User > CLI | B) CLI > User > Project | C) User > CLI > Project | D) 完全同等
- **正确答案**：B
- **解析**：CLI 定义的 agent（--agents 标志）优先级最高，其次用户级（~/.claude/agents/），再次项目级（.claude/agents/）。
- **复习**：Agents configuration 一节

### Q8
- **类别**：实践
- **题干**：如何分叉现有会话以尝试不同做法而不丢失原会话？
- **选项**：A) 使用 `/fork` 命令 | B) 使用 `--resume session-name --fork-session "branch name"` | C) 使用 `--clone session-name` | D) 使用 `/branch session-name`
- **正确答案**：B
- **解析**：`--resume` 配合 `--fork-session` 会从恢复的会话创建新的独立分支，保留原对话。
- **复习**：Session management 一节

### Q9
- **类别**：概念
- **题干**：用户已登录时，`claude auth status` 返回什么退出码？
- **选项**：A) 1 | B) 0 | C) 200 | D) 不返回退出码
- **正确答案**：B
- **解析**：`claude auth status` 已登录时退出码为 0，未登录为 1。便于在 CI/CD 中脚本化检查认证状态。
- **复习**：CLI commands table

### Q10
- **类别**：实践
- **题干**：如何批量处理多个文件？
- **选项**：A) `claude --batch *.md` | B) 使用 for 循环：`for file in *.md; do claude -p "summarize: $(cat $file)" > ${file%.md}.json; done` | C) `claude -p --files *.md "summarize all"` | D) 不支持批处理
- **正确答案**：B
- **解析**：将 shell for 循环与 print 模式结合，逐文件处理。每次调用独立，可产生结构化输出。
- **复习**：Batch processing 一节
