<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

<a id="checkpoints-and-rewind"></a>
# Checkpoints 与 Rewind

Checkpoints 让你保存对话状态，并在 Claude Code 会话中回退到更早的时间点。这在尝试不同方案、从错误中恢复或对比备选解法时非常有用。

<a id="overview"></a>
## 概述

Checkpoints 让你保存对话状态并回退到更早的时间点，从而安全地试验并探索多种做法。它们是对话状态的快照，包括：
- 已交换的全部消息
- 已做出的文件修改
- 工具使用历史
- 会话上下文

在探索不同方案、从错误中恢复或对比备选解法时，Checkpoints 非常有价值。

<a id="key-concepts"></a>
## 核心概念

| 概念 | 说明 |
|---------|-------------|
| **Checkpoint** | 对话状态快照，包含消息、文件与上下文 |
| **Rewind** | 回到某一 Checkpoint，并丢弃之后的变更 |
| **分支点（Branch Point）** | 从该 Checkpoint 起向多个方向探索 |

<a id="accessing-checkpoints"></a>
## 如何打开 Checkpoints

你可以通过两种主要方式访问并管理 Checkpoints：

<a id="using-keyboard-shortcut"></a>
### 使用键盘快捷键

连按两次 `Esc`（`Esc` + `Esc`）打开 Checkpoint 界面并浏览已保存的 Checkpoints。

<a id="using-slash-command"></a>
### 使用斜杠命令

使用 `/rewind` 命令（别名：`/checkpoint`）快速访问：

```bash
# 打开 Rewind 界面
/rewind

# 或使用别名
/checkpoint
```

<a id="rewind-options"></a>
## Rewind 选项

执行 Rewind 时，你会看到包含五个选项的菜单：

1. **恢复代码与对话** — 将文件与消息都恢复到该 Checkpoint
2. **仅恢复对话** — 仅回退消息，代码保持当前状态不变
3. **仅恢复代码** — 仅撤销文件变更，保留完整对话历史
4. **从此处摘要** — 从该点起将对话压缩为 AI 生成的摘要，而不是直接丢弃；原始消息仍会保留在会话转录中。你也可以选择提供说明，让摘要聚焦在特定主题上。
5. **取消** — 取消并回到当前状态

<a id="automatic-checkpoints"></a>
## 自动 Checkpoints

Claude Code 会自动为你创建 Checkpoints：

- **每次用户输入** — 每次你发送输入都会新建一个 Checkpoint
- **持久化** — Checkpoints 在会话之间保留
- **自动清理** — 超过 30 天后会自动清理

因此你可以回退到对话中任意较早时刻，无论是几分钟前还是数天之前。

<a id="use-cases"></a>
## 使用场景

| 场景 | 工作流 |
|----------|----------|
| **探索多种方案** | 保存 → 试 A → 保存 → Rewind → 试 B → 对比 |
| **安全重构** | 保存 → 重构 → 测试 → 若失败：Rewind |
| **A/B 对比** | 保存 → 设计 A → 保存 → Rewind → 设计 B → 对比 |
| **从错误中恢复** | 发现问题 → Rewind 到最后一次良好状态 |

<a id="using-checkpoints"></a>
## 使用 Checkpoints

<a id="viewing-and-rewinding"></a>
### 查看与 Rewind

连按两次 `Esc` 或使用 `/rewind` 打开 Checkpoint 浏览器。你会看到带时间戳的全部可用 Checkpoint 列表。选择任意 Checkpoint 即可回退到该状态。

<a id="checkpoint-details"></a>
### Checkpoint 详情

每个 Checkpoint 会显示：
- 创建时间的时间戳
- 被修改过的文件
- 对话中的消息条数
- 使用过的工具

<a id="practical-examples"></a>
## 实例

<a id="example-1-exploring-different-approaches"></a>
### 示例 1：探索不同做法

```
用户：我们给 API 加一层缓存吧

Claude：我会在你的 API 端点上加入 Redis 缓存……
【在 checkpoint A 处完成修改】

用户：其实我想先试试内存缓存

Claude：我会回退以便换种做法探索……
【用户连按 Esc+Esc 并回退到 checkpoint A】
【在 checkpoint B 实现内存缓存】

用户：现在我可以对比两种做法了
```

