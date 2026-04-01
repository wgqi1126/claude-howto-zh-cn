<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To 教程" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks

Hooks 是在 Claude Code 会话中响应特定事件而执行的自动化脚本，用于实现自动化、校验、权限管理和自定义工作流。

## 概述

Hooks 是自动化动作（shell 命令、HTTP webhook、LLM 提示词或 subagent 评估），在 Claude Code 中发生特定事件时自动执行。它们接收 JSON 输入，并通过退出码与 JSON 输出传递结果。

**主要特性：**
- 事件驱动自动化
- 基于 JSON 的输入/输出
- 支持 command、prompt、http、agent 等 hook 类型
- 针对工具的 pattern 匹配

## 配置

Hooks 在配置文件中按固定结构编写：

- `~/.claude/settings.json` - 用户设置（所有项目）
- `.claude/settings.json` - 项目设置（可分享、可提交）
- `.claude/settings.local.json` - 本地项目设置（不提交）
- 托管策略（组织托管）- 组织级设置
- 插件 `hooks/hooks.json` - 插件作用域内的 hooks
- Skill 与 Agent 的 frontmatter - 组件生命周期内的 hooks

### 基本配置结构

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "在此处替换为你的命令",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**主要字段：**

| 字段 | 说明 | 示例 |
|-------|-------------|---------|
| `matcher` | 匹配工具名的模式（区分大小写） | `"Write"`, `"Edit\|Write"`, `"*"` |
| `hooks` | Hook 定义数组 | `[{ "type": "command", ... }]` |
| `type` | Hook 类型：`"command"`（bash）、`"prompt"`（LLM）、`"http"`（webhook）或 `"agent"`（subagent） | `"command"` |
| `command` | 要执行的 shell 命令 | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | 可选超时（秒，默认 60） | `30` |
| `once` | 若为 `true`，每个会话只运行一次该 hook | `true` |

### Matcher 模式

| 模式 | 说明 | 示例 |
|---------|-------------|---------|
| 精确字符串 | 匹配特定工具 | `"Write"` |
| 正则模式 | 匹配多个工具 | `"Edit\|Write"` |
| 通配符 | 匹配所有工具 | `"*"` 或 `""` |
| MCP 工具 | 服务器与工具模式 | `"mcp__memory__.*"` |

## Hook 类型

Claude Code 支持四种 hook 类型：

<a id="command-hooks"></a>

### 命令型 Hooks（`command`）

默认 hook 类型。执行 shell 命令，通过 JSON stdin/stdout 与退出码通信。

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

<a id="http-hooks"></a>

### HTTP 型 Hooks（`http`）

> 自 v2.1.63 起提供。

远程 webhook 端点，接收与命令型 hooks 相同的 JSON 输入。HTTP hooks 将 JSON POST 到 URL，并接收 JSON 响应。启用沙箱时，HTTP hooks 会经由沙箱路由。URL 中的环境变量插值需要显式配置 `allowedEnvVars` 列表以保证安全。

```json
{
  "hooks": {
    "PostToolUse": [{
      "type": "http",
      "url": "https://my-webhook.example.com/hook",
      "matcher": "Write"
    }]
  }
}
```

**主要属性：**
- `"type": "http"` — 标识为 HTTP hook
- `"url"` — webhook 端点 URL
- 启用沙箱时经由沙箱路由
- URL 中若使用环境变量插值，必须为相关变量提供显式 `allowedEnvVars` 列表

<a id="prompt-hooks"></a>

### Prompt 型 Hooks（`prompt`）

由 LLM 评估的提示词，hook 内容即待 Claude 评估的 prompt。主要用于 `Stop` 与 `SubagentStop` 事件，做智能的任务完成检查。

```json
{
  "type": "prompt",
  "prompt": "评估 Claude 是否已完成用户请求的全部任务。",
  "timeout": 30
}
```

