from dataclasses import dataclass, field
from datetime import datetime

VALID_STATES = {
    "raw", "parsed", "candidate", "reviewed", "ratified", "active", "under_review",
    "superseded", "revoked", "quarantined", "rejected"
}

@dataclass
class Artifact:
    artifact_id: str
    state: str = "raw"
    canon_status: str = "not_canon"
    deployment_status: str = "not_deployable"
    lineage: list[str] = field(default_factory=list)
    contradiction_records: list[dict] = field(default_factory=list)
    ratification_expires_at: datetime | None = None