<a id="example-2-recovering-from-mistakes"></a>
### 示例 2：从错误中恢复

```
用户：把认证模块重构为使用 JWT

Claude：我来重构认证模块……
【做了大量修改】

用户：等等，OAuth 集成被弄坏了。我们回去吧。

Claude：我帮你回退到重构之前……
【用户连按 Esc+Esc 并选择重构前的 Checkpoint】

用户：这次我们换一种更稳妥的做法
```

<a id="example-3-safe-experimentation"></a>
### 示例 3：安全试验

```
用户：我们试试用函数式风格重写这段
【在试验前创建了 Checkpoint】

Claude：【做出试验性修改】

用户：测试挂了。我们回退吧。
【用户连按 Esc+Esc 并回退到该 Checkpoint】

Claude：已回退这些修改。我们换种做法试试。
```

<a id="example-4-branching-approaches"></a>
### 示例 4：分支式尝试

```
用户：我想对比两种数据库设计
【记下当前 Checkpoint，称之为「起点」】

Claude：我来实现第一种设计……
【实现 Schema A】

用户：现在我回去试第二种做法
【用户连按 Esc+Esc 并回退到「起点」】

Claude：接下来实现 Schema B……
【实现 Schema B】

用户：太好了！现在两种数据库结构我都能选了
```

<a id="checkpoint-retention"></a>
## Checkpoint 保留策略

Claude Code 会自动管理你的 Checkpoints：

- 每次用户输入都会自动创建 Checkpoint
- 较早的 Checkpoint 最多保留约 30 天
- 会自动清理，避免存储无限增长

<a id="workflow-patterns"></a>
## 工作流模式

<a id="branching-strategy-for-exploration"></a>
### 探索用的分支策略

在尝试多种方案时：

```
1. 从初始实现开始 → Checkpoint A
2. 尝试做法 1 → Checkpoint B
3. Rewind 回到 Checkpoint A
4. 尝试做法 2 → Checkpoint C
5. 对比 B 与 C 的结果
6. 选出最佳做法并继续
```

<a id="safe-refactoring-pattern"></a>
### 安全重构模式

在进行较大改动时：

```
1. 当前状态 → Checkpoint（自动）
2. 开始重构
3. 运行测试
4. 若通过 → 继续工作
5. 若失败 → Rewind 并换种做法
```

<a id="best-practices"></a>
## 最佳实践

由于 Checkpoints 会自动创建，你可以专心工作，而不必担心手动保存状态。但仍建议注意：

<a id="using-checkpoints-effectively"></a>
### 有效使用 Checkpoints

✅ **建议：**
- 在 Rewind 之前先查看可用的 Checkpoints
- 想换方向探索时使用 Rewind
- 保留 Checkpoints 以便对比不同做法
- 弄清每种 Rewind 选项的含义（恢复代码与对话、仅恢复对话、仅恢复代码，或从此处摘要）

❌ **不建议：**
- 仅依赖 Checkpoints 来保存代码
- 指望 Checkpoints 追踪外部文件系统的变更
- 用 Checkpoints 代替 git commit

<a id="configuration"></a>
## 配置

你可以在设置中开关自动 Checkpoint：

```json
{
  "autoCheckpoint": true
}
```

- `autoCheckpoint`：是否在每次用户输入时自动创建 Checkpoint（默认：`true`）

<a id="limitations"></a>
## 局限

Checkpoints 存在以下限制：

- **不会跟踪 Bash 命令带来的变更** — 诸如 `rm`、`mv`、`cp` 等对文件系统的操作不会被纳入 Checkpoints
- **不会跟踪外部变更** — 在 Claude Code 之外（编辑器、终端等）做出的修改不会被捕获
- **不能替代版本控制** — 对代码库做持久、可审计的变更请使用 git

<a id="troubleshooting"></a>
## 故障排除

<a id="missing-checkpoints"></a>
### 找不到 Checkpoint

