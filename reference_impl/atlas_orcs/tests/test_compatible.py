from __future__ import annotations

from reference_impl.atlas_orcs.compatible import compatible, compatible_path


def test_canon_increase_without_ratification_fails_even_if_locally_valid() -> None:
    edge = {
        "local_valid": True,
        "from": {"canon": "NOT_CANON"},
        "to": {"canon": "RATIFIED_CANON"},
        "governance_delta": {},
    }
    assert compatible(edge) == "FALSE"


def test_receipt_only_cannot_become_proof_without_attestation() -> None:
    edge = {
        "local_valid": True,
        "from": {"proof": "RECEIPT_ONLY"},
        "to": {"proof": "PROOF"},
        "governance_delta": {},
    }
    assert compatible(edge) == "FALSE"


def test_public_visibility_cannot_become_authority_without_grant() -> None:
    edge = {
        "local_valid": True,
        "from": {"public_claim": "PUBLIC_VISIBLE", "authority": "QUERY_ONLY"},
        "to": {"public_claim": "PUBLIC_VISIBLE", "authority": "GOVERNED"},
        "governance_delta": {},
    }
    assert compatible(edge) == "FALSE"


def test_hold_blocks_promotion() -> None:
    edge = {
        "local_valid": True,
        "hold": True,
        "from": {"canon": "NOT_CANON"},
        "to": {"canon": "CANDIDATE"},
        "governance_delta": {"ratification_event_id": "evt-1"},
    }
    assert compatible(edge) == "HOLD"


def test_false_blocks_path() -> None:
    path = [
        {
            "local_valid": True,
            "from": {"canon": "NOT_CANON"},
            "to": {"canon": "CANDIDATE"},
            "governance_delta": {"ratification_event_id": "evt-1"},
        },
        {
            "local_valid": True,
            "from": {"canon": "CANDIDATE"},
            "to": {"canon": "RATIFIED_CANON"},
            "governance_delta": {},
        },
    ]
    assert compatible_path(path) is False


def test_authorized_path_passes() -> None:
    path = [
        {
            "local_valid": True,
            "from": {
                "canon": "NOT_CANON",
                "proof": "RECEIPT_ONLY",
                "public_claim": "PRIVATE",
                "authority": "QUERY_ONLY",
                "deployment": "NON_DEPLOYABLE",
            },
            "to": {
                "canon": "CANDIDATE",
                "proof": "PROOF",
                "public_claim": "PUBLIC_VISIBLE",
                "authority": "FORMALIZATION_ONLY",
                "deployment": "CANDIDATE_ONLY",
            },
            "governance_delta": {
                "ratification_event_id": "evt-1",
                "proof_attestation_id": "att-1",
                "public_claim_approval_id": "pub-1",
                "authority_grant_id": "auth-1",
                "deployment_approval_id": "dep-1",
            },
        }
    ]
    assert compatible_path(path) is True
