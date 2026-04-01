#!/usr/bin/env node

/**
 * Pre-review 钩子
 * 在开始 PR 审查前运行，确保前置条件已满足
 */

async function preReview() {
  console.log('正在运行 pre-review 检查...');

  // 检查是否为 git 仓库
  const { execSync } = require('child_process');
  try {
    execSync('git rev-parse --git-dir', { stdio: 'pipe' });
  } catch (error) {
    console.error('❌ 当前目录不是 git 仓库');
    process.exit(1);
  }

  // 检查是否有未提交的更改
  try {
    const status = execSync('git status --porcelain', { encoding: 'utf-8' });
    if (status.trim()) {
      console.warn('⚠️  警告：检测到未提交的更改');
    }
  } catch (error) {
    console.error('❌ 检查 git 状态失败');
    process.exit(1);
  }

  console.log('✅ Pre-review 检查已通过');
}

preReview().catch(error => {
  console.error('Pre-review 钩子执行失败:', error);
  process.exit(1);
});