**现象**：预期的 Checkpoint 不存在

**处理**：
- 确认 Checkpoints 是否已被清理
- 确认设置中已启用 `autoCheckpoint`
- 检查磁盘空间

<a id="rewind-failed"></a>
### Rewind 失败

**现象**：无法回退到某个 Checkpoint

**处理**：
- 确认没有未提交的变更与之冲突
- 检查该 Checkpoint 是否已损坏
- 尝试回退到其他 Checkpoint

<a id="integration-with-git"></a>
## 与 Git 的配合

Checkpoints 是对 git 的补充（而非替代）：

| 特性 | Git | Checkpoints |
|---------|-----|-------------|
| 范围 | 文件系统 | 对话 + 文件 |
| 持久性 | 长期 | 随会话策略保留 |
| 粒度 | Commit | 任意时刻 |
| 速度 | 较慢 | 即时 |
| 共享 | 可以 | 有限 |

建议两者一起用：
1. 用 Checkpoints 做快速试验
2. 用 git commit 固化最终变更
3. 在执行 git 操作前先创建 Checkpoint
4. 把成功的 Checkpoint 状态再提交到 git

<a id="quick-start-guide"></a>
## 快速上手

<a id="basic-workflow"></a>
### 基本流程

1. **照常工作** — Claude Code 会自动创建 Checkpoints
2. **想回到过去？** — 连按两次 `Esc` 或使用 `/rewind`
3. **选择 Checkpoint** — 从列表中选取要回退到的点
4. **选择恢复内容** — 在「恢复代码与对话」「仅恢复对话」「仅恢复代码」「从此处摘要」或「取消」之间选择
5. **继续工作** — 你已回到该时刻的状态

<a id="keyboard-shortcuts"></a>
### 键盘快捷键

- **`Esc` + `Esc`** — 打开 Checkpoint 浏览器
- **`/rewind`** — 另一种打开方式
- **`/checkpoint`** — `/rewind` 的别名

<a id="knowing-when-to-rewind-context-monitoring"></a>
## 何时该 Rewind：上下文监控

Checkpoints 让你能往回走——但怎么知道**什么时候**该走？随着对话变长，Claude 的上下文窗口会逐渐占满，模型质量会在不知不觉中下降。你可能在没意识到的情况下，就把「半盲」模型产出的代码推上线了。

**[cc-context-stats](https://github.com/luongnv89/cc-context-stats)** 通过在 Claude Code 状态栏加入实时 **context zones（上下文分区）** 来解决这一问题。它会显示你在上下文窗口中的位置——从 **Plan**（绿色，适合规划与编码）到 **Code**（黄色，避免再开新计划），再到 **Dump**（橙色，应收尾并考虑 Rewind）。当你看到分区变化时，就知道该做 Checkpoint 并新开一轮对话，而不是在质量下滑时硬撑。

<a id="related-concepts"></a>
## 相关概念

- **[高级功能](../09-advanced-features/)** — 规划模式及其他高级能力
- **[Memory](../02-memory/)** — 管理对话历史与上下文
- **[Slash Commands](../01-slash-commands/)** — 用户触发的快捷方式
- **[Hooks](../06-hooks/)** — 事件驱动自动化
- **[Plugins](../07-plugins/)** — 打包的扩展集合

<a id="additional-resources"></a>
## 延伸阅读

- [官方文档：Checkpointing](https://code.claude.com/docs/en/checkpointing)
- [高级功能指南](../09-advanced-features/) — 扩展思考（Extended thinking）及其他能力

<a id="summary"></a>
## 小结

Checkpoints 是 Claude Code 中的自动功能，让你可以放心尝试多种做法，而不必担心「回不去」。每次用户输入都会自动新建 Checkpoint，因此你可以回退到本会话中任意较早时刻。

主要收益：
- 大胆试验多种方案
- 快速从错误中恢复
- 并排对比不同解法
- 与版本控制系统安全配合

请记住：Checkpoints 不能替代 git。快速试验用 Checkpoints，永久性的代码变更用 git。
