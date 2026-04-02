<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude 概念完全指南

涵盖 Slash Commands、Subagents、Memory、MCP Protocol 与 Agent Skills 的参考手册，配有表格、示意图与实操示例。

---

## 目录

1. [Slash Commands](#slash-commands)
2. [Subagents](#subagents)
3. [Memory](#memory)
4. [MCP Protocol](#mcp-protocol)
5. [Agent Skills](#agent-skills)
6. [Plugins](#claude-code-plugins)
7. [Hooks](#hooks)
8. [Checkpoints and Rewind](#checkpoints-and-rewind)
9. [Advanced Features](#advanced-features)
10. [Comparison & Integration](#comparison--integration)

---

## Slash Commands

### 概述

Slash commands 是以 Markdown 文件形式存储、由用户触发的快捷方式，Claude Code 可执行其中的内容。团队可用其将常用提示与工作流标准化。

### 架构

```mermaid
graph TD
    A["用户输入: /command-name"] -->|触发| B["搜索 .claude/commands/"]
    B -->|找到| C["command-name.md"]
    C -->|加载| D["Markdown 内容"]
    D -->|执行| E["Claude 处理提示"]
    E -->|返回| F["上下文中结果"]
```

### 文件结构

```mermaid
graph LR
    A["项目根目录"] -->|包含| B[".claude/commands/"]
    B -->|包含| C["optimize.md"]
    B -->|包含| D["test.md"]
    B -->|包含| E["docs/"]
    E -->|包含| F["generate-api-docs.md"]
    E -->|包含| G["generate-readme.md"]
```

### 命令组织方式

| 位置 | 作用域 | 可用范围 | 适用场景 | 是否纳入 Git |
|----------|-------|--------------|----------|-------------|
| `.claude/commands/` | 项目级 | 团队成员 | 团队工作流、共享规范 | ✅ 是 |
| `~/.claude/commands/` | 个人 | 单个用户 | 跨项目的个人快捷方式 | ❌ 否 |
| 子目录 | 命名空间 | 随父级而定 | 按类别组织 | ✅ 是 |

### 功能与能力

| 功能 | 示例 | 是否支持 |
|---------|---------|-----------|
| 执行 Shell 脚本 | `bash scripts/deploy.sh` | ✅ 是 |
| 文件引用 | `@path/to/file.js` | ✅ 是 |
| Bash 集成 | `$(git log --oneline)` | ✅ 是 |
| 参数 | `/pr --verbose` | ✅ 是 |
| MCP 命令 | `/mcp__github__list_prs` | ✅ 是 |

### 实操示例

#### 示例 1：代码优化命令

**文件：** `.claude/commands/optimize.md`

```markdown
---
name: Code Optimization
description: 分析代码中的性能问题并提出优化建议
tags: performance, analysis
---

# Code Optimization

按优先级顺序审查所提供代码中的以下问题：

1. **性能瓶颈** — 识别 O(n²) 级操作、低效循环
2. **内存泄漏** — 查找未释放资源、循环引用
3. **算法改进** — 建议更优算法或数据结构
4. **缓存机会** — 识别重复计算
5. **并发问题** — 查找竞态或线程问题

请按以下结构组织回答：
- 问题严重程度（Critical/High/Medium/Low）
- 在代码中的位置
- 说明
- 建议修复方案并附代码示例
```

**用法：**
```bash
# 在 Claude Code 中输入
/optimize

# Claude 加载提示并等待代码输入
```

#### 示例 2：Pull Request 辅助命令

**文件：** `.claude/commands/pr.md`

```markdown
---
name: Prepare Pull Request
description: 整理代码、暂存变更并准备 pull request
tags: git, workflow
---

# Pull Request Preparation Checklist

创建 PR 前执行以下步骤：

1. 运行格式化：`prettier --write .`
2. 运行测试：`npm test`
3. 查看 git diff：`git diff HEAD`
4. 暂存变更：`git add .`
5. 按 conventional commits 撰写提交信息：
   - `fix:` 修复 bug
   - `feat:` 新功能
   - `docs:` 文档
   - `refactor:` 代码结构调整
   - `test:` 新增测试
   - `chore:` 维护类变更

6. 生成 PR 摘要，包含：
   - 改了什么
   - 为何改动
   - 已做哪些测试
   - 可能影响
```

**用法：**
```bash
/pr

# Claude 按清单执行并准备 PR
```

#### 示例 3：分层文档生成器

**文件：** `.claude/commands/docs/generate-api-docs.md`

```markdown
---
name: Generate API Documentation
description: 根据源代码生成完整的 API 文档
tags: documentation, api
---

# API Documentation Generator

通过以下方式生成 API 文档：

1. 扫描 `/src/api/` 下所有文件
2. 提取函数签名与 JSDoc 注释
3. 按端点/模块组织
4. 生成带示例的 Markdown
5. 包含请求/响应 schema
6. 补充错误说明

输出格式：
- `/docs/api.md` 中的 Markdown 文件
- 为所有端点提供 curl 示例
- 补充 TypeScript 类型
```

### 命令生命周期示意图

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant FS as File System
    participant CLI as Shell/Bash

    User->>Claude: 输入 /optimize
    Claude->>FS: 搜索 .claude/commands/
    FS-->>Claude: 返回 optimize.md
    Claude->>Claude: 加载 Markdown 内容
    Claude->>User: 展示提示上下文
    User->>Claude: 提供待分析代码
    Claude->>CLI: （可执行脚本）
    CLI-->>Claude: 结果
    Claude->>User: 返回分析
```

### 最佳实践

| ✅ 建议 | ❌ 避免 |
|------|---------|
| 使用清晰、面向动作的名称 | 为一次性任务创建命令 |
| 在 description 中写明触发词 | 在命令中堆砌复杂逻辑 |
| 每条命令聚焦单一任务 | 创建重复命令 |
| 将项目命令纳入版本控制 | 硬编码敏感信息 |
| 用子目录分类组织 | 罗列过长命令列表 |
| 使用简明可读的提示 | 使用晦涩缩写 |

---

## Subagents

### 概述

Subagents 是具有独立上下文窗口与定制系统提示的专业化 AI 助手，可在保持职责分离的前提下委派执行任务。

### 架构示意图

```mermaid
graph TB
    User["👤 User"]
    Main["🎯 Main Agent<br/>(Coordinator)"]
    Reviewer["🔍 Code Reviewer<br/>Subagent"]
    Tester["✅ Test Engineer<br/>Subagent"]
    Docs["📝 Documentation<br/>Subagent"]

    User -->|提问| Main
    Main -->|委派| Reviewer
    Main -->|委派| Tester
    Main -->|委派| Docs
    Reviewer -->|返回结果| Main
    Tester -->|返回结果| Main
    Docs -->|返回结果| Main
    Main -->|汇总| User
```

### Subagent 生命周期

```mermaid
sequenceDiagram
    participant User
    participant MainAgent as Main Agent
    participant CodeReviewer as Code Reviewer<br/>Subagent
    participant Context as Separate<br/>Context Window

    User->>MainAgent: "Build new auth feature"
    MainAgent->>MainAgent: 分析任务
    MainAgent->>CodeReviewer: "Review this code"
    CodeReviewer->>Context: 初始化干净上下文
    Context->>CodeReviewer: 加载审查者说明
    CodeReviewer->>CodeReviewer: 执行审查
    CodeReviewer-->>MainAgent: 返回发现
    MainAgent->>MainAgent: 整合结果
    MainAgent-->>User: 给出汇总
```

### Subagent 配置表

| 配置项 | 类型 | 用途 | 示例 |
|---------------|------|---------|---------|
| `name` | String | Agent 标识 | `code-reviewer` |
| `description` | String | 用途与触发用语 | `Comprehensive code quality analysis` |
| `tools` | List/String | 允许的能力 | `read, grep, diff, lint_runner` |
| `system_prompt` | Markdown | 行为说明 | 自定义准则 |

### 工具访问层级

```mermaid
graph TD
    A["Subagent 配置"] -->|选项 1| B["继承主线程<br/>全部工具"]
    A -->|选项 2| C["指定个别工具"]
    B -->|包含| B1["文件操作"]
    B -->|包含| B2["Shell 命令"]
    B -->|包含| B3["MCP 工具"]
    C -->|显式列表| C1["read, grep, diff"]
    C -->|显式列表| C2["Bash(npm:*), Bash(test:*)"]
```

### 实操示例

#### 示例 1：完整的 Subagent 配置

**文件：** `.claude/agents/code-reviewer.md`

```yaml
---
name: code-reviewer
description: 全面的代码质量与可维护性分析
tools: read, grep, diff, lint_runner
---

# Code Reviewer Agent

你是专注以下方面的代码审查专家：
- 性能优化
- 安全漏洞
- 代码可维护性
- 测试覆盖
- 设计模式

## 审查优先级（按顺序）

1. **安全问题** — 认证、授权、数据暴露
2. **性能问题** — O(n²) 操作、内存泄漏、低效查询
3. **代码质量** — 可读性、命名、文档
4. **测试覆盖** — 缺失测试、边界情况
5. **设计模式** — SOLID、架构

## 审查输出格式

对每个问题说明：
- **Severity**：Critical / High / Medium / Low
- **Category**：Security / Performance / Quality / Testing / Design
- **Location**：文件路径与行号
- **Issue Description**：问题与原因
- **Suggested Fix**：代码示例
- **Impact**：对系统的影响

## 示例审查

### Issue: N+1 Query Problem
- **Severity**: High
- **Category**: Performance
- **Location**: src/user-service.ts:45
- **Issue**: 循环中每次迭代都执行数据库查询
- **Fix**: 使用 JOIN 或批量查询
```

**文件：** `.claude/agents/test-engineer.md`

```yaml
---
name: test-engineer
description: 测试策略、覆盖分析与自动化测试
tools: read, write, bash, grep
---

# Test Engineer Agent

你擅长：
- 编写完整测试套件
- 保证较高代码覆盖率（>80%）
- 覆盖边界与错误场景
- 性能基准测试
- 集成测试

## 测试策略

1. **Unit Tests** — 单个函数/方法
2. **Integration Tests** — 组件交互
3. **End-to-End Tests** — 完整工作流
4. **Edge Cases** — 边界条件
5. **Error Scenarios** — 失败处理

## 测试输出要求

- JavaScript/TypeScript 使用 Jest
- 每个测试包含 setup/teardown
- Mock 外部依赖
- 说明测试目的
- 必要时包含性能断言

## 覆盖要求

- 最低 80% 代码覆盖率
- 关键路径 100%
- 报告未覆盖区域
```

**文件：** `.claude/agents/documentation-writer.md`

```yaml
---
name: documentation-writer
description: 技术文档、API 文档与用户指南
tools: read, write, grep
---

# Documentation Writer Agent

你负责产出：
- 带示例的 API 文档
- 用户指南与教程
- 架构文档
- Changelog 条目
- 代码注释改进

## 文档标准

1. **Clarity** — 语言简明清晰
2. **Examples** — 提供可运行代码示例
3. **Completeness** — 覆盖参数与返回值
4. **Structure** — 格式一致
5. **Accuracy** — 与真实代码核对

## 文档章节

### 针对 API
- Description
- Parameters（含类型）
- Returns（含类型）
- Throws（可能错误）
- Examples（curl、JavaScript、Python）
- Related endpoints

### 针对功能
- Overview
- Prerequisites
- 分步说明
- 预期结果
- Troubleshooting
- Related topics
```

#### 示例 2：Subagent 委派实战

```markdown
# 场景：构建支付功能

## 用户请求
"Build a secure payment processing feature that integrates with Stripe"

## 主 Agent 流程

1. **规划阶段**
   - 理解需求
   - 确定所需任务
   - 规划架构

2. **委派给 Code Reviewer Subagent**
   - 任务："Review the payment processing implementation for security"
   - 上下文：认证、API 密钥、令牌处理
   - 审查重点：SQL 注入、密钥暴露、HTTPS 强制

3. **委派给 Test Engineer Subagent**
   - 任务："Create comprehensive tests for payment flows"
   - 上下文：成功场景、失败、边界情况
   - 测试覆盖：有效支付、拒付、网络失败、webhook

4. **委派给 Documentation Writer Subagent**
   - 任务："Document the payment API endpoints"
   - 上下文：请求/响应 schema
   - 产出：含 curl 示例与错误码的 API 文档

5. **汇总**
   - 主 Agent 收集各输出
   - 整合结论
   - 向用户返回完整方案
```

#### 示例 3：工具权限范围

**限制性配置 — 仅允许特定能力**

```yaml
---
name: secure-reviewer
description: 以最小权限进行安全向代码审查
tools: read, grep
---

# Secure Code Reviewer

仅针对安全漏洞审查代码。

该 Agent：
- ✅ 读取文件进行分析
- ✅ 搜索模式
- ❌ 不能执行代码
- ❌ 不能修改文件
- ❌ 不能运行测试

从而避免审查者意外破坏环境。
```

**扩展配置 — 实现功能所需的全部工具**

```yaml
---
name: implementation-agent
description: 功能开发所需的完整实现能力
tools: read, write, bash, grep, edit, glob
---

# Implementation Agent

根据规格实现功能。

该 Agent：
- ✅ 阅读规格说明
- ✅ 编写新代码文件
- ✅ 运行构建命令
- ✅ 搜索代码库
- ✅ 编辑已有文件
- ✅ 按模式查找文件

具备独立完成功能开发的完整能力。
```

### Subagent 上下文管理

```mermaid
graph TB
    A["主 Agent 上下文<br/>50,000 tokens"]
    B["Subagent 1 上下文<br/>20,000 tokens"]
    C["Subagent 2 上下文<br/>20,000 tokens"]
    D["Subagent 3 上下文<br/>20,000 tokens"]

    A -->|干净起点| B
    A -->|干净起点| C
    A -->|干净起点| D

    B -->|仅结果| A
    C -->|仅结果| A
    D -->|仅结果| A

    style A fill:#e1f5ff
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

### 何时使用 Subagents

| 场景 | 是否使用 Subagent | 原因 |
|----------|--------------|-----|
| 步骤多的复杂功能 | ✅ 是 | 分离关注点，避免上下文污染 |
| 快速代码审查 | ❌ 否 | 不必要开销 |
| 并行执行任务 | ✅ 是 | 各 Subagent 有独立上下文 |
| 需要专项能力 | ✅ 是 | 可定制 system prompt |
| 长时间分析 | ✅ 是 | 避免主上下文耗尽 |
| 单一简单任务 | ❌ 否 | 徒增延迟 |

### Agent Teams

Agent Teams 协调多个 Agent 处理相关任务。与一次只委派一个 Subagent 不同，Agent Teams 让主 Agent 编排一组协作的 Agent，共享中间结果并朝共同目标推进。适合全栈功能开发等大规模任务，例如前端、后端与测试 Agent 并行工作。

---

## Memory

### 概述

Memory 让 Claude 在会话与对话之间保留上下文。有两种形态：claude.ai 中的自动合成，以及 Claude Code 中基于文件系统的 CLAUDE.md。

### Memory 架构

```mermaid
graph TB
    A["Claude Session"]
    B["User Input"]
    C["Memory System"]
    D["Memory Storage"]

    B -->|用户提供信息| C
    C -->|每 24 小时合成| D
    D -->|自动加载| A
    A -->|使用上下文| C
```

### Claude Code 中的 Memory 层级（7 层）

Claude Code 从 7 个层级加载 memory，以下按优先级从高到低列出：

```mermaid
graph TD
    A["1. Managed Policy<br/>企业管理员策略"] --> B["2. Project Memory<br/>./CLAUDE.md"]
    B --> C["3. Project Rules<br/>.claude/rules/*.md"]
    C --> D["4. User Memory<br/>~/.claude/CLAUDE.md"]
    D --> E["5. User Rules<br/>~/.claude/rules/*.md"]
    E --> F["6. Local Memory<br/>.claude/local/CLAUDE.md"]
    F --> G["7. Auto Memory<br/>自动捕获的偏好"]

    style A fill:#fce4ec,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e1f5fe,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
    style G fill:#fff3e0,stroke:#333,color:#333
```

### Memory 位置一览

| 层级 | 位置 | 作用域 | 优先级 | 共享 | 最适用 |
|------|----------|-------|----------|--------|----------|
| 1. Managed Policy | 企业管理员 | 组织 | 最高 | 组织内用户 | 合规与安全策略 |
| 2. Project | `./CLAUDE.md` | 项目 | 高 | 团队（Git） | 团队规范与架构 |
| 3. Project Rules | `.claude/rules/*.md` | 项目 | 高 | 团队（Git） | 模块化项目约定 |
| 4. User | `~/.claude/CLAUDE.md` | 个人 | 中 | 个人 | 个人偏好 |
| 5. User Rules | `~/.claude/rules/*.md` | 个人 | 中 | 个人 | 个人规则模块 |
| 6. Local | `.claude/local/CLAUDE.md` | 本地 | 低 | 不共享 | 机器相关设置 |
| 7. Auto Memory | 自动 | 会话 | 最低 | 个人 | 习得的偏好与模式 |

### Auto Memory

Auto Memory 会自动捕获会话中观察到的用户偏好与模式。Claude 从你的交互中学习并记住：

- 代码风格偏好
- 你常做的修正
- 框架与工具选择
- 沟通风格偏好

Auto Memory 在后台工作，无需手动配置。

### Memory 更新生命周期

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Editor as File System
    participant Memory as CLAUDE.md

    User->>Claude: "Remember: use async/await"
    Claude->>User: "Which memory file?"
    User->>Claude: "Project memory"
    Claude->>Editor: 打开 ~/.claude/settings.json
    Claude->>Memory: 写入 ./CLAUDE.md
    Memory-->>Claude: 文件已保存
    Claude->>Claude: 加载更新后的 memory
    Claude-->>User: "Memory saved!"
```

### 实操示例

#### 示例 1：项目 Memory 结构

**文件：** `./CLAUDE.md`

```markdown
# Project Configuration

## Project Overview
- **Name**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Team Size**: 5 developers
- **Deadline**: Q4 2025

## Architecture
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## Development Standards

### Code Style
- 使用 Prettier 格式化
- ESLint 使用 airbnb 配置
- 最大行宽：100 字符
- 使用 2 空格缩进

### Naming Conventions
- **Files**: kebab-case（如 user-controller.js）
- **Classes**: PascalCase（如 UserService）
- **Functions/Variables**: camelCase（如 getUserById）
- **Constants**: UPPER_SNAKE_CASE（如 API_BASE_URL）
- **Database Tables**: snake_case（如 user_accounts）

### Git Workflow
- 分支名：`feature/description` 或 `fix/description`
- 提交信息：遵循 conventional commits
- 合并前需要 PR
- 必须通过全部 CI/CD 检查
- 至少 1 人审批

### Testing Requirements
- 最低 80% 代码覆盖率
- 关键路径必须有测试
- 单元测试使用 Jest
- E2E 使用 Cypress
- 测试文件名：`*.test.ts` 或 `*.spec.ts`

### API Standards
- 仅 RESTful 端点
- JSON 请求/响应
- 正确使用 HTTP 状态码
- API 版本：`/api/v1/`
- 为所有端点编写文档与示例

### Database
- 使用 migration 管理 schema 变更
- 禁止硬编码凭据
- 使用连接池
- 开发环境启用查询日志
- 定期备份

### Deployment
- 基于 Docker 部署
- Kubernetes 编排
- 蓝绿发布策略
- 失败时自动回滚
- 部署前运行数据库 migration

## Common Commands

| Command | 说明 |
|---------|---------|
| `npm run dev` | 启动开发服务器 |
| `npm test` | 运行测试套件 |
| `npm run lint` | 检查代码风格 |
| `npm run build` | 生产构建 |
| `npm run migrate` | 执行数据库 migration |

## Team Contacts
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## Known Issues & Workarounds
- 高峰时段 PostgreSQL 连接池上限为 20
- 变通：实现查询排队
- Safari 14 与 async generator 的兼容问题
- 变通：使用 Babel 转译

## Related Projects
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`
```

#### 示例 2：目录级 Memory

**文件：** `./src/api/CLAUDE.md`

~~~~markdown
# API Module Standards

本文件覆盖 /src/api/ 下所有内容，优先级高于根目录 CLAUDE.md

## API-Specific Standards

### Request Validation
- 使用 Zod 做 schema 校验
- 始终校验输入
- 校验失败返回 400
- 提供字段级错误详情

### Authentication
- 所有端点需要 JWT
- Token 放在 Authorization 头
- Token 24 小时过期
- 实现 refresh token 机制

### Response Format

所有响应须符合以下结构：

```json
{
  "success": true,
  "data": { /* actual data */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

### Error responses
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* field errors */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Pagination
- 使用基于游标的分页（不用 offset）
- 包含 `hasMore` 布尔值
- 单页最大 100 条
- 默认每页 20 条

### Rate Limiting
- 已认证用户每小时 1000 次请求
- 公开端点每小时 100 次
- 超限时返回 429
- 包含 retry-after 头

### Caching
- 使用 Redis 做会话缓存
- 默认缓存时长 5 分钟
- 写操作后失效
- 缓存键按资源类型打标签
~~~~

#### 示例 3：个人 Memory

**文件：** `~/.claude/CLAUDE.md`

~~~~markdown
# My Development Preferences

## About Me
- **Experience Level**: 8 years full-stack development
- **Preferred Languages**: TypeScript, Python
- **Communication Style**: Direct, with examples
- **Learning Style**: Visual diagrams with code

## Code Preferences

### Error Handling
偏好使用 try-catch 与有意义的错误信息，避免笼统报错；调试时务必记录日志。

### Comments
注释说明「为什么」，而非「做什么」；代码应自解释；注释用于业务逻辑或非显而易见决策。

### Testing
偏好 TDD：先写测试再实现；关注行为而非实现细节。

### Architecture
偏好模块化、松耦合；用依赖注入便于测试；职责分离（Controllers、Services、Repositories）。

## Debugging Preferences
- console.log 使用前缀：`[DEBUG]`
- 附带上下文：函数名、相关变量
- 可用时使用堆栈
- 日志包含时间戳

## Communication
- 用图表解释复杂概念
- 先给具体示例再讲理论
- 提供修改前后代码片段
- 结尾总结要点

## Project Organization
项目目录组织示例：
```
project/
  ├── src/
  │   ├── api/
  │   ├── services/
  │   ├── models/
  │   └── utils/
  ├── tests/
  ├── docs/
  └── docker/
```

## Tooling
- **IDE**: VS Code with vim keybindings
- **Terminal**: Zsh with Oh-My-Zsh
- **Format**: Prettier（100 字符行宽）
- **Linter**: ESLint with airbnb config
- **Test Framework**: Jest with React Testing Library
~~~~

#### 示例 4：会话中更新 Memory

**会话交互：**

```markdown
User: Remember that I prefer using React hooks instead of class components
     for all new components.

Claude: I'm adding that to your memory. Which memory file should this go in?
        1. Project memory (./CLAUDE.md)
        2. Personal memory (~/.claude/CLAUDE.md)

User: Project memory

Claude: ✅ Memory saved!

Added to ./CLAUDE.md:
---

### Component Development
- Use functional components with React Hooks
- Prefer hooks over class components
- Custom hooks for reusable logic
- Use useCallback for event handlers
- Use useMemo for expensive computations
```

### Claude Web / Desktop 中的 Memory

#### Memory 合成时间线

```mermaid
graph LR
    A["第 1 天：用户<br/>对话"] -->|24 小时| B["第 2 天：Memory<br/>合成"]
    B -->|自动| C["Memory 更新<br/>摘要"]
    C -->|加载到| D["第 2–N 天：<br/>新对话"]
    D -->|并入| E["Memory"]
    E -->|再过 24 小时| F["Memory 刷新"]
```

**Memory 摘要示例：**

```markdown
## Claude's Memory of User

### Professional Background
- 8 年经验的高级全栈开发者
- 侧重 TypeScript/Node.js 后端与 React 前端
- 积极参与开源
- 关注 AI 与机器学习

### Project Context
- 正在搭建电商平台
- 技术栈：Node.js、PostgreSQL、React 18、Docker
- 5 人开发团队
- 使用 CI/CD 与蓝绿部署

### Communication Preferences
- 偏好直接、简洁说明
- 喜欢示意图与示例
- 重视代码片段
- 在注释中说明业务逻辑

### Current Goals
- 提升 API 性能
- 测试覆盖率提升至 90%
- 实施缓存策略
- 文档化架构
```

### Memory 功能对比

| 功能 | Claude Web/Desktop | Claude Code（CLAUDE.md） |
|---------|-------------------|------------------------|
| 自动合成 | ✅ 每 24 小时 | ❌ 手动 |
| 跨项目 | ✅ 共享 | ❌ 按项目 |
| 团队访问 | ✅ 共享项目 | ✅ Git 跟踪 |
| 可搜索 | ✅ 内置 | ✅ 通过 `/memory` |
| 可编辑 | ✅ 对话内 | ✅ 直接编辑文件 |
| 导入/导出 | ✅ 支持 | ✅ 复制粘贴 |
| 持久性 | ✅ 24h+ | ✅ 长期 |

---

## MCP Protocol

### 概述

MCP（Model Context Protocol）是 Claude 访问外部工具、API 与实时数据源的标准方式。与 Memory 不同，MCP 提供对变化中数据的实时访问。

### MCP 架构

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|请求: list_issues| B
    B -->|查询| C
    C -->|数据| B
    B -->|响应| A

    A -->|请求: create_issue| B
    B -->|操作| C
    C -->|结果| B
    B -->|响应| A
```

### MCP 生态

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|文件 I/O| G["本地文件"]
    C -->|API| H["GitHub 仓库"]
    D -->|查询| I["PostgreSQL/MySQL"]
    E -->|消息| J["Slack Workspace"]
    F -->|文档| K["Google Drive"]
```

### MCP 配置流程

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as External Service

    User->>Claude: 输入 /mcp
    Claude->>Claude: 列出可用 MCP 服务器
    Claude->>User: 展示选项
    User->>Claude: 选择 GitHub MCP
    Claude->>Config: 更新配置
    Config->>Claude: 激活连接
    Claude->>Service: 测试连接
    Service-->>Claude: 认证成功
    Claude->>User: ✅ MCP connected!
```

### 常用 MCP 服务器一览

| MCP Server | 用途 | 常见工具 | 认证 | 实时 |
|------------|---------|--------------|------|-----------|
| **Filesystem** | 文件操作 | read, write, delete | 操作系统权限 | ✅ 是 |
| **GitHub** | 仓库管理 | list_prs, create_issue, push | OAuth | ✅ 是 |
| **Slack** | 团队沟通 | send_message, list_channels | Token | ✅ 是 |
| **Database** | SQL 查询 | query, insert, update | 凭据 | ✅ 是 |
| **Google Docs** | 文档访问 | read, write, share | OAuth | ✅ 是 |
| **Asana** | 项目管理 | create_task, update_status | API Key | ✅ 是 |
| **Stripe** | 支付数据 | list_charges, create_invoice | API Key | ✅ 是 |
| **Memory** | 持久 memory | store, retrieve, delete | 本地 | ❌ 否 |

### 实操示例

#### 示例 1：GitHub MCP 配置

**文件：** `.mcp.json`（项目级）或 `~/.claude.json`（用户级）

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**可用的 GitHub MCP 工具：**

~~~~markdown
# GitHub MCP Tools

## Pull Request Management
- `list_prs` - 列出仓库内所有 PR
- `get_pr` - 获取 PR 详情（含 diff）
- `create_pr` - 创建新 PR
- `update_pr` - 更新 PR 描述/标题
- `merge_pr` - 将 PR 合并到 main
- `review_pr` - 添加审查评论

示例请求：
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

## Issue Management
- `list_issues` - 列出所有 issue
- `get_issue` - 获取 issue 详情
- `create_issue` - 创建 issue
- `close_issue` - 关闭 issue
- `add_comment` - 在 issue 下评论

## Repository Information
- `get_repo_info` - 仓库信息
- `list_files` - 文件树结构
- `get_file_content` - 读取文件内容
- `search_code` - 在代码库中搜索

## Commit Operations
- `list_commits` - 提交历史
- `get_commit` - 指定提交详情
- `create_commit` - 创建新提交
~~~~

#### 示例 2：Database MCP 配置

**配置：**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-database"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

**用法示例：**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# 使用 MCP database 工具：
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Results:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

#### 示例 3：多 MCP 工作流

**场景：每日报告生成**

```markdown
# Daily Report Workflow using Multiple MCPs

## Setup
1. GitHub MCP - 拉取 PR 指标
2. Database MCP - 查询销售数据
3. Slack MCP - 发布报告
4. Filesystem MCP - 保存报告

## Workflow

### Step 1: Fetch GitHub Data
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Step 2：查询数据库
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Step 3：生成报告
将数据合并为 HTML 报告

### Step 4：保存到 Filesystem
将 report.html 写入 /reports/

### Step 5：发布到 Slack
将摘要发到 #daily-reports 频道

Final Output:
✅ 报告已生成并发布
📊 本周合并 47 个 PR
💰 日销售额 $12,450
```

#### 示例 4：Filesystem MCP 操作

**配置：**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    }
  }
}
```

**可用操作：**

| Operation | Command | 用途 |
|-----------|---------|---------|
| List files | `ls ~/projects` | 列出目录内容 |
| Read file | `cat src/main.ts` | 读取文件 |
| Write file | `create docs/api.md` | 创建新文件 |
| Edit file | `edit src/app.ts` | 修改文件 |
| Search | `grep "async function"` | 在文件中搜索 |
| Delete | `rm old-file.js` | 删除文件 |

### MCP 与 Memory：决策矩阵

```mermaid
graph TD
    A["需要外部数据？"]
    A -->|否| B["使用 Memory"]
    A -->|是| C["是否频繁变化？"]
    C -->|否/很少| B
    C -->|是/经常| D["使用 MCP"]

    B -->|存储| E["偏好<br/>上下文<br/>历史"]
    D -->|访问| F["实时 API<br/>数据库<br/>服务"]

    style B fill:#e1f5ff
    style D fill:#fff9c4
```

### 请求/响应模式

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
    App->>App: Process result
    App->>App: Continue task

    Note over MCP,DB: 实时访问<br/>无缓存
```

---

## Agent Skills

### 概述

Agent Skills 是可复用、由模型调用的能力，以目录形式打包说明、脚本与资源。Claude 会自动识别并使用相关 Skills。

### Skill 架构

```mermaid
graph TB
    A["Skill 目录"]
    B["SKILL.md"]
    C["YAML 元数据"]
    D["说明"]
    E["脚本"]
    F["模板"]

    A --> B
    B --> C
    B --> D
    E --> A
    F --> A
```

### Skill 加载流程

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude
    participant System as System
    participant Skill as Skill

    User->>Claude: "Create Excel report"
    Claude->>System: 扫描可用 skills
    System->>System: 加载 skill 元数据
    Claude->>Claude: 将用户请求与 skills 匹配
    Claude->>Skill: 加载 xlsx skill 的 SKILL.md
    Skill-->>Claude: 返回说明与工具
    Claude->>Claude: 执行 skill
    Claude->>User: 生成 Excel 文件
```

### Skill 类型与位置

| 类型 | 位置 | 作用域 | 共享 | 同步 | 最适用 |
|------|----------|-------|--------|------|----------|
| Pre-built | 内置 | 全局 | 所有用户 | 自动 | 文档创建 |
| Personal | `~/.claude/skills/` | 个人 | 否 | 手动 | 个人自动化 |
| Project | `.claude/skills/` | 团队 | 是 | Git | 团队规范 |
| Plugin | 通过 plugin 安装 | 视情况而定 | 视插件而定 | 自动 | 集成功能 |

### 预置 Skills

```mermaid
graph TB
    A["Pre-built Skills"]
    B["PowerPoint (pptx)"]
    C["Excel (xlsx)"]
    D["Word (docx)"]
    E["PDF"]

    A --> B
    A --> C
    A --> D
    A --> E

    B --> B1["创建演示文稿"]
    B --> B2["编辑幻灯片"]
    C --> C1["创建电子表格"]
    C --> C2["分析数据"]
    D --> D1["创建文档"]
    D --> D2["排版文本"]
    E --> E1["生成 PDF"]
    E --> E2["填写表单"]
```

### 捆绑 Skills

Claude Code 现内置 5 个捆绑 skills，开箱即用：

| Skill | Command | 用途 |
|-------|---------|---------|
| **Simplify** | `/simplify` | 简化复杂代码或说明 |
| **Batch** | `/batch` | 在多个文件或条目上批量执行操作 |
| **Debug** | `/debug` | 系统化调试并分析根因 |
| **Loop** | `/loop` | 按定时器安排重复任务 |
| **Claude API** | `/claude-api` | 直接调用 Anthropic API |

这些捆绑 skills 始终可用，无需安装或配置。

### 实操示例

#### 示例 1：自定义代码审查 Skill

**目录结构：**

```
~/.claude/skills/code-review/
├── SKILL.md
├── templates/
│   ├── review-checklist.md
│   └── finding-template.md
└── scripts/
    ├── analyze-metrics.py
    └── compare-complexity.py
```

**文件：** `~/.claude/skills/code-review/SKILL.md`

```yaml
---
name: Code Review Specialist
description: 涵盖安全、性能与质量的全面代码审查
version: "1.0.0"
tags:
  - code-review
  - quality
  - security
when_to_use: 当用户要求审查代码、分析代码质量或评估 pull request 时
effort: high
shell: bash
---

# Code Review Skill

本 skill 提供全面的代码审查能力，重点包括：

1. **Security Analysis**
   - 认证/授权问题
   - 数据暴露风险
   - 注入类漏洞
   - 加密实现弱点
   - 敏感数据写入日志

2. **Performance Review**
   - 算法效率（Big O）
   - 内存优化
   - 数据库查询优化
   - 缓存机会
   - 并发问题

3. **Code Quality**
   - SOLID 原则
   - 设计模式
   - 命名约定
   - 文档
   - 测试覆盖

4. **Maintainability**
   - 代码可读性
   - 函数体量（建议 < 50 行）
   - 圈复杂度
   - 依赖管理
   - 类型安全

## Review Template

对每段被审查的代码请提供：

### Summary
- 总体质量评分（1–5）
- 主要发现数量
- 建议优先处理项

### Critical Issues (if any)
- **Issue**：清晰描述
- **Location**：文件与行号
- **Impact**：为何重要
- **Severity**：Critical/High/Medium
- **Fix**：代码示例

### Findings by Category

#### Security (if issues found)
列出安全问题并附示例

#### Performance (if issues found)
列出性能问题并做复杂度分析

#### Quality (if issues found)
列出代码质量问题与重构建议

#### Maintainability (if issues found)
列出可维护性问题与改进方向
```
## Python 脚本：analyze-metrics.py

```python
#!/usr/bin/env python3
import re
import sys

def analyze_code_metrics(code):
    """Analyze code for common metrics."""

    # Count functions
    functions = len(re.findall(r'^def\s+\w+', code, re.MULTILINE))

    # Count classes
    classes = len(re.findall(r'^class\s+\w+', code, re.MULTILINE))

    # Average line length
    lines = code.split('\n')
    avg_length = sum(len(l) for l in lines) / len(lines) if lines else 0

    # Estimate complexity
    complexity = len(re.findall(r'\b(if|elif|else|for|while|and|or)\b', code))

    return {
        'functions': functions,
        'classes': classes,
        'avg_line_length': avg_length,
        'complexity_score': complexity
    }

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        code = f.read()
    metrics = analyze_code_metrics(code)
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")
```

## Python 脚本：compare-complexity.py

```python
#!/usr/bin/env python3
"""
Compare cyclomatic complexity of code before and after changes.
Helps identify if refactoring actually simplifies code structure.
"""

import re
import sys
from typing import Dict, Tuple

class ComplexityAnalyzer:
    """Analyze code complexity metrics."""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split('\n')

    def calculate_cyclomatic_complexity(self) -> int:
        """
        Calculate cyclomatic complexity using McCabe's method.
        Count decision points: if, elif, else, for, while, except, and, or
        """
        complexity = 1  # Base complexity

        # Count decision points
        decision_patterns = [
            r'\bif\b',
            r'\belif\b',
            r'\bfor\b',
            r'\bwhile\b',
            r'\bexcept\b',
            r'\band\b(?!$)',
            r'\bor\b(?!$)'
        ]

        for pattern in decision_patterns:
            matches = re.findall(pattern, self.code)
            complexity += len(matches)

        return complexity

    def calculate_cognitive_complexity(self) -> int:
        """
        Calculate cognitive complexity - how hard is it to understand?
        Based on nesting depth and control flow.
        """
        cognitive = 0
        nesting_depth = 0

        for line in self.lines:
            # Track nesting depth
            if re.search(r'^\s*(if|for|while|def|class|try)\b', line):
                nesting_depth += 1
                cognitive += nesting_depth
            elif re.search(r'^\s*(elif|else|except|finally)\b', line):
                cognitive += nesting_depth

            # Reduce nesting when unindenting
            if line and not line[0].isspace():
                nesting_depth = 0

        return cognitive

    def calculate_maintainability_index(self) -> float:
        """
        Maintainability Index ranges from 0-100.
        > 85: Excellent
        > 65: Good
        > 50: Fair
        < 50: Poor
        """
        lines = len(self.lines)
        cyclomatic = self.calculate_cyclomatic_complexity()
        cognitive = self.calculate_cognitive_complexity()

        # Simplified MI calculation
        mi = 171 - 5.2 * (cyclomatic / lines) - 0.23 * (cognitive) - 16.2 * (lines / 1000)

        return max(0, min(100, mi))

    def get_complexity_report(self) -> Dict:
        """Generate comprehensive complexity report."""
        return {
            'cyclomatic_complexity': self.calculate_cyclomatic_complexity(),
            'cognitive_complexity': self.calculate_cognitive_complexity(),
            'maintainability_index': round(self.calculate_maintainability_index(), 2),
            'lines_of_code': len(self.lines),
            'avg_line_length': round(sum(len(l) for l in self.lines) / len(self.lines), 2) if self.lines else 0
        }


def compare_files(before_file: str, after_file: str) -> None:
    """Compare complexity metrics between two code versions."""

    with open(before_file, 'r') as f:
        before_code = f.read()

    with open(after_file, 'r') as f:
        after_code = f.read()

    before_analyzer = ComplexityAnalyzer(before_code)
    after_analyzer = ComplexityAnalyzer(after_code)

    before_metrics = before_analyzer.get_complexity_report()
    after_metrics = after_analyzer.get_complexity_report()

    print("=" * 60)
    print("CODE COMPLEXITY COMPARISON")
    print("=" * 60)

    print("\nBEFORE:")
    print(f"  Cyclomatic Complexity:    {before_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {before_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {before_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {before_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {before_metrics['avg_line_length']}")

    print("\nAFTER:")
    print(f"  Cyclomatic Complexity:    {after_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {after_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {after_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {after_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {after_metrics['avg_line_length']}")

    print("\nCHANGES:")
    cyclomatic_change = after_metrics['cyclomatic_complexity'] - before_metrics['cyclomatic_complexity']
    cognitive_change = after_metrics['cognitive_complexity'] - before_metrics['cognitive_complexity']
    mi_change = after_metrics['maintainability_index'] - before_metrics['maintainability_index']
    loc_change = after_metrics['lines_of_code'] - before_metrics['lines_of_code']

    print(f"  Cyclomatic Complexity:    {cyclomatic_change:+d}")
    print(f"  Cognitive Complexity:     {cognitive_change:+d}")
    print(f"  Maintainability Index:    {mi_change:+.2f}")
    print(f"  Lines of Code:            {loc_change:+d}")

    print("\nASSESSMENT:")
    if mi_change > 0:
        print("  ✅ Code is MORE maintainable")
    elif mi_change < 0:
        print("  ⚠️  Code is LESS maintainable")
    else:
        print("  ➡️  Maintainability unchanged")

    if cyclomatic_change < 0:
        print("  ✅ Complexity DECREASED")
    elif cyclomatic_change > 0:
        print("  ⚠️  Complexity INCREASED")
    else:
        print("  ➡️  Complexity unchanged")

    print("=" * 60)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python compare-complexity.py <before_file> <after_file>")
        sys.exit(1)

    compare_files(sys.argv[1], sys.argv[2])
```

## 模板：review-checklist.md

```markdown
# Code Review Checklist

## Security Checklist
- [ ] 无硬编码凭据或密钥
- [ ] 对所有用户输入做校验
- [ ] 防止 SQL 注入（参数化查询）
- [ ] 对改变状态的操作做 CSRF 防护
- [ ] 正确转义以防 XSS
- [ ] 受保护端点有认证检查
- [ ] 资源级有授权检查
- [ ] 密码使用安全哈希（bcrypt、argon2 等）
- [ ] 日志中无敏感数据
- [ ] 强制 HTTPS

## Performance Checklist
- [ ] 无 N+1 查询
- [ ] 索引使用得当
- [ ] 在有益处使用缓存
- [ ] 主线程无阻塞操作
- [ ] 正确使用 async/await
- [ ] 大数据集分页
- [ ] 数据库连接池化
- [ ] 正则表达式已优化
- [ ] 无不必要的对象创建
- [ ] 防止内存泄漏

## Quality Checklist
- [ ] 函数少于 50 行
- [ ] 变量命名清晰
- [ ] 无重复代码
- [ ] 错误处理得当
- [ ] 注释说明「为什么」而非「做什么」
- [ ] 生产环境无 console.log
- [ ] 有类型检查（TypeScript/JSDoc）
- [ ] 遵循 SOLID
- [ ] 设计模式使用正确
- [ ] 代码自解释

## Testing Checklist
- [ ] 已编写单元测试
- [ ] 覆盖边界情况
- [ ] 已测错误场景
- [ ] 有集成测试
- [ ] 覆盖率 > 80%
- [ ] 无不稳定测试
- [ ] Mock 外部依赖
- [ ] 测试命名清晰
```

## 模板：finding-template.md

~~~~markdown
# Code Review Finding Template

记录审查中发现的每个问题时使用本模板。

---

## Issue: [TITLE]

### Severity
- [ ] Critical（阻塞发布）
- [ ] High（合并前应修复）
- [ ] Medium（应尽快修复）
- [ ] Low（锦上添花）

### Category
- [ ] Security
- [ ] Performance
- [ ] Code Quality
- [ ] Maintainability
- [ ] Testing
- [ ] Design Pattern
- [ ] Documentation

### Location
**File:** `src/components/UserCard.tsx`

**Lines:** 45-52

**Function/Method:** `renderUserDetails()`

### Issue Description

**What：** 说明问题是什么。

**Why it matters：** 说明影响及为何需要修复。

**Current behavior：** 展示有问题的代码或行为。

**Expected behavior：** 说明期望行为。

### Code Example

#### Current (Problematic)

```typescript
// Shows the N+1 query problem
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // Query per user!
  renderUserPosts(posts);
});
```

#### Suggested Fix

```typescript
// Optimized with JOIN query
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### Impact Analysis

| Aspect | Impact | Severity |
|--------|--------|----------|
| Performance | 20 个用户触发 100+ 次查询 | High |
| User Experience | 页面加载慢 | High |
| Scalability | 规模扩大时崩溃 | Critical |
| Maintainability | 难以调试 | Medium |

### Related Issues

- `AdminUserList.tsx` 第 120 行存在类似问题
- 相关 PR：#456
- 相关 issue：#789

### Additional Resources

- [N+1 Query Problem](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Database Join Documentation](https://docs.example.com/joins)

### Reviewer Notes

- 在本代码库中较常见
- 可考虑写入代码风格指南
- 可抽取为辅助函数

### Author Response (for feedback)

*由代码作者填写：*

- [ ] 修复已提交：`abc123`
- [ ] 修复状态：Complete / In Progress / Needs Discussion
- [ ] 疑问或顾虑：（说明）

---

## Finding Statistics (for Reviewer)

审查多项发现时请统计：

- **Total Issues Found：** X
- **Critical：** X
- **High：** X
- **Medium：** X
- **Low：** X

**Recommendation：** ✅ Approve / ⚠️ Request Changes / 🔄 Needs Discussion

**Overall Code Quality：** 1–5 星
~~~~

## 用法示例

~~~~markdown
User: Review this React component code

Claude: 我将使用 Code Review Skill 进行全面审查。

[加载 SKILL.md]
[对照清单分析代码]
[运行 Python 指标脚本]
[套用模板]

## Code Review Results

### Summary
Quality Score: 3.5/5
Key Findings: 7 条
Priority Areas: 性能优化、错误处理

### Critical Issues: 1

**Issue**: N+1 Query Problem
**Location**: UserComponent.tsx, lines 45-52
**Impact**: 20 个用户的列表触发 100+ 次数据库查询
**Severity**: High
**Fix**:
```javascript
// Before: N+1 queries
const users = fetchUsers();
users.forEach(user => fetchUserPosts(user.id)); // 20+ queries

// After: Single query with JOIN
const users = fetchUsersWithPosts(); // 1 query
```

### Performance Findings
- 大列表缺少分页
- 建议：列表项使用 React.memo()
- 数据库查询：可通过索引优化

### Quality Findings
- 第 20 行函数 127 行（上限 50）
- 缺少 error boundary
- Props 应有 TypeScript 类型
~~~~

#### 示例 2：Brand Voice Skill

**目录结构：**

```
.claude/skills/brand-voice/
├── SKILL.md
├── brand-guidelines.md
├── tone-examples.md
└── templates/
    ├── email-template.txt
    ├── social-post-template.txt
    └── blog-post-template.md
```

**文件：** `.claude/skills/brand-voice/SKILL.md`

```yaml
---
name: Brand Voice Consistency
description: 确保所有沟通符合品牌声线与语气指南
tags:
  - brand
  - writing
  - consistency
when_to_use: 撰写营销文案、客户沟通或对外内容时
---

# Brand Voice Skill

## Overview
本 skill 确保沟通在品牌声线、语气与信息上保持一致。

## Brand Identity

### Mission
Help teams automate their development workflows with AI

### Values
- **Simplicity**：把复杂事变简单
- **Reliability**：可靠执行
- **Empowerment**：赋能人的创造力

### Tone of Voice
- **Friendly but professional**：亲切但不随意
- **Clear and concise**：少术语，技术概念讲清楚
- **Confident**：体现专业把握
- **Empathetic**：理解用户需求与痛点

## Writing Guidelines

### Do's ✅
- 对读者用「你」
- 主动语态：用「Claude generates reports」而非「Reports are generated by Claude」
- 开篇点出价值主张
- 使用具体示例
- 单句尽量少于 20 词
- 用列表提高可读性
- 包含明确行动号召

### Don'ts ❌
- 不用空洞「企业腔」
- 不居高临下或过度简化
- 少用「we believe」「we think」
- 除强调外不用全大写
- 避免大段文字墙
- 不预设读者技术水平

## Vocabulary

### ✅ Preferred Terms
- Claude（不说 “the Claude AI”）
- Code generation（不说 “auto-coding”）
- Agent（不说 “bot”）
- Streamline（不说 “revolutionize”）
- Integrate（不说 “synergize”）

### ❌ Avoid Terms
- “Cutting-edge”（滥用）
- “Game-changer”（空洞）
- “Leverage”（套话）
- “Utilize”（改用 “use”）
- “Paradigm shift”（含糊）
```
## Examples

### ✅ Good Example
"Claude automates your code review process. Instead of manually checking each PR, Claude reviews security, performance, and quality—saving your team hours every week."

有效原因：价值清晰、收益具体、导向行动

### ❌ Bad Example
"Claude leverages cutting-edge AI to provide comprehensive software development solutions."

无效原因：空洞、套话、无具体价值

## 模板：Email

```
Subject: [清晰、突出益处的主题]

Hi [Name],

[开篇：对对方的价值]

[正文：如何运作 / 能得到什么]

[具体示例或收益]

[行动号召：下一步做什么]

Best regards,
[Name]
```

## 模板：Social Media

```
[首行抓注意力]
[2–3 行：价值或有趣事实]
[行动号召：链接、提问或互动]
[表情：最多 1–2 个点缀]
```

## 文件：tone-examples.md
```
Exciting announcement:
"Save 8 hours per week on code reviews. Claude reviews your PRs automatically."

Empathetic support:
"We know deployments can be stressful. Claude handles testing so you don't have to worry."

Confident product feature:
"Claude doesn't just suggest code. It understands your architecture and maintains consistency."

Educational blog post:
"Let's explore how agents improve code review workflows. Here's what we learned..."
```

#### 示例 3：文档生成 Skill

**文件：** `.claude/skills/doc-generator/SKILL.md`

~~~~yaml
---
name: API Documentation Generator
description: 根据源代码生成完整、准确的 API 文档
version: "1.0.0"
tags:
  - documentation
  - api
  - automation
when_to_use: 创建或更新 API 文档时
---

# API Documentation Generator Skill

## Generates

- OpenAPI/Swagger 规格
- API 端点文档
- SDK 使用示例
- 集成指南
- 错误码参考
- 认证指南

## Documentation Structure

### For Each Endpoint

```markdown
## GET /api/v1/users/:id

### Description
简要说明该端点作用

### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

### Response

**200 Success**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 Not Found**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "User does not exist"
}
```

### Examples

**cURL**
```bash
curl -X GET "https://api.example.com/api/v1/users/usr_123" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**JavaScript**
```javascript
const user = await fetch('/api/v1/users/usr_123', {
  headers: { 'Authorization': 'Bearer token' }
}).then(r => r.json());
```

**Python**
```python
response = requests.get(
    'https://api.example.com/api/v1/users/usr_123',
    headers={'Authorization': 'Bearer token'}
)
user = response.json()
```

## Python Script：generate-docs.py

```python
#!/usr/bin/env python3
import ast
import json
from typing import Dict, List

class APIDocExtractor(ast.NodeVisitor):
    """Extract API documentation from Python source code."""

    def __init__(self):
        self.endpoints = []

    def visit_FunctionDef(self, node):
        """Extract function documentation."""
        if node.name.startswith('get_') or node.name.startswith('post_'):
            doc = ast.get_docstring(node)
            endpoint = {
                'name': node.name,
                'docstring': doc,
                'params': [arg.arg for arg in node.args.args],
                'returns': self._extract_return_type(node)
            }
            self.endpoints.append(endpoint)
        self.generic_visit(node)

    def _extract_return_type(self, node):
        """Extract return type from function annotation."""
        if node.returns:
            return ast.unparse(node.returns)
        return "Any"

def generate_markdown_docs(endpoints: List[Dict]) -> str:
    """Generate markdown documentation from endpoints."""
    docs = "# API Documentation\n\n"

    for endpoint in endpoints:
        docs += f"## {endpoint['name']}\n\n"
        docs += f"{endpoint['docstring']}\n\n"
        docs += f"**Parameters**: {', '.join(endpoint['params'])}\n\n"
        docs += f"**Returns**: {endpoint['returns']}\n\n"
        docs += "---\n\n"

    return docs

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        tree = ast.parse(f.read())

    extractor = APIDocExtractor()
    extractor.visit(tree)

    markdown = generate_markdown_docs(extractor.endpoints)
    print(markdown)
~~~~
### Skill 发现与调用

```mermaid
graph TD
    A["用户请求"] --> B["Claude 分析"]
    B -->|扫描| C["可用 Skills"]
    C -->|元数据匹配| D["Skill 描述是否匹配？"]
    D -->|是| E["加载 SKILL.md"]
    D -->|否| F["尝试下一个 skill"]
    F -->|还有更多？| D
    F -->|没有| G["使用通用知识"]
    E --> H["提取说明"]
    H --> I["执行 Skill"]
    I --> J["返回结果"]
```

### Skill 与其他功能

```mermaid
graph TB
    A["扩展 Claude"]
    B["Slash Commands"]
    C["Subagents"]
    D["Memory"]
    E["MCP"]
    F["Skills"]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F

    B -->|用户触发| G["快捷方式"]
    C -->|自动委派| H["隔离上下文"]
    D -->|持久| I["跨会话上下文"]
    E -->|实时| J["外部数据访问"]
    F -->|自动调用| K["自主执行"]
```

---

<a id="plugins"></a>
<a id="claude-code-plugins"></a>

## Claude Code Plugins

### 概述

Claude Code Plugins 是可一次命令安装的定制集合（slash commands、subagents、MCP servers 与 hooks），代表最高层扩展机制，将多种能力打包为可分享的统一体。

### 架构

```mermaid
graph TB
    A["Plugin"]
    B["Slash Commands"]
    C["Subagents"]
    D["MCP Servers"]
    E["Hooks"]
    F["Configuration"]

    A -->|打包| B
    A -->|打包| C
    A -->|打包| D
    A -->|打包| E
    A -->|打包| F
```

### Plugin 加载流程

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Plugin as Plugin Marketplace
    participant Install as Installation
    participant SlashCmds as Slash Commands
    participant Subagents
    participant MCPServers as MCP Servers
    participant Hooks
    participant Tools as Configured Tools

    User->>Claude: /plugin install pr-review
    Claude->>Plugin: 下载 plugin manifest
    Plugin-->>Claude: 返回 plugin 定义
    Claude->>Install: 解压组件
    Install->>SlashCmds: 配置
    Install->>Subagents: 配置
    Install->>MCPServers: 配置
    Install->>Hooks: 配置
    SlashCmds-->>Tools: 就绪
    Subagents-->>Tools: 就绪
    MCPServers-->>Tools: 就绪
    Hooks-->>Tools: 就绪
    Tools-->>Claude: Plugin installed ✅
```

### Plugin 类型与分发

| 类型 | 作用域 | 共享 | 权威来源 | 示例 |
|------|-------|--------|-----------|----------|
| Official | 全局 | 所有用户 | Anthropic | PR Review、Security Guidance |
| Community | 公开 | 所有用户 | 社区 | DevOps、Data Science |
| Organization | 内部 | 团队成员 | 公司 | 内部规范与工具 |
| Personal | 个人 | 单用户 | 开发者 | 自定义工作流 |

### Plugin 定义结构

```yaml
---
name: plugin-name
version: "1.0.0"
description: "本 plugin 的作用"
author: "Your Name"
license: MIT

# Plugin metadata
tags:
  - category
  - use-case

# Requirements
requires:
  - claude-code: ">=1.0.0"

# Components bundled
components:
  - type: commands
    path: commands/
  - type: agents
    path: agents/
  - type: mcp
    path: mcp/
  - type: hooks
    path: hooks/

# Configuration
config:
  auto_load: true
  enabled_by_default: true
---
```

### Plugin 目录结构

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── task-1.md
│   ├── task-2.md
│   └── workflows/
├── agents/
│   ├── specialist-1.md
│   ├── specialist-2.md
│   └── configs/
├── skills/
│   ├── skill-1.md
│   └── skill-2.md
├── hooks/
│   └── hooks.json
├── .mcp.json
├── .lsp.json
├── settings.json
├── templates/
│   └── issue-template.md
├── scripts/
│   ├── helper-1.sh
│   └── helper-2.py
├── docs/
│   ├── README.md
│   └── USAGE.md
└── tests/
    └── plugin.test.js
```

### 实操示例

#### 示例 1：PR Review Plugin

**文件：** `.claude-plugin/plugin.json`

```json
{
  "name": "pr-review",
  "version": "1.0.0",
  "description": "Complete PR review workflow with security, testing, and docs",
  "author": {
    "name": "Anthropic"
  },
  "license": "MIT"
}
```

**文件：** `commands/review-pr.md`

```markdown
---
name: Review PR
description: 启动包含安全与测试检查的全面 PR 审查
---

# PR Review

本命令启动完整的 pull request 审查，包括：

1. 安全分析
2. 测试覆盖验证
3. 文档更新
4. 代码质量检查
5. 性能影响评估
```

**文件：** `agents/security-reviewer.md`

```yaml
---
name: security-reviewer
description: 面向安全的代码审查
tools: read, grep, diff
---

# Security Reviewer

专注发现安全漏洞：
- 认证/授权问题
- 数据暴露
- 注入攻击
- 安全配置
```

**安装：**

```bash
/plugin install pr-review

# Result:
# ✅ 3 slash commands installed
# ✅ 3 subagents configured
# ✅ 2 MCP servers connected
# ✅ 4 hooks registered
# ✅ Ready to use!
```

#### 示例 2：DevOps Plugin

**组件：**

```
devops-automation/
├── commands/
│   ├── deploy.md
│   ├── rollback.md
│   ├── status.md
│   └── incident.md
├── agents/
│   ├── deployment-specialist.md
│   ├── incident-commander.md
│   └── alert-analyzer.md
├── mcp/
│   ├── github-config.json
│   ├── kubernetes-config.json
│   └── prometheus-config.json
├── hooks/
│   ├── pre-deploy.js
│   ├── post-deploy.js
│   └── on-error.js
└── scripts/
    ├── deploy.sh
    ├── rollback.sh
    └── health-check.sh
```

#### 示例 3：Documentation Plugin

**捆绑组件：**

```
documentation/
├── commands/
│   ├── generate-api-docs.md
│   ├── generate-readme.md
│   ├── sync-docs.md
│   └── validate-docs.md
├── agents/
│   ├── api-documenter.md
│   ├── code-commentator.md
│   └── example-generator.md
├── mcp/
│   ├── github-docs-config.json
│   └── slack-announce-config.json
└── templates/
    ├── api-endpoint.md
    ├── function-docs.md
    └── adr-template.md
```

### Plugin Marketplace

```mermaid
graph TB
    A["Plugin Marketplace"]
    B["Official<br/>Anthropic"]
    C["Community<br/>Marketplace"]
    D["Enterprise<br/>Registry"]

    A --> B
    A --> C
    A --> D

    B -->|分类| B1["Development"]
    B -->|分类| B2["DevOps"]
    B -->|分类| B3["Documentation"]

    C -->|搜索| C1["DevOps Automation"]
    C -->|搜索| C2["Mobile Dev"]
    C -->|搜索| C3["Data Science"]

    D -->|内部| D1["Company Standards"]
    D -->|内部| D2["Legacy Systems"]
    D -->|内部| D3["Compliance"]
```

### Plugin 安装与生命周期

```mermaid
graph LR
    A["发现"] -->|浏览| B["Marketplace"]
    B -->|选择| C["Plugin 页面"]
    C -->|查看| D["组件"]
    D -->|安装| E["/plugin install"]
    E -->|解压| F["配置"]
    F -->|激活| G["使用"]
    G -->|检查| H["更新"]
    H -->|可用| G
    G -->|完成| I["禁用"]
    I -->|稍后| J["启用"]
    J -->|返回| G
```

### Plugin 功能对比

| Feature | Slash Command | Skill | Subagent | Plugin |
|---------|---------------|-------|----------|--------|
| **Installation** | 手动复制 | 手动复制 | 手动配置 | 一条命令 |
| **Setup Time** | 约 5 分钟 | 约 10 分钟 | 约 15 分钟 | 约 2 分钟 |
| **Bundling** | 单文件 | 单文件 | 单文件 | 多项 |
| **Versioning** | 手动 | 手动 | 手动 | 自动 |
| **Team Sharing** | 复制文件 | 复制文件 | 复制文件 | Install ID |
| **Updates** | 手动 | 手动 | 手动 | 自动可用 |
| **Dependencies** | 无 | 无 | 无 | 可包含 |
| **Marketplace** | 否 | 否 | 否 | 是 |
| **Distribution** | 仓库 | 仓库 | 仓库 | Marketplace |

### Plugin 适用场景

| Use Case | Recommendation | Why |
|----------|-----------------|-----|
| **Team Onboarding** | ✅ 用 Plugin | 即时就绪，配置齐全 |
| **Framework Setup** | ✅ 用 Plugin | 捆绑框架相关命令 |
| **Enterprise Standards** | ✅ 用 Plugin | 集中分发与版本管理 |
| **Quick Task Automation** | ❌ 用 Command | Plugin 过重 |
| **Single Domain Expertise** | ❌ 用 Skill | 过重，用 skill 更合适 |
| **Specialized Analysis** | ❌ 用 Subagent | 手动创建或用 skill |
| **Live Data Access** | ❌ 用 MCP | 独立使用，不宜捆绑 |

### 何时创建 Plugin

```mermaid
graph TD
    A["是否应创建 plugin？"]
    A -->|需要多个组件| B{"多个 command<br/>或 subagent<br/>或 MCP？"}
    B -->|是| C["✅ 创建 Plugin"]
    B -->|否| D["使用单项功能"]
    A -->|团队工作流| E{"与团队<br/>共享？"}
    E -->|是| C
    E -->|否| F["保留本地配置"]
    A -->|复杂搭建| G{"需要自动<br/>配置？"}
    G -->|是| C
    G -->|否| D
```

### 发布 Plugin

**发布步骤：**

1. 创建包含全部组件的 plugin 结构
2. 编写 `.claude-plugin/plugin.json` manifest
3. 编写含文档的 `README.md`
4. 本地用 `/plugin install ./my-plugin` 测试
5. 提交到 plugin marketplace
6. 通过审核
7. 在 marketplace 上架
8. 用户一条命令即可安装

**提交示例：**

~~~~markdown
# PR Review Plugin

## Description
Complete PR review workflow with security, testing, and documentation checks.

## What's Included
- 3 条 slash commands，覆盖不同审查类型
- 3 个专业 subagents
- GitHub 与 CodeQL MCP 集成
- 自动化安全扫描 hooks

## Installation
```bash
/plugin install pr-review
```

## Features
✅ 安全分析
✅ 测试覆盖检查
✅ 文档校验
✅ 代码质量评估
✅ 性能影响分析

## Usage
```bash
/review-pr
/check-security
/check-tests
```

## Requirements
- Claude Code 1.0+
- GitHub access
- CodeQL (optional)
~~~~

### Plugin 与手动配置

**手动搭建（2+ 小时）：**
- 逐个安装 slash commands
- 分别创建 subagents
- 单独配置 MCP
- 手动设置 hooks
- 自行编写文档
- 发给团队（对方未必配置正确）

**使用 Plugin（约 2 分钟）：**
```bash
/plugin install pr-review
# ✅ 全部安装并配置完成
# ✅ 立即可用
# ✅ 团队可复现相同环境
```

---

## Comparison & Integration

### 功能对比矩阵

| Feature | Invocation | Persistence | Scope | Use Case |
|---------|-----------|------------|-------|----------|
| **Slash Commands** | 手动（`/cmd`） | 仅当前会话 | 单条命令 | 快捷方式 |
| **Subagents** | 自动委派 | 隔离上下文 | 专项任务 | 任务分发 |
| **Memory** | 自动加载 | 跨会话 | 用户/团队上下文 | 长期学习 |
| **MCP Protocol** | 自动查询 | 实时外部 | 实时数据 | 动态信息 |
| **Skills** | 自动调用 | 基于文件系统 | 可复用专长 | 自动化工作流 |

### 交互时间线

```mermaid
graph LR
    A["会话开始"] -->|加载| B["Memory（CLAUDE.md）"]
    B -->|发现| C["可用 Skills"]
    C -->|注册| D["Slash Commands"]
    D -->|连接| E["MCP Servers"]
    E -->|就绪| F["用户交互"]

    F -->|输入 /cmd| G["Slash Command"]
    F -->|请求| H["Skill 自动调用"]
    F -->|查询| I["MCP 数据"]
    F -->|复杂任务| J["委派给 Subagent"]

    G -->|使用| B
    H -->|使用| B
    I -->|使用| B
    J -->|使用| B
```

### 实操整合示例：客户支持自动化

#### 架构

```mermaid
graph TB
    User["客户邮件"] -->|接收| Router["Support Router"]

    Router -->|分析| Memory["Memory<br/>客户历史"]
    Router -->|查询| MCP1["MCP: Customer DB<br/>历史工单"]
    Router -->|检查| MCP2["MCP: Slack<br/>团队状态"]

    Router -->|复杂路由| Sub1["Subagent: Tech Support<br/>Context: Technical issues"]
    Router -->|简单路由| Sub2["Subagent: Billing<br/>Context: Payment issues"]
    Router -->|紧急路由| Sub3["Subagent: Escalation<br/>Context: Priority handling"]

    Sub1 -->|格式化| Skill1["Skill: Response Generator<br/>保持品牌声线"]
    Sub2 -->|格式化| Skill2["Skill: Response Generator"]
    Sub3 -->|格式化| Skill3["Skill: Response Generator"]

    Skill1 -->|生成| Output["格式化回复"]
    Skill2 -->|生成| Output
    Skill3 -->|生成| Output

    Output -->|发布| MCP3["MCP: Slack<br/>通知团队"]
    Output -->|发送| Reply["客户回复"]
```

#### 请求流程

```markdown
## Customer Support Request Flow

### 1. Incoming Email
"I'm getting error 500 when trying to upload files. This is blocking my workflow!"

### 2. Memory Lookup
- 加载含支持标准的 CLAUDE.md
- 查看客户历史：VIP、本月第 3 起事件

### 3. MCP Queries
- GitHub MCP：列出 open issues（找到相关 bug 报告）
- Database MCP：检查系统状态（无宕机报告）
- Slack MCP：确认工程团队是否知情

### 4. Skill Detection & Loading
- 请求匹配 “Technical Support” skill
- 从 Skill 加载支持回复模板

### 5. Subagent Delegation
- 路由到 Tech Support Subagent
- 提供上下文：客户历史、错误详情、已知问题
- Subagent 可使用：read、bash、grep

### 6. Subagent Processing
Tech Support Subagent：
- 在代码库中搜索文件上传相关 500 错误
- 在提交 8f4a2c 中发现近期变更
- 编写变通方案文档

### 7. Skill Execution
Response Generator Skill：
- 使用 Brand Voice 指南
- 以共情方式排版回复
- 包含变通步骤
- 链接相关文档

### 8. MCP Output
- 在 #support Slack 频道发帖
- @ 工程团队
- 在 Jira MCP 更新工单

### 9. Response
客户收到：
- 共情式确认
- 原因说明
- 即时变通方案
- 永久修复时间线
- 相关 issue 链接
```

### 完整功能编排

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Memory as Memory<br/>CLAUDE.md
    participant MCP as MCP Servers
    participant Skills as Skills
    participant SubAgent as Subagents

    User->>Claude: 请求："Build auth system"
    Claude->>Memory: 加载项目规范
    Memory-->>Claude: 认证规范、团队实践
    Claude->>MCP: 在 GitHub 查询类似实现
    MCP-->>Claude: 代码示例、最佳实践
    Claude->>Skills: 检测匹配的 Skills
    Skills-->>Claude: Security Review Skill + Testing Skill
    Claude->>SubAgent: 委派实现
    SubAgent->>SubAgent: 构建功能
    Claude->>Skills: 应用 Security Review Skill
    Skills-->>Claude: 安全清单结果
    Claude->>SubAgent: 委派测试
    SubAgent-->>Claude: 测试结果
    Claude->>User: 交付完整系统
```

### 何时使用各功能

```mermaid
graph TD
    A["新任务"] --> B{任务类型？}

    B -->|重复工作流| C["Slash Command"]
    B -->|需要实时数据| D["MCP Protocol"]
    B -->|下次还要记住| E["Memory"]
    B -->|专项子任务| F["Subagent"]
    B -->|领域特定工作| G["Skill"]

    C --> C1["✅ 团队快捷方式"]
    D --> D1["✅ 实时 API"]
    E --> E1["✅ 持久上下文"]
    F --> F1["✅ 并行执行"]
    G --> G1["✅ 自动调用的专长"]
```

### 选择决策树

```mermaid
graph TD
    Start["需要扩展 Claude？"]

    Start -->|快速重复任务| A{"手动还是自动？"}
    A -->|手动| B["Slash Command"]
    A -->|自动| C["Skill"]

    Start -->|需要外部数据| D{"是否实时？"}
    D -->|是| E["MCP Protocol"]
    D -->|否/跨会话| F["Memory"]

    Start -->|复杂项目| G{"多角色？"}
    G -->|是| H["Subagents"]
    G -->|否| I["Skills + Memory"]

    Start -->|长期上下文| J["Memory"]
    Start -->|团队工作流| K["Slash Command +<br/>Memory"]
    Start -->|全流程自动化| L["Skills +<br/>Subagents +<br/>MCP"]
```

---

## 总览表

| Aspect | Slash Commands | Subagents | Memory | MCP | Skills | Plugins |
|--------|---|---|---|---|---|---|
| **Setup Difficulty** | 易 | 中 | 易 | 中 | 中 | 易 |
| **Learning Curve** | 低 | 中 | 低 | 中 | 中 | 低 |
| **Team Benefit** | 高 | 高 | 中 | 高 | 高 | 很高 |
| **Automation Level** | 低 | 高 | 中 | 高 | 高 | 很高 |
| **Context Management** | 单会话 | 隔离 | 持久 | 实时 | 持久 | 全部能力 |
| **Maintenance Burden** | 低 | 中 | 低 | 中 | 中 | 低 |
| **Scalability** | 好 | 优 | 好 | 优 | 优 | 优 |
| **Shareability** | 一般 | 一般 | 好 | 好 | 好 | 优 |
| **Versioning** | 手动 | 手动 | 手动 | 手动 | 手动 | 自动 |
| **Installation** | 手动复制 | 手动配置 | 不适用 | 手动配置 | 手动复制 | 一条命令 |

---

## 快速上手

### 第 1 周：从简开始
- 为常见任务创建 2–3 条 slash commands
- 在设置中启用 Memory
- 在 CLAUDE.md 中记录团队规范

### 第 2 周：接入实时能力
- 配置 1 个 MCP（GitHub 或 Database）
- 使用 `/mcp` 完成配置
- 在工作流中查询实时数据

### 第 3 周：分工协作
- 为特定角色创建第一个 Subagent
- 使用 `/agents` 命令
- 用简单任务测试委派

### 第 4 周：自动化
- 为重复自动化创建第一个 Skill
- 使用 Skill marketplace 或自建
- 组合全部能力形成完整工作流

### 持续
- 每月回顾并更新 Memory
- 随模式沉淀新增 Skills
- 优化 MCP 查询
- 迭代 Subagent 提示

---

## Hooks

### 概述

Hooks 是事件驱动的 shell 命令，在 Claude Code 事件发生时自动执行，用于自动化、校验与自定义工作流，无需人工逐步触发。

### Hook 事件

Claude Code 在四类 hook（command、http、prompt、agent）下支持 **25 种 hook 事件**：

| Hook Event | Trigger | Use Cases |
|------------|---------|-----------|
| **SessionStart** | 会话开始/恢复/clear/compact | 环境准备、初始化 |
| **InstructionsLoaded** | 加载 CLAUDE.md 或 rules 文件 | 校验、转换、增强 |
| **UserPromptSubmit** | 用户提交提示 | 输入校验、提示过滤 |
| **PreToolUse** | 任意工具运行前 | 校验、审批门禁、日志 |
| **PermissionRequest** | 显示权限对话框 | 自动同意/拒绝流程 |
| **PostToolUse** | 工具成功执行后 | 自动格式化、通知、清理 |
| **PostToolUseFailure** | 工具执行失败 | 错误处理、日志 |
| **Notification** | 发送通知 | 告警、外部集成 |
| **SubagentStart** | 创建 Subagent | 注入上下文、初始化 |
| **SubagentStop** | Subagent 结束 | 结果校验、日志 |
| **Stop** | Claude 完成回复 | 生成摘要、清理任务 |
| **StopFailure** | API 错误结束本轮 | 错误恢复、日志 |
| **TeammateIdle** | Agent team 中队友空闲 | 工作分配、协调 |
| **TaskCompleted** | 任务标记完成 | 任务后处理 |
| **TaskCreated** | 通过 TaskCreate 创建任务 | 任务跟踪、日志 |
| **ConfigChange** | 配置文件变更 | 校验、传播 |
| **CwdChanged** | 工作目录变化 | 目录级设置 |
| **FileChanged** | 监视的文件变化 | 文件监控、触发重建 |
| **PreCompact** | 上下文压缩前 | 状态保留 |
| **PostCompact** | 压缩完成后 | 压缩后动作 |
| **WorktreeCreate** | 正在创建 worktree | 环境准备、依赖安装 |
| **WorktreeRemove** | 正在移除 worktree | 清理、释放资源 |
| **Elicitation** | MCP 服务器请求用户输入 | 输入校验 |
| **ElicitationResult** | 用户响应 elicitation | 响应处理 |
| **SessionEnd** | 会话结束 | 清理、最终日志 |

### 常用 Hooks

Hooks 配置在 `~/.claude/settings.json`（用户级）或 `.claude/settings.json`（项目级）：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write $CLAUDE_FILE_PATH"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "eslint $CLAUDE_FILE_PATH"
          }
        ]
      }
    ]
  }
}
```

### Hook 环境变量

- `$CLAUDE_FILE_PATH` — 正在编辑/写入的文件路径
- `$CLAUDE_TOOL_NAME` — 当前使用的工具名
- `$CLAUDE_SESSION_ID` — 当前会话标识
- `$CLAUDE_PROJECT_DIR` — 项目目录路径

### 最佳实践

✅ **建议：**
- 保持 hook 快速（< 1 秒）
- 将 hook 用于校验与自动化
- 妥善处理错误
- 使用绝对路径

❌ **避免：**
- 让 hook 交互式运行
- 用 hook 跑长时间任务
- 硬编码凭据

**详见：** [06-hooks/](06-hooks/) 中的示例

---

## Checkpoints and Rewind

### 概述

Checkpoints 可保存对话状态并回退到先前节点，便于安全尝试与探索多种方案。

### 关键概念

| Concept | Description |
|---------|-------------|
| **Checkpoint** | 对话状态快照，含消息、文件与上下文 |
| **Rewind** | 回到某一 checkpoint，丢弃之后变更 |
| **Branch Point** | 可从此处分叉尝试多种做法的 checkpoint |

### 使用 Checkpoints

每次用户提交提示时都会自动创建 Checkpoint。回退方式：

```bash
# 连按两次 Esc 打开 checkpoint 浏览器
Esc + Esc

# 或使用 /rewind 命令
/rewind
```

选择 checkpoint 时共有五种选项：
1. **Restore code and conversation** — 代码与对话均恢复到该点
2. **Restore conversation** — 回退消息，保留当前代码
3. **Restore code** — 回退文件，保留对话
4. **Summarize from here** — 将对话压缩为摘要
5. **Never mind** — 取消

### 适用场景

| Scenario | Workflow |
|----------|----------|
| **Exploring Approaches** | 保存 → 试 A → 保存 → 回退 → 试 B → 对比 |
| **Safe Refactoring** | 保存 → 重构 → 测试 → 失败则回退 |
| **A/B Testing** | 保存 → 方案 A → 保存 → 回退 → 方案 B → 对比 |
| **Mistake Recovery** | 发现问题 → 回退到最后良好状态 |

### 配置

```json
{
  "autoCheckpoint": true
}
```

**详见：** [08-checkpoints/](08-checkpoints/) 中的示例

---

## Advanced Features

### Planning Mode

在编码前生成详细实现计划。

**启用：**
```bash
/plan Implement user authentication system
```

**益处：**
- 路线图清晰，可含时间预估
- 风险评估
- 任务系统化拆解
- 便于评审与修改

### Extended Thinking

针对复杂问题做深度推理。

**启用：**
- 会话中按 `Alt+T`（macOS 上为 `Option+T`）切换
- 通过环境变量 `MAX_THINKING_TOKENS` 编程控制

```bash
# 通过环境变量启用 extended thinking
export MAX_THINKING_TOKENS=50000
claude -p "Should we use microservices or monolith?"
```

**益处：**
- 充分分析权衡
- 更稳妥的架构决策
- 覆盖边界情况
- 系统化评估

### Background Tasks

长时间操作可在不阻塞对话的情况下运行。

**用法：**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Show all tasks
/task status bg-1234 # Check progress
/task show bg-1234   # View output
/task cancel bg-1234 # Cancel task
```

### Permission Modes

控制 Claude 可执行的操作。

| Mode | Description | Use Case |
|------|-------------|----------|
| **default** | 标准权限，敏感操作会提示 | 日常开发 |
| **acceptEdits** | 自动接受文件编辑，无需确认 | 可信编辑流程 |
| **plan** | 仅分析与规划，不修改文件 | 代码审查、架构规划 |
| **auto** | 安全操作自动批准，风险操作仍提示 | 平衡自主与安全 |
| **dontAsk** | 所有操作不弹出确认 | 熟练用户、自动化 |
| **bypassPermissions** | 完全无限制，无安全检查 | CI/CD、可信脚本 |

**用法：**
```bash
claude --permission-mode plan          # 只读分析
claude --permission-mode acceptEdits   # 自动接受编辑
claude --permission-mode auto          # 安全操作自动批准
claude --permission-mode dontAsk       # 不弹出确认
```

### Headless Mode（Print Mode）

使用 `-p`（print）标志在无交互输入下运行 Claude Code，适用于自动化与 CI/CD。

**用法：**
```bash
# 运行指定任务
claude -p "Run all tests"

# 管道输入供分析
cat error.log | claude -p "explain this error"

# CI/CD 集成（GitHub Actions）
- name: AI Code Review
  run: claude -p "Review PR changes and report issues"

# JSON 输出便于脚本处理
claude -p --output-format json "list all functions in src/"
```

### Scheduled Tasks

使用 `/loop` 命令按周期运行任务。

**用法：**
```bash
/loop every 30m "Run tests and report failures"
/loop every 2h "Check for dependency updates"
/loop every 1d "Generate daily summary of code changes"
```

定时任务在后台运行，完成后汇报结果，适用于持续监控、定期检查与自动化维护工作流。

### Chrome Integration

Claude Code 可与 Chrome 浏览器集成以完成网页自动化，例如导航页面、填写表单、截图与从网站提取数据，并融入开发工作流。

### Session Management

管理多个工作会话。

**命令：**
```bash
/resume                # 恢复先前对话
/rename "Feature"      # 为当前会话命名
/fork                  # 分叉为新会话
claude -c              # 继续最近一次对话
claude -r "Feature"    # 按名称或 ID 恢复会话
```

### Interactive Features

**快捷键：**
- `Ctrl + R` — 搜索命令历史
- `Tab` — 自动补全
- `↑ / ↓` — 命令历史
- `Ctrl + L` — 清屏

**多行输入：**
```bash
User: \
> 较长、较复杂的提示
> 可跨多行
> \end
```

### 配置

完整配置示例：

```json
{
  "planning": {
    "autoEnter": true,
    "requireApproval": true
  },
  "extendedThinking": {
    "enabled": true,
    "showThinkingProcess": true
  },
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5
  },
  "permissions": {
    "mode": "default"
  }
}
```

**详见：** [09-advanced-features/](09-advanced-features/) 完整指南

---

## 参考资源

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [Anthropic Documentation](https://docs.anthropic.com)
- [MCP GitHub Servers](https://github.com/modelcontextprotocol/servers)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

---

*最后更新：2026 年 3 月*
*适用于 Claude Haiku 4.5、Sonnet 4.6 与 Opus 4.6*
*现包含：Hooks、Checkpoints、Planning Mode、Extended Thinking、Background Tasks、Permission Modes（6 种）、Headless Mode、Session Management、Auto Memory、Agent Teams、Scheduled Tasks、Chrome Integration、Channels、Voice Dictation 与 Bundled Skills*
