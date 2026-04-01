<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To 教程" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 文档插件

为项目提供全面的文档生成与维护。

## 功能

✅ API 文档生成
✅ README 编写与更新
✅ 文档同步
✅ 代码注释改进
✅ 示例生成

## 安装

```bash
/plugin install documentation
```

## 包含内容

### Slash Commands
- `/generate-api-docs` — 生成 API 文档
- `/generate-readme` — 创建或更新 README
- `/sync-docs` — 将文档与代码变更同步
- `/validate-docs` — 校验文档

### Subagents
- `api-documenter` — API 文档专项
- `code-commentator` — 代码注释改进
- `example-generator` — 代码示例生成

### 模板
- `api-endpoint.md` — API 端点文档模板
- `function-docs.md` — 函数文档模板
- `adr-template.md` — 架构决策记录（ADR）模板

### MCP 服务器
- 用于文档同步的 GitHub 集成

## 使用

### 生成 API 文档
```
/generate-api-docs
```

### 创建 README
```
/generate-readme
```

### 同步文档
```
/sync-docs
```

### 校验文档
```
/validate-docs
```

## 环境要求

- Claude Code 1.0+
- GitHub 访问权限（可选）

## 示例工作流

```
用户: /generate-api-docs

Claude:
1. 扫描 /src/api/ 下的所有 API 端点
2. 委派给 api-documenter Subagent
3. 提取函数签名与 JSDoc
4. 按模块/端点组织
5. 使用 api-endpoint.md 模板
6. 生成完整的 Markdown 文档
7. 包含 curl、JavaScript 与 Python 示例

结果：
✅ 已生成 API 文档
📄 创建的文件：
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 覆盖率：23/23 个端点已写入文档
```

## 模板用法

### API 端点模板
用于编写带完整示例的 REST API 端点文档。

### 函数文档模板
用于编写单个函数或方法的文档。

### ADR 模板
用于记录架构决策。

## 配置

为文档同步配置 GitHub token：
```bash
export GITHUB_TOKEN="your_github_token"
```

## 最佳实践

- 让文档尽量贴近代码
- 随代码变更同步更新文档
- 提供可落地的示例
- 定期校验
- 使用模板保持一致性
