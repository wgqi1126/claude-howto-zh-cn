<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# PR 审查插件

完整的 PR 审查工作流，包含安全、测试与文档检查。

## 功能

✅ 安全分析  
✅ 测试覆盖率检查  
✅ 文档校验  
✅ 代码质量评估  
✅ 性能影响分析  

## 安装

```bash
/plugin install pr-review
```

## 包含内容

### Slash 命令

- `/review-pr` - 全面 PR 审查  
- `/check-security` - 以安全为重点的审查  
- `/check-tests` - 测试覆盖率分析  

### Subagents

- `security-reviewer` - 安全漏洞检测  
- `test-checker` - 测试覆盖率分析  
- `performance-analyzer` - 性能影响评估  

### MCP 服务器

- 用于获取 PR 数据的 GitHub 集成  

### Hooks

- `pre-review.js` - 审查前校验  

## 使用

### 基础 PR 审查

```
/review-pr
```

### 仅安全检查

```
/check-security
```

### 测试覆盖率检查

```
/check-tests
```

## 环境要求

- Claude Code 1.0+  
- GitHub 访问权限  
- Git 仓库  

## 配置

设置 GitHub token：

```bash
export GITHUB_TOKEN="your_github_token"
```

## 示例工作流

```
用户：/review-pr

Claude：
1. 运行 pre-review hook（校验 git 仓库）
2. 通过 GitHub MCP 拉取 PR 数据
3. 将安全审查委托给 security-reviewer subagent
4. 将测试相关分析委托给 test-checker subagent
5. 将性能分析委托给 performance-analyzer subagent
6. 汇总所有发现
7. 输出完整审查报告

结果：
✅ 安全：未发现严重问题
⚠️  测试：覆盖率 65%，建议达到 80% 以上
✅ 性能：无明显影响
📝 建议：为边界情况补充测试
```
