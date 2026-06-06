"""Receipt Habitat review logic v0.1.

No network. No execution. No canon. No deployment.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

from .overclaim import scan_claims, verdict_from_findings


@dataclass(frozen=True)
class ReviewResult:
    artifact_id: str
    review_verdict: str
    blocker_level: str
    public_claim_allowed: bool
    missing_receipts: List[str]
    overclaims_detected: List[str]
    strongest_safe_claim: str
    next_safest_action: str

    def to_packet(self, raw_export_status: str) -> Dict[str, Any]:
        return {
            "schema_version": "receipt_habitat.review.v0.1",
            "artifact_id": self.artifact_id,
            "source_packet_ref": None,
            "review_verdict": self.review_verdict,
            "blocker_level": self.blocker_level,
            "canon_status": "not_canon",
            "deployment_status": "not_deployable",
            "authority_scope": "none",
            "runtime_status": "local_dry_run_only",
            "raw_export_status": raw_export_status,
            "public_claim_allowed": self.public_claim_allowed,
            "review_dissent": [],
            "falsification_condition": None,
            "unresolved_questions": [],
            "missing_receipts": self.missing_receipts,
            "overclaims_detected": self.overclaims_detected,
            "overclaims_to_avoid": self.overclaims_detected,
            "strongest_safe_claim": self.strongest_safe_claim,
            "next_safest_action": self.next_safest_action,
        }


def _claim_texts(packet: Dict[str, Any]) -> List[str]:
    return [claim.get("claim_text", "") for claim in packet.get("claims", [])]


def review_packet(packet: Dict[str, Any]) -> ReviewResult:
    """Review an ingestion packet and produce a conservative review result."""
    artifact_id = packet.get("artifact_id", "UNKNOWN")
    raw_status = packet.get("raw_export_status")
    missing: List[str] = []

    for field in ["raw_export_status", "thread_time_range", "access_scope"]:
        if not packet.get(field):
            missing.append(field)

    if raw_status == "unavailable" and not packet.get("unavailable_sources"):
        missing.append("unavailable_sources")

    findings = scan_claims(_claim_texts(packet))
    risky_terms = sorted({finding.term for finding in findings})

    public_claim_allowed = raw_status == "full_raw" and not missing

    # Summary-only packets cannot create public claims.
    if raw_status == "summary_only":
        public_claim_allowed = False

    verdict = verdict_from_findings(findings)
    if missing:
        verdict = "block"

    blocker_level = "none"
    if verdict == "patch":
        blocker_level = "minor"
    if verdict == "block":
        blocker_level = "blocking"

    safe_claim = (
        "This packet may be used as a non-canon local review aid only. "
        "It does not establish canon, deployment, authority, or public factual claims."
    )

    next_action = packet.get("next_safest_action") or "Patch missing fields, attach receipts, then re-review."
    if missing:
        next_action = f"Patch missing required fields: {', '.join(missing)}."
    elif risky_terms:
        next_action = "Patch or remove risky canon/deployment/authority language before further routing."

    return ReviewResult(
        artifact_id=artifact_id,
        review_verdict=verdict,
        blocker_level=blocker_level,
        public_claim_allowed=public_claim_allowed,
        missing_receipts=missing,
        overclaims_detected=risky_terms,
        strongest_safe_claim=safe_claim,
        next_safest_action=next_action,
    )
