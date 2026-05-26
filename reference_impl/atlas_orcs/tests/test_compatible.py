from reference_impl.atlas_orcs.compatible import compatible_path, Decision


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
