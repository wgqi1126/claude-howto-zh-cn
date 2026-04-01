<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

<a id="contributing-to-claude-how-to"></a>

# 参与 Claude How To 贡献

感谢你有意为本项目做贡献！本指南将帮助你了解如何有效地参与贡献。

<a id="about-this-project"></a>

## 关于本项目

Claude How To 是一份面向 Claude Code 的可视化、示例驱动指南。我们提供：
- **Mermaid 图表**，说明各功能如何工作
- **可直接用于生产的模板**，开箱即用
- **贴近实践的示例**，附背景与最佳实践
- **循序渐进的学习路径**，从入门到进阶

<a id="types-of-contributions"></a>

## 贡献类型

<a id="1-new-examples-or-templates"></a>

### 1. 新示例或模板
为现有功能（slash commands、skills、hooks 等）补充示例：
- 可复制粘贴的代码
- 清晰说明其工作原理
- 使用场景与收益
- 排错提示

<a id="2-documentation-improvements"></a>

### 2. 文档改进
- 澄清容易混淆的段落
- 修正错别字与语法
- 补充缺失信息
- 改进代码示例

<a id="3-feature-guides"></a>

### 3. 功能指南
为新的 Claude Code 功能撰写指南：
- 分步教程
- 架构示意图
- 常见模式与反模式
- 真实工作流

<a id="4-bug-reports"></a>

### 4. 问题反馈
报告你遇到的问题：
- 说明你的预期行为
- 说明实际发生的情况
- 提供复现步骤
- 附上相关的 Claude Code 版本与操作系统信息

<a id="5-feedback-and-suggestions"></a>

### 5. 意见与建议
帮助改进本指南：
- 建议更清晰的讲解方式
- 指出覆盖不足之处
- 建议新增章节或调整结构

<a id="getting-started"></a>

## 入门步骤

<a id="1-fork-and-clone"></a>

### 1. Fork 与克隆
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

<a id="2-create-a-branch"></a>

### 2. 创建分支
使用能说明意图的分支名：
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

<a id="3-set-up-your-environment"></a>

### 3. 配置本地环境
```bash
# 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装 pre-commit hooks（可选，但建议安装）
pip install pre-commit
pre-commit install

# 手动运行 pre-commit 检查
pre-commit run --all-files
```

<a id="directory-structure"></a>

## 目录结构

```
├── 01-slash-commands/      # 用户调用的快捷方式
├── 02-memory/              # 持久化上下文示例
├── 03-skills/              # 可复用能力
├── 04-subagents/           # 专用 AI 助手
├── 05-mcp/                 # Model Context Protocol 示例
├── 06-hooks/               # 事件驱动自动化
├── 07-plugins/             # 打包功能
├── 08-checkpoints/         # 会话快照
├── 09-advanced-features/   # 规划、思考、后台等
├── 10-cli/                 # CLI 参考
├── scripts/                # 构建与工具脚本
└── README.md               # 主指南
```

<a id="how-to-contribute-examples"></a>

## 如何贡献示例

<a id="adding-a-slash-command"></a>

### 添加 Slash Command
1. 在 `01-slash-commands/` 中创建 `.md` 文件
2. 内容需包含：
   - 功能说明
   - 使用场景
   - 安装说明
   - 使用示例
   - 自定义建议
3. 更新 `01-slash-commands/README.md`

<a id="adding-a-skill"></a>

### 添加 Skill
1. 在 `03-skills/` 下创建目录
2. 内容需包含：
   - `SKILL.md` — 主文档
   - `scripts/` — 如需可放辅助脚本
   - `templates/` — 提示词模板
   - 在 README 中给出示例用法
3. 更新 `03-skills/README.md`

<a id="adding-a-subagent"></a>

### 添加 Subagent
1. 在 `04-subagents/` 中创建 `.md` 文件
2. 内容需包含：
   - 智能体用途与能力
   - 系统提示结构
   - 示例使用场景
   - 集成示例
3. 更新 `04-subagents/README.md`

<a id="adding-mcp-configuration"></a>

### 添加 MCP 配置
1. 在 `05-mcp/` 中创建 `.json` 文件
2. 内容需包含：
   - 配置说明
   - 所需环境变量
   - 安装步骤
   - 使用示例
3. 更新 `05-mcp/README.md`

<a id="adding-a-hook"></a>

### 添加 Hook
1. 在 `06-hooks/` 中创建 `.sh` 文件
2. 内容需包含：
   - Shebang 与说明
   - 用注释清楚解释逻辑
   - 错误处理
   - 安全方面的考虑
3. 更新 `06-hooks/README.md`

<a id="writing-guidelines"></a>

## 写作规范

<a id="markdown-style"></a>

### Markdown 风格
- 使用清晰的标题（章节用 H2，小节用 H3）
- 段落简短、聚焦主题
- 列表使用项目符号
- 代码块注明语言
- 各节之间空行分隔

<a id="code-examples"></a>

### 代码示例
- 保证示例可直接复制运行
- 对非显而易见的逻辑加注释
- 同时提供简单版与进阶版
- 展示真实使用场景
- 标出可能的问题

<a id="documentation"></a>

### 文档内容
- 说明「为什么」，不只「是什么」
- 写明前置条件
- 增加排错小节
- 链接到相关主题
- 保持对初学者友好

<a id="jsonyaml"></a>

