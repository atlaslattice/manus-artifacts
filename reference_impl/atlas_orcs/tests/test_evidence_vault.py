from reference_impl.atlas_orcs.evidence_vault import (
    BenchmarkClaim,
    PublicClaim,
    benchmark_publish_allowed,
    evaluate_public_claim,
    parsed_packet_record,
    raw_export_record,
)


def test_raw_tape_preserved_and_hashed():
    rec = raw_export_record("raw-1", "a" * 64)
    assert rec["storage_lane"] == "raw_exports"
    assert rec["raw_tape_preserved"] is True
    assert len(rec["hash_sha256"]) == 64


def test_parsed_packet_is_derived():
    rec = parsed_packet_record("parsed-1", "raw-1")
    assert rec["storage_lane"] == "parsed_packets"
    assert rec["derived_from_raw"] is True
    assert rec["raw_export_id"] == "raw-1"


def test_benchmark_claim_publish_requires_evidence_and_review():
    blocked_no_evidence = BenchmarkClaim("c1", "claim", evidence_packet_id=None, review_status="approved")
    blocked_no_review = BenchmarkClaim("c2", "claim", evidence_packet_id="ev-1", review_status="pending")
    allowed = BenchmarkClaim("c3", "claim", evidence_packet_id="ev-2", review_status="approved")

    assert benchmark_publish_allowed(blocked_no_evidence) is False
    assert benchmark_publish_allowed(blocked_no_review) is False
    assert benchmark_publish_allowed(allowed) is True


def test_public_claim_quarantined_until_source_complete():
    q = evaluate_public_claim(PublicClaim("p1", source_completeness="incomplete"))
    r = evaluate_public_claim(PublicClaim("p2", source_completeness="complete"))
    assert q == {"quarantine_status": "quarantined", "publish_allowed": False}
    assert r == {"quarantine_status": "released", "publish_allowed": True}
