<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP（Model Context Protocol）

本文件夹包含在 Claude Code 中使用 MCP 服务器配置与用法的完整文档与示例。

<a id="overview"></a>
## 概述

MCP（Model Context Protocol）让 Claude 能够以标准化方式访问外部工具、API 与实时数据源。与 Memory 不同，MCP 提供对变化中数据的实时访问。

主要特点：
- 实时访问外部服务
- 实时数据同步
- 可扩展架构
- 安全认证
- 基于工具的交互

<a id="mcp-architecture"></a>
## MCP 架构

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
```

<a id="mcp-ecosystem"></a>
## MCP 生态

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["Local Files"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Slack Workspace"]
    F -->|Docs| K["Google Drive"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#f3e5f5,stroke:#333,color:#333
    style G fill:#e8f5e9,stroke:#333,color:#333
    style H fill:#e8f5e9,stroke:#333,color:#333
    style I fill:#e8f5e9,stroke:#333,color:#333
    style J fill:#e8f5e9,stroke:#333,color:#333
    style K fill:#e8f5e9,stroke:#333,color:#333
```

<a id="mcp-installation-methods"></a>
## MCP 安装方式

Claude Code 支持多种传输协议用于连接 MCP 服务器：

<a id="http-transport-recommended"></a>
### HTTP 传输（推荐）

```bash
# Basic HTTP connection
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP with authentication header
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

<a id="stdio-transport-local"></a>
### Stdio 传输（本地）

适用于在本地运行的 MCP 服务器：

```bash
# Local Node.js server
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# With environment variables
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

<a id="sse-transport-deprecated"></a>
### SSE 传输（已弃用）

Server-Sent Events 传输已弃用，建议改用 `http`，但仍受支持：

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

<a id="websocket-transport"></a>
### WebSocket 传输

用于持久双向连接的 WebSocket 传输：

```bash
claude mcp add --transport ws realtime-server wss://example.com/mcp
```

<a id="windows-specific-note"></a>
### Windows 特别说明

在原生 Windows（非 WSL）上，对 npx 命令请使用 `cmd /c`：

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

<a id="oauth-20-authentication"></a>
### OAuth 2.0 认证

Claude Code 支持需要 OAuth 2.0 的 MCP 服务器。连接已启用 OAuth 的服务器时，Claude Code 会处理完整认证流程：

```bash
# Connect to an OAuth-enabled MCP server (interactive flow)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# Pre-configure OAuth credentials for non-interactive setup
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| 功能 | 说明 |
|---------|-------------|
| **交互式 OAuth** | 使用 `/mcp` 触发基于浏览器的 OAuth 流程 |
| **预配置 OAuth 客户端** | 针对 Notion、Stripe 等常见服务的内置 OAuth 客户端（v2.1.30+） |
| **预配置凭据** | 使用 `--client-id`、`--client-secret`、`--callback-port` 实现自动化配置 |
| **令牌存储** | 令牌安全保存在系统钥匙串中 |
| **阶梯式认证（Step-up auth）** | 支持对敏感操作进行阶梯式认证 |
| **发现缓存** | 缓存 OAuth 发现元数据以加快重连 |
| **元数据覆盖** | 在 `.mcp.json` 中设置 `oauth.authServerMetadataUrl` 以覆盖默认 OAuth 元数据发现 |

<a id="overriding-oauth-metadata-discovery"></a>
#### 覆盖 OAuth 元数据发现

若你的 MCP 服务器在标准 OAuth 元数据端点（`/.well-known/oauth-authorization-server`）上返回错误，但提供了可用的 OIDC 端点，可让 Claude Code 从指定 URL 拉取 OAuth 元数据。在服务器配置的 `oauth` 对象中设置 `authServerMetadataUrl`：

```json
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "authServerMetadataUrl": "https://auth.example.com/.well-known/openid-configuration"
      }
    }
  }
}
```

URL 必须使用 `https://`。此选项需要 Claude Code v2.1.64 或更高版本。

<a id="claudeai-mcp-connectors"></a>
### Claude.ai MCP Connectors

在 Claude.ai 账号中配置的 MCP 服务器会自动出现在 Claude Code 中。也就是说，通过 Claude.ai 网页界面建立的 MCP 连接无需额外配置即可使用。

