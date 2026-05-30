"""
Atlas/ORCS Compatible Anti-Laundering Predicate
NOT CANON — NOT DEPLOYABLE — reference implementation only

Implements compatible_Γ(edge) ∈ {TRUE, FALSE, HOLD}
See: archive/spec/gptdream/appendices/APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md

Authority is a state transition, not a vibe.
"""

from typing import Optional, TYPE_CHECKING
from state import (
    TrustState, CanonStatus, DeploymentStatus, AuthorityScope,
    PERMITTED_TRANSITIONS, GOVERNANCE_REQUIRED_TRANSITIONS,
    CompatibleResult,
)

if TYPE_CHECKING:
    from delta import GovernanceEvent
    from transitions import Artifact


def compatible(
    from_state: TrustState,
    to_state: TrustState,
    event: "GovernanceEvent",
    artifact: "Artifact",
) -> CompatibleResult:
    """
    compatible_Γ(edge) ∈ {TRUE, FALSE, HOLD}

    Returns:
        TRUE  — Edge is permitted; no laundering detected
        FALSE — Edge is prohibited; path must be blocked
        HOLD  — Edge is structurally permitted but governance event is missing
    """
    edge = (from_state, to_state)

    # Step 1: Is this transition in the permitted edge set?
    if edge not in PERMITTED_TRANSITIONS:
        return CompatibleResult.FALSE

    # Step 2: Does this transition require a specific governance event?
    required_event_type = GOVERNANCE_REQUIRED_TRANSITIONS.get(edge)
    if required_event_type and event.event_type != required_event_type:
        # Check if we're moving to ratified without ORCS-RATIFY → HOLD (not FALSE)
        # because the edge itself is valid but the event is wrong
        if to_state == TrustState.RATIFIED:
            return CompatibleResult.HOLD
        return CompatibleResult.HOLD

    # Step 3: Does this transition increase canon status?
    if _canon_status_increases(artifact, to_state, event):
        if not _has_ratification_event(event):
            return CompatibleResult.FALSE  # L1 laundering

    # Step 4: Does this transition increase authority scope?
    # Authority scope increase without governance event → HOLD
    if _authority_scope_increases(artifact, to_state, event):
        if not _has_governance_event(event):
            return CompatibleResult.HOLD  # L3 — needs governance event

    # Step 5: Deployment status change without governance event?
    if _deployment_status_increases(artifact, event):
        if not _has_deployment_governance_event(event):
            return CompatibleResult.HOLD  # L4

    # Step 6: Claim type promotion to proof without ratification?
    if _claim_promoted_to_proof(artifact, event):
        if not _has_proof_ratification(event):
            return CompatibleResult.FALSE  # L2 laundering

    return CompatibleResult.TRUE


def compatible_path(path: list, events: list, artifact: "Artifact") -> CompatibleResult:
    """
    compatible_path_Γ(path)
    = all edges TRUE
      AND NOT launder(path)

    Returns the first non-TRUE result encountered, or TRUE if all edges pass.
    """
    if len(path) != len(events) + 1:
        raise ValueError("path must have exactly one more element than events")

    held_position = None

    for i, event in enumerate(events):
        from_state = path[i]
        to_state = path[i + 1]

        result = compatible(
            from_state=from_state,
            to_state=to_state,
            event=event,
            artifact=artifact,
        )

        if result == CompatibleResult.FALSE:
            return CompatibleResult.FALSE

        if result == CompatibleResult.HOLD and held_position is None:
            held_position = i

    # Check for path-level laundering (L5: HOLD bypass)
    if held_position is not None:
        # Path continued past a HOLD without resolving it
        if len(events) > held_position + 1:
            return CompatibleResult.FALSE  # L5: HOLD bypass attempt

    if held_position is not None:
        return CompatibleResult.HOLD

    # Check overall path for laundering
    if _path_launders(path, events, artifact):
        return CompatibleResult.FALSE

    return CompatibleResult.TRUE


# ── Helper Predicates ─────────────────────────────────────────────────────────

def _canon_status_increases(artifact: "Artifact", to_state: TrustState, event: "GovernanceEvent") -> bool:
    """Does this transition increase canon_status?"""
    # Moving to ratified implies canon status should increase
    return to_state == TrustState.RATIFIED and artifact.canon_status == CanonStatus.NOT_CANON


def _has_ratification_event(event: "GovernanceEvent") -> bool:
    """Is this event a valid ORCS-RATIFY event?"""
    return event.event_type == "ORCS-RATIFY"


def _authority_scope_increases(
    artifact: "Artifact",
    to_state: TrustState,
    event: "GovernanceEvent",
) -> bool:
    """Does this transition increase authority scope?"""
    # Only active artifacts have elevated authority scope
    if to_state == TrustState.ACTIVE and artifact.trust_state == TrustState.RATIFIED:
        return True
    return False


def _has_governance_event(event: "GovernanceEvent") -> bool:
    """Does the event constitute a governance action?"""
    governance_events = {"ORCS-RATIFY", "ORCS-PROMOTE", "ORCS-REVOKE", "ORCS-REVIEW"}
    return event.event_type in governance_events


def _deployment_status_increases(artifact: "Artifact", event: "GovernanceEvent") -> bool:
    """Is this a deployment status change?"""
    # Look for deployment-related event types
    return event.event_type in ("ORCS-DEPLOY", "ORCS-APPROVE-DEPLOYMENT")


def _has_deployment_governance_event(event: "GovernanceEvent") -> bool:
    """Is this an explicit deployment governance event?"""
    return event.event_type in ("ORCS-DEPLOY", "ORCS-APPROVE-DEPLOYMENT")


def _claim_promoted_to_proof(artifact: "Artifact", event: "GovernanceEvent") -> bool:
    """Is a claim being promoted to proof level?"""
    return event.event_type in ("ORCS-PROMOTE-TO-PROOF",)


def _has_proof_ratification(event: "GovernanceEvent") -> bool:
    """Is this a proof-level ratification event?"""
    return (
        event.event_type == "ORCS-RATIFY"
        and hasattr(event, "ratification_scope")
        and "proof" in getattr(event, "ratification_scope", [])
    )


def _path_launders(path: list, events: list, artifact: "Artifact") -> bool:
    """
    Check if the overall path launders authority.

    A path launders if authority, canon, deployment, proof, or public-claim status
    increases without an explicit permitted governance delta.
    """
    # Count authority increases vs governance events
    authority_increases = 0
    governance_events_count = 0

    governance_event_types = {"ORCS-RATIFY", "ORCS-PROMOTE", "ORCS-REVOKE", "ORCS-REVIEW", "ORCS-DEPLOY"}

    for i, event in enumerate(events):
        if path[i] in (TrustState.REVIEWED,) and path[i + 1] in (TrustState.RATIFIED,):
            authority_increases += 1
        if event.event_type in governance_event_types:
            governance_events_count += 1

    # If authority increased more times than governance events, that's laundering
    if authority_increases > governance_events_count:
        return True

    return False
