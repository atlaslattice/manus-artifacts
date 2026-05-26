from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
ATLAS = ROOT / "schemas/atlas_orcs/v0_1"


def test_all_atlas_schemas_have_v01_and_parse():
    files = sorted(ATLAS.glob("*.yaml"))
    assert files
    for f in files:
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        assert data
        if "required" in data and "schema_version" in data["required"]:
            props = data.get("properties", {})
            sv = props.get("schema_version", {})
            assert sv.get("const") == "0.1"


def test_ratification_requires_explicit_event_and_no_self_ratify_rule_present():
    data = yaml.safe_load((ATLAS / "atlas-ratification-event.schema.yaml").read_text(encoding="utf-8"))
    assert "ratification_event_id" in data.get("required", [])
    assert data.get("x-rules", {}).get("no_self_ratification")
