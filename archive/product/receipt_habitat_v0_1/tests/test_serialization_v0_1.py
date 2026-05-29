import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "receipt_habitat"
sys.path.insert(0, str(SRC))

from ingest import build_ingestion_packet
from serialize import to_simple_yaml, to_stable_json, write_packet


def test_stable_json_round_trips():
    packet = {
        "packet_id": "pkt-json-001",
        "canon_status": "not_canon",
        "deployment_status": "not_deployed",
        "authority_scope": "none",
    }
    rendered = to_stable_json(packet)
    loaded = json.loads(rendered)
    assert loaded == packet
    assert rendered.endswith("\n")


def test_simple_yaml_contains_boundary_defaults():
    packet = {
        "packet_id": "pkt-yaml-001",
        "canon_status": "not_canon",
        "deployment_status": "not_deployed",
        "authority_scope": "none",
    }
    rendered = to_simple_yaml(packet)
    assert "canon_status: not_canon" in rendered
    assert "deployment_status: not_deployed" in rendered
    assert "authority_scope: none" in rendered


def test_write_packet_json(tmp_path):
    packet = {"packet_id": "pkt-write-001", "canon_status": "not_canon"}
    out = tmp_path / "packet.json"
    write_packet(packet, str(out))
    assert json.loads(out.read_text(encoding="utf-8"))["packet_id"] == "pkt-write-001"


def test_build_ingestion_packet_serializes_to_json(tmp_path):
    input_file = tmp_path / "summary.md"
    input_file.write_text("MODE: TEST\nGOAL: preserve receipts\n", encoding="utf-8")
    packet = build_ingestion_packet(
        str(input_file),
        raw_status="summary_only",
        timezone="America/Chicago",
        seat_name="Fossilbranch",
        model_surface="ChatGPT",
    )
    rendered = to_stable_json(packet)
    loaded = json.loads(rendered)
    assert loaded["raw_export_status"] == "summary_only"
    assert loaded["canon_status"] == "not_canon"
    assert loaded["deployment_status"] == "not_deployable"
    assert loaded["authority_scope"] == "none"
