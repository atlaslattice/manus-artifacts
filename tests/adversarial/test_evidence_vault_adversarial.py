import json
from pathlib import Path

from reference_impl.atlas_orcs.evidence_vault import (
    BenchmarkClaim,
    PublicClaim,
    benchmark_publish_allowed,
    evaluate_public_claim,
)


def _load_cases():
    fixture = (
        Path(__file__).resolve().parents[2] / "fixtures" / "evidence_vault.adversarial.json"
    )
    return json.loads(fixture.read_text(encoding="utf-8"))


def test_evidence_vault_adversarial_cases():
    for case in _load_cases():
        if "benchmark_claim" in case:
            claim = BenchmarkClaim(**case["benchmark_claim"])
            assert benchmark_publish_allowed(claim) is case["expected_publish_allowed"], case["test_id"]

        if "public_claim" in case:
            public_claim = PublicClaim(**case["public_claim"])
            result = evaluate_public_claim(public_claim)
            assert result["quarantine_status"] == case["expected_quarantine_status"], case["test_id"]
            assert result["publish_allowed"] is case["expected_publish_allowed"], case["test_id"]
