#!/bin/bash
# 校验用户提示词
# Hook: UserPromptSubmit

# 从标准输入读取提示词
PROMPT=$(cat)

echo "🔍 正在校验提示词..."

# 检查危险操作
DANGEROUS_PATTERNS=(
  "rm -rf /"
  "delete database"
  "drop database"
  "format disk"
  "dd if="
)

for pattern in "${DANGEROUS_PATTERNS[@]}"; do
  if echo "$PROMPT" | grep -qi "$pattern"; then
    echo "❌ 已拦截：检测到危险操作：$pattern"
    exit 1
  fi
done

# 检查生产环境部署
if echo "$PROMPT" | grep -qiE "(deploy|push).*production"; then
  if [ ! -f ".deployment-approved" ]; then
    echo "❌ 已拦截：生产环境部署需要审批"
    echo "请创建 .deployment-approved 文件后再继续"
    exit 1
  fi
fi

# 检查特定操作是否具备所需上下文
if echo "$PROMPT" | grep -qi "refactor"; then
  if [ ! -f "tests/" ] && [ ! -f "test/" ]; then
    echo "⚠️  警告：在没有测试的情况下重构可能存在风险"
  fi
fi

echo "✅ 提示词校验通过"
exit 0