Claude.ai MCP connectors 在 `--print` 模式下也可用（v2.1.83+），便于非交互与脚本化使用。

若要在 Claude Code 中禁用 Claude.ai 的 MCP 服务器，请将环境变量 `ENABLE_CLAUDEAI_MCP_SERVERS` 设为 `false`：

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **说明：** 此功能仅适用于使用 Claude.ai 账号登录的用户。

<a id="mcp-setup-process"></a>
## MCP 配置流程

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as External Service

    User->>Claude: Type /mcp
    Claude->>Claude: List available MCP servers
    Claude->>User: Show options
    User->>Claude: Select GitHub MCP
    Claude->>Config: Update configuration
    Config->>Claude: Activate connection
    Claude->>Service: Test connection
    Service-->>Claude: Authentication successful
    Claude->>User: ✅ MCP connected!
```

<a id="mcp-tool-search"></a>
## MCP 工具搜索

当 MCP 工具描述超过上下文窗口的 10% 时，Claude Code 会自动启用工具搜索，以便高效选用合适工具，避免撑满模型上下文。

| 设置 | 取值 | 说明 |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | `auto`（默认） | 工具描述超过上下文的 10% 时自动启用 |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | 在自定义阈值 `N` 个工具时自动启用 |
| `ENABLE_TOOL_SEARCH` | `true` | 始终启用，与工具数量无关 |
| `ENABLE_TOOL_SEARCH` | `false` | 禁用；完整发送所有工具描述 |

> **说明：** 工具搜索需要 Sonnet 4 或更高版本，或 Opus 4 或更高版本。Haiku 模型不支持工具搜索。

<a id="dynamic-tool-updates"></a>
## 动态工具更新

Claude Code 支持 MCP 的 `list_changed` 通知。当 MCP 服务器动态增删或修改可用工具时，Claude Code 会收到更新并自动调整工具列表，无需重连或重启。

<a id="mcp-elicitation"></a>
## MCP 引导输入（Elicitation）

MCP 服务器可通过交互式对话框向用户请求结构化输入（v2.1.49+）。这样 MCP 服务器可在工作流中途索取更多信息，例如确认、从选项列表中选择或填写必填字段，从而增强 MCP 交互。

<a id="tool-description-and-instruction-cap"></a>
## 工具描述与指令上限

自 v2.1.84 起，Claude Code 对每个 MCP 服务器的工具描述与指令强制执行 **2 KB 上限**，避免个别服务器用冗长工具定义占用过多上下文，减轻上下文膨胀并保持交互高效。

<a id="mcp-prompts-as-slash-commands"></a>
## 将 MCP Prompts 作为 Slash Commands

MCP 服务器可暴露在 Claude Code 中显示为 slash commands 的 prompts。按以下命名约定访问：

```
/mcp__<server>__<prompt>
```

例如，若名为 `github` 的服务器暴露名为 `review` 的 prompt，可调用 `/mcp__github__review`。

<a id="server-deduplication"></a>
## 服务器去重

当同一 MCP 服务器在多个作用域（local、project、user）中定义时，以本地配置为准。这样可用本地自定义覆盖项目级或用户级 MCP 设置，且不会冲突。

<a id="mcp-resources-via--mentions"></a>
## 通过 @ 提及引用 MCP 资源

可在提示词中用 `@` 提及语法直接引用 MCP 资源：

```
@server-name:protocol://resource/path
```

例如引用特定数据库资源：

```
@database:postgres://mydb/users
```

这样 Claude 可拉取并将 MCP 资源内容内联纳入对话上下文。

<a id="mcp-scopes"></a>
## MCP 作用域

MCP 配置可存放在不同作用域，共享程度不同：

| 作用域 | 位置 | 说明 | 与谁共享 | 是否需要批准 |
|-------|----------|-------------|-------------|------------------|
| **Local**（默认） | `~/.claude.json`（项目路径下） | 仅当前用户、当前项目私有（旧版本中曾称为 `project`） | 仅本人 | 否 |
| **Project** | `.mcp.json` | 可纳入 git 仓库 | 团队成员 | 是（首次使用） |
| **User** | `~/.claude.json` | 所有项目可用（旧版本中曾称为 `global`） | 仅本人 | 否 |

<a id="using-project-scope"></a>
### 使用 Project 作用域

将项目专用 MCP 配置放在 `.mcp.json`：

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.github.com/mcp"
    }
  }
}
```

