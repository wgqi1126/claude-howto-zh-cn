#!/usr/bin/env node

/**
 * 部署前 Hook
 * 在部署前校验环境与前置条件
 */

async function preDeploy() {
  console.log('正在执行部署前检查...');

  const { execSync } = require('child_process');

  // 检查是否已安装 kubectl
  try {
    execSync('which kubectl', { stdio: 'pipe' });
  } catch (error) {
    console.error('❌ 未找到 kubectl。请安装 Kubernetes CLI。');
    process.exit(1);
  }

  // 检查是否已连接到集群
  try {
    execSync('kubectl cluster-info', { stdio: 'pipe' });
  } catch (error) {
    console.error('❌ 未连接到 Kubernetes 集群');
    process.exit(1);
  }

  console.log('✅ 部署前检查已通过');
}

preDeploy().catch(error => {
  console.error('部署前 Hook 失败:', error);
  process.exit(1);
});
