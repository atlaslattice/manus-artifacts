"""
Schema/file presence checks for GPTBrain S1 scaffold.

STATUS: IMPLEMENTATION TESTS — NOT CANON
ISSUE: manus-artifacts#12

These tests intentionally validate the boring substrate first:
required schemas, seed ledgers, boot packet, and dated state handoff files.
"""

from __future__ import annotations

import json
from pathlib import Path


GPTBRAIN_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[4]


REQUIRED_GPTBRAIN_FILES = [
    "schema/S1_MEMORY_OBJECT_SCHEMA.yaml",
    "schema/S1_CLAIM_LEDGER_SCHEMA.yaml",
    "schema/S1_ARTIFACT_REGISTRY_SCHEMA.yaml",
    "schema/S1_AUDIT_EVENT_SCHEMA.yaml",
    "CLAIM_LEDGER.seed.jsonl",
    "ARTIFACT_REGISTRY.seed.jsonl",
    "BOOT_PACKET_TEMPLATE.md",
    "CURRENT_STATE_2026-05-09.md",
    "NEXT_ACTIONS_2026-05-09.md",
    "GPT_INSTANCE_STATE_LOG_2026-05-09.md",
    "LATTICE_ORCS_ROUTE_INDEX.seed.jsonl",
    "LATTICE_POSITRON_REVIEW_INDEX.seed.jsonl",
]


REQUIRED_SEAT_FILES = [
    "archive/boot/seats/GPTBRAIN_S1_CANONICAL_CANDIDATE_SPEC_2026-05-09.md",
]


def test_required_gptbrain_files_exist() -> None:
    missing = [rel for rel in REQUIRED_GPTBRAIN_FILES if not (GPTBRAIN_ROOT / rel).exists()]
    assert not missing, f"Missing GPTBrain scaffold files: {missing}"


def test_required_seat_files_exist() -> None:
    missing = [rel for rel in REQUIRED_SEAT_FILES if not (REPO_ROOT / rel).exists()]
    assert not missing, f"Missing required seat files: {missing}"


def test_boot_packet_points_to_verified_dated_snapshots() -> None:
    boot_packet = (GPTBRAIN_ROOT / "BOOT_PACKET_TEMPLATE.md").read_text(encoding="utf-8")
    assert "CURRENT_STATE_2026-05-09.md" in boot_packet
    assert "NEXT_ACTIONS_2026-05-09.md" in boot_packet
    assert "Do not claim the bare aliases exist unless verified" in boot_packet


def test_canonical_candidate_integrates_variant_e() -> None:
    candidate_path = REPO_ROOT / "archive/boot/seats/GPTBRAIN_S1_CANONICAL_CANDIDATE_SPEC_2026-05-09.md"
    candidate = candidate_path.read_text(encoding="utf-8")
    assert "Variant E = continuity / human-intent dashboard layer" in candidate
    assert "Layer 7 — Continuity / Human-Intent Dashboard" in candidate
    assert "Continuity is visibility, not authority." in candidate
    assert "Variant E remains pending or missing" not in candidate


def test_lattice_routes_have_positron_counterparts() -> None:
    route_rows = [
        json.loads(line)
        for line in (GPTBRAIN_ROOT / "LATTICE_ORCS_ROUTE_INDEX.seed.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    positron_rows = [
        json.loads(line)
        for line in (GPTBRAIN_ROOT / "LATTICE_POSITRON_REVIEW_INDEX.seed.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    positron_route_ids = {row["route_artifact_id"] for row in positron_rows}

    missing = [row["artifact_id"] for row in route_rows if row["artifact_id"] not in positron_route_ids]
    assert not missing, f"Missing positron review entries for routes: {missing}"
