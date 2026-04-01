<a id="security-policy"></a>
# 安全策略

<a id="overview"></a>
## 概述

我们重视 Claude How To 项目的安全。本文说明我们的安全实践，以及如何负责任地报告安全漏洞。

<a id="supported-versions"></a>
## 受支持版本

我们为以下版本提供安全更新：

| 版本 | 状态 | 支持至 |
|---------|--------|---------------|
| Latest (main) | ✅ 活跃中 | 当前起 6 个月内 |
| 1.x releases | ✅ 活跃中 | 下一主版本发布前 |

**说明**：作为教育类指南项目，我们侧重维护当前最佳实践与文档安全，而非传统意义上的多版本长期支持。更新会直接应用在 `main` 分支。

<a id="security-practices"></a>
## 安全实践

<a id="code-security"></a>
### 代码安全

1. **依赖管理**
   - 所有 Python 依赖在 `requirements.txt` 中固定版本
   - 通过 dependabot 与人工审核定期更新
   - 每次提交使用 Bandit 进行安全扫描
   - 使用 pre-commit hooks 做安全检查

2. **代码质量**
   - 使用 Ruff 做 lint，发现常见问题
   - 使用 mypy 做类型检查，减少与类型相关的风险
   - pre-commit hooks 强制执行规范
   - 合并前审查所有变更

3. **访问控制**
   - 对 `main` 分支启用分支保护
   - 合并前要求评审
   - 合并前必须通过状态检查
   - 仓库写入权限受限

<a id="documentation-security"></a>
### 文档安全

1. **示例中不含密钥**
   - 示例中的 API 密钥均为占位符
   - 从不硬编码凭据
   - `.env.example` 展示所需变量
   - 对密钥管理有明确警示

2. **安全最佳实践**
   - 示例展示安全用法
   - 在文档中突出安全提示
   - 链接到官方安全指南
   - 在相关章节讨论凭据处理

3. **内容审查**
   - 审查全部文档中的安全问题
   - 在贡献指南中说明安全考量
   - 校验外部链接与引用

<a id="dependency-security"></a>
### 依赖安全

1. **扫描**
   - Bandit 扫描全部 Python 代码中的漏洞
   - 通过 GitHub security alerts 检查依赖漏洞
   - 定期进行人工安全审计

2. **更新**
   - 及时应用安全补丁
   - 谨慎评估大版本升级
   - 变更日志包含与安全相关的更新

3. **透明**
   - 在提交中记录安全相关更新
   - 负责任地处理漏洞披露
   - 在适当时发布公开安全公告

<a id="reporting-a-vulnerability"></a>
## 报告漏洞

<a id="security-issues-we-care-about"></a>
### 我们关注的安全问题

欢迎报告：
- 脚本或示例中的**代码漏洞**
- Python 包中的**依赖漏洞**
- 任意代码示例中的**密码学问题**
- 文档中的**认证/授权缺陷**
- 配置示例中的**数据暴露风险**
- **注入类漏洞**（SQL、命令等）
- **SSRF/XXE/路径遍历**等问题

<a id="security-issues-out-of-scope"></a>
### 不在范围内的问题

以下不属于本项目范围：
- Claude Code 本身的漏洞（请向 Anthropic 报告）
- 外部服务或库的问题（请向上游报告）
- 社会工程学或用户教育类问题（与本指南无关）
- 无概念验证的理论漏洞
- 已通过官方渠道报告的依赖漏洞

<a id="how-to-report"></a>
## 如何报告

<a id="private-reporting-preferred"></a>
### 私密报告（推荐）

**对于敏感安全问题，请使用 GitHub 的私密漏洞报告：**

1. 打开：https://github.com/luongnv89/claude-howto/security/advisories
2. 点击 “Report a vulnerability”
3. 填写漏洞详情
4. 请包含：
   - 对漏洞的清晰描述
   - 受影响组件（文件、章节、示例）
   - 可能影响
   - 复现步骤（如适用）
   - 建议修复方案（如有）

**后续流程：**
- 我们会在 48 小时内确认收到
- 我们会调查并评估严重程度
- 我们会与你协作制定修复方案
- 我们会协调披露时间线
- 我们会在安全公告中致谢（除非你希望匿名）

<a id="public-reporting"></a>
### 公开报告

对于非敏感问题或已公开的问题：

1. **开启 GitHub Issue**，并打上 `security` 标签
2. 请包含：
   - 标题：`[SECURITY]` 加简短描述
   - 详细说明
   - 受影响文件或章节
   - 可能影响
   - 建议修复

<a id="vulnerability-response-process"></a>
## 漏洞响应流程

<a id="assessment-24-hours"></a>
### 评估（24 小时内）

