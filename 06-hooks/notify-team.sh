#!/bin/bash
# 在事件发生时发送通知
# Hook: PostPush

REPO_NAME=$(basename $(git rev-parse --show-toplevel 2>/dev/null) 2>/dev/null)
COMMIT_MSG=$(git log -1 --pretty=%B 2>/dev/null)
AUTHOR=$(git log -1 --pretty=%an 2>/dev/null)
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)

echo "📢 正在向团队发送通知..."

# Slack Webhook 示例（请替换为你的 Webhook URL）
SLACK_WEBHOOK="${SLACK_WEBHOOK_URL:-}"

if [ -n "$SLACK_WEBHOOK" ]; then
  curl -X POST "$SLACK_WEBHOOK" \
    -H 'Content-Type: application/json' \
    -d "{
      \"text\": \"推送到 *$REPO_NAME*\",
      \"attachments\": [{
        \"color\": \"good\",
        \"fields\": [
          {\"title\": \"分支\", \"value\": \"$BRANCH\", \"short\": true},
          {\"title\": \"作者\", \"value\": \"$AUTHOR\", \"short\": true},
          {\"title\": \"提交\", \"value\": \"$COMMIT_MSG\"}
        ]
      }]
    }" \
    --silent --output /dev/null

  echo "✅ 已发送 Slack 通知"
fi

# Discord Webhook 示例（请替换为你的 Webhook URL）
DISCORD_WEBHOOK="${DISCORD_WEBHOOK_URL:-}"

if [ -n "$DISCORD_WEBHOOK" ]; then
  curl -X POST "$DISCORD_WEBHOOK" \
    -H 'Content-Type: application/json' \
    -d "{
      \"content\": \"**推送到 $REPO_NAME**\",
      \"embeds\": [{
        \"title\": \"$COMMIT_MSG\",
        \"color\": 3066993,
        \"fields\": [
          {\"name\": \"分支\", \"value\": \"$BRANCH\", \"inline\": true},
          {\"name\": \"作者\", \"value\": \"$AUTHOR\", \"inline\": true}
        ]
      }]
    }" \
    --silent --output /dev/null

  echo "✅ 已发送 Discord 通知"
fi

# 邮件通知示例
EMAIL_TO="${TEAM_EMAIL:-}"

if [ -n "$EMAIL_TO" ]; then
  echo "$AUTHOR 推送到 $REPO_NAME" | \
    mail -s "Git 推送：$BRANCH" "$EMAIL_TO"

  echo "✅ 已发送邮件通知"
fi

exit 0
