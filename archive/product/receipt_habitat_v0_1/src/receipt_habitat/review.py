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

    changes: list[str] = list(validation.errors)
    notes: list[str] = []
    verdict = "approve"

    if validation.errors:
        verdict = "block"

    if risky_terms and verdict != "block":
        verdict = "patch"
        changes.append("attach receipts or soften risky canon/deployment/completion language")

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
