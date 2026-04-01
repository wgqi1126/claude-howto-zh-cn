#!/usr/bin/env node

/**
 * 部署后 Hook
 * 在部署完成后运行
 */

async function postDeploy() {
  console.log('正在执行部署后任务...');

  const { execSync } = require('child_process');

  // 等待 Pod 就绪
  console.log('正在等待 Pod 就绪...');
  try {
    execSync('kubectl wait --for=condition=ready pod -l app=myapp --timeout=300s', {
      stdio: 'inherit'
    });
  } catch (error) {
    console.error('❌ Pod 未能就绪');
    process.exit(1);
  }

  // 运行冒烟测试
  console.log('正在运行冒烟测试...');
  // 在此添加你的冒烟测试命令

  console.log('✅ 部署后任务已完成');
}

postDeploy().catch(error => {
  console.error('部署后 Hook 失败:', error);
  process.exit(1);
});
