def make_audit_event(event_type: str, artifact_id: str, details: dict | None = None) -> dict:
    return {
        "schema_version": "0.1",
        "event_type": event_type,
        "artifact_id": artifact_id,
        "details": details or {},
    }
