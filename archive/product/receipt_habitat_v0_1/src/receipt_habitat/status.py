"""Boring scoreboard status renderer v0.1."""

from __future__ import annotations

from typing import Any, Dict


WARNING_LINES = {
    "summary_only": "RAW EXPORT NOT VERIFIED — THIS IS A RETRIEVAL AID, NOT A FOSSIL RECORD.",
    "partial_raw": "PARTIAL RAW EXPORT — LINEAGE IS INCOMPLETE.",
    "unavailable": "RAW EXPORT UNAVAILABLE — SOURCE LINEAGE MUST BE DECLARED MISSING.",
}


def render_status(packet: Dict[str, Any], review: Dict[str, Any]) -> str:
    raw_status = packet.get("raw_export_status", "unknown")
    lines = [
        "# Receipt Habitat Status",
        "",
        "```text",
        f"ARTIFACT: {packet.get('artifact_id', 'UNKNOWN')}",
        f"TITLE: {packet.get('title', 'UNKNOWN')}",
        f"RAW EXPORT STATUS: {raw_status}",
        f"CANON STATUS: {review.get('canon_status', 'not_canon')}",
        f"DEPLOYMENT STATUS: {review.get('deployment_status', 'not_deployable')}",
        f"AUTHORITY SCOPE: {review.get('authority_scope', 'none')}",
        f"REVIEW VERDICT: {review.get('review_verdict', 'unknown')}",
        "```",
        "",
    ]

    if raw_status in WARNING_LINES:
        lines.extend([WARNING_LINES[raw_status], ""])

    if review.get("canon_status") == "not_canon":
        lines.extend(["NOT CANON — REVIEW REQUIRED.", ""])

    if review.get("deployment_status") == "not_deployable":
        lines.extend(["NOT DEPLOYED — NO RUNTIME CLAIM.", ""])

    if review.get("authority_scope") == "none":
        lines.extend(["NO EXECUTION AUTHORITY.", ""])

    overclaims = review.get("overclaims_detected") or []
    if overclaims:
        lines.extend([
            "## Overclaims Detected",
            "",
            *[f"- `{term}`" for term in overclaims],
            "",
        ])

    missing = review.get("missing_receipts") or []
    if missing:
        lines.extend([
            "## Missing Receipts / Required Fields",
            "",
            *[f"- `{field}`" for field in missing],
            "",
        ])

    lines.extend([
        "## Strongest Safe Claim",
        "",
        review.get("strongest_safe_claim", "This artifact is not reviewed."),
        "",
        "## Next Safest Action",
        "",
        review.get("next_safest_action", "Patch and re-review."),
        "",
    ])

    return "\n".join(lines)