LLM 会评估该 prompt 并返回结构化决策（详见 [基于 Prompt 的 Hooks](#prompt-based-hooks)）。

<a id="agent-hooks"></a>

### Agent 型 Hooks（`agent`）

基于 subagent 的校验 hook，会启动专用 agent 来评估条件或执行复杂检查。与 prompt hooks（单轮 LLM 评估）不同，agent hooks 可以使用工具并进行多步推理。

```json
{
  "type": "agent",
  "prompt": "核实代码变更是否符合我们的架构规范；查阅相关设计文档并对比。",
  "timeout": 120
}
```

**主要属性：**
- `"type": "agent"` — 标识为 agent hook
- `"prompt"` — 交给 subagent 的任务说明
- Agent 可使用工具（Read、Grep、Bash 等）完成评估
- 返回与 prompt hooks 类似的结构化决策

## Hook 事件

Claude Code 支持 **25 个 hook 事件**：

| 事件 | 触发时机 | Matcher 输入 | 可阻塞 | 常见用途 |
|-------|---------------|---------------|-----------|------------|
| **SessionStart** | 会话开始/恢复/清空/压缩 | startup/resume/clear/compact | 否 | 环境准备 |
| **InstructionsLoaded** | 在加载 CLAUDE.md 或规则文件之后 | （无） | 否 | 修改/过滤说明 |
| **UserPromptSubmit** | 用户提交提示词 | （无） | 是 | 校验提示词 |
| **PreToolUse** | 工具执行之前 | 工具名 | 是（allow/deny/ask） | 校验、修改输入 |
| **PermissionRequest** | 显示权限对话框 | 工具名 | 是 | 自动批准/拒绝 |
| **PostToolUse** | 工具成功之后 | 工具名 | 否 | 补充上下文、反馈 |
| **PostToolUseFailure** | 工具执行失败 | 工具名 | 否 | 错误处理、日志 |
| **Notification** | 发送通知 | 通知类型 | 否 | 自定义通知 |
| **SubagentStart** | 创建 subagent | Agent 类型名 | 否 | Subagent 初始化 |
| **SubagentStop** | Subagent 结束 | Agent 类型名 | 是 | Subagent 校验 |
| **Stop** | Claude 结束回复 | （无） | 是 | 任务完成检查 |
| **StopFailure** | API 错误结束本轮 | （无） | 否 | 错误恢复、日志 |
| **TeammateIdle** | Agent 团队中队友空闲 | （无） | 是 | 队友协调 |
| **TaskCompleted** | 任务标记为完成 | （无） | 是 | 任务后动作 |
| **TaskCreated** | 通过 TaskCreate 创建任务 | （无） | 否 | 任务跟踪、日志 |
| **ConfigChange** | 配置文件变更 | （无） | 是（policy 除外） | 响应配置更新 |
| **CwdChanged** | 工作目录变更 | （无） | 否 | 按目录的配置 |
| **FileChanged** | 监视的文件变更 | （无） | 否 | 文件监视、重建 |
| **PreCompact** | 上下文压缩之前 | manual/auto | 否 | 压缩前动作 |
| **PostCompact** | 压缩完成之后 | （无） | 否 | 压缩后动作 |
| **WorktreeCreate** | 正在创建 worktree | （无） | 是（可返回路径） | Worktree 初始化 |
| **WorktreeRemove** | 正在移除 worktree | （无） | 否 | Worktree 清理 |
| **Elicitation** | MCP 服务器请求用户输入 | （无） | 是 | 输入校验 |
| **ElicitationResult** | 用户对征询（elicitation）的响应 | （无） | 是 | 响应处理 |
| **SessionEnd** | 会话结束 | （无） | 否 | 清理、最终日志 |

### PreToolUse

在 Claude 创建工具参数之后、实际处理之前运行。用于校验或修改工具输入。

**配置：**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py"
          }
        ]
      }
    ]
  }
}
```

**常用 matcher：** `Task`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**输出控制：**
- `permissionDecision`：`"allow"`、`"deny"` 或 `"ask"`
- `permissionDecisionReason`：决策说明
- `updatedInput`：修改后的工具输入参数

### PostToolUse

在工具完成后立即运行。用于校验、日志记录，或向 Claude 回传上下文。

**配置：**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py"
          }
        ]
      }
    ]
  }
}
```

**输出控制：**
- `"block"` 决策会用反馈提示 Claude
- `additionalContext`：为 Claude 追加的上下文

### UserPromptSubmit

在用户提交提示词时、Claude 处理之前运行。

