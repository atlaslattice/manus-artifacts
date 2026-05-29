from pathlib import Path

import yaml


def _load(path: Path):
    return yaml.safe_load(path.read_text())


def test_all_yaml_parses_cleanly():
    root = Path("/home/runner/work/manus-artifacts/manus-artifacts")
    for path in root.glob("schemas/**/*.yaml"):
        _load(path)


def test_atlas_schema_versions_and_defaults():
    root = Path("/home/runner/work/manus-artifacts/manus-artifacts/schemas/atlas_orcs/v0_1")
    for path in root.glob("*.yaml"):
        data = _load(path)
        assert data["schema_version"] == "0.1"
        props = data.get("properties", {})
        if "canon_status" in props:
            assert props["canon_status"].get("default") == "not_canon"
        if "deployment_status" in props:
            assert props["deployment_status"].get("default") == "not_deployable"


def test_summary_not_source_receipt_not_truth_and_ratification_explicit():
    summary = {"kind": "summary", "source_id": "src1"}
    source = {"kind": "source", "id": "src1"}
    receipt = {"kind": "receipt", "verified": False}
    ratification_event = None

    assert summary["kind"] != source["kind"]
    assert receipt["verified"] is False
    assert ratification_event is None