### JSON/YAML
- 使用规范的缩进（全文统一 2 或 4 空格）
- 用注释解释配置含义
- 提供校验示例

<a id="diagrams"></a>

### 图表
- 尽量使用 Mermaid
- 保持图表简洁可读
- 在图下附文字说明
- 链接到相关章节

<a id="commit-guidelines"></a>

## 提交说明（Commit）

遵循 conventional commit 格式：
```
type(scope): description

[optional body]
```

类型（Types）：
- `feat`：新功能或新示例
- `fix`：缺陷修复或更正
- `docs`：文档变更
- `refactor`：代码结构调整
- `style`：格式调整
- `test`：测试的新增或变更
- `chore`：构建、依赖等杂项

示例：
```
feat(slash-commands): Add API documentation generator
docs(memory): Improve personal preferences example
fix(README): Correct table of contents link
docs(skills): Add comprehensive code review skill
```

<a id="before-submitting"></a>

## 提交前检查

<a id="checklist"></a>

### 清单
- [ ] 代码符合项目风格与约定
- [ ] 新示例配有清晰文档
- [ ] 已更新 README（模块内与仓库根目录）
- [ ] 未包含敏感信息（API 密钥、凭据等）
- [ ] 示例已测试且可用
- [ ] 链接已核对无误
- [ ] 文件权限正确（脚本可执行）
- [ ] 提交信息清楚、描述准确

<a id="local-testing"></a>

### 本地测试
```bash
# 检查文件格式
pre-commit run --all-files

# 验证链接是否有效（如适用）
# 在 Claude Code 中手动测试示例

# 查看你的改动
git diff

# 测试 EPUB 生成（若文档有变更）
uv run scripts/build_epub.py
```

<a id="pull-request-process"></a>

## Pull Request 流程

1. **创建 PR 并写清说明**：
   - 本 PR 增加或修复了什么？
   - 为什么需要这项改动？
   - 关联的 issue（若有）

2. **附上必要细节**：
   - 新功能？请写使用场景
   - 文档？请说明改进点
   - 示例？可展示修改前后对比

3. **关联 issue**：
   - 使用 `Closes #123` 可在合并后自动关闭对应 issue

4. **耐心等待评审**：
   - 维护者可能会提出修改建议
   - 根据反馈迭代
   - 是否合入由维护者最终决定

<a id="code-review-process"></a>

## 代码评审关注点

评审将检查：
- **准确性**：是否与描述一致、是否可用？
- **质量**：是否达到可上线水平？
- **一致性**：是否符合项目既有模式？
- **文档**：是否清楚、完整？
- **安全**：是否存在安全隐患？

<a id="reporting-issues"></a>

## 报告问题

<a id="bug-reports"></a>

### 缺陷报告（Bug）
请包含：
- Claude Code 版本
- 操作系统
- 复现步骤
- 预期行为
- 实际行为
- 如有请附截图

<a id="feature-requests"></a>

### 功能建议
请包含：
- 要解决的使用场景或问题
- 拟议方案
- 你考虑过的替代方案
- 其他背景信息

<a id="documentation-issues"></a>

### 文档问题
请包含：
- 哪里不清楚或缺失
- 改进建议
- 可参考的示例或资料

<a id="project-policies"></a>

## 项目政策

<a id="sensitive-information"></a>

### 敏感信息
- 切勿提交 API 密钥、令牌或凭据
- 示例中使用占位符
- 对配置文件提供 `.env.example`
- 文档中列出所需环境变量

<a id="code-quality"></a>

### 代码质量
- 示例保持聚焦、易读
- 避免过度设计
- 对非显而易见的逻辑加注释
- 提交前充分测试

<a id="intellectual-property"></a>

### 知识产权
- 原创内容归作者所有
- 本项目采用教育用途许可
- 尊重既有版权
- 需要处请标明出处

<a id="getting-help"></a>

## 获取帮助

- **疑问**：在 GitHub Issues 中发起讨论
- **通用帮助**：先查阅现有文档
- **开发相关**：参考类似示例
- **代码评审**：在 PR 中 @ 维护者

<a id="recognition"></a>

## 致谢与展示

贡献者可能会在以下位置被列出：
- README.md 中的贡献者章节
- GitHub 的 contributors 页面
- 提交历史

<a id="security"></a>

## 安全

贡献示例与文档时，请遵循安全编码实践：

- **切勿在代码中硬编码密钥或 API key** — 请使用环境变量
- **说明安全影响** — 标出潜在风险
- **采用安全默认值** — 默认启用安全相关选项
- **校验输入** — 展示合理的校验与清理
- **附带安全说明** — 文档中写明安全注意事项

安全问题请阅读 [SECURITY.md](SECURITY.md) 中的漏洞报告流程。

<a id="code-of-conduct"></a>

## 行为准则

我们致力于营造友好、包容的社区环境。完整准则见 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

简要说明：
- 相互尊重、包容差异
- 虚心接受反馈
- 帮助他人学习与成长
- 禁止骚扰与歧视
- 发现问题请向维护者报告

所有贡献者应遵守本准则，彼此以善意与尊重相待。

<a id="license"></a>

## 许可

向本项目贡献内容，即表示你同意将贡献以 MIT License 授权。详见 [LICENSE](LICENSE) 文件。

<a id="questions"></a>

## 还有问题？

- 查看 [README](README.md)
- 阅读 [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)
- 浏览现有示例
- 开启 issue 进行讨论

感谢你的贡献！🙏
