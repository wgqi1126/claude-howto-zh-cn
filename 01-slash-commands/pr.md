---
description: 清理代码、暂存更改并准备 pull request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

<a id="pull-request-preparation-checklist"></a>

# PR 准备清单

创建 PR 前，请执行以下步骤：

1. 运行 Prettier 格式化：`prettier --write .`
2. 运行测试：`npm test`
3. 查看 git 差异：`git diff HEAD`
4. 暂存更改：`git add .`
5. 按约定式提交（Conventional Commits）规范撰写提交说明：
   - `fix:` 用于缺陷修复
   - `feat:` 用于新功能
   - `docs:` 用于文档
   - `refactor:` 用于代码重构
   - `test:` 用于新增或修改测试
   - `chore:` 用于维护性工作

6. 生成 PR 摘要，需包含：
   - 变更内容
   - 变更原因
   - 已执行的测试
   - 可能影响
