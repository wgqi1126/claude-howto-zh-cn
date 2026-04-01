#!/usr/bin/env python3
"""
上下文用量追踪器 — 按请求统计 token 消耗。

将 UserPromptSubmit 作为「消息前」钩子、Stop 作为「响应后」钩子，
计算每次请求的 token 用量增量。

本版本使用按字符估算（无依赖）。
若需更高精度，见 context-tracker-tiktoken.py。

用法：
    将两个钩子都配置为同一脚本：
    - UserPromptSubmit：保存当前 token 计数
    - Stop：计算增量并报告用量
"""
import json
import os
import sys
import tempfile

# 配置
CONTEXT_LIMIT = 128000  # Claude 上下文窗口（按所用模型调整）


def get_state_file(session_id: str) -> str:
    """获取用于保存消息前 token 计数的临时文件路径，按会话隔离。"""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens_estimate(text: str) -> int:
    """
    使用按字符近似估算 token 数量。

    按约每 4 个字符对应 1 个 token，英文文本约 80–90% 准确度。
    对代码与非英文文本准确度较低。
    """
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """读取 transcript 文件并拼接全部内容。"""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # 从多种消息格式中提取文本内容
                if "message" in entry:
                    msg = entry["message"]
                    if isinstance(msg.get("content"), str):
                        content.append(msg["content"])
                    elif isinstance(msg.get("content"), list):
                        for block in msg["content"]:
                            if isinstance(block, dict) and block.get("type") == "text":
                                content.append(block.get("text", ""))
            except json.JSONDecodeError:
                continue

    return "\n".join(content)


def handle_user_prompt_submit(data: dict) -> None:
    """消息前钩子：在请求前保存当前 token 计数。"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens_estimate(transcript_content)

    # 写入临时文件，供后续对比
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """响应后钩子：计算并报告 token 增量。"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens_estimate(transcript_content)

    # 读取消息前计数
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # 计算增量
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # 报告用量（stderr，避免干扰钩子标准输出）
    print(
        f"上下文（估算）：约 {current_tokens:,} tokens "
        f"（已用 {percentage:.1f}%，约剩余 {remaining:,}）",
        file=sys.stderr,
    )
    if delta_tokens > 0:
        print(f"本次请求：约 {delta_tokens:,} tokens", file=sys.stderr)


def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name", "")

    if event == "UserPromptSubmit":
        handle_user_prompt_submit(data)
    elif event == "Stop":
        handle_stop(data)

    sys.exit(0)


if __name__ == "__main__":
    main()
