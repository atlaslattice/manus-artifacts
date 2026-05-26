"""
Atlas / ORCS Compatible Anti-Laundering Predicate.

STATUS: CANDIDATE IMPLEMENTATION — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE

compatible_Γ(edge) ∈ {TRUE, FALSE, HOLD}

compatible_path_Γ(path)
= all edges TRUE AND NOT launder(path)

A path launders if authority, canon, deployment, proof, or public-claim status
increases without an explicit permitted governance delta.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Literal, Optional
from .state import TrustState, CanonStatus, DeploymentStatus
from .delta import GovernanceDelta, EventType
from .transitions import PERMITTED_TRANSITIONS


CompatibleResult = Literal["TRUE", "FALSE", "HOLD"]


@dataclass
class Edge:
    """An edge in a transition path."""
    artifact_id: str
    from_state: TrustState
    to_state: TrustState
    delta: GovernanceDelta
    canon_before: CanonStatus = CanonStatus.NOT_CANON
    canon_after: CanonStatus = CanonStatus.NOT_CANON
    deployment_before: DeploymentStatus = DeploymentStatus.NOT_DEPLOYABLE
    deployment_after: DeploymentStatus = DeploymentStatus.NOT_DEPLOYABLE
    authority_before: str = "none"
    authority_after: str = "none"
    proof_before: bool = False
    proof_after: bool = False
    public_claim_before: bool = False
    public_claim_after: bool = False


@dataclass
class GovernanceContext:
    """The governance context Γ."""
    recognized_authorities: List[str] = field(default_factory=list)
    permitted_ratification_event_types: List[str] = field(
        default_factory=lambda: [EventType.RATIFICATION]
    )
    permitted_governance_event_types: List[str] = field(
        default_factory=lambda: [EventType.GOVERNANCE, EventType.DEPLOYMENT]
    )


def compatible_edge(edge: Edge, context: GovernanceContext) -> CompatibleResult:
    """
    Evaluate a single edge.

    Returns:
      TRUE  — edge is permitted and does not begin laundering
      FALSE — edge is not permitted; block
      HOLD  — edge is locally permitted but requires review
    """
    from_state = edge.from_state
    to_state = edge.to_state
    delta = edge.delta

    # Check if base transition is permitted
    if (from_state, to_state) not in PERMITTED_TRANSITIONS:
        return "FALSE"

    # Check delta validity
    if not delta.is_valid():
        return "FALSE"

    # Ratification: requires explicit ratification_event + human permission
    if to_state == TrustState.RATIFIED:
        if delta.event_type != EventType.RATIFICATION:
            return "FALSE"
        if not delta.human_permission:
            return "FALSE"
        if delta.authority_key not in context.recognized_authorities:
            return "FALSE"

    # Canon inflation check
    canon_order = {
        CanonStatus.NOT_CANON: 0,
        CanonStatus.CANDIDATE_CANON: 1,
        CanonStatus.RATIFIED_CANON: 2,
    }
    if canon_order[edge.canon_after] > canon_order[edge.canon_before]:
        # Canon increased — requires ratification_event
        if delta.event_type != EventType.RATIFICATION:
            return "FALSE"
        if not delta.human_permission:
            return "FALSE"

    # Deployment inflation check
    deploy_order = {
        DeploymentStatus.NOT_DEPLOYABLE: 0,
        DeploymentStatus.DEPLOYMENT_CANDIDATE: 1,
        DeploymentStatus.DEPLOYED: 2,
    }
    if deploy_order[edge.deployment_after] > deploy_order[edge.deployment_before]:
        # Deployment increased — requires governance_event
        if delta.event_type not in context.permitted_governance_event_types:
            return "FALSE"

    # Proof inflation check: receipt cannot become proof
    if edge.proof_after and not edge.proof_before:
        # Proof status increased without independent verification marker
        if not getattr(delta, 'independent_verification', False):
            return "FALSE"

    # Public claim inflation check
    if edge.public_claim_after and not edge.public_claim_before:
        # Public visibility gained — requires explicit authorization
        if not getattr(delta, 'publicity_authorization', False):
            return "HOLD"

    # Authority inflation check
    authority_order = {"none": 0, "local": 1, "reviewed": 2, "ratified": 3, "canon": 4}
    before_rank = authority_order.get(edge.authority_before, 0)
    after_rank = authority_order.get(edge.authority_after, 0)
    if after_rank > before_rank:
        if delta.event_type != EventType.RATIFICATION:
            return "FALSE"
        if not delta.human_permission:
            return "FALSE"

    return "TRUE"


def launder(path: List[Edge], context: GovernanceContext) -> bool:
    """
    Return True if this path launders authority, canon, deployment,
    proof, or public-claim status without explicit permitted governance delta.

    Laundering: status increases without authorized delta.
    """
    canon_order = {
        CanonStatus.NOT_CANON: 0,
        CanonStatus.CANDIDATE_CANON: 1,
        CanonStatus.RATIFIED_CANON: 2,
    }
    deploy_order = {
        DeploymentStatus.NOT_DEPLOYABLE: 0,
        DeploymentStatus.DEPLOYMENT_CANDIDATE: 1,
        DeploymentStatus.DEPLOYED: 2,
    }
    authority_order = {"none": 0, "local": 1, "reviewed": 2, "ratified": 3, "canon": 4}

    if not path:
        return False

    # Track cumulative status across path
    initial_canon = path[0].canon_before
    initial_deploy = path[0].deployment_before
    initial_authority = path[0].authority_before
    initial_proof = path[0].proof_before
    initial_public = path[0].public_claim_before

    final_canon = path[-1].canon_after
    final_deploy = path[-1].deployment_after
    final_authority = path[-1].authority_after
    final_proof = path[-1].proof_after
    final_public = path[-1].public_claim_after

    # L-1: Authority inflation
    if authority_order.get(final_authority, 0) > authority_order.get(initial_authority, 0):
        # Check if any edge had a valid ratification delta
        has_ratification = any(
            e.delta.event_type == EventType.RATIFICATION
            and e.delta.human_permission
            and e.delta.is_valid()
            for e in path
        )
        if not has_ratification:
            return True

    # L-2: Canon inflation
    if canon_order[final_canon] > canon_order[initial_canon]:
        has_ratification = any(
            e.delta.event_type == EventType.RATIFICATION
            and e.delta.human_permission
            and e.delta.is_valid()
            for e in path
        )
        if not has_ratification:
            return True

    # L-3: Deployment inflation
    if deploy_order[final_deploy] > deploy_order[initial_deploy]:
        has_governance = any(
            e.delta.event_type in context.permitted_governance_event_types
            and e.delta.is_valid()
            for e in path
        )
        if not has_governance:
            return True

    # L-4: Proof inflation (receipt → proof)
    if final_proof and not initial_proof:
        has_verification = any(
            getattr(e.delta, 'independent_verification', False)
            for e in path
        )
        if not has_verification:
            return True

    # L-5: Public claim inflation
    if final_public and not initial_public:
        has_authorization = any(
            getattr(e.delta, 'publicity_authorization', False)
            for e in path
        )
        if not has_authorization:
            return True

    return False


def compatible_path(path: List[Edge], context: GovernanceContext) -> bool:
    """
    Return True if the path is compatible (all edges TRUE AND NOT launder).

    A HOLD or FALSE on any edge blocks the entire path.
    """
    if not path:
        return True

    for edge in path:
        result = compatible_edge(edge, context)
        if result != "TRUE":
            return False  # HOLD or FALSE both block

    return not launder(path, context)
