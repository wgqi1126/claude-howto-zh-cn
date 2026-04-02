"""上游仓库监听工作流的辅助脚本。"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import time
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class UpstreamState:
    """持久化到仓库中的上游同步状态。"""

    upstream_repo: str
    upstream_branch: str
    last_seen_upstream_sha: str = ""
    last_synced_upstream_sha: str = ""
    last_alerted_upstream_sha: str = ""
    sync_status: str = "idle"


def default_state(upstream_repo: str, upstream_branch: str) -> UpstreamState:
    """创建默认状态。"""

    return UpstreamState(
        upstream_repo=upstream_repo,
        upstream_branch=upstream_branch,
    )


def load_state(state_file: Path, upstream_repo: str, upstream_branch: str) -> UpstreamState:
    """读取状态文件, 不存在时返回默认状态。"""

    if not state_file.exists():
        return default_state(upstream_repo, upstream_branch)

    with state_file.open(encoding="utf-8") as fh:
        data = json.load(fh)

    return UpstreamState(
        upstream_repo=data.get("upstream_repo", upstream_repo),
        upstream_branch=data.get("upstream_branch", upstream_branch),
        last_seen_upstream_sha=data.get("last_seen_upstream_sha", ""),
        last_synced_upstream_sha=data.get("last_synced_upstream_sha", ""),
        last_alerted_upstream_sha=data.get("last_alerted_upstream_sha", ""),
        sync_status=data.get("sync_status", "idle"),
    )


def save_state(state_file: Path, state: UpstreamState) -> None:
    """保存状态文件。"""

    state_file.parent.mkdir(parents=True, exist_ok=True)
    with state_file.open("w", encoding="utf-8") as fh:
        json.dump(asdict(state), fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def write_github_outputs(output_file: str | None, outputs: dict[str, str]) -> None:
    """向 GitHub Actions 输出文件写入键值。"""

    if not output_file:
        return

    with Path(output_file).open("a", encoding="utf-8") as fh:
        for key, value in outputs.items():
            fh.write(f"{key}={value}\n")


def ensure_state_file(state_file: Path, upstream_repo: str, upstream_branch: str) -> None:
    """确保状态文件存在。"""

    if state_file.exists():
        return

    save_state(state_file, default_state(upstream_repo, upstream_branch))


def inspect_state_file(state_file: Path, upstream_repo: str, upstream_branch: str) -> dict[str, str]:
    """读取当前状态并转换为 workflow 输出。"""

    state = load_state(state_file, upstream_repo, upstream_branch)
    return {
        "last_seen_sha": state.last_seen_upstream_sha,
        "last_synced_sha": state.last_synced_upstream_sha,
        "last_alerted_sha": state.last_alerted_upstream_sha,
        "sync_status": state.sync_status,
    }


def update_state_file(
    state_file: Path,
    latest_sha: str,
    upstream_repo: str,
    upstream_branch: str,
) -> dict[str, str]:
    """根据最新上游提交更新状态文件。"""

    state = load_state(state_file, upstream_repo, upstream_branch)

    previous_seen = state.last_seen_upstream_sha
    previous_synced = state.last_synced_upstream_sha
    previous_alerted = state.last_alerted_upstream_sha

    has_new_upstream = bool(previous_seen) and bool(latest_sha) and latest_sha != previous_seen
    needs_alert = has_new_upstream and latest_sha not in {
        previous_alerted,
        previous_synced,
    }

    state.upstream_repo = upstream_repo
    state.upstream_branch = upstream_branch
    state.last_seen_upstream_sha = latest_sha
    state.sync_status = "pending" if previous_synced and latest_sha != previous_synced else "idle"

    save_state(state_file, state)

    return {
        "has_new_upstream": "true" if has_new_upstream else "false",
        "needs_alert": "true" if needs_alert else "false",
        "previous_seen_sha": previous_seen,
        "previous_synced_sha": previous_synced,
        "previous_alerted_sha": previous_alerted,
    }


def mark_alerted_state(
    state_file: Path, latest_sha: str, upstream_repo: str, upstream_branch: str
) -> None:
    """在钉钉消息发送成功后记录已告警的 SHA。"""

    state = load_state(state_file, upstream_repo, upstream_branch)
    state.last_alerted_upstream_sha = latest_sha
    save_state(state_file, state)


def build_signed_dingtalk_webhook(webhook: str, secret: str) -> str:
    """为钉钉机器人 URL 追加签名参数。"""

    if not secret:
        return webhook

    timestamp = str(round(time.time() * 1000))
    sign_text = f"{timestamp}\n{secret}".encode()
    signature = base64.b64encode(
        hmac.new(secret.encode(), sign_text, hashlib.sha256).digest()
    )
    encoded_signature = urllib.parse.quote_plus(signature)
    separator = "&" if "?" in webhook else "?"
    return f"{webhook}{separator}timestamp={timestamp}&sign={encoded_signature}"


def send_dingtalk_alert(
    latest_sha: str,
    last_synced_sha: str,
    webhook: str,
    secret: str,
    upstream_repo: str,
    upstream_branch: str,
) -> None:
    """发送钉钉机器人文本告警。"""

    signed_webhook = build_signed_dingtalk_webhook(webhook, secret)
    lines = [
        "检测到上游仓库有新提交",
        f"仓库: {upstream_repo}",
        f"分支: {upstream_branch}",
        f"最新 SHA: {latest_sha}",
        f"提交链接: https://github.com/{upstream_repo}/commit/{latest_sha}",
    ]

    if last_synced_sha:
        lines.append(f"已同步 SHA: {last_synced_sha}")
        lines.append(
            f"差异范围: https://github.com/{upstream_repo}/compare/{last_synced_sha}...{latest_sha}"
        )
    else:
        lines.append("已同步 SHA: 尚未初始化")

    payload = {
        "msgtype": "text",
        "text": {
            "content": "\n".join(lines),
        },
    }

    request = urllib.request.Request(
        signed_webhook,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=15) as response:
        body = response.read().decode("utf-8")

    result = json.loads(body)
    if result.get("errcode") != 0:
        raise SystemExit(f"DingTalk notification failed: {body}")


def build_parser() -> argparse.ArgumentParser:
    """构建命令行参数。"""

    parser = argparse.ArgumentParser(description="上游监听工作流辅助脚本")
    subparsers = parser.add_subparsers(dest="command", required=True)

    shared = argparse.ArgumentParser(add_help=False)
    shared.add_argument("--state-file", required=True)
    shared.add_argument("--upstream-repo", required=True)
    shared.add_argument("--upstream-branch", required=True)

    ensure_parser = subparsers.add_parser("ensure-state", parents=[shared])
    ensure_parser.set_defaults(handler=handle_ensure_state)

    inspect_parser = subparsers.add_parser("inspect", parents=[shared])
    inspect_parser.add_argument("--github-output", default=os.getenv("GITHUB_OUTPUT", ""))
    inspect_parser.set_defaults(handler=handle_inspect)

    update_parser = subparsers.add_parser("update", parents=[shared])
    update_parser.add_argument("--latest-sha", required=True)
    update_parser.add_argument("--github-output", default=os.getenv("GITHUB_OUTPUT", ""))
    update_parser.set_defaults(handler=handle_update)

    mark_alerted_parser = subparsers.add_parser("mark-alerted", parents=[shared])
    mark_alerted_parser.add_argument("--latest-sha", required=True)
    mark_alerted_parser.set_defaults(handler=handle_mark_alerted)

    notify_parser = subparsers.add_parser("notify-dingtalk")
    notify_parser.add_argument("--latest-sha", required=True)
    notify_parser.add_argument("--last-synced-sha", default="")
    notify_parser.add_argument("--webhook", required=True)
    notify_parser.add_argument("--secret", default="")
    notify_parser.add_argument("--upstream-repo", required=True)
    notify_parser.add_argument("--upstream-branch", required=True)
    notify_parser.set_defaults(handler=handle_notify_dingtalk)

    return parser


def handle_ensure_state(args: argparse.Namespace) -> None:
    """处理 ensure-state 子命令。"""

    ensure_state_file(Path(args.state_file), args.upstream_repo, args.upstream_branch)


def handle_inspect(args: argparse.Namespace) -> None:
    """处理 inspect 子命令。"""

    outputs = inspect_state_file(
        Path(args.state_file),
        args.upstream_repo,
        args.upstream_branch,
    )
    write_github_outputs(args.github_output, outputs)


def handle_update(args: argparse.Namespace) -> None:
    """处理 update 子命令。"""

    outputs = update_state_file(
        Path(args.state_file),
        args.latest_sha,
        args.upstream_repo,
        args.upstream_branch,
    )
    write_github_outputs(args.github_output, outputs)


def handle_mark_alerted(args: argparse.Namespace) -> None:
    """处理 mark-alerted 子命令。"""

    mark_alerted_state(
        Path(args.state_file),
        args.latest_sha,
        args.upstream_repo,
        args.upstream_branch,
    )


def handle_notify_dingtalk(args: argparse.Namespace) -> None:
    """处理 notify-dingtalk 子命令。"""

    send_dingtalk_alert(
        latest_sha=args.latest_sha,
        last_synced_sha=args.last_synced_sha,
        webhook=args.webhook,
        secret=args.secret,
        upstream_repo=args.upstream_repo,
        upstream_branch=args.upstream_branch,
    )


def main() -> None:
    """CLI 入口。"""

    parser = build_parser()
    args = parser.parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
