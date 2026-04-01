---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: 结合上下文创建 git 提交
---

<a id="context"></a>

## 上下文

- 当前 git 状态：!`git status`
- 当前 git diff：!`git diff HEAD`
- 当前分支：!`git branch --show-current`
- 最近提交：!`git log --oneline -10`

<a id="your-task"></a>

## 你的任务

根据上述变更，创建一次 git 提交。

如果通过参数提供了提交说明，请使用：$ARGUMENTS

否则，分析变更并按照 Conventional Commits 格式撰写合适的提交说明：
- `feat:` 表示新功能
- `fix:` 表示缺陷修复
- `docs:` 表示文档变更
- `refactor:` 表示代码重构
- `test:` 表示新增测试
- `chore:` 表示维护类杂项