**配置：**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py"
          }
        ]
      }
    ]
  }
}
```

**输出控制：**
- `decision`：`"block"` 可阻止继续处理
- `reason`：被阻止时的说明
- `additionalContext`：追加到提示词的上下文

### Stop 与 SubagentStop

在 Claude 结束回复（Stop）或 subagent 完成（SubagentStop）时运行。支持基于 prompt 的评估，用于智能检查任务是否完成。

**额外输入字段：** `Stop` 与 `SubagentStop` 的 JSON 输入中均包含 `last_assistant_message` 字段，内容为停止前 Claude 或 subagent 的最后一条消息，便于评估任务完成情况。

**配置：**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "评估 Claude 是否已完成用户请求的全部任务。",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### SubagentStart

在 subagent 开始执行时运行。Matcher 的输入为 agent 类型名，便于针对特定 subagent 类型挂接 hook。

**配置：**
```json
{
  "hooks": {
    "SubagentStart": [
      {
        "matcher": "code-review",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/subagent-init.sh"
          }
        ]
      }
    ]
  }
}
```

### SessionStart

在会话启动或恢复时运行。可持久化环境变量。

**Matcher：** `startup`, `resume`, `clear`, `compact`

**特殊能力：** 使用 `CLAUDE_ENV_FILE` 持久化环境变量（在 `CwdChanged` 与 `FileChanged` hooks 中也可用）：

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### SessionEnd

在会话结束时运行，用于清理或最终日志。无法阻止终止。

**结束原因（reason）取值：**
- `clear` - 用户清空了会话
- `logout` - 用户登出
- `prompt_input_exit` - 用户通过提示输入退出
- `other` - 其他原因

**配置：**
```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-cleanup.sh\""
          }
        ]
      }
    ]
  }
}
```

### Notification 事件

通知类事件的 matcher 已更新：
- `permission_prompt` - 权限请求通知
- `idle_prompt` - 空闲状态通知
- `auth_success` - 认证成功
- `elicitation_dialog` - 向用户展示的对话框

## 组件作用域 Hooks

Hooks 可挂在具体组件（skills、agents、commands）的 frontmatter 中：

**在 SKILL.md、agent.md 或 command.md 中：**

```yaml
---
name: secure-operations
description: 在执行操作时附带安全检查
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/check.sh"
          once: true  # 每个会话仅运行一次
---
```

**组件 hooks 支持的事件：** `PreToolUse`, `PostToolUse`, `Stop`

这样可直接在使用该 hook 的组件内定义，相关代码集中在一处。

### Subagent 的 frontmatter 中的 Hooks

若在 subagent 的 frontmatter 中定义 `Stop` hook，会自动转换为仅作用于该 subagent 的 `SubagentStop` hook，从而保证 stop hook 只在该 subagent 完成时触发，而非主会话停止时。

```yaml
---
name: code-review-agent
description: 自动化代码审查 subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "确认代码审查是否充分、完整。"
  # 上述 Stop hook 会针对该 subagent 自动转换为 SubagentStop
---
```

## PermissionRequest 事件

使用自定义输出格式处理权限请求：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow|deny",
      "updatedInput": {},
      "message": "自定义提示信息",
      "interrupt": false
    }
  }
}
```

## Hook 输入与输出

### JSON 输入（经 stdin）

