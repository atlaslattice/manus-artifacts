from pathlib import Path


def _read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def test_raw_export_requires_hash_and_preserved_tape():
    text = _read("/home/runner/work/manus-artifacts/manus-artifacts/schemas/atlas_orcs/v0_1/atlas-raw-export.schema.yaml")
    assert "hash_sha256" in text
    assert "raw_tape_preserved: { const: true }" in text


def test_parsed_packet_must_be_derived_and_separate_lane():
    text = _read("/home/runner/work/manus-artifacts/manus-artifacts/schemas/atlas_orcs/v0_1/atlas-parsed-packet.schema.yaml")
    assert "storage_lane: { const: parsed_packets }" in text
    assert "derived_from_raw: { const: true }" in text


def test_benchmark_publish_is_review_and_evidence_gated():
    text = _read("/home/runner/work/manus-artifacts/manus-artifacts/schemas/atlas_orcs/v0_1/atlas-benchmark-claim.schema.yaml")
    assert "publish_status: { enum: [blocked, publishable]" in text
    assert "review_status: { const: approved }" in text
    assert "evidence_packet_id" in text


def test_public_claim_quarantine_requires_source_complete():
    text = _read("/home/runner/work/manus-artifacts/manus-artifacts/schemas/atlas_orcs/v0_1/atlas-public-claim.schema.yaml")
    assert "source_completeness: { enum: [incomplete, complete]" in text
    assert "quarantine_status: { const: quarantined }" in text
    assert "publish_allowed: { const: false }" in text
