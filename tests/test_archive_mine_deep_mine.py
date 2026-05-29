"""
Candidate tests for Archive Mine / Deep Mine ingestion lane.

STATUS: CANDIDATE TESTS — NOT CANON — NOT DEPLOYABLE
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _load_json(path: Path) -> dict:
    return json.loads(_read(path))


def test_archive_mine_protocol_exists_with_boundaries() -> None:
    path = ROOT / "archive/spec/archive-mine/ARCHIVE_MINE_DEEP_MINE_PROTOCOL_v0.1.md"
    text = _read(path)
    assert "NOT CANON" in text
    assert "NOT DEPLOYABLE" in text
    assert "Contaminated artifacts must be preserved" in text
    assert "blocked from authority" in text


def test_archive_mine_schema_bundle_exists() -> None:
    schema_dir = ROOT / "schemas/archive_mine/v0_1"
    expected = {
        "source-inventory.schema.yaml",
        "artifact-status.schema.yaml",
        "candidate-delta-packet.schema.yaml",
        "canon-recoverability-package.schema.yaml",
    }
    observed = {p.name for p in schema_dir.glob("*.yaml")}
    assert observed == expected


def test_source_inventory_fixture_is_searchable_and_not_auto_trusted() -> None:
    data = _load_json(ROOT / "fixtures/archive_mine/source_inventory.valid.candidate.json")
    assert data["default_trust_status"] == "candidate"
    assert all(src["searchable"] is True for src in data["sources"])
    assert any(src["surface"] == "notion" for src in data["sources"])
    assert any(src["surface"] == "drive" for src in data["sources"])
    assert any(src["surface"] == "github" for src in data["sources"]) is False
    assert any(src["surface"] == "website" for src in data["sources"])


def test_contaminated_material_is_preserved_but_blocked() -> None:
    data = _load_json(ROOT / "fixtures/archive_mine/source_inventory.valid.candidate.json")
    contaminated = [s for s in data["sources"] if s["contamination_flags"]]
    assert contaminated
    for src in contaminated:
        assert src["authority_blocked"] is True
        assert src["trust_status"] != "ratified"


def test_invalid_contaminated_authority_fixture_fails_local_guardrail() -> None:
    data = _load_json(
        ROOT / "fixtures/archive_mine/source_inventory.invalid.contaminated_authority.json"
    )
    src = data["sources"][0]
    assert src["contamination_flags"]
    assert src["trust_status"] == "ratified"
    assert src["authority_blocked"] is False


def test_canon_recoverability_is_auditable() -> None:
    data = _load_json(ROOT / "fixtures/archive_mine/canon_recoverability.valid.candidate.json")
    assert data["website_surface"] == "website"
    assert data["recoverable"] is True
    assert len(data["website_snapshots"]) >= 1
    assert len(data["audit_events"]) >= 1


def test_invalid_recoverability_fixture_flags_missing_audit_material() -> None:
    data = _load_json(ROOT / "fixtures/archive_mine/canon_recoverability.invalid.missing_audit.json")
    assert data["recoverable"] is True
    assert data["website_snapshots"] == []
    assert data["audit_events"] == []


def test_optional_jsonschema_validation_when_available() -> None:
    try:
        import jsonschema  # type: ignore
        import yaml  # type: ignore
    except Exception:
        return

    source_schema = yaml.safe_load(
        _read(ROOT / "schemas/archive_mine/v0_1/source-inventory.schema.yaml")
    )
    recover_schema = yaml.safe_load(
        _read(ROOT / "schemas/archive_mine/v0_1/canon-recoverability-package.schema.yaml")
    )

    valid_source = _load_json(ROOT / "fixtures/archive_mine/source_inventory.valid.candidate.json")
    invalid_source = _load_json(
        ROOT / "fixtures/archive_mine/source_inventory.invalid.contaminated_authority.json"
    )
    valid_recover = _load_json(
        ROOT / "fixtures/archive_mine/canon_recoverability.valid.candidate.json"
    )
    invalid_recover = _load_json(
        ROOT / "fixtures/archive_mine/canon_recoverability.invalid.missing_audit.json"
    )

    jsonschema.Draft202012Validator(source_schema).validate(valid_source)
    jsonschema.Draft202012Validator(recover_schema).validate(valid_recover)

    bad_source = list(jsonschema.Draft202012Validator(source_schema).iter_errors(invalid_source))
    bad_recover = list(jsonschema.Draft202012Validator(recover_schema).iter_errors(invalid_recover))
    assert bad_source, "expected invalid contaminated authority fixture to fail schema validation"
    assert bad_recover, "expected invalid recoverability fixture to fail schema validation"