所有 hook 都通过 stdin 接收 JSON：

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.js",
    "content": "..."
  },
  "tool_use_id": "toolu_01ABC123...",
  "agent_id": "agent-abc123",
  "agent_type": "main",
  "worktree": "/path/to/worktree"
}
```

**常见字段：**

| 字段 | 说明 |
|-------|-------------|
| `session_id` | 唯一会话标识 |
| `transcript_path` | 对话 transcript 文件路径 |
| `cwd` | 当前工作目录 |
| `hook_event_name` | 触发该 hook 的事件名 |
| `agent_id` | 运行该 hook 的 agent 标识 |
| `agent_type` | Agent 类型（`"main"`、subagent 类型名等） |
| `worktree` | 若 agent 在 git worktree 中运行，则为 worktree 路径 |

### 退出码

| 退出码 | 含义 | 行为 |
|-----------|---------|----------|
| **0** | 成功 | 继续，解析 JSON stdout |
| **2** | 阻塞性错误 | 阻塞操作，stderr 作为错误展示 |
| **其他** | 非阻塞错误 | 继续，stderr 在详细模式下展示 |

### JSON 输出（stdout，退出码为 0）

```json
{
  "continue": true,
  "stopReason": "若停止则在此填写原因",
  "suppressOutput": false,
  "systemMessage": "可选的系统警告信息",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "文件位于允许的目录内",
    "updatedInput": {
      "file_path": "/modified/path.js"
    }
  }
}
```

## 环境变量

| 变量 | 可用范围 | 说明 |
|----------|-------------|-------------|
| `CLAUDE_PROJECT_DIR` | 所有 hooks | 项目根目录的绝对路径 |
| `CLAUDE_ENV_FILE` | SessionStart, CwdChanged, FileChanged | 用于持久化环境变量的文件路径 |
| `CLAUDE_CODE_REMOTE` | 所有 hooks | 远程环境中为 `"true"` |
| `${CLAUDE_PLUGIN_ROOT}` | 插件 hooks | 插件目录路径 |
| `${CLAUDE_PLUGIN_DATA}` | 插件 hooks | 插件数据目录路径 |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | SessionEnd hooks | SessionEnd hooks 的可配置超时（毫秒，覆盖默认值） |

<a id="prompt-based-hooks"></a>

## 基于 Prompt 的 Hooks

对 `Stop` 与 `SubagentStop` 事件，可使用基于 LLM 的评估：

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "检查是否所有任务均已完成，并给出你的判断。",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**LLM 响应结构：**
```json
{
  "decision": "approve",
  "reason": "所有任务已成功完成",
  "continue": false,
  "stopReason": "任务已完成"
}
```

## 示例

### 示例 1：Bash 命令校验（PreToolUse）

**文件：** `.claude/hooks/validate-bash.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"\brm\s+-rf\s+/", "已拦截危险的 rm -rf / 命令"),
    (r"\bsudo\s+rm", "已拦截 sudo rm 命令"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name != "Bash":
        sys.exit(0)

    command = input_data.get("tool_input", {}).get("command", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, command):
            print(message, file=sys.stderr)
            sys.exit(2)  # 退出码 2 = 阻塞性错误

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**配置：**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\""
          }
        ]
      }
    ]
  }
}
```

### 示例 2：安全扫描（PostToolUse）

**文件：** `.claude/hooks/security-scan.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

SECRET_PATTERNS = [
    (r"password\s*=\s*['\"][^'\"]+['\"]", "疑似硬编码密码"),
    (r"api[_-]?key\s*=\s*['\"][^'\"]+['\"]", "疑似硬编码 API 密钥"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})
    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    file_path = tool_input.get("file_path", "")

    warnings = []
    for pattern, message in SECRET_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            warnings.append(message)

    if warnings:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"{file_path} 的安全警告：" + "；".join(warnings)
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### 示例 3：自动格式化代码（PostToolUse）

**文件：** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# 从 stdin 读取 JSON
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# 按文件扩展名格式化
case "$FILE_PATH" in
    *.js|*.jsx|*.ts|*.tsx|*.json)
        command -v prettier &>/dev/null && prettier --write "$FILE_PATH" 2>/dev/null
        ;;
    *.py)
        command -v black &>/dev/null && black "$FILE_PATH" 2>/dev/null
        ;;
    *.go)
        command -v gofmt &>/dev/null && gofmt -w "$FILE_PATH" 2>/dev/null
        ;;
esac

exit 0
```

### 示例 4：提示词校验（UserPromptSubmit）

**文件：** `.claude/hooks/validate-prompt.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"delete\s+(all\s+)?database", "危险：删除数据库"),
    (r"rm\s+-rf\s+/", "危险：删除根目录"),
]

