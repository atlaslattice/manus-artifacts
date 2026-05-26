def quarantine_artifact(artifact: dict, reason: str) -> dict:
    lineage = list(artifact.get("lineage", []))
    lineage.append({"event": "quarantined", "reason": reason})
    out = dict(artifact)
    out["state"] = "quarantined"
    out["lineage"] = lineage
    return out
