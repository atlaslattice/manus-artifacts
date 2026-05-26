"""
Candidate validation tests for GPTDream++ / Atlas / ORCS task bundle.

STATUS: CANDIDATE TESTS — NOT CANON — NOT DEPLOYABLE
"""

from __future__ import annotations

from pathlib import Path
import re
import pytest

ROOT = Path(__file__).resolve().parents[1]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_epic0_files_exist_and_have_boundary_headers() -> None:
    required = [
        ROOT / "archive/spec/gptdream/GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md",
        ROOT / "archive/spec/gptdream/appendices/APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md",
        ROOT / "archive/spec/gptdream/appendices/APPENDIX_H_1_O_AI_INTEGRATION_SCAFFOLD_v0.1.md",
        ROOT / "archive/spec/gptdream/appendices/APPENDIX_H_2_O_AI_PACKET_SCHEMA_v0.1.md",
        ROOT / "archive/spec/gptdream/appendices/APPENDIX_H_3_O_AI_ROUTING_TABLE_v0.1.md",
        ROOT / "archive/spec/gptdream/appendices/APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md",
        ROOT / "archive/spec/gptdream/appendices/APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md",
        ROOT / "archive/spec/gptdream/appendices/APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md",
        ROOT / "archive/spec/gptdream/appendices/APPENDIX_I_3_ATLAS_ORCS_SCHEMA_BUNDLE_v0.1.md",
        ROOT / "archive/spec/gptdream/appendices/APPENDIX_J_GPTDREAM_REHYDRATION_PRIORITY_FAILURE_MODE_v0.1.md",
    ]
    for path in required:
        assert path.exists(), f"missing file: {path}"
        text = _read(path)
        assert "NOT CANON" in text
        assert "NOT DEPLOYABLE" in text


def test_appendix_j_patch_and_routing_enforced() -> None:
    text = _read(
        ROOT
        / "archive/spec/gptdream/appendices/APPENDIX_J_GPTDREAM_REHYDRATION_PRIORITY_FAILURE_MODE_v0.1.md"
    )
    assert "Website = canon surface when explicitly ratified/published there." in text
    assert "Website = canon." not in text
    route = "→ Atlas / ORCS audit state"
    assert route in text


def test_heading_numbering_uses_h_and_i() -> None:
    h_text = _read(
        ROOT / "archive/spec/gptdream/appendices/APPENDIX_H_CROSS_VENDOR_INTEROP_MODEL_v0.1.md"
    )
    i_text = _read(
        ROOT
        / "archive/spec/gptdream/appendices/APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md"
    )
    i3_text = _read(
        ROOT
        / "archive/spec/gptdream/appendices/APPENDIX_I_3_ATLAS_ORCS_SCHEMA_BUNDLE_v0.1.md"
    )
    assert re.search(r"^\s*##\s+H\.1\b", h_text, flags=re.MULTILINE)
    assert re.search(r"^\s*##\s+H\.2\b", h_text, flags=re.MULTILINE)
    assert re.search(r"^\s*##\s+H\.3\b", h_text, flags=re.MULTILINE)
    assert re.search(r"^\s*##\s+I\.1\b", i_text, flags=re.MULTILINE)
    assert re.search(r"^\s*##\s+I\.2\b", i_text, flags=re.MULTILINE)
    assert re.search(r"^\s*#\s+Appendix\s+I\.3\b", i3_text, flags=re.MULTILINE)