def main():
    input_data = json.load(sys.stdin)
    prompt = input_data.get("user_prompt", "") or input_data.get("prompt", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            output = {
                "decision": "block",
                "reason": f"已拦截：{message}"
            }
            print(json.dumps(output))
            sys.exit(0)

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### 示例 5：智能 Stop Hook（基于 Prompt）

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "检查 Claude 是否完成了用户请求的全部任务。请核对：1）所需文件是否均已创建或修改？2）是否仍有未解决的错误？若未完成，请说明缺了什么。",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### 示例 6：上下文用量追踪（Hook 配对）

同时使用 `UserPromptSubmit`（消息前）与 `Stop`（回复后）hooks，按请求追踪 token 消耗。

**文件：** `.claude/hooks/context-tracker.py`

```python
#!/usr/bin/env python3
"""
上下文用量追踪：按每次请求统计 token 消耗。

将 UserPromptSubmit 作为「消息前」hook、Stop 作为「回复后」hook，
计算单次请求的 token 用量增量。

计数方式：
1. 字符估算（默认）：约每 4 个字符折合 1 token，无额外依赖
2. tiktoken（可选）：更准（约 90–95%），需执行：pip install tiktoken
"""
import json
import os
import sys
import tempfile

# 配置
CONTEXT_LIMIT = 128000  # Claude 上下文窗口上限（可按所用模型调整）
USE_TIKTOKEN = False    # 若已安装 tiktoken 可改为 True 以提高准确度


def get_state_file(session_id: str) -> str:
    """返回用于保存「消息前」token 计数的临时文件路径，按 session 隔离。"""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    统计文本中的 token 数。

    若可用则使用 tiktoken 的 p50k_base 编码（约 90–95% 准确度），
    否则回退为字符估算（约 80–90% 准确度）。
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # 回退到估算

    # 按字符估算：英文约每 4 个字符 1 token
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """读取 transcript 文件并拼接全部文本内容。"""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # 从多种消息格式中提取文本
                if "message" in entry:
                    msg = entry["message"]
                    if isinstance(msg.get("content"), str):
                        content.append(msg["content"])
                    elif isinstance(msg.get("content"), list):
                        for block in msg["content"]:
                            if isinstance(block, dict) and block.get("type") == "text":
                                content.append(block.get("text", ""))
            except json.JSONDecodeError:
                continue

    return "\n".join(content)


def handle_user_prompt_submit(data: dict) -> None:
    """消息前 hook：在请求发出前保存当前 token 计数。"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # 写入临时文件供后续对比
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """回复后 hook：计算并输出 token 增量。"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # 读取消息前计数
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # 计算增量
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # 输出用量
    method_label = "tiktoken" if USE_TIKTOKEN else "估算"
    print(
        f"上下文（{method_label}）：约 {current_tokens:,} 个 token（已用 {percentage:.1f}%，约剩余 {remaining:,}）",
        file=sys.stderr,
    )
    if delta_tokens > 0:
        print(f"本次请求：约 {delta_tokens:,} 个 token", file=sys.stderr)


def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name", "")

    if event == "UserPromptSubmit":
        handle_user_prompt_submit(data)
    elif event == "Stop":
        handle_stop(data)

    sys.exit(0)


if __name__ == "__main__":
    main()
```

**配置：**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ]
  }
}
```

**工作原理：**
1. `UserPromptSubmit` 在处理你的提示词之前触发 — 保存当前 token 计数
2. `Stop` 在 Claude 回复之后触发 — 计算增量并报告用量
3. 通过临时文件名中的 `session_id` 隔离各会话

**Token 计数方式：**

| 方式 | 准确度 | 依赖 | 速度 |
|--------|----------|--------------|-------|
| 字符估算 | 约 80–90% | 无 | <1ms |
| tiktoken（p50k_base） | 约 90–95% | `pip install tiktoken` | <10ms |

> **说明：** Anthropic 尚未发布官方离线 tokenizer。两种方式均为近似。Transcript 包含用户提示、Claude 回复与工具输出，但不包含系统提示或内部上下文。

### 示例 7：播种 Auto-Mode 权限（一次性安装脚本）

一次性安装脚本，向 `~/.claude/settings.json` 写入约 67 条与 Claude Code auto-mode 基线等价的安全权限规则 — 无需任何 hook，也无需记住后续选择。执行一次即可；可安全重复执行（已存在的规则会跳过）。

**文件：** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# 预览将要添加的内容
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# 应用
python3 09-advanced-features/setup-auto-mode-permissions.py
```

**会添加的内容：**

| 类别 | 示例 |
|----------|---------|
| 内置工具 | `Read(*)`, `Edit(*)`, `Write(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)` |
| Git 只读 | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)` |
| Git 写入（本地） | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| 包管理器 | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| 构建与测试 | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| 常用 shell | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

**有意排除的内容**（本脚本不会添加）：
- `rm -rf`、`sudo`、force push、`git reset --hard`
- `DROP TABLE`、`kubectl delete`、`terraform destroy`
- `npm publish`、`curl | bash`、生产环境部署

## 插件 Hooks

插件可在 `hooks/hooks.json` 中包含 hooks：

**文件：** `plugins/hooks/hooks.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh"
          }
        ]
      }
    ]
  }
}
```

**插件 Hooks 中的环境变量：**
- `${CLAUDE_PLUGIN_ROOT}` - 插件目录路径
- `${CLAUDE_PLUGIN_DATA}` - 插件数据目录路径

这样插件可自带自定义校验与自动化 hooks。

## MCP 工具 Hooks

MCP 工具遵循模式 `mcp__<server>__<tool>`：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"systemMessage\": \"已记录 Memory 操作\"}'"
          }
        ]
      }
    ]
  }
}
```

