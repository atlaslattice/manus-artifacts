"""
Candidate tests for Atlas / ORCS crosswalk index fixtures.

STATUS: CANDIDATE TESTS — NOT CANON — NON-DEPLOYABLE
SCOPE: fixtures/crosswalk_index.* and schemas/crosswalk_index.schema.json only
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "crosswalk_index.schema.json"
VALID_FIXTURE = ROOT / "fixtures" / "crosswalk_index.valid.candidate.json"
INVALID_RATIFIED_FIXTURE = ROOT / "fixtures" / "crosswalk_index.invalid.ratified_pending_signature.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def basic_required_fields(record: dict) -> None:
    required = {
        "schema_id",
        "status",
        "canon_status",
        "deployment_status",
        "authority_status",
        "crosswalk_id",
        "source_ref",
        "promotion_target",
        "evidence_set",
        "human_root_review_required",
    }
    missing = required - set(record)
    assert not missing, f"missing required fields: {sorted(missing)}"


def enforce_ratified_requires_completed_signature(record: dict) -> None:
    if record.get("canon_status") != "RATIFIED_CANON":
        return
    signature = record.get("human_root_signature") or {}
    assert signature.get("status") == "COMPLETE"
    assert signature.get("signed_by")
    assert signature.get("signed_at")
    assert record.get("canon_promotion_receipt") is not None


def test_schema_file_exists_and_declares_candidate_status_boundary() -> None:
    schema = load_json(SCHEMA_PATH)
    assert schema["title"] == "Atlas / ORCS Crosswalk Index"
    assert "CANDIDATE ONLY" in schema["description"]
    assert "NOT CANON" in schema["description"]
    assert "NON-DEPLOYABLE" in schema["description"]


def test_valid_candidate_fixture_shape() -> None:
    record = load_json(VALID_FIXTURE)
    basic_required_fields(record)
    assert record["schema_id"] == "crosswalk_index.v0.1"
    assert record["canon_status"] == "NOT_CANON"
    assert record["deployment_status"] == "NON_DEPLOYABLE"
    assert record["authority_status"] == "FORMALIZATION_ONLY"
    assert record["human_root_review_required"] is True
    assert record["source_ref"]["raw_export_status"] == "RAW_NOT_EXPORTED"
    assert record["evidence_set"]["notation"] == "E_t^{q,*}"
    assert record["evidence_set"]["subset_of"] == "E(S_t)"
    enforce_ratified_requires_completed_signature(record)


def test_invalid_ratified_fixture_fails_local_guardrail() -> None:
    record = load_json(INVALID_RATIFIED_FIXTURE)
    basic_required_fields(record)
    assert record["canon_status"] == "RATIFIED_CANON"
    try:
        enforce_ratified_requires_completed_signature(record)
    except AssertionError:
        return
    raise AssertionError("invalid ratified fixture unexpectedly passed human-root signature guardrail")


def test_optional_jsonschema_validation_when_available() -> None:
    try:
        import jsonschema  # type: ignore
    except Exception:
        return

    schema = load_json(SCHEMA_PATH)
    valid = load_json(VALID_FIXTURE)
    invalid = load_json(INVALID_RATIFIED_FIXTURE)

    jsonschema.Draft202012Validator(schema).validate(valid)

    try:
        jsonschema.Draft202012Validator(schema).validate(invalid)
    except jsonschema.ValidationError:
        return
    raise AssertionError("invalid ratified fixture unexpectedly passed JSON Schema validation")
