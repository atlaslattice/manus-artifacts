from reference_impl.atlas_orcs.compatible import Verdict, compatible_path


def test_canon_increase_without_ratification_fails():
    path = [
        {"verdict": "TRUE"},
        {"verdict": "TRUE", "canon_increase": True, "governance_delta": False},
    ]
    assert compatible_path(path) == Verdict.FALSE


def test_receipt_only_cannot_become_proof():
    path = [{"verdict": "TRUE", "proof_increase": True, "governance_delta": False}]
    assert compatible_path(path) == Verdict.FALSE


def test_public_visibility_cannot_become_authority():
    path = [{"verdict": "TRUE", "authority_increase": True, "governance_delta": False}]
    assert compatible_path(path) == Verdict.FALSE


def test_hold_blocks_promotion():
    assert compatible_path([{"verdict": "HOLD"}]) == Verdict.HOLD


def test_false_blocks_path():
    assert compatible_path([{"verdict": "FALSE"}]) == Verdict.FALSE
