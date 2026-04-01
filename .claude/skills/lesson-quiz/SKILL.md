---
name: lesson-quiz
version: 1.0.0
description: 面向 Claude Code 教程的互动式课时测验。针对某一课时（01–10）用 8–10 道题考查概念与实操；可在课前预习自测、课中检验进度或课后巩固。适用于用户说「考我 hooks」「测一下第 3 课」「lesson quiz」「MCP 练习测验」或「我懂不懂 skills」等场景。
---

<a id="lesson-quiz"></a>
# 课时测验

互动式测验，用 8–10 道题考查你对某一 Claude Code 课时的理解，逐题给出反馈，并标出需要复习的部分。

<a id="instructions"></a>
## 使用说明

<a id="step-1-determine-the-lesson"></a>
### 步骤 1：确定课时

若用户以参数给出了课时（例如 `/lesson-quiz hooks` 或 `/lesson-quiz 03`），将其映射到对应课时目录：

**课时映射：**
- `01`, `slash-commands`, `commands` → 01-slash-commands
- `02`, `memory` → 02-memory
- `03`, `skills` → 03-skills
- `04`, `subagents`, `agents` → 04-subagents
- `05`, `mcp` → 05-mcp
- `06`, `hooks` → 06-hooks
- `07`, `plugins` → 07-plugins
- `08`, `checkpoints`, `checkpoint` → 08-checkpoints
- `09`, `advanced`, `advanced-features` → 09-advanced-features
- `10`, `cli` → 10-cli

若未提供参数，用 AskUserQuestion 展示选项：

**问题 1**（标题：「课时」）：
「你想测验哪一课？」
选项：
1. 「Slash Commands (01)」— 自定义命令、Skills、frontmatter、参数
2. 「Memory (02)」— CLAUDE.md、memory 层级、rules、auto memory
3. 「Skills (03)」— Progressive disclosure、自动调用、SKILL.md
4. 「Subagents (04)」— 任务委派、智能体配置、隔离

**问题 2**（标题：「课时」）：
「你想测验哪一课？（续）」
选项：
1. 「MCP (05)」— 外部集成、传输、服务器、工具检索
2. 「Hooks (06)」— 事件自动化、PreToolUse、退出码、JSON I/O
3. 「Plugins (07)」— 打包方案、marketplace、plugin.json
4. 「更多课时…」— Checkpoints、Advanced Features、CLI

若选择「更多课时…」，再展示：

**问题 3**（标题：「课时」）：
「请选择课时：」
选项：
1. 「Checkpoints (08)」— 回退、恢复、安全实验
2. 「Advanced Features (09)」— Planning、权限、print mode、thinking
3. 「CLI Reference (10)」— 标志位、输出格式、脚本、管道

<a id="step-2-read-the-lesson-content"></a>
### 步骤 2：阅读课时内容

阅读该课时的 README.md 以恢复上下文：
- 读取文件：`<lesson-directory>/README.md`

接着使用该课时在 `references/question-bank.md` 中的题库。题库为每课提供 10 道预制题，含正确答案与解析。

<a id="step-3-present-the-quiz"></a>
### 步骤 3：呈现测验

向用户确认测验所处的时间语境：

使用 AskUserQuestion（标题：「时间」）：
「你相对这节课而言，是在什么阶段做这次测验？」
选项：
1. 「课前（预习测验）」— 还没读这节课，测既有知识
2. 「课中（进度检查）」— 学到一半
3. 「课后（掌握检查）」— 已学完，想验证理解程度

该语境会影响结果的表述方式（见步骤 5）。

<a id="step-4-present-questions-in-rounds"></a>
### 步骤 4：分轮出题

从题库中抽取 10 道题，每轮 2 题，共 5 轮。每题使用 AskUserQuestion，展示题干与 3–4 个选项。

**重要**：AskUserQuestion 每题最多 4 个选项，每轮 2 题。

每轮展示 2 题。5 轮结束后进入计分。

**每轮题目格式：**

题库中每道题包含：
- `question`：题干
- `options`：3–4 个选项（其一正确，在题库中已标注）
- `correct`：正确选项标签
- `explanation`：为何正确
- `category`：`conceptual` 或 `practical`

