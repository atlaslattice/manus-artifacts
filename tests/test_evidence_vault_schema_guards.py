from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def _load(path: str):
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def test_evidence_vault_schemas_exist_and_have_version():
    base = ROOT / "schemas/evidence_vault/v0_1"
    required = {
        "raw_export.schema.yaml",
        "parsed_packet.schema.yaml",
        "evidence_packet.schema.yaml",
        "benchmark_claim.schema.yaml",
        "public_claim.schema.yaml",
    }
    existing = {p.name for p in base.glob("*.yaml")}
    assert required.issubset(existing)

    for name in required:
        schema = yaml.safe_load((base / name).read_text(encoding="utf-8"))
        assert schema["properties"]["schema_version"]["const"] == "0.1"


def test_parsed_packet_requires_derived_from_raw_true():
    parsed = _load("schemas/evidence_vault/v0_1/parsed_packet.schema.yaml")
    assert parsed["properties"]["derived_from_raw"]["const"] is True


def test_raw_export_pointer_preserved_and_parsed_marked_derived():
    raw_path = ROOT / "archive/boot/atlasbrain/raw_exports/ATLAS_PRIME_SELECT_ALL_RAW_2026-05-23.txt"
    parsed_path = ROOT / "archive/boot/atlasbrain/parsed_packets/ATLAS_PRIME_NATIVE_THREAD_INGESTION_PACKET_2026-05-23.md"

    assert raw_path.exists()
    assert parsed_path.exists()

    raw_text = raw_path.read_text(encoding="utf-8")
    parsed_text = parsed_path.read_text(encoding="utf-8")

    assert "raw_sha256:" in raw_text
    assert "derived_from_raw: true" in parsed_text
    assert "raw_sha256:" in parsed_text
