from reference_impl.atlas_orcs.compatible import CompatibleDecision, compatible_path


def test_path_fails_on_canon_increase_without_ratification():
    path = [{"allowed": True, "increased": ["canon_status"], "governance_delta_permitted": False}]
    assert compatible_path(path) == CompatibleDecision.FALSE


def test_receipt_only_cannot_become_proof_without_governance_delta():
    path = [{"allowed": True, "increased": ["proof_status"], "governance_delta_permitted": False}]
    assert compatible_path(path) == CompatibleDecision.FALSE


def test_public_visibility_cannot_become_authority_without_governance_delta():
    path = [{"allowed": True, "increased": ["authority_scope"], "governance_delta_permitted": False}]
    assert compatible_path(path) == CompatibleDecision.FALSE


def test_hold_blocks_promotion():
    path = [{"allowed": True, "hold": True}]
    assert compatible_path(path) == CompatibleDecision.HOLD


def test_false_blocks_path():
    path = [{"allowed": False}]
    assert compatible_path(path) == CompatibleDecision.FALSE
