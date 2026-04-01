# Code Review 问题记录模板

在代码审查中记录每个问题时请使用本模板。

---

## 问题：[标题]

### 严重程度
- [ ] Critical（阻塞发布）
- [ ] High（合并前应修复）
- [ ] Medium（应尽快修复）
- [ ] Low（锦上添花）

### 类别
- [ ] 安全（Security）
- [ ] 性能（Performance）
- [ ] 代码质量（Code Quality）
- [ ] 可维护性（Maintainability）
- [ ] 测试（Testing）
- [ ] 设计模式（Design Pattern）
- [ ] 文档（Documentation）

### 位置
**文件：** `src/components/UserCard.tsx`

**行号：** 45-52

**函数/方法：** `renderUserDetails()`

### 问题说明

**是什么：** 说明问题具体是什么。

**为何重要：** 说明影响以及为何需要修复。

**当前行为：** 展示有问题的代码或行为。

**预期行为：** 说明应当如何表现。

### 代码示例

#### 当前（有问题）

```typescript
// 展示 N+1 查询问题
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // 每个用户一次查询！
  renderUserPosts(posts);
});
```

#### 建议修复

```typescript
// 使用 JOIN 查询优化
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### 影响分析

| 方面 | 影响 | 严重程度 |
|--------|--------|----------|
| 性能 | 20 个用户触发 100+ 次查询 | High |
| 用户体验 | 页面加载缓慢 | High |
| 可扩展性 | 规模一大就会出问题 | Critical |
| 可维护性 | 难以调试 | Medium |

### 相关问题

- 类似问题：`AdminUserList.tsx` 第 120 行
- 相关 PR：#456
- 相关 issue：#789

### 延伸阅读

- [N+1 Query Problem](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Database Join Documentation](https://docs.example.com/joins)
- [Performance Optimization Guide](./docs/performance.md)

### 审查者备注

- 在本代码库中这是常见写法
- 可考虑写入代码风格指南
- 或许值得抽一个辅助函数

### 作者反馈（供回复填写）

*由代码作者填写：*

- [ ] 修复已提交于 commit：`abc123`
- [ ] 修复状态：已完成 / 进行中 / 需讨论
- [ ] 疑问或顾虑：（说明）

---

## 问题统计（供审查者使用）

审查多条问题时请记录：

- **发现问题总数：** X
- **Critical：** X
- **High：** X
- **Medium：** X
- **Low：** X

**建议：** ✅ 通过 / ⚠️ 请求修改 / 🔄 需讨论

**整体代码质量：** 1–5 星
