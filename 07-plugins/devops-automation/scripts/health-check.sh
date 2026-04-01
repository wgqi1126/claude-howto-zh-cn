#!/bin/bash

echo "🏥 系统健康检查"
echo "===================="

ENV=${1:-production}

# 检查 API
echo -n "API："
if curl -sf http://api.$ENV.example.com/health > /dev/null; then
  echo "✅ 健康"
else
  echo "❌ 不健康"
fi

# 检查数据库
echo -n "数据库："
if pg_isready -h db.$ENV.example.com > /dev/null 2>&1; then
  echo "✅ 健康"
else
  echo "❌ 不健康"
fi

# 检查 Pod
echo -n "Kubernetes Pod："
PODS_READY=$(kubectl get pods -n $ENV --no-headers | grep "Running" | wc -l)
PODS_TOTAL=$(kubectl get pods -n $ENV --no-headers | wc -l)
echo "$PODS_READY/$PODS_TOTAL 已就绪"

echo "===================="
