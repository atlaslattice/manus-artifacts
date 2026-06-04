"""Graph write candidate helpers for Receipt Habitat v0.1.

Local dry-run only. These helpers do not mutate a graph, ratify claims,
or grant authority. They only turn reviewed packets into candidate node/edge
proposals for later human and review-lane handling.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

try:
    from .packet import validate_ingestion_packet
except ImportError:  # pragma: no cover - allows direct script use
    from packet import validate_ingestion_packet


@dataclass
class GraphCandidateResult:
    ok: bool
    candidate: dict[str, Any] | None = None
    errors: list[str] = field(default_factory=list)


def _stable_id(prefix: str, value: str) -> str:
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]
    return f"{prefix}-{digest}"


def packet_to_graph_candidate(packet: dict[str, Any]) -> GraphCandidateResult:
    """Create a non-authoritative graph write candidate from an ingestion packet."""
    validation = validate_ingestion_packet(packet)
    if not validation.ok:
        return GraphCandidateResult(ok=False, errors=validation.errors)

    packet_id = packet.get("packet_id", "unknown")
    source_refs = packet.get("source_refs") or []
    if not source_refs:
        source_refs = packet.get("access_scope", {}).get("visible_sources", []) or []

    source_node_id = _stable_id("source", packet_id + "|" + "|".join(source_refs))
    packet_node_id = _stable_id("packet", packet_id)

    proposed_nodes = [
        {
            "node_id": source_node_id,
            "node_type": "SourceArtifact",
            "title": packet.get("source_thread_label", packet_id),
            "status": "candidate",
            "raw_export_status": packet.get("raw_export_status"),
            "canon_status": "not_canon",
            "deployment_status": "not_deployed",
            "authority_scope": "none",
            "evidence_refs": source_refs,
        },
        {
            "node_id": packet_node_id,
            "node_type": "ParsedPacket",
            "title": f"Parsed packet for {packet.get('source_thread_label', packet_id)}",
            "status": "candidate",
            "raw_export_status": packet.get("raw_export_status"),
            "canon_status": "not_canon",
            "deployment_status": "not_deployed",
            "authority_scope": "none",
            "evidence_refs": [packet.get("sha256_if_available") or "hash_missing"],
        },
    ]

    proposed_edges = [
        {
            "edge_id": _stable_id("edge", source_node_id + "parsed_from" + packet_node_id),
            "edge_type": "parsed_from",
            "from_node": packet_node_id,
            "to_node": source_node_id,
            "evidence_ref": packet.get("sha256_if_available"),
            "status": "candidate",
        }
    ]

    missing_receipts: list[str] = []
    if not packet.get("sha256_if_available"):
        missing_receipts.append("sha256_if_available")
    if packet.get("raw_export_status") in {"summary_only", "unavailable"}:
        missing_receipts.append("full_raw_export")

    for idx, claim in enumerate(packet.get("claims_extracted", []) or []):
        if not isinstance(claim, dict):
            continue
        claim_text = claim.get("claim", "")
        claim_node_id = _stable_id("claim", packet_id + "|" + claim_text)
        evidence_ref = claim.get("evidence_ref")
        if not evidence_ref:
            missing_receipts.append(f"claim_{idx}_evidence_ref")
        proposed_nodes.append(
            {
                "node_id": claim_node_id,
                "node_type": "Claim",
                "title": claim_text[:120],
                "status": "candidate",
                "raw_export_status": packet.get("raw_export_status"),
                "canon_status": "not_canon",
                "deployment_status": "not_deployed",
                "authority_scope": "none",
                "evidence_refs": [evidence_ref] if evidence_ref else [],
            }
        )
        proposed_edges.append(
            {
                "edge_id": _stable_id("edge", claim_node_id + "derived_from" + packet_node_id),
                "edge_type": "derived_from",
                "from_node": claim_node_id,
                "to_node": packet_node_id,
                "evidence_ref": evidence_ref,
                "status": "candidate",
            }
        )

    candidate = {
        "candidate_id": _stable_id("gwc", packet_id),
        "generated_by": "Receipt Habitat v0.1",
        "source_packet_id": packet_id,
        "source_artifacts": source_refs,
        "proposed_nodes": proposed_nodes,
        "proposed_edges": proposed_edges,
        "contradictions_or_uncertainties": packet.get("contradictions_or_uncertainties", []),
        "missing_receipts": sorted(set(missing_receipts)),
        "review_required": ["Lucerna", "Hashlight"] if missing_receipts else [],
        "strongest_safe_claim": packet.get("strongest_safe_claim"),
        "forbidden_claims": packet.get("overclaims_to_avoid", []),
        "canon_status": "not_canon",
        "deployment_status": "not_deployed",
        "authority_scope": "none",
    }
    return GraphCandidateResult(ok=True, candidate=candidate)
