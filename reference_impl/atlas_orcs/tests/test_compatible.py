from reference_impl.atlas_orcs.compatible import compatible_path, launder, Decision


# ---------------------------------------------------------------------------
# Original acceptance tests (MODULE 4 spec)
# ---------------------------------------------------------------------------

def test_canon_increase_without_governance_fails():
    path = [{"local_valid": True, "before": {"canon": "not_canon"}, "after": {"canon": "ratified"}, "governance_delta_permitted": False}]
    assert compatible_path(path) == Decision.FALSE


def test_receipt_only_cannot_become_proof():
    path = [{"local_valid": True, "before": {"proof": "receipt"}, "after": {"proof": "proof"}, "governance_delta_permitted": False}]
    assert compatible_path(path) == Decision.FALSE


def test_public_visibility_not_authority():
    path = [{"local_valid": True, "before": {"public_claim": "visible"}, "after": {"authority": "official"}, "governance_delta_permitted": False}]
    assert compatible_path(path) == Decision.FALSE


def test_hold_blocks_promotion():
    path = [{"local_valid": True, "hold": True, "before": {}, "after": {}}]
    assert compatible_path(path) == Decision.HOLD


def test_false_blocks_path():
    path = [{"local_valid": False, "before": {}, "after": {}}]
    assert compatible_path(path) == Decision.FALSE


# ---------------------------------------------------------------------------
# Ordinal / direction tests — decreases are NOT laundering
# ---------------------------------------------------------------------------

def test_status_decrease_not_laundering():
    """Revoking canon (ratified → not_canon) must not trigger launder."""
    path = [{"local_valid": True, "before": {"canon": "ratified"}, "after": {"canon": "not_canon"}, "governance_delta_permitted": False}]
    assert compatible_path(path) == Decision.TRUE


def test_deployment_decrease_not_laundering():
    """Pulling deployment (deployable → not_deployable) is safe without a delta."""
    path = [{"local_valid": True, "before": {"deployment": "deployable"}, "after": {"deployment": "not_deployable"}, "governance_delta_permitted": False}]
    assert compatible_path(path) == Decision.TRUE


def test_no_status_change_not_laundering():
    """Same before and after → TRUE."""
    path = [{"local_valid": True, "before": {"canon": "candidate"}, "after": {"canon": "candidate"}, "governance_delta_permitted": False}]
    assert compatible_path(path) == Decision.TRUE


def test_proof_increase_allowed_with_permitted_delta():
    """receipt → proof is fine when governance_delta_permitted=True."""
    path = [{"local_valid": True, "before": {"proof": "receipt"}, "after": {"proof": "proof"}, "governance_delta_permitted": True}]
    assert compatible_path(path) == Decision.TRUE


def test_authority_increase_allowed_with_permitted_delta():
    """none → official is allowed with an explicit delta."""
    path = [{"local_valid": True, "before": {"authority": "none"}, "after": {"authority": "official"}, "governance_delta_permitted": True}]
    assert compatible_path(path) == Decision.TRUE


# ---------------------------------------------------------------------------
# Priority: FALSE > HOLD
# ---------------------------------------------------------------------------

def test_false_takes_priority_over_hold():
    """A path with a HOLD edge followed by a FALSE edge must return FALSE."""
    path = [
        {"local_valid": True, "hold": True, "before": {}, "after": {}},
        {"local_valid": False, "before": {}, "after": {}},
    ]
    assert compatible_path(path) == Decision.FALSE


def test_hold_returned_when_no_false():
    """HOLD is returned when no edge is FALSE."""
    path = [
        {"local_valid": True, "hold": True, "before": {}, "after": {}},
        {"local_valid": True, "before": {}, "after": {}},
    ]
    assert compatible_path(path) == Decision.HOLD


# ---------------------------------------------------------------------------
# Multi-edge path laundering
# ---------------------------------------------------------------------------

def test_multi_edge_laundering_in_later_edge():
    """Clean early edges should not mask laundering in a later edge."""
    path = [
        {"local_valid": True, "before": {}, "after": {}, "governance_delta_permitted": False},
        {"local_valid": True, "before": {"canon": "candidate"}, "after": {"canon": "ratified"}, "governance_delta_permitted": False},
    ]
    assert compatible_path(path) == Decision.FALSE


def test_multi_edge_all_clean():
    """Multiple clean edges → TRUE."""
    path = [
        {"local_valid": True, "before": {"canon": "candidate"}, "after": {"canon": "candidate"}, "governance_delta_permitted": False},
        {"local_valid": True, "before": {"proof": "receipt"}, "after": {"proof": "receipt"}, "governance_delta_permitted": False},
    ]
    assert compatible_path(path) == Decision.TRUE


def test_empty_path_is_true():
    """An empty path has no laundering and all (zero) edges TRUE → TRUE."""
    assert compatible_path([]) == Decision.TRUE


# ---------------------------------------------------------------------------
# launder() unit tests
# ---------------------------------------------------------------------------

def test_launder_false_when_permitted():
    edges = [{"before": {"canon": "not_canon"}, "after": {"canon": "ratified"}, "governance_delta_permitted": True}]
    assert launder(edges) is False


def test_launder_true_on_authority_increase():
    edges = [{"before": {"authority": "none"}, "after": {"authority": "official"}, "governance_delta_permitted": False}]
    assert launder(edges) is True


def test_launder_false_on_authority_decrease():
    edges = [{"before": {"authority": "official"}, "after": {"authority": "none"}, "governance_delta_permitted": False}]
    assert launder(edges) is False


def test_launder_true_when_any_dimension_increases():
    edges = [{
        "before": {"canon": "candidate", "proof": "receipt"},
        "after": {"canon": "candidate", "proof": "proof"},
        "governance_delta_permitted": False,
    }]
    assert launder(edges) is True


def test_launder_true_with_unknown_to_known_status_upgrade():
    edges = [{
        "before": {"authority": "unknown"},
        "after": {"authority": "official"},
        "governance_delta_permitted": False,
    }]
    assert launder(edges) is True


def test_compatible_path_true_for_status_downgrade_with_unknown_target():
    path = [{
        "local_valid": True,
        "before": {"proof": "proof"},
        "after": {"proof": "unknown"},
        "governance_delta_permitted": False,
    }]
    assert compatible_path(path) == Decision.TRUE
