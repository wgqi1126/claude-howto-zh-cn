---
description: 暂存全部更改、创建提交并推送到远程（请谨慎使用）
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

<a id="commit-and-push-everything"></a>

# 提交并推送全部内容

⚠️ **注意**：会暂存**全部**更改、提交并推送到远程。仅在确信所有更改可以一起提交时使用。

<a id="workflow"></a>

## 工作流

<a id="1-analyze-changes"></a>

### 1. 分析更改

并行执行：
- `git status` — 列出已修改/新增/删除/未跟踪的文件
- `git diff --stat` — 显示变更统计
- `git log -1 --oneline` — 查看最近一条提交，参考提交信息风格

<a id="2-safety-checks"></a>

### 2. 安全检查

**若发现以下情况，请 ❌ 停止并发出警告：**
- 密钥：`.env*`、`*.key`、`*.pem`、`credentials.json`、`secrets.yaml`、`id_rsa`、`*.p12`、`*.pfx`、`*.cer`
- API 密钥：任何带真实值的 `*_API_KEY`、`*_SECRET`、`*_TOKEN` 变量（非占位符，如 `your-api-key`、`xxx`、`placeholder`）
- 大文件：未使用 Git LFS 且 `>10MB`
- 构建产物：`node_modules/`、`dist/`、`build/`、`__pycache__/`、`*.pyc`、`.venv/`
- 临时文件：`.DS_Store`、`thumbs.db`、`*.swp`、`*.tmp`

**API 密钥校验：**
在已修改文件中检查类似模式：
```bash
OPENAI_API_KEY=sk-proj-xxxxx  # ❌ 检测到真实密钥！
AWS_SECRET_KEY=AKIA...         # ❌ 检测到真实密钥！
STRIPE_API_KEY=sk_live_...    # ❌ 检测到真实密钥！

# ✅ 可接受的占位符：
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**✅ 请确认：**
- `.gitignore` 已正确配置
- 无合并冲突
- 分支正确（若在 main/master 上请提示警告）
- API 密钥仅为占位符

<a id="3-request-confirmation"></a>

### 3. 请求确认

展示摘要：
```
📊 变更摘要：
- X 个文件已修改，Y 个新增，Z 个已删除
- 合计：+AAA 行新增，-BBB 行删除

🔒 安全：✅ 无密钥 | ✅ 无大文件 | ⚠️ [警告]
🌿 分支：[name] → origin/[name]

将执行：git add . → commit → push

输入 yes 继续，或 no 取消。
```

**在继续之前必须等待用户明确回复 `yes`。**

<a id="4-execute-after-confirmation"></a>

### 4. 执行（确认后）

按顺序执行：
```bash
git add .
git status  # 确认暂存区
```

<a id="5-generate-commit-message"></a>

### 5. 生成提交信息

分析更改并撰写 conventional commit 风格的信息：

**格式：**
```
[type]: 简要说明（最多 72 个字符）

- 关键变更 1
- 关键变更 2
- 关键变更 3
```

**类型：** `feat`、`fix`、`docs`、`style`、`refactor`、`test`、`chore`、`perf`、`build`、`ci`

**示例：**
```
docs: 为概念说明 README 补充完整文档

- 增加架构图与表格
- 加入可运行示例
- 扩展最佳实践章节
```

<a id="6-commit-and-push"></a>

### 6. 提交并推送

```bash
git commit -m "$(cat <<'EOF'
[生成的提交信息]
EOF
)"
git push  # 若失败：git pull --rebase && git push
git log -1 --oneline --decorate  # 确认
```

<a id="7-confirm-success"></a>

### 7. 确认成功

```
✅ 已成功推送到远程！

Commit: [hash] [message]
Branch: [branch] → origin/[branch]
变更：X 个文件（+insertions / -deletions）
```

<a id="error-handling"></a>

## 错误处理

- **`git add` 失败**：检查权限、文件是否被锁定，确认仓库已初始化
- **`git commit` 失败**：修复 pre-commit hooks，检查 git 配置（user.name / email）
- **`git push` 失败**：
  - 非快进：执行 `git pull --rebase && git push`
  - 无远程分支：执行 `git push -u origin [branch]`
  - 受保护分支：改用 PR 工作流

<a id="when-to-use"></a>

## 适用场景

✅ **适合：**
- 多文件文档更新
- 带测试与文档的功能开发
- 跨多个文件的缺陷修复
- 全项目范围的格式化或重构
- 配置变更

❌ **避免：**
- 不确定将要提交什么
- 包含密钥或敏感数据
- 未经评审就推送到受保护分支
- 存在合并冲突
- 需要细粒度的提交历史
- pre-commit hooks 失败

<a id="alternatives"></a>

## 替代做法

若用户希望更可控，可建议：
1. **选择性暂存**：审阅并只暂存指定文件
2. **交互式暂存**：使用 `git add -p` 按补丁选择
3. **PR 工作流**：创建分支 → 推送 → 提 PR（使用 `/pr` 命令）

**⚠️ 提醒**：推送前务必审阅更改。若有疑虑，请改用单独的 git 命令以获得更细控制。