团队成员在首次使用项目 MCP 时会看到批准提示。

<a id="mcp-configuration-management"></a>
## MCP 配置管理

<a id="adding-mcp-servers"></a>
### 添加 MCP 服务器

```bash
# Add HTTP-based server
claude mcp add --transport http github https://api.github.com/mcp

# Add local stdio server
claude mcp add --transport stdio database -- npx @company/db-server

# List all MCP servers
claude mcp list

# Get details on specific server
claude mcp get github

# Remove an MCP server
claude mcp remove github

# Reset project-specific approval choices
claude mcp reset-project-choices

# Import from Claude Desktop
claude mcp add-from-claude-desktop
```

<a id="available-mcp-servers-table"></a>
## 常用 MCP 服务器一览

| MCP Server | 用途 | 常见工具 | 认证 | 实时 |
|------------|---------|--------------|------|-----------|
| **Filesystem** | 文件操作 | read, write, delete | 操作系统权限 | ✅ 是 |
| **GitHub** | 仓库管理 | list_prs, create_issue, push | OAuth | ✅ 是 |
| **Slack** | 团队沟通 | send_message, list_channels | Token | ✅ 是 |
| **Database** | SQL 查询 | query, insert, update | 凭据 | ✅ 是 |
| **Google Docs** | 文档访问 | read, write, share | OAuth | ✅ 是 |
| **Asana** | 项目管理 | create_task, update_status | API Key | ✅ 是 |
| **Stripe** | 支付数据 | list_charges, create_invoice | API Key | ✅ 是 |
| **Memory** | 持久记忆 | store, retrieve, delete | 本地 | ❌ 否 |

<a id="practical-examples"></a>
## 实践示例

<a id="example-1-github-mcp-configuration"></a>
### 示例 1：GitHub MCP 配置

**文件：** `.mcp.json`（项目根目录）

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

**GitHub MCP 可用工具：**

<a id="pull-request-management"></a>
#### Pull Request 管理
- `list_prs` - 列出仓库内所有 PR
- `get_pr` - 获取 PR 详情（含 diff）
- `create_pr` - 创建新 PR
- `update_pr` - 更新 PR 描述/标题
- `merge_pr` - 将 PR 合并到 main
- `review_pr` - 添加评审评论

**示例请求：**
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

<a id="issue-management"></a>
#### Issue 管理
- `list_issues` - 列出所有 issue
- `get_issue` - 获取 issue 详情
- `create_issue` - 创建新 issue
- `close_issue` - 关闭 issue
- `add_comment` - 在 issue 下添加评论

<a id="repository-information"></a>
#### 仓库信息
- `get_repo_info` - 仓库详情
- `list_files` - 文件树结构
- `get_file_content` - 读取文件内容
- `search_code` - 在代码库中搜索

<a id="commit-operations"></a>
#### 提交操作
- `list_commits` - 提交历史
- `get_commit` - 指定提交的详情
- `create_commit` - 创建新提交

**配置：**
```bash
export GITHUB_TOKEN="your_github_token"
# Or use the CLI to add directly:
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

<a id="environment-variable-expansion-in-configuration"></a>
### 配置中的环境变量展开

MCP 配置支持带默认回退的环境变量展开。`${VAR}` 与 `${VAR:-default}` 语法适用于以下字段：`command`、`args`、`env`、`url`、`headers`。

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}",
        "X-Custom-Header": "${CUSTOM_HEADER:-default-value}"
      }
    },
    "local-server": {
      "command": "${MCP_BIN_PATH:-npx}",
      "args": ["${MCP_PACKAGE:-@company/mcp-server}"],
      "env": {
        "DB_URL": "${DATABASE_URL:-postgresql://localhost/dev}"
      }
    }
  }
}
```

变量在运行时展开：
- `${VAR}` - 使用环境变量，未设置则报错
- `${VAR:-default}` - 使用环境变量，未设置则使用默认值

