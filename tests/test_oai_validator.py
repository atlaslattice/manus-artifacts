from pathlib import Path

import pytest
import yaml
from jsonschema import ValidationError, validate

from reference_impl.o_ai.validator import validate_oai_packet


def _load_example(name: str):
    base = Path(__file__).resolve().parents[1] / "schemas/o_ai/v0_1/o-ai-packet-examples"
    return yaml.safe_load((base / name).read_text())


def _load_schema():
    schema_path = Path(__file__).resolve().parents[1] / "schemas/o_ai/v0_1/o-ai-packet.schema.yaml"
    return yaml.safe_load(schema_path.read_text())


def test_valid_packets_pass():
    schema = _load_schema()
    summary = _load_example("valid_summary_only_packet.yaml")
    full_raw = _load_example("valid_full_raw_packet.yaml")
    validate(summary, schema)
    validate(full_raw, schema)
    assert validate_oai_packet(summary)[0]
    assert validate_oai_packet(full_raw)[0]


def test_invalid_packets_fail():
    schema = _load_schema()
    missing_access = _load_example("invalid_missing_access_scope.yaml")
    invalid_exec = _load_example("invalid_execution_without_gates.yaml")
    with pytest.raises(ValidationError):
        validate(missing_access, schema)
    with pytest.raises(ValidationError):
        validate(invalid_exec, schema)
    assert not validate_oai_packet(missing_access)[0]
    assert not validate_oai_packet(invalid_exec)[0]


def test_summary_only_cannot_be_source_complete():
    packet = _load_example("valid_summary_only_packet.yaml")
    packet["public_use_status"] = "source_complete"
    assert not validate_oai_packet(packet)[0]


def test_execution_request_requires_human_permission_and_receipt_pass():
    packet = _load_example("valid_full_raw_packet.yaml")
    packet["packet_kind"] = "execution_request"
    packet["gates"]["human_permission_gate"] = "fail"
    packet["gates"]["receipt_gate"] = "fail"
    assert not validate_oai_packet(packet)[0]
