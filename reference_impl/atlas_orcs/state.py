from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional


class TrustState(str, Enum):
    RAW = "raw"
    PARSED = "parsed"
    CANDIDATE = "candidate"
    REVIEWED = "reviewed"
    RATIFIED = "ratified"
    ACTIVE = "active"
    UNDER_REVIEW = "under_review"
    SUPERSEDED = "superseded"
    REVOKED = "revoked"
    QUARANTINED = "quarantined"
    REJECTED = "rejected"


@dataclass
class Artifact:
    artifact_id: str
    trust_state: TrustState = TrustState.RAW
    canon_status: str = "not_canon"
    deployment_status: str = "not_deployable"
    lineage: list[str] = field(default_factory=list)
    contradiction_records: list[dict[str, Any]] = field(default_factory=list)
    ratification_expires_at: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
