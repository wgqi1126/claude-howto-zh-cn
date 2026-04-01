#!/bin/bash
set -e

echo "🚀 开始部署..."

# 加载环境
ENV=${1:-staging}
echo "📦 目标环境: $ENV"

# 部署前检查
echo "✓ 正在执行部署前检查..."
npm run lint
npm test

# 构建
echo "🔨 正在构建应用..."
npm run build

# 部署
echo "🚢 正在部署到 $ENV..."
kubectl apply -f k8s/$ENV/

# 健康检查
echo "🏥 正在执行健康检查..."
sleep 10
curl -f http://api.$ENV.example.com/health

echo "✅ 部署完成！"
