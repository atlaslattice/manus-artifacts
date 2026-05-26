"""
Atlas / ORCS Trust State definitions.

STATUS: CANDIDATE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE

Core rule: Authority is a state transition, not a vibe.
"""

from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Optional, List
import datetime


class TrustState(str, Enum):
    """All valid trust states for an Atlas artifact."""
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


class CanonStatus(str, Enum):
    NOT_CANON = "not_canon"
    CANDIDATE_CANON = "candidate_canon"
    RATIFIED_CANON = "ratified_canon"


class DeploymentStatus(str, Enum):
    NOT_DEPLOYABLE = "not_deployable"
    DEPLOYMENT_CANDIDATE = "deployment_candidate"
    DEPLOYED = "deployed"


@dataclass
class Artifact:
    """Core artifact record with trust state."""
    artifact_id: str
    title: str
    trust_state: TrustState = TrustState.RAW
    canon_status: CanonStatus = CanonStatus.NOT_CANON
    deployment_status: DeploymentStatus = DeploymentStatus.NOT_DEPLOYABLE
    lineage: List[str] = field(default_factory=list)
    receipts: List[str] = field(default_factory=list)
    ratification_event_id: Optional[str] = None
    ratification_expiry: Optional[datetime.datetime] = None
    is_summary: bool = False
    source_artifact_ids: List[str] = field(default_factory=list)
    created_at: datetime.datetime = field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

    # Invariant: no artifact can self-ratify
    SELF_RATIFICATION_ALLOWED: bool = False

    def is_ratification_expired(self, at_time: Optional[datetime.datetime] = None) -> bool:
        """Return True if ratification has expired."""
        if self.ratification_expiry is None:
            return False
        check_time = at_time or datetime.datetime.now(datetime.timezone.utc)
        return check_time > self.ratification_expiry
