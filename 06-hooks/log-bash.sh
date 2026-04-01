#!/bin/bash
# 记录所有 bash 命令
# Hook: PostToolUse:Bash

COMMAND="$1"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
LOGFILE="$HOME/.claude/bash-commands.log"

# 若日志目录不存在则创建
mkdir -p "$(dirname "$LOGFILE")"

# 将命令追加到日志文件
echo "[$TIMESTAMP] $COMMAND" >> "$LOGFILE"

# 可选：同时写入系统日志
# logger -t "claude-bash" "$COMMAND"

exit 0
