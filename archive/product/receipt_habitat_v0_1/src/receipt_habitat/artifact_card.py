"""Artifact Card helpers for Receipt Habitat v0.1.

Artifact cards are human-facing windows into graph write candidates. They do
not mutate graphs, ratify claims, grant authority, or prove deployment.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ArtifactCardResult:
    ok: bool
    card: dict[str, Any] | None = None
    errors: list[str] = field(default_factory=list)


def _first_source(candidate: dict[str, Any]) -> str | None:
    sources = candidate.get("source_artifacts") or []
    if sources:
        return sources[0]
    return None


def _infer_surface(path: str | None) -> str:
    if not path:
        return "unknown"
    lowered = path.lower()
    if "github.com" in lowered or lowered.startswith("archive/"):
        return "github"
    if "drive.google.com" in lowered or "docs.google.com" in lowered:
        return "drive"
    if "notion.so" in lowered:
        return "notion"
    return "unknown"


def _infer_source_type(path: str | None) -> str:
    if not path:
        return "graph_write_candidate"
    lowered = path.lower()
    if "/pull/" in lowered:
        return "pr"
    if "/issues/" in lowered:
        return "issue"
    if "notion.so" in lowered:
        return "notion_page"
    if "drive.google.com" in lowered or "docs.google.com" in lowered:
        return "doc"
    if lowered.endswith((".md", ".txt", ".yaml", ".yml", ".json", ".pdf", ".docx")):
        return "file"
    return "unknown"


def build_artifact_card(candidate: dict[str, Any]) -> ArtifactCardResult:
    """Build an artifact_card.v0.1 from a graph_write_candidate.v0.1 packet."""
    required = [
        "candidate_id",
        "source_packet_id",
        "proposed_nodes",
        "proposed_edges",
        "canon_status",
        "deployment_status",
        "authority_scope",
    ]
    errors = [f"missing {key}" for key in required if key not in candidate]
    if errors:
        return ArtifactCardResult(ok=False, errors=errors)

    source = _first_source(candidate)
    proposed_nodes = candidate.get("proposed_nodes") or []
    first_node = proposed_nodes[0] if proposed_nodes else {}
    title = first_node.get("title") or candidate.get("source_packet_id") or candidate.get("candidate_id")
    raw_export_status = first_node.get("raw_export_status") or "unknown"
    review_required = candidate.get("review_required") or []
    missing_receipts = candidate.get("missing_receipts") or []
    forbidden_claims = candidate.get("forbidden_claims") or []

    card = {
        "artifact_id": candidate["candidate_id"],
        "title": title,
        "surface": _infer_surface(source),
        "source_type": _infer_source_type(source),
        "url_or_path": source,
        "created_or_modified": None,
        "status_strip": {
            "raw_export_status": raw_export_status,
            "canon_status": candidate.get("canon_status", "not_canon"),
            "deployment_status": candidate.get("deployment_status", "not_deployed"),
            "authority_scope": candidate.get("authority_scope", "none"),
            "review_state": "needs_review" if review_required or missing_receipts else "review_ready",
        },
        "evidence": {
            "stable_id": candidate.get("candidate_id"),
            "sha256_if_available": None,
            "source_refs": candidate.get("source_artifacts", []),
            "mirror_refs": [],
            "commit_or_pr_refs": [source] if source and "/pull/" in source else [],
        },
        "claims": {
            "strongest_safe_claim": candidate.get("strongest_safe_claim"),
            "claims_extracted": [
                node for node in proposed_nodes if node.get("node_type") == "Claim"
            ],
            "forbidden_claims": forbidden_claims,
            "overclaims_to_avoid": forbidden_claims,
        },
        "graph": {
            "proposed_nodes": proposed_nodes,
            "proposed_edges": candidate.get("proposed_edges", []),
            "missing_receipts": missing_receipts,
            "contradictions_or_uncertainties": candidate.get("contradictions_or_uncertainties", []),
            "review_required": review_required,
        },
        "routing": {
            "assigned_review_lanes": review_required,
            "next_safe_action": "Attach missing receipts before synthesis." if missing_receipts else "Route for review.",
            "public_release_status": "not_public_release_ready",
        },
    }
    return ArtifactCardResult(ok=True, card=card)


def artifact_card_to_markdown(card: dict[str, Any]) -> str:
    """Render an artifact card as conservative Markdown."""
    status = card.get("status_strip", {})
    evidence = card.get("evidence", {})
    graph = card.get("graph", {})
    claims = card.get("claims", {})
    routing = card.get("routing", {})

    lines = [
        f"# Artifact Card: {card.get('title')}",
        "",
        "```text",
        f"ARTIFACT_ID: {card.get('artifact_id')}",
        f"SURFACE: {card.get('surface')}",
        f"SOURCE_TYPE: {card.get('source_type')}",
        f"RAW_EXPORT_STATUS: {status.get('raw_export_status')}",
        f"CANON_STATUS: {status.get('canon_status')}",
        f"DEPLOYMENT_STATUS: {status.get('deployment_status')}",
        f"AUTHORITY_SCOPE: {status.get('authority_scope')}",
        f"REVIEW_STATE: {status.get('review_state')}",
        "```",
        "",
        "## Source",
        "",
        f"- URL/path: {card.get('url_or_path')}",
        f"- Stable ID: {evidence.get('stable_id')}",
        f"- SHA-256: {evidence.get('sha256_if_available')}",
        "",
        "## Missing receipts",
        "",
    ]
    missing = graph.get("missing_receipts") or []
    if missing:
        lines.extend([f"- {item}" for item in missing])
    else:
        lines.append("- None recorded in this card.")

    lines.extend([
        "",
        "## Strongest safe claim",
        "",
        str(claims.get("strongest_safe_claim")),
        "",
        "## Forbidden / risky claims",
        "",
    ])
    forbidden = claims.get("forbidden_claims") or []
    if forbidden:
        lines.extend([f"- {item}" for item in forbidden])
    else:
        lines.append("- None recorded in this card.")

    lines.extend([
        "",
        "## Review routing",
        "",
    ])
    lanes = routing.get("assigned_review_lanes") or []
    if lanes:
        lines.extend([f"- {lane}" for lane in lanes])
    else:
        lines.append("- Review lane not assigned yet.")

    lines.extend([
        "",
        "## Boundary",
        "",
        "```text",
        "This card is not the artifact.",
        "This card is not canon.",
        "This card is not deployment evidence.",
        "This card grants no authority.",
        "```",
    ])
    return "\n".join(lines) + "\n"
