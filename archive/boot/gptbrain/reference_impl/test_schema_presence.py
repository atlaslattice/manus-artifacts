"""
Schema/file presence checks for GPTBrain S1 scaffold.

STATUS: IMPLEMENTATION TESTS — NOT CANON
ISSUE: manus-artifacts#12 / manus-artifacts#118

These tests intentionally validate the boring substrate first:
required schemas, seed ledgers, boot packet, and dated state handoff files.
"""

from __future__ import annotations

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
    "schema/S1_DREAM_EXTRACTION_SCHEMA.yaml",
    "schema/S1_DREAM_PROMOTION_GATE_SCHEMA.yaml",
    "CLAIM_LEDGER.seed.jsonl",
    "ARTIFACT_REGISTRY.seed.jsonl",
    "BOOT_PACKET_TEMPLATE.md",
    "CURRENT_STATE_2026-05-09.md",
    "NEXT_ACTIONS_2026-05-09.md",
    "GPT_INSTANCE_STATE_LOG_2026-05-09.md",
]


REQUIRED_SEAT_FILES = [
    "archive/boot/seats/GPTBRAIN_S1_CANONICAL_CANDIDATE_SPEC_2026-05-09.md",
]


def _yaml_parse(path: Path) -> dict:
    if yaml is None:
        pytest.skip("PyYAML unavailable; skipping structured schema parse.")
    parsed = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(parsed, dict), f"Expected mapping at {path}"
    return parsed


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


def test_dream_extraction_schema_carries_authority_scope_and_receipts() -> None:
    schema = (GPTBRAIN_ROOT / "schema/S1_DREAM_EXTRACTION_SCHEMA.yaml").read_text(encoding="utf-8")
    assert "authority_scope" in schema
    assert "receipt_refs" in schema
    assert "receipts:" in schema
    assert "Authority scope is review posture, not execution permission." in schema
    assert "No dream/play extraction may exceed REVIEW_SIGNAL authority_scope by default." in schema


def test_dream_extraction_schema_parses_when_yaml_available() -> None:
    parsed = _yaml_parse(GPTBRAIN_ROOT / "schema/S1_DREAM_EXTRACTION_SCHEMA.yaml")
    assert parsed["schema_id"] == "S1_DREAM_EXTRACTION_SCHEMA"
    assert "authority_scope" in parsed["required_fields"]
    assert "receipt_refs" in parsed["required_fields"]


def test_dream_promotion_gate_schema_enforces_transition_boundaries() -> None:
    schema = (GPTBRAIN_ROOT / "schema/S1_DREAM_PROMOTION_GATE_SCHEMA.yaml").read_text(encoding="utf-8")
    required_terms = [
        "DREAM / PLAY / culture-layer output",
        "transition_ladder",
        "authority_scope",
        "artifact_status",
        "receipt_refs",
        "dream_or_play",
        "max_authority_scope: REVIEW_SIGNAL",
        "No artifact may move toward implementation or canon review without artifact_status and authority_scope.",
        "No dream/play artifact may exceed REVIEW_SIGNAL authority_scope by default.",
        "UNKNOWN and BLOCKED are diagnostic states, not promotion states.",
        "Source references and receipt references are not interchangeable, and neither proves truth by itself.",
    ]
    missing = [term for term in required_terms if term not in schema]
    assert not missing, f"Promotion gate missing expected boundary terms: {missing}"


def test_dream_promotion_gate_schema_parses_and_exposes_diagnostic_states() -> None:
    parsed = _yaml_parse(GPTBRAIN_ROOT / "schema/S1_DREAM_PROMOTION_GATE_SCHEMA.yaml")
    assert parsed["schema_id"] == "S1_DREAM_PROMOTION_GATE_SCHEMA"

    current_state_values = set(parsed["fields"]["current_state"]["values"])
    artifact_status_values = set(parsed["fields"]["artifact_status"]["values"])
    assert {"unknown", "blocked"}.issubset(current_state_values)
    assert {"UNKNOWN", "BLOCKED"}.issubset(artifact_status_values)
    assert parsed["transition_rules"]["unknown"]["diagnostic_only"] is True
    assert parsed["transition_rules"]["blocked"]["diagnostic_only"] is True


def test_generated_output_policy_requires_authority_scope_and_receipts() -> None:
    policy = (GPTBRAIN_ROOT / "GPTBRAIN_GENERATED_OUTPUT_POLICY_2026-05-09.md").read_text(encoding="utf-8")
    assert "authority_scope is set" in policy
    assert "No schema without status." in policy
    assert "No status without authority scope." in policy
    assert "No authority scope without receipts for promotion." in policy
    assert "Receipts do not prove truth by themselves. They make provenance inspectable." in policy
    assert "GPTDream++ proposes." in policy
    assert "Human-root ratifies." in policy


def test_public_safe_translation_table_is_available_in_generated_output_policy() -> None:
    policy = (GPTBRAIN_ROOT / "GPTBRAIN_GENERATED_OUTPUT_POLICY_2026-05-09.md").read_text(encoding="utf-8")
    assert "Public-safe translation table" in policy
    assert "memory palace" in policy
    assert "externalized persistent-context archive" in policy
    assert "dream cycle" in policy
    assert "bounded reflection / consolidation cycle" in policy
    assert "AI remembers" in policy
    assert "archive context was loaded" in policy
