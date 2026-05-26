from __future__ import annotations

from copy import deepcopy

from reference_impl.atlas_orcs.audit import append_audit_event


def quarantine_artifact(artifact: dict, reason: str) -> dict:
    updated = deepcopy(artifact)
    previous = updated.get("trust_state")

    lineage = list(updated.get("lineage") or [])
    artifact_id = updated.get("artifact_id")
    if artifact_id and artifact_id not in lineage:
        lineage.append(artifact_id)

    updated["lineage"] = lineage
    updated["quarantined_from"] = previous
    updated["trust_state"] = "quarantined"
    updated["quarantine_reason"] = reason
    return append_audit_event(updated, "artifact_quarantined", {"reason": reason, "from": previous})
