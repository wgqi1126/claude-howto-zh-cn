<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To 教程" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps 自动化插件

面向部署、监控与事件响应的完整 DevOps 自动化。

## 功能

✅ 自动化部署
✅ 回滚流程
✅ 系统健康监控
✅ 事件响应工作流
✅ Kubernetes 集成

## 安装

```bash
/plugin install devops-automation
```

## 包含内容

### Slash Commands
- `/deploy` - 部署到生产或预发布（staging）环境
- `/rollback` - 回滚到上一版本
- `/status` - 检查系统健康
- `/incident` - 处理生产环境事件

### Subagents
- `deployment-specialist` - 部署运维
- `incident-commander` - 事件协调
- `alert-analyzer` - 系统健康分析

### MCP Servers
- Kubernetes 集成

### Scripts
- `deploy.sh` - 部署自动化
- `rollback.sh` - 回滚自动化
- `health-check.sh` - 健康检查工具

### Hooks
- `pre-deploy.js` - 部署前校验
- `post-deploy.js` - 部署后任务

## 使用方式

### 部署到预发布（staging）
```
/deploy staging
```

### 部署到生产环境
```
/deploy production
```

### 回滚
```
/rollback production
```

### 查看状态
```
/status
```

### 处理事件
```
/incident
```

## 要求

- Claude Code 1.0+
- Kubernetes CLI（kubectl）
- 已配置集群访问权限

## 配置

配置 Kubernetes：
```bash
export KUBECONFIG=~/.kube/config
```

## 示例工作流

```
用户: /deploy production

Claude:
1. 运行 pre-deploy hook（校验 kubectl、集群连接）
2. 委派给 deployment-specialist Subagent
3. 执行 deploy.sh 脚本
4. 通过 Kubernetes MCP 监控部署进度
5. 运行 post-deploy hook（等待 Pod、冒烟测试）
6. 输出部署摘要

结果：
✅ 部署完成
📦 版本：v2.1.0
🚀 Pod：3/3 就绪
⏱️  耗时：2 分 34 秒
```
