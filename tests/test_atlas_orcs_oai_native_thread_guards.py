from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_appendix_j_has_canon_surface_patch():
    p = "archive/spec/gptdream/appendices/APPENDIX_J_GPTDREAM_REHYDRATION_PRIORITY_FAILURE_MODE_v0.1.md"
    text = _read(p)
    assert "canon surface when explicitly ratified/published there" in text
    assert "Website = canon." not in text


def test_execution_route_includes_atlas_orcs_audit():
    p = "archive/spec/gptdream/appendices/APPENDIX_H_3_O_AI_ROUTING_TABLE_v0.1.md"
    text = _read(p)
    assert ("Atlas/ORCS audit state" in text) or ("atlas_orcs_audit_state" in text)


def test_summary_not_source_and_receipt_not_truth_rules_present():
    summary_schema = _read("schemas/atlas_orcs/v0_1/atlas-summary-lineage.schema.yaml")
    receipt_schema = _read("schemas/atlas_orcs/v0_1/atlas-provenance-receipt.schema.yaml")
    assert "summary_replaces_source: { const: false" in summary_schema
    assert "truth_claim: { type: string, enum: [not_truth]" in receipt_schema


def test_ratification_requires_explicit_event_fields_and_no_self_ratify():
    ratification_schema = _read("schemas/atlas_orcs/v0_1/atlas-ratification-event.schema.yaml")
    assert "required: [schema_version, event_id, artifact_id, ratified_by, ratified_at]" in ratification_schema
    assert "self_ratified: { const: false" in ratification_schema


def test_oai_required_fields_and_gate_rules_are_present():
    schema = _read("schemas/o_ai/v0_1/o-ai-packet.schema.yaml")
    assert "- raw_export_status" in schema
    assert "- thread_time_range" in schema
    assert "- access_scope" in schema
    assert "public_use_status: { enum: [source_incomplete] }" in schema
    assert "packet_type: { const: execution_request }" in schema
    assert "human_permission_gate: { const: pass }" in schema
    assert "receipt_gate: { const: pass }" in schema


def test_native_thread_required_fields_and_summary_guard_present():
    schema = _read("schemas/native_thread/v0_1/native-thread-ingestion-packet.schema.yaml")
    assert "- raw_export_status" in schema
    assert "- thread_time_range" in schema
    assert "- access_scope" in schema
    assert "ingestion_completeness: { const: partial_ingestion }" in schema
