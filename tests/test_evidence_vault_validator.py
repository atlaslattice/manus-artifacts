from reference_impl.atlas_orcs.evidence_vault import (
    BenchmarkClaim,
    PublicClaim,
    benchmark_publish_allowed,
    evaluate_public_claim,
)


def test_benchmark_publish_blocked_without_evidence_and_review():
    claim = BenchmarkClaim(
        claim_id="bm-1",
        claim_text="Model A beats Model B",
        source_raw_sha256="a04d606272128055d63e4e82c9b0557a9327c6ea45803ddae27ac51e06cc36dc",
        evidence_packet_ids=[],
        review_status="pending",
        publish_requested=True,
    )
    assert benchmark_publish_allowed(claim) is False


def test_benchmark_publish_blocked_without_raw_hash():
    claim = BenchmarkClaim(
        claim_id="bm-2",
        claim_text="Claim missing raw hash",
        source_raw_sha256=None,
        evidence_packet_ids=["ev-1"],
        review_status="approved",
        publish_requested=True,
    )
    assert benchmark_publish_allowed(claim) is False


def test_public_claim_quarantined_until_source_complete():
    claim = PublicClaim(
        public_claim_id="pc-1",
        claim_text="Public statement",
        source_completeness="incomplete",
        evidence_packet_ids=["ev-1"],
        review_status="approved",
    )
    result = evaluate_public_claim(claim)
    assert result["quarantine_status"] == "quarantined"
    assert result["publish_allowed"] is False


def test_public_claim_released_when_complete_with_evidence_and_review():
    claim = PublicClaim(
        public_claim_id="pc-2",
        claim_text="Public statement",
        source_completeness="complete",
        evidence_packet_ids=["ev-1"],
        review_status="approved",
    )
    result = evaluate_public_claim(claim)
    assert result["quarantine_status"] == "released"
    assert result["publish_allowed"] is True