<a id="example-2-database-mcp-setup"></a>
### 示例 2：Database MCP 搭建

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

**示例用法：**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# Using MCP database tool:
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

**配置：**
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# Or use the CLI to add directly:
claude mcp add --transport stdio database -- npx @modelcontextprotocol/server-database
```

<a id="example-3-multi-mcp-workflow"></a>
### 示例 3：多 MCP 工作流

**场景：每日报告生成**

```markdown
# Daily Report Workflow using Multiple MCPs

## Setup
1. GitHub MCP - fetch PR metrics
2. Database MCP - query sales data
3. Slack MCP - post report
4. Filesystem MCP - save report

## Workflow

### Step 1: Fetch GitHub Data
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Step 2: Query Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Step 3: Generate Report
Combine data into HTML report

### Step 4: Save to Filesystem
Write report.html to /reports/

### Step 5: Post to Slack
Send summary to #daily-reports channel

Final Output:
✅ Report generated and posted
📊 47 PRs merged this week
💰 $12,450 in daily sales
```

**配置：**
```bash
export GITHUB_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="your_slack_token"
# Add each MCP server via the CLI or configure them in .mcp.json
```

<a id="example-4-filesystem-mcp-operations"></a>
### 示例 4：Filesystem MCP 操作

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

| 操作 | 命令 | 用途 |
|-----------|---------|---------|
| List files | `ls ~/projects` | 显示目录内容 |
| Read file | `cat src/main.ts` | 读取文件内容 |
| Write file | `create docs/api.md` | 创建新文件 |
| Edit file | `edit src/app.ts` | 修改文件 |
| Search | `grep "async function"` | 在文件中搜索 |
| Delete | `rm old-file.js` | 删除文件 |

**配置：**
```bash
# Use the CLI to add directly:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

<a id="mcp-vs-memory-decision-matrix"></a>
## MCP 与 Memory：决策矩阵

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

<a id="requestresponse-pattern"></a>
## 请求/响应模式

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

    Note over MCP,DB: Real-time access<br/>No caching
```

<a id="environment-variables"></a>
## 环境变量

将敏感凭据放在环境变量中：

```bash
# ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

然后在 MCP 配置中引用：

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

<a id="claude-as-mcp-server-claude-mcp-serve"></a>
## 将 Claude 作为 MCP 服务器（`claude mcp serve`）

Claude Code 自身也可作为 MCP 服务器供其他应用使用。这样外部工具、编辑器与自动化系统可通过标准 MCP 协议使用 Claude 的能力。

```bash
# Start Claude Code as an MCP server on stdio
claude mcp serve
```

其他应用可像连接任意基于 stdio 的 MCP 服务器一样连接该服务。例如，在另一个 Claude Code 实例中将 Claude Code 添加为 MCP 服务器：

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

适用于构建多智能体工作流，由一个 Claude 实例编排另一个实例。

<a id="managed-mcp-configuration-enterprise"></a>
## 托管 MCP 配置（企业版）

在企业部署中，IT 管理员可通过 `managed-mcp.json` 配置文件强制执行 MCP 服务器策略。该文件可集中控制组织范围内允许或禁止的 MCP 服务器。

**位置：**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `~/.config/ClaudeCode/managed-mcp.json`
- Windows: `%APPDATA%\ClaudeCode\managed-mcp.json`

**功能：**
- `allowedMcpServers` — 允许列表
- `deniedMcpServers` — 禁止列表
- 支持按服务器名称、命令与 URL 模式匹配
- 在用户配置之前强制执行组织级 MCP 策略
- 阻止未授权的服务器连接

**配置示例：**

```json
{
  "allowedMcpServers": [
    {
      "serverName": "github",
      "serverUrl": "https://api.github.com/mcp"
    },
    {
      "serverName": "company-internal",
      "serverCommand": "company-mcp-server"
    }
  ],
  "deniedMcpServers": [
    {
      "serverName": "untrusted-*"
    },
    {
      "serverUrl": "http://*"
    }
  ]
}
```

> **说明：** 若某服务器同时匹配 `allowedMcpServers` 与 `deniedMcpServers`，以禁止规则为准。

