from dataclasses import dataclass, field


@dataclass
class BenchmarkClaim:
    claim_id: str
    claim_text: str
    source_raw_sha256: str | None
    evidence_packet_ids: list[str] = field(default_factory=list)
    review_status: str = "pending"
    publish_requested: bool = False


@dataclass
class PublicClaim:
    public_claim_id: str
    claim_text: str
    source_completeness: str = "incomplete"
    evidence_packet_ids: list[str] = field(default_factory=list)
    review_status: str = "pending"


def benchmark_publish_allowed(claim: BenchmarkClaim) -> bool:
    """Publish allowed only when raw hash exists, evidence exists, and review is approved."""
    if not claim.publish_requested:
        return False
    if not claim.source_raw_sha256:
        return False
    if not claim.evidence_packet_ids:
        return False
    if claim.review_status != "approved":
        return False
    return True


def evaluate_public_claim(claim: PublicClaim) -> dict:
    """Public claims are quarantined until source is complete + evidence + approved review."""
    has_evidence = bool(claim.evidence_packet_ids)
    review_ok = claim.review_status == "approved"
    source_complete = claim.source_completeness == "complete"

    if source_complete and has_evidence and review_ok:
        return {"quarantine_status": "released", "publish_allowed": True}

    return {
        "quarantine_status": "quarantined",
        "publish_allowed": False,
        "reasons": {
            "source_complete": source_complete,
            "has_evidence": has_evidence,
            "review_ok": review_ok,
        },
    }
