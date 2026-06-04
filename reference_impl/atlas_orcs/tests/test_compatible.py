"""
Tests for Atlas / ORCS compatible() anti-laundering predicate.

STATUS: CANDIDATE TESTS — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
"""

import pytest
from reference_impl.atlas_orcs.state import TrustState, CanonStatus, DeploymentStatus
from reference_impl.atlas_orcs.delta import GovernanceDelta, EventType
from reference_impl.atlas_orcs.compatible import (
    Edge, GovernanceContext, compatible_edge, compatible_path, launder
)


# ── Helpers ──────────────────────────────────────────────────────────────────

def default_context() -> GovernanceContext:
    return GovernanceContext(
        recognized_authorities=["council-authority-001", "human-adjudicator"],
    )


def make_edge(
    from_state=TrustState.CANDIDATE,
    to_state=TrustState.REVIEWED,
    event_type=EventType.GOVERNANCE,
    authority_key="council-authority-001",
    human=True,
    evidence=None,
    canon_before=CanonStatus.NOT_CANON,
    canon_after=CanonStatus.NOT_CANON,
    deploy_before=DeploymentStatus.NOT_DEPLOYABLE,
    deploy_after=DeploymentStatus.NOT_DEPLOYABLE,
    authority_before="none",
    authority_after="none",
    proof_before=False,
    proof_after=False,
    public_before=False,
    public_after=False,
) -> Edge:
    delta = GovernanceDelta(
        event_type=event_type,
        authority_key=authority_key,
        artifact_id="test-artifact",
        previous_state=from_state,
        new_state=to_state,
        evidence_refs=evidence or ["evidence-001"],
        human_permission=human,
        delta_id="delta-test-001",
    )
    return Edge(
        artifact_id="test-artifact",
        from_state=from_state,
        to_state=to_state,
        delta=delta,
        canon_before=canon_before,
        canon_after=canon_after,
        deployment_before=deploy_before,
        deployment_after=deploy_after,
        authority_before=authority_before,
        authority_after=authority_after,
        proof_before=proof_before,
        proof_after=proof_after,
        public_claim_before=public_before,
        public_claim_after=public_after,
    )


# ── Test: Valid edge returns TRUE ─────────────────────────────────────────

def test_valid_edge_returns_true():
    edge = make_edge(TrustState.CANDIDATE, TrustState.REVIEWED)
    ctx = default_context()
    assert compatible_edge(edge, ctx) == "TRUE"


# ── Test: Unpermitted transition returns FALSE ────────────────────────────

def test_unpermitted_transition_returns_false():
    edge = make_edge(TrustState.RAW, TrustState.RATIFIED)  # Skips required steps
    ctx = default_context()
    result = compatible_edge(edge, ctx)
    assert result == "FALSE"


# ── Test: Canon inflation without ratification returns FALSE ─────────────

def test_canon_inflation_without_ratification_returns_false():
    """Path with all locally valid edges still fails if canon status increases
    without ratification."""
    edge = make_edge(
        from_state=TrustState.CANDIDATE,
        to_state=TrustState.REVIEWED,
        event_type=EventType.GOVERNANCE,  # Not a ratification event
        canon_before=CanonStatus.NOT_CANON,
        canon_after=CanonStatus.RATIFIED_CANON,  # Canon increased!
    )
    ctx = default_context()
    result = compatible_edge(edge, ctx)
    assert result == "FALSE"


# ── Test: Receipt cannot become proof ────────────────────────────────────

def test_receipt_cannot_become_proof():
    """Path with receipt only cannot become proof."""
    edge = make_edge(
        from_state=TrustState.PARSED,
        to_state=TrustState.CANDIDATE,
        event_type=EventType.GOVERNANCE,
        proof_before=False,
        proof_after=True,  # Proof status increased!
        # No independent_verification on delta
    )
    ctx = default_context()
    result = compatible_edge(edge, ctx)
    assert result == "FALSE"


# ── Test: Public visibility cannot become authority ───────────────────────

def test_public_visibility_cannot_become_authority():
    """Public claim gained without publicity_authorization → HOLD."""
    edge = make_edge(
        from_state=TrustState.CANDIDATE,
        to_state=TrustState.REVIEWED,
        public_before=False,
        public_after=True,  # Gained public visibility without authorization
    )
    ctx = default_context()
    result = compatible_edge(edge, ctx)
    assert result == "HOLD"


# ── Test: HOLD blocks promotion ───────────────────────────────────────────

def test_hold_blocks_path():
    """A HOLD on any edge blocks the entire path."""
    e1 = make_edge(TrustState.RAW, TrustState.PARSED)
    e2 = make_edge(TrustState.PARSED, TrustState.CANDIDATE)
    # e3 has HOLD (public claim without authorization)
    e3 = make_edge(
        TrustState.CANDIDATE, TrustState.REVIEWED,
        public_before=False, public_after=True
    )
    path = [e1, e2, e3]
    ctx = default_context()
    assert compatible_path(path, ctx) is False


# ── Test: FALSE blocks path ───────────────────────────────────────────────

def test_false_blocks_path():
    """A FALSE on any edge blocks the entire path."""
    e1 = make_edge(TrustState.RAW, TrustState.PARSED)
    e2 = make_edge(TrustState.RAW, TrustState.RATIFIED)  # Invalid — FALSE
    path = [e1, e2]
    ctx = default_context()
    assert compatible_path(path, ctx) is False


# ── Test: Launder detection — canon inflation across path ─────────────────

def test_launder_detects_canon_inflation_without_ratification():
    """Launder returns True when canon increases without ratification across path."""
    e1 = make_edge(
        TrustState.CANDIDATE, TrustState.REVIEWED,
        event_type=EventType.GOVERNANCE,
        canon_before=CanonStatus.NOT_CANON,
        canon_after=CanonStatus.NOT_CANON,
    )
    e2 = make_edge(
        TrustState.REVIEWED, TrustState.REVIEWED,
        event_type=EventType.GOVERNANCE,
        canon_before=CanonStatus.NOT_CANON,
        canon_after=CanonStatus.RATIFIED_CANON,  # Jumped to canon without ratification
    )
    path = [e1, e2]
    ctx = default_context()
    assert launder(path, ctx) is True


# ── Test: Valid path with ratification does not launder ───────────────────

def test_valid_ratification_path_does_not_launder():
    """A path with a proper ratification event does not launder."""
    e1 = make_edge(TrustState.CANDIDATE, TrustState.REVIEWED)
    e2 = make_edge(
        TrustState.REVIEWED, TrustState.RATIFIED,
        event_type=EventType.RATIFICATION,
        authority_key="council-authority-001",
        human=True,
        canon_before=CanonStatus.NOT_CANON,
        canon_after=CanonStatus.CANDIDATE_CANON,
        authority_before="none",
        authority_after="ratified",
    )
    path = [e1, e2]
    ctx = default_context()
    assert launder(path, ctx) is False


# ── Test: Empty path is compatible ────────────────────────────────────────

def test_empty_path_is_compatible():
    ctx = default_context()
    assert compatible_path([], ctx) is True
    assert launder([], ctx) is False