<a id="plugin-provided-mcp-servers"></a>
## 插件提供的 MCP 服务器

插件可打包自带 MCP 服务器，安装插件后即可自动可用。插件提供的 MCP 服务器有两种定义方式：

1. **独立 `.mcp.json`** — 在插件根目录放置 `.mcp.json`
2. **内联于 `plugin.json`** — 在插件清单中直接定义 MCP 服务器

使用 `${CLAUDE_PLUGIN_ROOT}` 变量引用相对于插件安装目录的路径：

```json
{
  "mcpServers": {
    "plugin-tools": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/dist/mcp-server.js"],
      "env": {
        "CONFIG_PATH": "${CLAUDE_PLUGIN_ROOT}/config.json"
      }
    }
  }
}
```

<a id="subagent-scoped-mcp"></a>
## Subagent 作用域内的 MCP

可在智能体 frontmatter 中用 `mcpServers:` 键内联定义 MCP 服务器，使其仅作用于特定 subagent，而非整个项目。适用于某智能体需要某 MCP 服务器，而同工作流中的其他智能体不需要时。

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

Subagent 作用域内的 MCP 服务器仅在该智能体的执行上下文中可用，不会与父级或同级智能体共享。

<a id="mcp-output-limits"></a>
## MCP 输出限制

Claude Code 对 MCP 工具输出设有限制，以防上下文溢出：

| 限制 | 阈值 | 行为 |
|-------|-----------|----------|
| **警告** | 10,000 tokens | 提示输出体积较大 |
| **默认上限** | 25,000 tokens | 超过此限制会截断输出 |
| **磁盘持久化** | 50,000 字符 | 超过 50K 字符的工具结果会写入磁盘 |

可通过环境变量 `MAX_MCP_OUTPUT_TOKENS` 配置最大输出上限：

```bash
# Increase the max output to 50,000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

<a id="solving-context-bloat-with-code-execution"></a>
## 用代码执行缓解上下文膨胀

随着 MCP 普及，连接数十个服务器与成百上千个工具会带来严峻挑战：**上下文膨胀**。这可以说是大规模使用 MCP 时的首要问题，Anthropic 工程团队提出了一种思路——用代码执行替代直接工具调用。

> **来源**：[Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic 工程博客

<a id="the-problem-two-sources-of-token-waste"></a>
### 问题：两类 token 浪费

**1. 工具定义挤占上下文窗口**

多数 MCP 客户端会预先加载全部工具定义。连接数千个工具时，模型在处理用户请求前就要消化数十万 token。

**2. 中间结果额外消耗 token**

每个中间工具结果都会进入模型上下文。例如把会议记录从 Google Drive 转到 Salesforce——完整逐字稿会在上下文中**经过两次**：一次读取，一次写入目标。一场 2 小时会议的逐字稿可能意味着额外 5 万+ token。

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

<a id="the-solution-mcp-tools-as-code-apis"></a>
### 方案：将 MCP 工具当作代码 API

不把工具定义与结果经由上下文窗口传递，而是由智能体**编写代码**，将 MCP 工具作为 API 调用。代码在沙箱执行环境中运行，仅将最终结果返回模型。

```mermaid
graph LR
    A["Model"] -->|"Writes code"| B["Code Execution<br/>Environment"]
    B -->|"Calls tools directly"| C["MCP Servers"]
    C -->|"Data stays in<br/>execution env"| B
    B -->|"Only final result<br/>(minimal tokens)"| A

    style A fill:#c8e6c9,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
```

<a id="how-it-works"></a>
#### 工作原理

MCP 工具以类型化函数构成的文件树形式呈现：

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
└── ...
```

每个工具文件包含类型化封装：

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

