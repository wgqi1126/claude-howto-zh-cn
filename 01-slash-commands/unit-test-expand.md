---
name: Expand Unit Tests
description: 通过针对未覆盖分支与边界情况补充测试，提升测试覆盖率
tags: testing, coverage, unit-tests
---

<a id="expand-unit-tests"></a>

# 扩展单元测试

在现有单元测试基础上进行扩展，并适配项目使用的测试框架：

1. **分析覆盖率**：运行覆盖率报告，找出未覆盖的分支、边界情况以及覆盖率偏低的区域
2. **找出缺口**：审阅代码中的逻辑分支、错误路径、边界条件以及 null/空输入等情况
3. **编写测试**，使用项目采用的框架：
   - Jest/Vitest/Mocha（JavaScript/TypeScript）
   - pytest/unittest（Python）
   - Go testing/testify（Go）
   - Rust test framework（Rust）
4. **覆盖具体场景**：
   - 错误处理与异常
   - 边界值（最小/最大、空、null）
   - 边界情况与极端情况
   - 状态转换与副作用
5. **验证改进**：再次运行覆盖率，确认有可量化的提升

仅输出新的测试代码块。遵循既有测试风格与命名约定。
