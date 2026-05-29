def build_audit_event(event_type: str, artifact_id: str, status: str, details: dict | None = None) -> dict:
    return {
        "event_type": event_type,
        "artifact_id": artifact_id,
        "status": status,
        "details": details or {},
    }
