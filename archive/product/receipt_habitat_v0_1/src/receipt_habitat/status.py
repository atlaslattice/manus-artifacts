"""Status helpers for Receipt Habitat v0.1.

Local dry-run only. Status output is descriptive, not authoritative.
"""

from __future__ import annotations

from typing import Any


def summarize_status(packet: dict[str, Any]) -> dict[str, Any]:
    """Return the minimal status surface for a packet."""
    return {
        "packet_id": packet.get("packet_id"),
        "raw_export_status": packet.get("raw_export_status"),
        "canon_status": packet.get("canon_status", "not_canon"),
        "deployment_status": packet.get("deployment_status", "not_deployable"),
        "authority_scope": packet.get("authority_scope", "none"),
        "runtime_status": packet.get("runtime_status", "local_dry_run_only"),
        "strongest_safe_claim": packet.get("strongest_safe_claim"),
        "next_action": packet.get("next_action"),
    }


def markdown_status(packet: dict[str, Any]) -> str:
    status = summarize_status(packet)
    lines = ["# Receipt Habitat Packet Status", ""]
    for key, value in status.items():
        lines.append(f"- **{key}:** {value}")
    return "\n".join(lines) + "\n"
