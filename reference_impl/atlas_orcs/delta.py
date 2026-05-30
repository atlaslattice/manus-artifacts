"""
Atlas/ORCS Delta (Governance Events)
NOT CANON — NOT DEPLOYABLE — reference implementation only

Defines the governance events (ORCS operations) that drive state transitions.
See: archive/spec/gptdream/appendices/APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from state import TrustState, CanonStatus, DeploymentStatus


@dataclass
class GovernanceEvent:
    """Base class for all ORCS governance events."""

    event_id: str
    artifact_id: str
    actor_id: str
    occurred_at: str  # ISO 8601
    event_type: str = ""
    notes: Optional[str] = None


@dataclass
class RatificationEvent(GovernanceEvent):
    """
    ORCS-RATIFY event.
    CRITICAL: ratifier_id MUST differ from artifact.author_id (no self-ratification).
    """

    ratifier_id: str = ""
    ratification_scope: list = field(default_factory=list)
    council_quorum: int = 1
    council_members: list = field(default_factory=list)
    adjudicated_by: Optional[str] = None  # @atlaslattice for full canon
    expiry: str = ""  # ISO 8601 — when ratification expires

    def __post_init__(self):
        if not self.event_type:
            self.event_type = "ORCS-RATIFY"

    def validate(self, artifact_author_id: str) -> None:
        """Raises ValueError if ratification is invalid."""
        if self.ratifier_id == artifact_author_id:
            raise ValueError(
                f"Self-ratification prohibited: ratifier_id '{self.ratifier_id}' "
                f"equals artifact author_id '{artifact_author_id}'"
            )
        if not self.ratifier_id:
            raise ValueError("ratifier_id is required")
        if not self.expiry:
            raise ValueError("expiry is required for ratification events")
        if self.council_quorum < 1:
            raise ValueError("council_quorum must be >= 1")


@dataclass
class PromoteEvent(GovernanceEvent):
    """ORCS-PROMOTE event. Moves a ratified artifact to active."""

    def __post_init__(self):
        if not self.event_type:
            self.event_type = "ORCS-PROMOTE"
    # Requires prior trust_state == ratified


@dataclass
class SupersedeEvent(GovernanceEvent):
    """ORCS-SUPERSEDE event. Marks artifact as superseded by a newer version."""

    superseded_by: str = ""  # artifact_id of the newer version

    def __post_init__(self):
        if not self.event_type:
            self.event_type = "ORCS-SUPERSEDE"


@dataclass
class RevokeEvent(GovernanceEvent):
    """ORCS-REVOKE event. Explicit revocation with lineage preserved."""

    revocation_reason: str = ""
    revoker_id: str = ""

    def __post_init__(self):
        if not self.event_type:
            self.event_type = "ORCS-REVOKE"


@dataclass
class QuarantineEvent(GovernanceEvent):
    """
    ORCS-QUARANTINE event. Isolates artifact for safety/integrity review.
    Lineage ALWAYS preserved during quarantine.
    """

    quarantine_reason: str = ""
    trigger_rule_id: str = ""
    lineage_preserved: bool = True  # Always True; hardcoded

    def __post_init__(self):
        if not self.event_type:
            self.event_type = "ORCS-QUARANTINE"
        self.lineage_preserved = True  # Enforce: quarantine is not deletion


@dataclass
class ContradictEvent(GovernanceEvent):
    """
    ORCS-CONTRADICT event. Creates a contradiction record.
    NEVER overwrites existing artifacts.
    """

    artifact_id_b: str = ""  # The second artifact in the contradiction
    contradiction_type: str = ""
    contradiction_record_id: str = ""  # Created by this event

    def __post_init__(self):
        if not self.event_type:
            self.event_type = "ORCS-CONTRADICT"


@dataclass
class ChallengeEvent(GovernanceEvent):
    """ORCS-CHALLENGE event. Requests review of an active artifact."""

    challenge_reason: str = ""
    challenger_id: str = ""

    def __post_init__(self):
        if not self.event_type:
            self.event_type = "ORCS-CHALLENGE"


@dataclass
class ExpireEvent(GovernanceEvent):
    """ORCS-EXPIRE event. Fired when ratification expires. Moves to under_review."""

    expired_ratification_id: str = ""

    def __post_init__(self):
        if not self.event_type:
            self.event_type = "ORCS-EXPIRE"


@dataclass
class AuditEvent(GovernanceEvent):
    """ORCS-AUDIT event. Logs an audit event (no state change)."""

    event_subtype: str = ""
    details: str = ""
    compatible_result: Optional[str] = None  # TRUE | FALSE | HOLD
    gate_states: Optional[dict] = None

    def __post_init__(self):
        if not self.event_type:
            self.event_type = "ORCS-AUDIT"
