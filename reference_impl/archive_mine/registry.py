from __future__ import annotations

from typing import Any


REQUIRED_FIELDS = {
    "registry_id",
    "schema_version",
    "status",
    "deployment",
    "authority",
    "source_gravity",
    "notion_roots",
    "drive_roots",
    "github_archive_lanes",
    "website_canon_surfaces",
    "contamination_labels",
    "notion_candidate_deltas",
    "drive_candidate_deltas",
    "canon_recoverability_manifest",
    "fossil_to_github_receipt_crosswalk",
}

REQUIRED_LANES = {"#160", "#158", "#159", "#163", "#165", "#168", "#169", "#171", "#173", "#175"}
REQUIRED_CLAUDE_LABEL = "claude_touched_material"


def validate_source_surface_registry(packet: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []

    for field in sorted(REQUIRED_FIELDS):
        if field not in packet:
            errors.append(f"missing required field: {field}")

    if packet.get("schema_version") != "0.1":
        errors.append("schema_version must be 0.1")
    if packet.get("status") != "candidate":
        errors.append("status must be candidate")
    if packet.get("deployment") != "no":
        errors.append("deployment must be no")
    if packet.get("authority") != "none":
        errors.append("authority must be none")

    lanes = {lane.get("issue") for lane in packet.get("github_archive_lanes", []) if isinstance(lane, dict)}
    missing_lanes = sorted(REQUIRED_LANES - lanes)
    if missing_lanes:
        errors.append(f"github_archive_lanes missing required issues: {', '.join(missing_lanes)}")

    labels = packet.get("contamination_labels", [])
    if REQUIRED_CLAUDE_LABEL not in labels:
        errors.append(f"contamination_labels must include: {REQUIRED_CLAUDE_LABEL}")

    crosswalk = packet.get("fossil_to_github_receipt_crosswalk", [])
    if not crosswalk:
        errors.append("fossil_to_github_receipt_crosswalk must not be empty")
    else:
        for row in crosswalk:
            if not isinstance(row, dict):
                errors.append("crosswalk rows must be objects")
                continue
            if "fossil_id" not in row or "github_receipt" not in row:
                errors.append("crosswalk rows require fossil_id and github_receipt")

    return len(errors) == 0, errors
