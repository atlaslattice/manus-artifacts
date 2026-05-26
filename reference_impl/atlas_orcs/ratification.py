def requires_explicit_ratification(to_state: str, ratification_event_id: str | None) -> bool:
    if to_state != "ratified":
        return True
    return bool(ratification_event_id)
