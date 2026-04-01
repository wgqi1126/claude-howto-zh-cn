#!/usr/bin/env python3
"""
上下文用量追踪器（tiktoken 版）——按请求追踪 token 消耗。

将 UserPromptSubmit 用作「发消息前」Hook，将 Stop 用作「响应后」Hook，
以计算每次请求的 token 用量增量。

本版本使用 tiktoken 的 p50k_base 编码，准确度约 90–95%。
需要：pip install tiktoken

无依赖版本见 context-tracker.py。

用法：
    两个 Hook 均配置为同一脚本：
    - UserPromptSubmit：保存当前 token 计数
    - Stop：计算增量并报告用量
"""
import json
import os
import sys
import tempfile

try:
    import tiktoken

    TIKTOKEN_AVAILABLE = True
except ImportError:
    TIKTOKEN_AVAILABLE = False
    print(
        "警告：未安装 tiktoken。请执行：pip install tiktoken",
        file=sys.stderr,
    )

# 配置
CONTEXT_LIMIT = 128000  # Claude 上下文窗口（按你的模型调整）


def get_state_file(session_id: str) -> str:
    """获取用于保存发消息前 token 计数的临时文件路径，按会话隔离。"""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    使用 tiktoken 的 p50k_base 编码统计 token 数。

    与 Claude 实际分词器相比，准确度约 90–95%。
    若未安装 tiktoken，则回退为按字符估算。

    说明：Anthropic 未提供官方离线分词器。
    tiktoken 的 p50k_base 是合理近似，因为 Claude 与 GPT 均使用 BPE（字节对编码）。
    """
    if TIKTOKEN_AVAILABLE:
        enc = tiktoken.get_encoding("p50k_base")
        return len(enc.encode(text))
    else:
        # 无 tiktoken 时回退为按字符估算（约每 4 个字符 1 个 token）
        return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """读取并拼接 transcript 文件中的全部内容。"""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # 从各类消息格式中提取文本
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
    """发消息前 Hook：在请求发出前保存当前 token 计数。"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # 写入临时文件供后续对比
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """响应后 Hook：计算并报告 token 增量。"""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # 读取发消息前的计数
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

    # 输出用量（stderr，避免干扰 Hook 输出）
    method = "tiktoken" if TIKTOKEN_AVAILABLE else "估算"
    print(
        f"上下文（{method}）：约 {current_tokens:,} 个 token "
        f"（已用 {percentage:.1f}%，约剩余 {remaining:,}）",
        file=sys.stderr,
    )
    if delta_tokens > 0:
        print(f"本次请求：约 {delta_tokens:,} 个 token", file=sys.stderr)


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