export async function getDocument(
  input: GetDocumentInput
): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>(
    'google_drive__get_document', input
  );
}
```

智能体再编写代码编排工具：

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// Data flows directly between tools — never through the model
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**结果：token 用量从约 150,000 降至约 2,000，降幅约 98.7%。**

<a id="key-benefits"></a>
### 主要优势

| 优势 | 说明 |
|---------|-------------|
| **渐进式披露** | 智能体浏览文件系统，仅加载需要的工具定义，而非一次性加载全部 |
| **上下文高效的结果** | 数据在返回模型前于执行环境中过滤/转换 |
| **强大的控制流** | 循环、条件与错误处理在代码中执行，无需反复经过模型 |
| **隐私保护** | 中间数据（PII、敏感记录）留在执行环境，不进入模型上下文 |
| **状态持久化** | 智能体可将中间结果写入文件并构建可复用的技能函数 |

<a id="example-filtering-large-datasets"></a>
#### 示例：过滤大数据集

```typescript
// Without code execution — all 10,000 rows flow through context
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> returns 10,000 rows in context

// With code execution — filter in the execution environment
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Only 5 rows reach the model
```

<a id="example-loop-without-round-tripping"></a>
#### 示例：无往返轮询的循环

```typescript
// Poll for a deployment notification — runs entirely in code
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({
    channel: 'C123456'
  });
  found = messages.some(
    m => m.text.includes('deployment complete')
  );
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

<a id="trade-offs-to-consider"></a>
### 需要权衡之处

代码执行会引入额外复杂度。运行智能体生成的代码需要：

- 具备适当资源限制的**安全沙箱执行环境**
- 对执行代码的**监控与日志**
- 相较直接工具调用更高的**基础设施开销**

应将收益（降低 token 成本、降低延迟、改进工具组合）与实现成本权衡。若仅有少量 MCP 服务器，直接工具调用可能更简单；若在较大规模（数十服务器、数百工具），代码执行收益显著。

<a id="mcporter-a-runtime-for-mcp-tool-composition"></a>
### MCPorter：MCP 工具组合的运行时

