#!/usr/bin/env python3
import re
import sys


def analyze_code_metrics(code):
    """对代码进行常见指标分析。"""

    # 统计函数
    functions = len(re.findall(r"^def\s+\w+", code, re.MULTILINE))

    # 统计类
    classes = len(re.findall(r"^class\s+\w+", code, re.MULTILINE))

    # 平均行长度
    lines = code.split("\n")
    avg_length = sum(len(l) for l in lines) / len(lines) if lines else 0

    # 估算复杂度
    complexity = len(re.findall(r"\b(if|elif|else|for|while|and|or)\b", code))

    return {
        "functions": functions,
        "classes": classes,
        "avg_line_length": avg_length,
        "complexity_score": complexity,
    }


_METRIC_LABELS = {
    "functions": "函数数量",
    "classes": "类数量",
    "avg_line_length": "平均行长度",
    "complexity_score": "复杂度得分",
}

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        code = f.read()
    metrics = analyze_code_metrics(code)
    for key, value in metrics.items():
        label = _METRIC_LABELS.get(key, key)
        print(f"{label}: {value:.2f}")
