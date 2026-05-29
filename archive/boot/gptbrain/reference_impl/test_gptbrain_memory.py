"""
Tests for GPTBrain S1 reference implementation scaffold.

STATUS: IMPLEMENTATION TESTS — NOT CANON
ISSUE: manus-artifacts#12
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import gptbrain_memory as gm


def test_load_claim_ledger_has_seed_claims() -> None:
    claims = gm.load_jsonl(gm.CLAIM_LEDGER)
    assert claims
    assert any(c.get("claim_id") == "S1-CLAIM-2026-0509-0001" for c in claims)


def test_list_claims_by_confidence_c3() -> None:
    claims = gm.list_claims(confidence="C3")
    assert claims
    assert all(c.get("confidence") == "C3" for c in claims)


def test_trace_claim_returns_evidence_and_boundaries() -> None:
    trace = gm.trace_claim("S1-CLAIM-2026-0509-0001")
    assert trace["found"] is True
    assert trace["evidence_refs"]
    assert "forbidden_wording" in trace
    assert trace["missing_evidence"]


def test_challenge_missing_claim_fails_softly() -> None:
    report = gm.challenge_claim("S1-CLAIM-MISSING")
    data = report.to_dict()
    assert data["status"] == "not_found"
    assert data["required_next_steps"]


def test_challenge_seed_claim_preserves_review_boundary() -> None:
    report = gm.challenge_claim("S1-CLAIM-2026-0509-0001")
    data = report.to_dict()
    assert data["status"] in {"needs_review", "pass_with_boundaries"}
    assert any("missing evidence" in finding.lower() or "forbidden wording" in finding.lower() for finding in data["findings"])


def test_diff_jsonl_detects_added_removed_changed(tmp_path: Path) -> None:
    old_path = tmp_path / "old.jsonl"
    new_path = tmp_path / "new.jsonl"

    old_rows = [
        {"artifact_id": "A", "status": "candidate"},
        {"artifact_id": "B", "status": "reviewed"},
    ]
    new_rows = [
        {"artifact_id": "A", "status": "ratified"},
        {"artifact_id": "C", "status": "candidate"},
    ]

    old_path.write_text("\n".join(json.dumps(r) for r in old_rows) + "\n", encoding="utf-8")
    new_path.write_text("\n".join(json.dumps(r) for r in new_rows) + "\n", encoding="utf-8")

    diff = gm.diff_jsonl(old_path, new_path)
    assert diff["added"] == ["C"]
    assert diff["removed"] == ["B"]
    assert diff["changed"] == ["A"]


def test_c0_claim_is_challenged(tmp_path: Path, monkeypatch) -> None:
    ledger = tmp_path / "claims.jsonl"
    row = {
        "claim_id": "S1-CLAIM-C0",
        "claim_text": "Unsupported test claim.",
        "confidence": "C0",
        "claim_class": "raw_model_output",
        "evidence_refs": [],
        "missing_evidence": ["source artifact"],
        "forbidden_wording": ["This is proven."],
        "review_status": "unreviewed",
        "human_root_required": True,
    }
    ledger.write_text(json.dumps(row) + "\n", encoding="utf-8")
    monkeypatch.setattr(gm, "CLAIM_LEDGER", ledger)

    report = gm.challenge_claim("S1-CLAIM-C0").to_dict()
    assert report["status"] == "needs_review"
    assert any("C0" in finding for finding in report["findings"])
    assert report["required_next_steps"]


def test_ratified_canon_drift_is_flagged(tmp_path: Path, monkeypatch) -> None:
    ledger = tmp_path / "claims.jsonl"
    row = {
        "claim_id": "S1-CLAIM-DRIFT",
        "claim_text": "Drift case.",
        "confidence": "C2",
        "claim_class": "ratified_canon",
        "evidence_refs": ["archive/boot/atlasbrain/raw_logs/example.md"],
        "missing_evidence": [],
        "forbidden_wording": [],
        "review_status": "unreviewed",
        "human_root_required": True,
    }
    ledger.write_text(json.dumps(row) + "\n", encoding="utf-8")
    monkeypatch.setattr(gm, "CLAIM_LEDGER", ledger)

    report = gm.challenge_claim("S1-CLAIM-DRIFT").to_dict()
    assert report["status"] == "needs_review"
    assert any("ratified_canon" in finding for finding in report["findings"])


def test_trace_memory_includes_contradiction_links(tmp_path: Path, monkeypatch) -> None:
    memories = tmp_path / "memories.jsonl"
    row = {
        "memory_id": "S1-MEM-TEST-0001",
        "title": "Contradiction memory",
        "type": "claim_note",
        "confidence": "C1",
        "provenance": {"source_type": "manual_entry"},
        "permissions": {"executable": False},
        "review": {"canon_status": "raw"},
        "links": {"contradicts": ["S1-CLAIM-2026-0509-0001"]},
    }
    memories.write_text(json.dumps(row) + "\n", encoding="utf-8")
    monkeypatch.setattr(gm, "MEMORY_OBJECTS", memories)

    trace = gm.trace_memory("S1-MEM-TEST-0001")
    assert trace["found"] is True
    assert trace["links"]["contradicts"] == ["S1-CLAIM-2026-0509-0001"]


def test_cli_trace_requires_target_argument() -> None:
    cmd = [sys.executable, str(Path(gm.__file__).resolve()), "trace"]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    assert proc.returncode != 0
    assert "trace requires --claim-id or --memory-id" in proc.stderr
