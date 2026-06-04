"""Review gate for Receipt Habitat v0.1.

Local dry-run only. Produces approve/patch/block verdicts for non-canon processing.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

try:
    from .overclaim import find_risky_phrases
    from .packet import validate_ingestion_packet
except ImportError:  # pragma: no cover - allows direct script use in local prototypes
    from overclaim import find_risky_phrases
    from packet import validate_ingestion_packet


@dataclass
class ReviewResult:
    verdict: str
    risky_phrases: list[str] = field(default_factory=list)
    minimal_required_changes: list[str] = field(default_factory=list)
    next_safest_command_sequence: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def review_packet(packet: dict[str, Any], source_text: str = "") -> ReviewResult:
    validation = validate_ingestion_packet(packet)
    risky = find_risky_phrases(source_text + "\n" + str(packet))
    risky_terms = [item.term for item in risky]
    risky_categories = {item.category for item in risky}

    changes: list[str] = list(validation.errors)
    notes: list[str] = []
    verdict = "approve"

    if validation.errors:
        verdict = "block"

    # Deployment/runtime language is the highest-risk class for v0.1 because it
    # can imply live capability or external effects. Without explicit receipts,
    # it blocks rather than merely requesting a wording patch.
    if "deployment" in risky_categories:
        verdict = "block"
        changes.append("remove deployment/runtime language or attach explicit deployment receipts")

    # Canon, crypto, and completion terms are risky but can often be repaired by
    # softening status language and attaching receipts. They patch unless a
    # validation or deployment failure has already blocked the packet.
    non_deployment_risk = bool(risky_categories - {"deployment"})
    if non_deployment_risk and verdict != "block":
        verdict = "patch"
        changes.append("attach receipts or soften risky canon/crypto/completion language")

    if packet.get("raw_export_status") == "summary_only":
        notes.append("summary_only packet: public_claim_allowed=false")

    next_steps = [
        "preserve raw source if available",
        "attach source refs and hash when available",
        "keep canon_status=not_canon",
        "keep deployment_status=not_deployable",
    ]

    return ReviewResult(
        verdict=verdict,
        risky_phrases=risky_terms,
        minimal_required_changes=changes,
        next_safest_command_sequence=next_steps,
        notes=notes,
    )
