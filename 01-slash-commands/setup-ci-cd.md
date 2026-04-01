---
name: Setup CI/CD Pipeline
description: 为项目配置 pre-commit 钩子与 GitHub Actions，建立质量保障流程
tags: ci-cd, devops, automation
---

<a id="setup-cicd-pipeline"></a>

# 搭建 CI/CD 流水线

根据项目类型，落地一套完整的 DevOps 质量门禁：

1. **分析项目**：识别语言、框架、构建系统及既有工具链
2. **配置 pre-commit 钩子**，按语言选用相应工具：
   - 格式化：Prettier/Black/gofmt/rustfmt 等
   - 静态检查：ESLint/Ruff/golangci-lint/Clippy 等
   - 安全：Bandit/gosec/cargo-audit/npm audit 等
   - 类型检查：TypeScript/mypy/flow（如适用）
   - 测试：运行相关测试套件
3. **创建 GitHub Actions 工作流**（`.github/workflows/`）：
   - 在 push/PR 上与 pre-commit 检查保持一致
   - 多版本/多平台矩阵（如适用）
   - 构建与测试验证
   - 部署步骤（如需要）
4. **验证流水线**：在本地测试、创建测试 PR、确认所有检查通过

使用免费/开源工具。尊重既有配置。保持执行快速。
