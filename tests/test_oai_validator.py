from pathlib import Path

import yaml


def _load_example(name: str):
    base = Path("/home/runner/work/manus-artifacts/manus-artifacts/schemas/o_ai/v0_1/o-ai-packet-examples")
    return yaml.safe_load((base / name).read_text())


def _validate(packet: dict):
    required = ["raw_export_status", "thread_time_range", "access_scope", "epistemic_label", "authority_scope", "gates"]
    for r in required:
        if r not in packet:
            return False

    if packet["raw_export_status"] == "summary_only" and packet.get("public_use_status") == "source_complete":
        return False

    if packet.get("packet_kind") == "execution_request":
        g = packet.get("gates", {})
        needed = ["provenance_gate", "safety_gate", "governance_gate", "human_permission_gate", "receipt_gate"]
        if not all(g.get(k) == "pass" for k in needed):
            return False

    access = packet.get("access_scope", {})
    if "unavailable_sources" not in access or "assumed_context" not in access:
        return False

    return True


def test_valid_packets_pass():
    assert _validate(_load_example("valid_summary_only_packet.yaml"))
    assert _validate(_load_example("valid_full_raw_packet.yaml"))


def test_invalid_packets_fail():
    assert not _validate(_load_example("invalid_missing_access_scope.yaml"))
    assert not _validate(_load_example("invalid_execution_without_gates.yaml"))