每题用 AskUserQuestion 呈现，并记录用户的答案。

<a id="step-5-score-and-present-results"></a>
### 步骤 5：计分并展示结果

全部轮次结束后计算得分并展示结果。

**计分：**
- 每答对一题 = 1 分
- 满分 = 10 分

**等级划分：**
- 9–10：已掌握 — 理解扎实
- 7–8：熟练 — 整体较好，略有缺口
- 5–6：发展中 — 基础有数，尚需复习
- 3–4：起步 — 缺口较大，建议复习
- 0–2：尚未入门 — 建议从本课开头重新学

**输出格式：**

```markdown
## 课时测验结果：[课时名称]

**得分：N/10** — [等级标签]
**测验时机**：[课前 / 课中 / 课后]
**题型分布**：概念题答对 N 道，实操题答对 N 道

### 逐题结果

| # | 类别 | 题目（摘要） | 你的答案 | 结果 |
|---|------|-------------|---------|------|
| 1 | 概念 | [题干缩写] | [所选答案] | [正确 / 错误] |
| 2 | 实操 | ... | ... | ... |
| ... | ... | ... | ... | ... |

### 答错的题 — 请重点复习

[对每道错题列出：]

**第 N 题：[完整题干]**
- 你的答案：[所选选项]
- 正确答案：[正确选项]
- 解析：[为何正确]
- 复习建议：[建议重读课时 README 中的具体小节]

### [依时机而定的说明]

[若为课前]：
**预习测验得分：N/10。** 这是你的基线！重点补习做错的主题。学完本课后再测一次，看进步多少。

[若为课中]：
**进度检查：N/10。** [若 ≥7：进展不错 — 继续；若 4–6：先回顾错题再继续；若 <4：考虑从头重读。]

[若为课后]：
**掌握检查：N/10。** [若 9–10：本课已掌握！可进入下一课；若 7–8：差一点 — 复习遗漏项再测；若 <7：多花时间啃本课，尤其上面标出的小节。]

### 建议的下一步

[依得分与时机：]
- [若已掌握]：按学习路线进入下一课：[下一课链接]
- [若熟练]：先复习下列小节，再重测：[小节列表]
- [若发展中或更低]：通读本课：[课时链接]。重点：[薄弱类别列表]
- [可询问]：「是否要重测本课、换一课测验，或针对某一主题深入讲解？」
```

<a id="step-6-offer-follow-up"></a>
### 步骤 6：提供后续选项

展示结果后，使用 AskUserQuestion：

「接下来你想做什么？」
选项：
1. 「重测本课」— 再答同一课的测验
2. 「测验其他课时」— 换一课
3. 「讲解我错的题」— 对某道错题做详细讲解
4. 「结束」— 结束测验会话

若选 **重测**：回到步骤 4（跳过时间提问，沿用上次时间语境）。
若选 **测验其他课时**：回到步骤 1。
若选 **讲解错题**：先问题号，再阅读对应课时 README.md 中的相关小节，并结合示例讲解。

<a id="error-handling"></a>
## 错误处理

<a id="invalid-lesson-argument"></a>
### 无效课时参数
若参数无法匹配任一课时，列出有效课时并请用户选择。

<a id="user-wants-to-quit-mid-quiz"></a>
### 用户中途想退出
若用户在任一轮表示要停止，对已作答题目给出部分结果。

<a id="lesson-readme-not-found"></a>
### 找不到课时 README
若预期路径下不存在 README.md，告知用户并建议检查仓库结构。

<a id="validation"></a>
## 校验

<a id="triggering-test-suite"></a>
### 触发测试套件

**应触发：**
- "quiz me on hooks"
- "lesson quiz"
- "test my knowledge of lesson 3"
- "practice quiz for MCP"
- "do I understand skills"
- "quiz me on slash commands"
- "lesson-quiz 06"
- "test me on checkpoints"
- "how well do I know the CLI"
- "quiz me before I start the memory lesson"

**不应触发：**
- "assess my overall level"（应使用 /self-assessment）
- "explain hooks to me"
- "create a hook"
- "what is MCP"
- "review my code"
