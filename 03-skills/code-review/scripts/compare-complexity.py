#!/usr/bin/env python3
"""
比较代码变更前后的圈复杂度。
用于判断重构是否真正简化了代码结构。
"""

import re
import sys


class ComplexityAnalyzer:
    """分析代码复杂度指标。"""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split("\n")

    def calculate_cyclomatic_complexity(self) -> int:
        """
        使用 McCabe 方法计算圈复杂度。
        统计决策点：if、elif、else、for、while、except、and、or
        """
        complexity = 1  # 基础复杂度

        # 统计决策点
        decision_patterns = [
            r"\bif\b",
            r"\belif\b",
            r"\bfor\b",
            r"\bwhile\b",
            r"\bexcept\b",
            r"\band\b(?!$)",
            r"\bor\b(?!$)",
        ]

        for pattern in decision_patterns:
            matches = re.findall(pattern, self.code)
            complexity += len(matches)

        return complexity

    def calculate_cognitive_complexity(self) -> int:
        """
        计算认知复杂度——代码有多难理解？
        基于嵌套深度与控制流。
        """
        cognitive = 0
        nesting_depth = 0

        for line in self.lines:
            # 跟踪嵌套深度
            if re.search(r"^\s*(if|for|while|def|class|try)\b", line):
                nesting_depth += 1
                cognitive += nesting_depth
            elif re.search(r"^\s*(elif|else|except|finally)\b", line):
                cognitive += nesting_depth

            # 取消缩进时降低嵌套
            if line and not line[0].isspace():
                nesting_depth = 0

        return cognitive

    def calculate_maintainability_index(self) -> float:
        """
        可维护性指数范围为 0–100。
        > 85：优秀
        > 65：良好
        > 50：一般
        < 50：较差
        """
        lines = len(self.lines)
        cyclomatic = self.calculate_cyclomatic_complexity()
        cognitive = self.calculate_cognitive_complexity()

        # 简化的 MI 计算
        mi = (
            171
            - 5.2 * (cyclomatic / lines)
            - 0.23 * (cognitive)
            - 16.2 * (lines / 1000)
        )

        return max(0, min(100, mi))

    def get_complexity_report(self) -> dict:
        """生成完整的复杂度报告。"""
        return {
            "cyclomatic_complexity": self.calculate_cyclomatic_complexity(),
            "cognitive_complexity": self.calculate_cognitive_complexity(),
            "maintainability_index": round(self.calculate_maintainability_index(), 2),
            "lines_of_code": len(self.lines),
            "avg_line_length": round(
                sum(len(l) for l in self.lines) / len(self.lines), 2
            )
            if self.lines
            else 0,
        }


def compare_files(before_file: str, after_file: str) -> None:
    """比较两个代码版本的复杂度指标。"""

    with open(before_file) as f:
        before_code = f.read()

    with open(after_file) as f:
        after_code = f.read()

    before_analyzer = ComplexityAnalyzer(before_code)
    after_analyzer = ComplexityAnalyzer(after_code)

    before_metrics = before_analyzer.get_complexity_report()
    after_metrics = after_analyzer.get_complexity_report()

    print("=" * 60)
    print("代码复杂度对比")
    print("=" * 60)

    print("\n变更前：")
    print(f"  圈复杂度：                {before_metrics['cyclomatic_complexity']}")
    print(f"  认知复杂度：              {before_metrics['cognitive_complexity']}")
    print(f"  可维护性指数：            {before_metrics['maintainability_index']}")
    print(f"  代码行数：                {before_metrics['lines_of_code']}")
    print(f"  平均行长度：              {before_metrics['avg_line_length']}")

    print("\n变更后：")
    print(f"  圈复杂度：                {after_metrics['cyclomatic_complexity']}")
    print(f"  认知复杂度：              {after_metrics['cognitive_complexity']}")
    print(f"  可维护性指数：            {after_metrics['maintainability_index']}")
    print(f"  代码行数：                {after_metrics['lines_of_code']}")
    print(f"  平均行长度：              {after_metrics['avg_line_length']}")

    print("\n变化：")
    cyclomatic_change = (
        after_metrics["cyclomatic_complexity"] - before_metrics["cyclomatic_complexity"]
    )
    cognitive_change = (
        after_metrics["cognitive_complexity"] - before_metrics["cognitive_complexity"]
    )
    mi_change = (
        after_metrics["maintainability_index"] - before_metrics["maintainability_index"]
    )
    loc_change = after_metrics["lines_of_code"] - before_metrics["lines_of_code"]

    print(f"  圈复杂度：                {cyclomatic_change:+d}")
    print(f"  认知复杂度：              {cognitive_change:+d}")
    print(f"  可维护性指数：            {mi_change:+.2f}")
    print(f"  代码行数：                {loc_change:+d}")

    print("\n评估：")
    if mi_change > 0:
        print("  ✅ 代码更易维护")
    elif mi_change < 0:
        print("  ⚠️  代码更难维护")
    else:
        print("  ➡️  可维护性无变化")

    if cyclomatic_change < 0:
        print("  ✅ 复杂度降低")
    elif cyclomatic_change > 0:
        print("  ⚠️  复杂度上升")
    else:
        print("  ➡️  复杂度无变化")

    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法：python compare-complexity.py <before_file> <after_file>")
        sys.exit(1)

    compare_files(sys.argv[1], sys.argv[2])
