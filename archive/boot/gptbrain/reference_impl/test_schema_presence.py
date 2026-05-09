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

import pytest

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


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
    "AGENT_DNA_SCHEMA_DRAFT.yaml",
    "AGENT_DNA_SEED_INDEX.seed.jsonl",
    "AGENT_DNA_LIFECYCLE_SEED_PROFILES.seed.jsonl",
    "CURRENT_STATE_2026-05-09.md",
    "NEXT_ACTIONS_2026-05-09.md",
    "GPT_INSTANCE_STATE_LOG_2026-05-09.md",
]


REQUIRED_SEAT_FILES = [
    "archive/boot/seats/GPTBRAIN_S1_CANONICAL_CANDIDATE_SPEC_2026-05-09.md",
    "DECENTRALIZED_AGENT_CONSTITUTION_AND_BOOT_PROTOCOL_SPEC.md",
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


def test_agent_dna_schema_includes_constitutional_fields() -> None:
    schema = (GPTBRAIN_ROOT / "AGENT_DNA_SCHEMA_DRAFT.yaml").read_text(encoding="utf-8")
    if yaml is None:
        pytest.skip("PyYAML unavailable; skipping structured schema parse.")

    parsed = yaml.safe_load(schema)
    required_fields = set(parsed.get("required_fields", []))
    field_defs = set(parsed.get("fields", {}).keys())
    for field in {"boot_contract", "simulation_origin", "constitutional_status", "failure_ledger_ref"}:
        assert field in required_fields
        assert field in field_defs


def test_lifecycle_seed_profiles_cover_multiple_states_and_are_examples() -> None:
    lifecycle_path = GPTBRAIN_ROOT / "AGENT_DNA_LIFECYCLE_SEED_PROFILES.seed.jsonl"
    rows = [
        json.loads(line)
        for line in lifecycle_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert len(rows) >= 3
    states = {row["constitutional_status"]["state"] for row in rows}
    assert {"proposed", "reviewed", "bounded-operational"}.issubset(states)
    assert all(row.get("example_only") is True for row in rows)
