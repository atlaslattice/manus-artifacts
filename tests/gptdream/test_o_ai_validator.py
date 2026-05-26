from pathlib import Path
import yaml

from reference_impl.o_ai.validator import validate_o_ai_packet

ROOT = Path(__file__).resolve().parents[2]
EX = ROOT / "schemas/o_ai/v0_1/o-ai-packet-examples"


def load(name: str):
    return yaml.safe_load((EX / name).read_text(encoding="utf-8"))


def test_valid_packets_pass():
    assert validate_o_ai_packet(load("valid_summary_only_packet.yaml")) == []
    assert validate_o_ai_packet(load("valid_full_raw_packet.yaml")) == []


def test_missing_access_scope_fails():
    errors = validate_o_ai_packet(load("invalid_missing_access_scope.yaml"))
    assert "missing:access_scope" in errors


def test_execution_without_gates_fails():
    errors = validate_o_ai_packet(load("invalid_execution_without_gates.yaml"))
    assert any(e.startswith("execution_gate_failed") for e in errors)


def test_summary_only_cannot_claim_source_complete():
    pkt = load("valid_summary_only_packet.yaml")
    pkt["public_use_status"] = "source_complete"
    assert "summary_only_cannot_be_source_complete" in validate_o_ai_packet(pkt)