[MCPorter](https://github.com/steipete/mcporter) 是 TypeScript 运行时与 CLI 工具包，让调用 MCP 服务器更省事、少样板代码，并通过选择性暴露工具与类型化封装帮助减轻上下文膨胀。

**解决的问题：** 不必预先从所有 MCP 服务器加载全部工具定义，可按需发现、检查并调用特定工具，保持上下文精简。

**主要特性：**

| 特性 | 说明 |
|---------|-------------|
| **零配置发现** | 从 Cursor、Claude、Codex 或本地配置自动发现 MCP 服务器 |
| **类型化工具客户端** | `mcporter emit-ts` 生成 `.d.ts` 接口与可直接运行的封装 |
| **可组合 API** | `createServerProxy()` 将工具暴露为 camelCase 方法，并提供 `.text()`、`.json()`、`.markdown()` 等辅助函数 |
| **CLI 生成** | `mcporter generate-cli` 将任意 MCP 服务器转为独立 CLI，支持 `--include-tools` / `--exclude-tools` 过滤 |
| **参数隐藏** | 可选参数默认隐藏，减少 schema 冗长度 |

**安装：**

```bash
npx mcporter list          # No install required — discover servers instantly
pnpm add mcporter          # Add to a project
brew install steipete/tap/mcporter  # macOS via Homebrew
```

**示例 — 在 TypeScript 中组合工具：**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// Data flows between tools without passing through the model context
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**示例 — CLI 工具调用：**

```bash
# Call a specific tool directly
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# List available servers and tools
npx mcporter list
```

MCPorter 通过提供将 MCP 工具作为类型化 API 调用的运行时基础设施，与上文代码执行思路互补，便于将中间数据留在模型上下文之外。

<a id="best-practices"></a>
## 最佳实践

<a id="security-considerations"></a>
### 安全注意事项

<a id="dos"></a>
#### 建议 ✅
- 所有凭据使用环境变量
- 定期轮换 token 与 API 密钥（建议每月）
- 尽量使用只读 token
- 将 MCP 服务器访问范围限制在最小必要
- 监控 MCP 服务器使用与访问日志
- 对外部服务尽量使用 OAuth
- 对 MCP 请求实施速率限制
- 生产使用前测试 MCP 连接
- 文档化所有活跃 MCP 连接
- 保持 MCP 服务器包为最新

<a id="donts"></a>
#### 避免 ❌
- 不要在配置文件中硬编码凭据
- 不要将 token 或密钥提交到 git
- 不要在团队聊天或邮件中分享 token
- 不要在团队项目中使用个人 token
- 不要授予不必要权限
- 不要忽略认证错误
- 不要公开暴露 MCP 端点
- 不要使用 root/管理员权限运行 MCP 服务器
- 不要在日志中缓存敏感数据
- 不要关闭认证机制

<a id="configuration-best-practices"></a>
### 配置最佳实践

1. **版本控制**：将 `.mcp.json` 纳入 git，密钥用环境变量
2. **最小权限**：每个 MCP 服务器仅授予所需最小权限
3. **隔离**：尽量在不同进程中运行不同 MCP 服务器
4. **监控**：记录所有 MCP 请求与错误以便审计
5. **测试**：上线前测试所有 MCP 配置

<a id="performance-tips"></a>
### 性能提示

- 在应用层缓存频繁访问的数据
- 使用更具体的 MCP 查询以减少数据传输
- 监控 MCP 操作的响应时间
- 考虑对外部 API 做速率限制
- 批量执行多个操作时尽量批处理

<a id="installation-instructions"></a>
## 安装说明

<a id="prerequisites"></a>
### 前置条件
- 已安装 Node.js 与 npm
- 已安装 Claude Code CLI
- 外部服务的 API token/凭据

<a id="step-by-step-setup"></a>
### 分步配置

1. **添加第一个 MCP 服务器**（示例：GitHub）：
```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

   或在项目根目录创建 `.mcp.json`：
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

2. **设置环境变量：**
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

3. **测试连接：**
```bash
claude /mcp
```

4. **使用 MCP 工具：**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

<a id="installation-for-specific-services"></a>
### 特定服务安装

**GitHub MCP：**
```bash
npm install -g @modelcontextprotocol/server-github
```

**Database MCP：**
```bash
npm install -g @modelcontextprotocol/server-database
```

**Filesystem MCP：**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP：**
```bash
npm install -g @modelcontextprotocol/server-slack
```

<a id="troubleshooting"></a>
## 故障排除

<a id="mcp-server-not-found"></a>
### 找不到 MCP 服务器
```bash
# Verify MCP server is installed
npm list -g @modelcontextprotocol/server-github

# Install if missing
npm install -g @modelcontextprotocol/server-github
```

<a id="authentication-failed"></a>
### 认证失败
```bash
# Verify environment variable is set
echo $GITHUB_TOKEN

# Re-export if needed
export GITHUB_TOKEN="your_token"

# Verify token has correct permissions
# Check GitHub token scopes at: https://github.com/settings/tokens
```

<a id="connection-timeout"></a>
### 连接超时
- 检查网络连通性：`ping api.github.com`
- 确认 API 端点可访问
- 检查 API 速率限制
- 尝试在配置中增大超时
- 排查防火墙或代理问题

<a id="mcp-server-crashes"></a>
### MCP 服务器崩溃
- 查看 MCP 服务器日志：`~/.claude/logs/`
- 确认所有环境变量已设置
- 确认文件权限正确
- 尝试重新安装 MCP 服务器包
- 检查同一端口是否有冲突进程

<a id="related-concepts"></a>
## 相关概念

<a id="memory-vs-mcp"></a>
### Memory 与 MCP
- **Memory**：存储持久、相对静态的数据（偏好、上下文、历史）
- **MCP**：访问实时、变化中的数据（API、数据库、实时服务）

<a id="when-to-use-each"></a>
### 何时用哪一种
- **用 Memory**：用户偏好、对话历史、已学习的上下文
- **用 MCP**：当前 GitHub issue、实时数据库查询、实时数据

<a id="integration-with-other-claude-features"></a>
### 与其他 Claude 功能的结合
- 将 MCP 与 Memory 结合以获得更丰富的上下文
- 在提示词中使用 MCP 工具以改进推理
- 对复杂工作流组合多个 MCP

<a id="additional-resources"></a>
## 延伸阅读

- [Official MCP Documentation](https://code.claude.com/docs/en/mcp)
- [MCP Protocol Specification](https://modelcontextprotocol.io/specification)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol/servers)
- [Available MCP Servers](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — 以 TypeScript 运行时与 CLI 无样板调用 MCP 服务器
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — Anthropic 关于缓解上下文膨胀的工程博客
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Claude API Documentation](https://docs.anthropic.com)