## 安全注意事项

### 免责声明

**使用风险自负**：Hooks 会执行任意 shell 命令。你需自行负责：
- 你配置的命令
- 文件访问/修改权限
- 可能的数据丢失或系统损坏
- 在生产使用前于安全环境中测试 hooks

### 安全说明

- **需要信任工作区：** `statusLine` 与 `fileSuggestion` 的 hook 输出命令现需接受工作区信任后才会生效。
- **HTTP hooks 与环境变量：** HTTP hooks 若要在 URL 中使用环境变量插值，必须提供显式 `allowedEnvVars` 列表，避免敏感环境变量意外泄露到远程端点。
- **托管设置层级：** `disableAllHooks` 现遵循托管设置层级，组织级设置可强制禁用 hooks，个人用户无法覆盖。

### 最佳实践

| 建议 | 避免 |
|-----|-------|
| 校验并清理所有输入 | 盲目信任输入数据 |
| 为 shell 变量加引号：`"$VAR"` | 不加引号：`$VAR` |
| 阻止路径穿越（`..`） | 允许任意路径 |
| 使用 `$CLAUDE_PROJECT_DIR` 的绝对路径 | 硬编码路径 |
| 跳过敏感文件（`.env`、`.git/`、密钥等） | 处理所有文件 |
| 先隔离测试 hooks | 部署未测试的 hooks |
| 为 HTTP hooks 显式指定 `allowedEnvVars` | 向 webhook 暴露全部环境变量 |

## 调试

### 启用调试模式

使用 debug 标志运行 Claude 以查看详细 hook 日志：

```bash
claude --debug
```

### 详细模式

在 Claude Code 中使用 `Ctrl+O` 启用详细模式，查看 hook 执行进度。

### 独立测试 Hooks

```bash
# 使用示例 JSON 输入测试
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# 检查退出码
echo $?
```

## 完整配置示例

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/format-code.sh\"",
            "timeout": 30
          },
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py\""
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-init.sh\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "在结束前请确认所有任务均已完成。",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Hook 执行细节

| 方面 | 行为 |
|--------|----------|
| **超时** | 默认 60 秒，可按命令配置 |
| **并行** | 所有匹配的 hooks 并行运行 |
| **去重** | 相同的 hook 命令会去重 |
| **环境** | 在当前目录下运行，使用 Claude Code 的环境 |

## 故障排查

### Hook 未执行
- 确认 JSON 配置语法正确
- 检查 matcher 是否与工具名匹配
- 确认脚本存在且可执行：`chmod +x script.sh`
- 运行 `claude --debug` 查看 hook 执行日志
- 确认 hook 从 stdin 读取 JSON（而非命令行参数）

### Hook 意外阻塞
- 用示例 JSON 测试 hook：`echo '{"tool_name": "Write", ...}' | ./hook.py`
- 检查退出码：允许应为 0，阻塞应为 2
- 查看 stderr 输出（退出码为 2 时会显示）

### JSON 解析错误
- 始终从 stdin 读取，不要用命令行参数
- 使用正确的 JSON 解析（不要靠字符串拼接）
- 对缺失字段做容错处理

## 安装

### 步骤 1：创建 Hooks 目录
```bash
mkdir -p ~/.claude/hooks
```

### 步骤 2：复制示例 Hooks
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### 步骤 3：在设置中配置
编辑 `~/.claude/settings.json` 或 `.claude/settings.json`，按上文加入 hook 配置。

## 相关概念

- **[Checkpoints 与 Rewind](../08-checkpoints/)** - 保存与恢复对话状态
- **[Slash Commands](../01-slash-commands/)** - 创建自定义 slash commands
- **[Skills](../03-skills/)** - 可复用的自主能力
- **[Subagents](../04-subagents/)** - 委托执行任务
- **[Plugins](../07-plugins/)** - 打包的扩展包
- **[高级功能](../09-advanced-features/)** - 探索 Claude Code 高级能力

## 更多资源

- **[官方 Hooks 文档](https://code.claude.com/docs/en/hooks)** - Hooks 完整参考
- **[CLI 参考](https://code.claude.com/docs/en/cli-reference)** - 命令行界面文档
- **[Memory 指南](../02-memory/)** - 持久化上下文配置
