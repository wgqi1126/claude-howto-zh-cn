#!/bin/bash
set -e

echo "⏪ 开始回滚..."

ENV=${1:-staging}
echo "📦 目标环境: $ENV"

# 获取上一次部署
PREVIOUS=$(kubectl rollout history deployment/app -n $ENV | tail -2 | head -1 | awk '{print $1}')
echo "🔄 正在回滚到修订版本: $PREVIOUS"

# 执行回滚
kubectl rollout undo deployment/app -n $ENV

# 等待回滚完成
echo "⏳ 正在等待回滚完成..."
kubectl rollout status deployment/app -n $ENV

# 健康检查
echo "🏥 正在执行健康检查..."
sleep 5
curl -f http://api.$ENV.example.com/health

echo "✅ 回滚完成！"
