def cas001a_anchor(request: dict) -> dict:
    return {
        "anchor": "CAS-001-A",
        "request_id": request.get("id"),
        "human_permission": request.get("gates", {}).get("human_permission"),
    }
