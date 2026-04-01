# 函数：`functionName`

## 说明
简要说明该函数的作用。

## 签名
```typescript
function functionName(param1: Type1, param2: Type2): ReturnType
```

## 参数

| 参数 | 类型 | 必填 | 说明 |
|-----------|------|----------|-------------|
| param1 | Type1 | 是 | param1 的说明 |
| param2 | Type2 | 否 | param2 的说明 |

## 返回值
**类型**：`ReturnType`

说明返回的内容。

## 抛出
- `Error`：在输入无效时
- `TypeError`：在传入类型错误时

## 示例

### 基本用法
```typescript
const result = functionName('value1', 'value2');
console.log(result);
```

### 进阶用法
```typescript
const result = functionName(
  complexParam1,
  { option: true }
);
```

## 备注
- 额外说明或注意事项
- 性能相关考虑
- 最佳实践

## 另见
- [相关函数](#)
- [API 文档](#)
