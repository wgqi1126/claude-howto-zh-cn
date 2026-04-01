# API 模块规范

本文件覆盖 `/src/api/` 目录下内容相对根目录 `CLAUDE.md` 的约定。

## API 专用规范

### 请求校验

- 使用 Zod 进行 schema 校验
- 始终校验输入
- 校验失败时返回 400
- 包含字段级错误详情

### 认证

- 所有端点需要 JWT token
- Token 放在 `Authorization` 请求头中
- Token 在 24 小时后过期
- 实现 refresh token 机制

### 响应格式

所有响应必须遵循以下结构：

```json
{
  "success": true,
  "data": { /* 实际数据 */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

错误响应：

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "面向用户的错误说明",
    "details": { /* 字段错误 */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### 分页

- 使用基于游标的分页（不使用 offset）
- 包含布尔字段 `hasMore`
- 单页最大条数限制为 100
- 默认每页 20 条

### 限流

- 已认证用户每小时 1000 次请求
- 公开端点每小时 100 次请求
- 超限时返回 429
- 包含 `Retry-After` 响应头

### 缓存

- 使用 Redis 做会话缓存
- 默认缓存时长 5 分钟
- 写操作后使缓存失效
- 在缓存键上按资源类型打标签
