from dataclasses import dataclass


@dataclass
class BenchmarkClaim:
    benchmark_claim_id: str
    claim_text: str
    evidence_packet_id: str | None = None
    review_status: str = "pending"


@dataclass
class PublicClaim:
    public_claim_id: str
    source_completeness: str = "incomplete"


def raw_export_record(raw_export_id: str, hash_sha256: str) -> dict:
    return {
        "raw_export_id": raw_export_id,
        "storage_lane": "raw_exports",
        "hash_sha256": hash_sha256,
        "raw_tape_preserved": True,
    }


def parsed_packet_record(parsed_packet_id: str, raw_export_id: str) -> dict:
    return {
        "parsed_packet_id": parsed_packet_id,
        "storage_lane": "parsed_packets",
        "derived_from_raw": True,
        "raw_export_id": raw_export_id,
    }


def benchmark_publish_allowed(claim: BenchmarkClaim) -> bool:
    return bool(claim.evidence_packet_id) and claim.review_status == "approved"


def evaluate_public_claim(public_claim: PublicClaim) -> dict:
    if public_claim.source_completeness != "complete":
        return {"quarantine_status": "quarantined", "publish_allowed": False}
    return {"quarantine_status": "released", "publish_allowed": True}
