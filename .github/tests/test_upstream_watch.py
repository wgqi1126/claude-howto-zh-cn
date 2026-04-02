"""针对上游监听脚本的测试。"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".github" / "scripts"))

from upstream_watch import (  # noqa: E402
    ensure_state_file,
    load_state,
    mark_alerted_state,
    update_state_file,
)


def test_initial_update_does_not_alert(tmp_path: Path) -> None:
    """首次记录上游 SHA 时不应触发告警。"""

    state_file = tmp_path / "upstream-state.json"
    ensure_state_file(state_file, "owner/repo", "main")

    outputs = update_state_file(
        state_file=state_file,
        latest_sha="sha-001",
        upstream_repo="owner/repo",
        upstream_branch="main",
    )
    state = load_state(state_file, "owner/repo", "main")

    assert outputs["has_new_upstream"] == "false"
    assert outputs["needs_alert"] == "false"
    assert state.last_seen_upstream_sha == "sha-001"
    assert state.sync_status == "idle"


def test_new_upstream_sha_marks_pending_and_alerts(tmp_path: Path) -> None:
    """已有基线时, 上游新提交应进入 pending 并触发告警。"""

    state_file = tmp_path / "upstream-state.json"
    state_file.write_text(
        """{
  "upstream_repo": "owner/repo",
  "upstream_branch": "main",
  "last_seen_upstream_sha": "sha-001",
  "last_synced_upstream_sha": "sha-001",
  "last_alerted_upstream_sha": "",
  "sync_status": "idle"
}
""",
        encoding="utf-8",
    )

    outputs = update_state_file(
        state_file=state_file,
        latest_sha="sha-002",
        upstream_repo="owner/repo",
        upstream_branch="main",
    )
    state = load_state(state_file, "owner/repo", "main")

    assert outputs["has_new_upstream"] == "true"
    assert outputs["needs_alert"] == "true"
    assert outputs["previous_synced_sha"] == "sha-001"
    assert state.last_seen_upstream_sha == "sha-002"
    assert state.sync_status == "pending"


def test_mark_alerted_updates_state(tmp_path: Path) -> None:
    """发送成功后应记录已告警的 SHA。"""

    state_file = tmp_path / "upstream-state.json"
    ensure_state_file(state_file, "owner/repo", "main")

    mark_alerted_state(
        state_file=state_file,
        latest_sha="sha-123",
        upstream_repo="owner/repo",
        upstream_branch="main",
    )

    state = load_state(state_file, "owner/repo", "main")
    assert state.last_alerted_upstream_sha == "sha-123"