1. 确认收到报告
2. 使用 [CVSS v3.1](https://www.first.org/cvss/v3.1/specification-document) 评估严重程度
3. 判断是否在本项目范围内
4. 向你反馈初步评估

<a id="development-1-7-days"></a>
### 开发（1–7 天）

1. 开发修复
2. 审查并测试修复
3. 创建安全公告
4. 准备发布说明

<a id="disclosure-varies-by-severity"></a>
### 披露（视严重程度而定）

**严重（CVSS 9.0–10.0）**
- 立即发布修复
- 发布公开公告
- 提前 24 小时通知报告者

**高（CVSS 7.0–8.9）**
- 在 48–72 小时内发布修复
- 提前 5 天通知报告者
- 发布时公开公告

**中（CVSS 4.0–6.9）**
- 在下次常规更新中发布修复
- 发布时公开公告

**低（CVSS 0.1–3.9）**
- 在下次常规更新中包含修复
- 发布时公告

<a id="publication"></a>
### 发布

我们发布的安全公告包含：
- 漏洞说明
- 受影响组件
- 严重程度评估（CVSS 分数）
- 修复版本
- 变通办法（如适用）
- 致谢报告者（经同意后）

<a id="best-practices-for-reporters"></a>
## 给报告者的最佳实践

<a id="before-reporting"></a>
### 报告前

- **确认问题**：能否稳定复现？
- **检索已有 issue**：是否已有人报告？
- **查阅文档**：是否有安全使用说明？
- **验证修复**：你建议的修复是否可行？

<a id="when-reporting"></a>
### 报告时

- **具体**：提供准确文件路径与行号
- **交代背景**：为何构成安全问题？
- **说明影响**：攻击者可能做什么？
- **给出步骤**：我们如何复现？
- **建议修复**：你会如何修？

<a id="after-reporting"></a>
### 报告后

- **保持耐心**：我们资源有限
- **及时回复**：尽快回答跟进问题
- **保密**：在修复发布前请勿公开披露
- **配合协调**：遵守我们的披露时间线

<a id="security-headers-and-configuration"></a>
## 安全相关配置与仓库设置

<a id="repository-security"></a>
### 仓库安全

- **分支保护**：对 `main` 的变更需要 2 人批准
- **状态检查**：必须通过全部 CI/CD 检查
- **CODEOWNERS**：关键文件指定审查者
- **签名提交**：建议贡献者使用

<a id="development-security"></a>
### 开发安全

```bash
# 安装 pre-commit hooks
pre-commit install

# 在本地运行安全扫描
bandit -c pyproject.toml -r scripts/
mypy scripts/ --ignore-missing-imports
ruff check scripts/
```

<a id="dependency-security-1"></a>
### 依赖安全

```bash
# 检查已知漏洞
pip install safety
safety check

# 或使用 pip-audit
pip install pip-audit
pip-audit
```

<a id="security-guidelines-for-contributors"></a>
## 贡献者安全指南

<a id="when-writing-examples"></a>
### 撰写示例时

1. **不要硬编码密钥**
   ```python
   # ❌ 不推荐
   api_key = "sk-1234567890"

   # ✅ 推荐
   api_key = os.getenv("API_KEY")
   ```

2. **说明安全影响**
   ```markdown
   ⚠️ **安全提示**：切勿将 `.env` 文件提交到 git。
   请立即加入 `.gitignore`。
   ```

3. **采用安全默认值**
   - 默认启用认证
   - 在适用场景使用 HTTPS
   - 校验并清理输入
   - 使用参数化查询

4. **记录安全考量**
   - 说明为何与安全相关
   - 展示安全与不安全的写法
   - 链接权威资料
   - 显著位置加入警告

<a id="when-reviewing-contributions"></a>
### 审查贡献时

1. **检查是否泄露密钥**
   - 扫描常见模式（api_key=、password=）
   - 审查配置文件
   - 检查环境变量

2. **核实安全编码实践**
   - 无硬编码凭据
   - 正确的输入校验
   - 安全的认证/授权
   - 安全的文件处理

3. **评估安全影响**
   - 是否可能被滥用？
   - 最坏情况是什么？
   - 是否存在边界情况？

<a id="security-resources"></a>
## 安全资源

<a id="official-standards"></a>
### 官方标准
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [CVSS Calculator](https://www.first.org/cvss/calculator/3.1)

<a id="python-security"></a>
### Python 安全
- [Python Security Advisories](https://www.python.org/dev/security/)
- [PyPI Security](https://pypi.org/help/#security)
- [Bandit Documentation](https://bandit.readthedocs.io/)

<a id="dependency-management"></a>
### 依赖管理
- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)
- [GitHub Security Alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)

<a id="general-security"></a>
### 通用安全
- [Anthropic Security](https://www.anthropic.com/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

<a id="security-advisories-archive"></a>
## 安全公告归档

历史安全公告可在 [GitHub Security Advisories](https://github.com/luongnv89/claude-howto/security/advisories) 标签页查看。

<a id="contact"></a>
## 联系方式

如有关于安全的问题或希望讨论安全实践：

1. **私密安全报告**：使用 GitHub 私密漏洞报告
2. **一般安全问题**：开启讨论并打上 `[SECURITY]` 标签
3. **对本安全策略的反馈**：创建带 `security` 标签的 issue

<a id="acknowledgments"></a>
## 致谢

感谢帮助维护本项目安全的研究者与社区成员。负责任地报告漏洞的贡献者将在我们的安全公告中获得致谢（除非其希望匿名）。

<a id="policy-updates"></a>
## 策略更新

本安全策略会在以下情况审查并更新：
- 发现新漏洞时
- 安全最佳实践演进时
- 项目范围变化时
- 至少每年一次

**上次更新**：2026 年 1 月  
**下次审查**：2027 年 1 月

---

感谢你我共同守护 Claude How To 的安全！🔒
