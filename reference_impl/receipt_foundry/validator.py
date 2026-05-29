from __future__ import annotations


def _has_required_receipt_metadata(claim: dict) -> bool:
    receipt = claim.get("receipt_metadata")
    if not isinstance(receipt, dict):
        return False
    return all(receipt.get(key) for key in ("receipt_id", "receipt_type", "receipt_hash"))


def _has_governance_event(claim: dict) -> bool:
    event = claim.get("governance_event")
    return isinstance(event, dict) and bool(event.get("governance_event_id"))


def validate_receipt_habitat_claim(claim: dict) -> list[str]:
    errors: list[str] = []

    for field in ("claim_state", "evidence_refs"):
        if field not in claim:
            errors.append(f"missing:{field}")

    if "evidence_refs" in claim:
        refs = claim["evidence_refs"]
        if not isinstance(refs, list) or not refs or any(not isinstance(r, str) or not r.strip() for r in refs):
            errors.append("invalid:evidence_refs")

    previous = claim.get("previous_claim_state")
    current = claim.get("claim_state")

    if previous == "candidate" and current == "reviewed" and not _has_required_receipt_metadata(claim):
        errors.append("candidate_to_reviewed_requires_receipt_metadata")

    if previous == "reviewed" and current == "ratified" and not _has_governance_event(claim):
        errors.append("reviewed_to_ratified_requires_governance_event")

    if claim.get("source_basis") == "summary_only" and claim.get("source_status") == "source":
        errors.append("summary_cannot_become_source")

    if claim.get("truth_status") == "verified" and _has_required_receipt_metadata(claim):
        verification_event = claim.get("verification_event")
        if not isinstance(verification_event, dict) or not verification_event.get("verification_event_id"):
            errors.append("receipt_not_truth_requires_verification_event")

    return errors