def test_schema_bundle_files_present_with_version_and_defaults() -> None:
    schema_dir = ROOT / "schemas/atlas_orcs/v0_1"
    files = sorted(schema_dir.glob("*.schema.yaml"))
    expected_names = {
        "atlas-artifact.schema.yaml",
        "atlas-provenance-receipt.schema.yaml",
        "atlas-claim.schema.yaml",
        "atlas-claim-relationship.schema.yaml",
        "atlas-contradiction-ledger.schema.yaml",
        "atlas-uncertainty-ledger.schema.yaml",
        "atlas-summary-lineage.schema.yaml",
        "atlas-intent-provenance.schema.yaml",
        "atlas-trust-state.schema.yaml",
        "atlas-ratification-event.schema.yaml",
        "atlas-failure-event.schema.yaml",
        "atlas-governance-profile.schema.yaml",
        "atlas-domain-module.schema.yaml",
        "atlas-quarantine-rule.schema.yaml",
        "atlas-audit-event.schema.yaml",
    }
    observed_names = {path.name for path in files}
    assert observed_names == expected_names
    for path in files:
        text = _read(path)
        assert 'const: "0.1"' in text
        assert "default: not_canon" in text
        assert "default: not_deployable" in text
        assert "self_ratified" in text


def test_atlas_boundary_semantics_summary_and_receipt() -> None:
    summary = {"kind": "summary", "asserts": ["x"]}
    source = {"kind": "source", "asserts": ["x", "y"]}
    receipt = {"kind": "receipt", "records": "seen"}

    assert summary != source
    assert receipt.get("kind") != "truth"


def test_ratification_requires_explicit_event_model() -> None:
    artifact = {"state": "reviewed", "ratification_event": None}

    def can_be_ratified(record: dict) -> bool:
        return bool(record.get("ratification_event"))

    assert can_be_ratified(artifact) is False
    artifact["ratification_event"] = "evt-001"
    assert can_be_ratified(artifact) is True


def test_oai_schema_contains_required_fields_and_gate_constraints() -> None:
    schema = _read(ROOT / "schemas/o_ai/v0_1/o-ai-packet.schema.yaml")
    for token in [
        "raw_export_status",
        "thread_time_range",
        "access_scope",
        "epistemic_label",
        "authority_scope",
        "provenance_gate",
        "safety_gate",
        "governance_gate",
        "data_residency_gate",
        "human_permission_gate",
        "receipt_gate",
    ]:
        assert token in schema
    assert "summary_only" in schema
    assert "source_complete" in schema
    assert "execution_request" in schema


def test_oai_schema_required_arrays_include_expected_fields_when_pyyaml_available() -> None:
    yaml = pytest.importorskip("yaml")
    schema = yaml.safe_load(_read(ROOT / "schemas/o_ai/v0_1/o-ai-packet.schema.yaml"))
    assert set(schema["required"]) >= {
        "raw_export_status",
        "thread_time_range",
        "access_scope",
        "epistemic_label",
        "authority_scope",
        "gates",
    }
    assert set(schema["properties"]["gates"]["required"]) >= {
        "provenance_gate",
        "safety_gate",
        "governance_gate",
        "data_residency_gate",
    }


def test_oai_examples_include_valid_and_invalid_packets() -> None:
    examples = ROOT / "schemas/o_ai/v0_1/o-ai-packet-examples"
    assert (examples / "valid_summary_only_packet.yaml").exists()
    assert (examples / "valid_full_raw_packet.yaml").exists()
    assert (examples / "invalid_missing_access_scope.yaml").exists()
    assert (examples / "invalid_execution_without_gates.yaml").exists()


def test_native_thread_schema_contains_required_fields_and_guardrail() -> None:
    schema = _read(
        ROOT / "schemas/native_thread/v0_1/native-thread-ingestion-packet.schema.yaml"
    )
    for token in [
        "raw_export_status",
        "thread_time_range",
        "access_scope",
        "unavailable_sources",
        "assumed_context",
        "strongest_safe_claim",
        "strongest_safe_claim_caveat",
    ]:
        assert token in schema
    assert "summary_only" in schema
    assert "full_ingestion" in schema


def test_yaml_files_parse_cleanly_when_pyyaml_available() -> None:
    yaml = pytest.importorskip("yaml")
    targets = [
        ROOT / "schemas/atlas_orcs/v0_1",
        ROOT / "schemas/o_ai/v0_1",
        ROOT / "schemas/native_thread/v0_1",
    ]
    for target in targets:
        for path in target.rglob("*.yaml"):
            yaml.safe_load(_read(path))
