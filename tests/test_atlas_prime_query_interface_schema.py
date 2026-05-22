"""
Candidate tests for Atlas Prime JSON-RPC query interface fixtures.

STATUS: CANDIDATE TESTS — NOT CANON — NON-DEPLOYABLE
SCOPE: schemas/atlas_prime_query_interface.schema.json and fixtures/atlas_prime_query.* only
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "atlas_prime_query_interface.schema.json"
FIXTURE_PATHS = [
    ROOT / "fixtures" / "atlas_prime_query.define.valid.json",
    ROOT / "fixtures" / "atlas_prime_query.check_invariant.valid.json",
    ROOT / "fixtures" / "atlas_prime_query.resolve_ref.valid.json",
    ROOT / "fixtures" / "atlas_prime_query.tag_claim.valid.json",
]
EXPECTED_METHODS = {"DEFINE", "CHECK_INVARIANT", "RESOLVE_REF", "TAG_CLAIM"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_schema_declares_candidate_non_deployable_boundary() -> None:
    schema = load_json(SCHEMA_PATH)
    assert schema["title"] == "Atlas Prime Query Interface"
    description = schema["description"]
    assert "CANDIDATE ONLY" in description
    assert "NOT CANON" in description
    assert "NON-DEPLOYABLE" in description
    assert "does not create truth" in description
    assert "ratify" in description
    assert "execute" in description


def test_all_required_methods_have_valid_fixtures() -> None:
    methods = {load_json(path)["method"] for path in FIXTURE_PATHS}
    assert methods == EXPECTED_METHODS


def test_query_fixtures_preserve_boundary() -> None:
    for path in FIXTURE_PATHS:
        record = load_json(path)
        assert record["jsonrpc"] == "2.0"
        assert record["method"] in EXPECTED_METHODS
        params = record["params"]
        boundary = params["boundary"]
        assert boundary["canon"] is False
        assert boundary["deployment"] is False
        assert boundary["authority"] == "query_only"
        assert boundary["human_root_final_authority"] is True


def test_source_ref_fixtures_preserve_raw_export_status_when_present() -> None:
    for path in FIXTURE_PATHS:
        params = load_json(path)["params"]
        source_ref = params.get("source_ref") or params.get("ref")
        if source_ref is None:
            continue
        assert source_ref["raw_export_status"] in {
            "RAW_EXPORTED",
            "RAW_NOT_EXPORTED",
            "RAW_PARTIAL",
            "RAW_UNAVAILABLE",
            "UNKNOWN",
        }


def test_optional_jsonschema_validation_when_available() -> None:
    try:
        import jsonschema  # type: ignore
    except Exception:
        return

    schema = load_json(SCHEMA_PATH)
    validator = jsonschema.Draft202012Validator(schema)
    for path in FIXTURE_PATHS:
        validator.validate(load_json(path))
