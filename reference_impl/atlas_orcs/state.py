"""
Atlas/ORCS State Definitions
NOT CANON — NOT DEPLOYABLE — reference implementation only

Defines the artifact trust state space (Sigma) for the Atlas/ORCS system.
See: archive/spec/gptdream/appendices/APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md
"""

from enum import Enum


class TrustState(str, Enum):
    """
    The trust state space Sigma for Atlas/ORCS artifacts.
    Authority is a state transition, not a vibe.
    """

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
    CANDIDATE = "candidate"
    RATIFIED_CANON = "ratified_canon"


class DeploymentStatus(str, Enum):
    NOT_DEPLOYABLE = "not_deployable"
    REVIEW_PENDING = "review_pending"
    APPROVED = "approved"
    DEPLOYED = "deployed"


class AuthorityScope(str, Enum):
    NONE = "none"
    LOCAL = "local"
    COUNCIL = "council"
    RATIFIED_CANON = "ratified_canon"


class EpistemicLabel(str, Enum):
    WORKING = "working"
    CANDIDATE = "candidate"
    REVIEWED = "reviewed"
    RATIFIED = "ratified"


class RawExportStatus(str, Enum):
    FULL_RAW = "full_raw"
    PARTIAL_RAW = "partial_raw"
    SUMMARY_ONLY = "summary_only"
    UNAVAILABLE = "unavailable"


class CompatibleResult(str, Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
    HOLD = "HOLD"


# Permitted state transitions (from → to)
# This is the directed acyclic graph of valid edges.
PERMITTED_TRANSITIONS: set[tuple[TrustState, TrustState]] = {
    (TrustState.RAW, TrustState.PARSED),
    (TrustState.PARSED, TrustState.CANDIDATE),
    (TrustState.PARSED, TrustState.QUARANTINED),
    (TrustState.CANDIDATE, TrustState.REVIEWED),
    (TrustState.CANDIDATE, TrustState.REJECTED),
    (TrustState.CANDIDATE, TrustState.QUARANTINED),
    (TrustState.REVIEWED, TrustState.RATIFIED),
    (TrustState.REVIEWED, TrustState.REJECTED),
    (TrustState.RATIFIED, TrustState.ACTIVE),
    (TrustState.RATIFIED, TrustState.UNDER_REVIEW),
    (TrustState.ACTIVE, TrustState.UNDER_REVIEW),
    (TrustState.ACTIVE, TrustState.SUPERSEDED),
    (TrustState.ACTIVE, TrustState.REVOKED),
    (TrustState.UNDER_REVIEW, TrustState.REVIEWED),
    (TrustState.UNDER_REVIEW, TrustState.REVOKED),
    (TrustState.QUARANTINED, TrustState.REVIEWED),
    (TrustState.QUARANTINED, TrustState.REVOKED),
}

# Transitions that require specific governance events
GOVERNANCE_REQUIRED_TRANSITIONS: dict[tuple[TrustState, TrustState], str] = {
    (TrustState.REVIEWED, TrustState.RATIFIED): "ORCS-RATIFY",
    (TrustState.RATIFIED, TrustState.ACTIVE): "ORCS-PROMOTE",
    (TrustState.ACTIVE, TrustState.REVOKED): "ORCS-REVOKE",
    (TrustState.QUARANTINED, TrustState.REVIEWED): "ORCS-REVIEW",  # after remediation
}
