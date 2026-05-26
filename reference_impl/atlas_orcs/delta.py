"""
Atlas / ORCS Governance Delta — the atomic unit of authorized state change.

STATUS: CANDIDATE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
"""

from dataclasses import dataclass, field
from typing import Optional, List
import datetime
from .state import TrustState, CanonStatus, DeploymentStatus


class EventType(str):
    RATIFICATION = "ratification_event"
    GOVERNANCE = "governance_event"
    DEPLOYMENT = "deployment_event"
    SUPERSESSION = "supersession_event"
    REVOCATION = "revocation_event"
    REVIEW_INITIATED = "review_initiated"
    QUARANTINE_TRIGGERED = "quarantine_triggered"
    CONTRADICTION = "contradiction_event"
    EXPIRY_CHECK = "expiry_check"


@dataclass
class GovernanceDelta:
    """
    A governance delta authorizes a specific state transition.
    Without a valid delta, no transition is permitted.
    """
    event_type: str
    authority_key: str
    artifact_id: str
    previous_state: TrustState
    new_state: TrustState
    evidence_refs: List[str]
    timestamp: datetime.datetime = field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    delta_id: Optional[str] = None
    human_permission: bool = False
    safety_pass: bool = False
    expiry_timestamp: Optional[datetime.datetime] = None

    def is_valid(self) -> bool:
        """A delta is valid if it has non-empty evidence and a recognized event type."""
        return bool(self.evidence_refs) and bool(self.authority_key)

    def requires_human_gate(self) -> bool:
        """Ratification always requires human permission."""
        return self.event_type in (
            EventType.RATIFICATION,
            EventType.DEPLOYMENT,
            EventType.SUPERSESSION,
        )
