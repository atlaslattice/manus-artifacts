from pathlib import Path

import pytest
import yaml
from jsonschema import ValidationError, validate

from reference_impl.archive_mine import validate_source_surface_registry


def _load_yaml(path: Path):
    return yaml.safe_load(path.read_text())


def _load_sample():
    path = Path("/tmp/workspace/atlaslattice/manus-artifacts/fixtures/archive_mine/source_surface_registry_v0_1.sample.yaml")
    return _load_yaml(path)


def _load_schema():
    path = Path("/tmp/workspace/atlaslattice/manus-artifacts/schemas/archive_mine/v0_1/source-surface-registry.schema.yaml")
    return _load_yaml(path)


def test_source_surface_registry_sample_passes_schema_and_validator():
    sample = _load_sample()
    schema = _load_schema()
    validate(sample, schema)
    ok, errors = validate_source_surface_registry(sample)
    assert ok, errors


def test_missing_required_field_fails_schema_and_validator():
    sample = _load_sample()
    schema = _load_schema()
    sample.pop("drive_roots")

    with pytest.raises(ValidationError):
        validate(sample, schema)

    ok, errors = validate_source_surface_registry(sample)
    assert not ok
    assert any("missing required field: drive_roots" in e for e in errors)


def test_missing_claude_label_fails_validator():
    sample = _load_sample()
    sample["contamination_labels"] = ["claude_generated_summary"]
    ok, errors = validate_source_surface_registry(sample)
    assert not ok
    assert any("claude_touched_material" in e for e in errors)


def test_crosswalk_rows_require_github_receipt():
    sample = _load_sample()
    sample["fossil_to_github_receipt_crosswalk"] = [{"fossil_id": "f-001"}]
    ok, errors = validate_source_surface_registry(sample)
    assert not ok
    assert any("crosswalk rows require fossil_id and github_receipt" in e for e in errors)
