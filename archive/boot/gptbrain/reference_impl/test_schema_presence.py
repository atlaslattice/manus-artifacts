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
REQUIRED_LIFECYCLE_STATES = {"proposed", "reviewed", "bounded-operational"}


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
    required_field_names = set(parsed.get("required_fields", parsed.get("required", [])))
    field_defs = set(parsed.get("fields", {}).keys())
    expected_nested_required = {
        "boot_contract": {
            "startup_checks",
            "required_ledgers",
            "invariant_assertions",
            "allowed_task_classes",
            "required_reviewers",
        },
        "simulation_origin": {
            "derived_from_dream_logs",
            "extracted_by",
            "confidence_score",
            "governance_review_complete",
        },
        "constitutional_status": {"state", "approved_by", "review_cycle_days"},
        "failure_ledger_ref": {"entries", "risk_score", "last_reviewed"},
    }
    for field in expected_nested_required:
        assert field in required_field_names and field in field_defs, (
            f"{field} must be required and defined in schema fields."
        )
        field_schema = parsed["fields"][field]
        assert expected_nested_required[field].issubset(set(field_schema.get("required", [])))
        assert expected_nested_required[field].issubset(set(field_schema.get("properties", {}).keys()))


def test_schema_invariants_capture_authority_boundaries_and_precedence() -> None:
    schema = (GPTBRAIN_ROOT / "AGENT_DNA_SCHEMA_DRAFT.yaml").read_text(encoding="utf-8")
    if yaml is None:
        pytest.skip("PyYAML unavailable; skipping structured schema parse.")

    parsed = yaml.safe_load(schema)
    invariants = set(parsed.get("invariants", []))
    assert "Identity metadata is not execution authority." in invariants
    assert "Replayability does not imply canon authority." in invariants
    assert "Dream/play traits do not authorize work output or deployment." in invariants
    assert "Governance precedence is strict: governance > capability > role > lineage > temperament." in invariants


def test_can_execute_seed_records_still_require_high_impact_approval() -> None:
    seed_path = GPTBRAIN_ROOT / "AGENT_DNA_SEED_INDEX.seed.jsonl"
    rows = [json.loads(line) for line in seed_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    executable_rows = [row for row in rows if row.get("governance", {}).get("can_execute") is True]
    assert executable_rows, "Expected at least one executable seed profile for gate checks."

    for row in executable_rows:
        governance = row["governance"]
        assert governance.get("human_root_required") is True
        assert "high_impact_action" in governance.get("requires_approval_for", [])


def test_lifecycle_seed_profiles_cover_multiple_states_and_are_examples() -> None:
    lifecycle_path = GPTBRAIN_ROOT / "AGENT_DNA_LIFECYCLE_SEED_PROFILES.seed.jsonl"
    rows = [
        json.loads(line)
        for line in lifecycle_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert len(rows) >= len(REQUIRED_LIFECYCLE_STATES)
    states = {row["constitutional_status"]["state"] for row in rows}
    assert REQUIRED_LIFECYCLE_STATES.issubset(states)
    assert all(row.get("example_only") is True for row in rows)
    assert all(row.get("example_profile_only") is True for row in rows)
    assert all(row.get("proposal_status") == "proposal_not_deployed" for row in rows)
    assert all(row.get("not_canon") is True and row.get("not_authority") is True for row in rows)

    for row in rows:
        status = row["constitutional_status"]
        if status["state"] == "proposed":
            assert status["approved_by"] == []
        else:
            assert row.get("example_hypothetical_state") is True
            assert status["approved_by"] == ["EXAMPLE_ONLY_NOT_ACTUAL_APPROVAL"]


def test_dream_derived_examples_do_not_claim_real_approval() -> None:
    lifecycle_path = GPTBRAIN_ROOT / "AGENT_DNA_LIFECYCLE_SEED_PROFILES.seed.jsonl"
    rows = [
        json.loads(line)
        for line in lifecycle_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    dream_derived_rows = [row for row in rows if row.get("simulation_origin", {}).get("derived_from_dream_logs")]
    assert dream_derived_rows
    for row in dream_derived_rows:
        approvals = row["constitutional_status"].get("approved_by", [])
        assert "Human Root Review" not in approvals
