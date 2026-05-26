from __future__ import annotations

from reference_impl.receipt_foundry.validator import validate_receipt_habitat_claim


SAMPLES = {
    "candidate_to_reviewed_missing_receipt": {
        "previous_claim_state": "candidate",
        "claim_state": "reviewed",
        "evidence_refs": ["archive/boot/gptbrain/CLAIM_LEDGER.seed.jsonl#1"],
    },
    "reviewed_to_ratified_missing_governance": {
        "previous_claim_state": "reviewed",
        "claim_state": "ratified",
        "evidence_refs": ["archive/boot/gptbrain/CLAIM_LEDGER.seed.jsonl#1"],
        "receipt_metadata": {
            "receipt_id": "rcp-001",
            "receipt_type": "trace",
            "receipt_hash": "abc123",
        },
    },
    "summary_promoted_to_source": {
        "claim_state": "reviewed",
        "evidence_refs": ["summary-thread"],
        "receipt_metadata": {
            "receipt_id": "rcp-002",
            "receipt_type": "summary",
            "receipt_hash": "def456",
        },
        "source_basis": "summary_only",
        "source_status": "source",
    },
}


def main() -> int:
    print("== Receipt Foundry Dry Run ==")
    failed = 0
    for name, sample in SAMPLES.items():
        errors = validate_receipt_habitat_claim(sample)
        print(f"{name}: {'FAIL' if errors else 'PASS'}")
        if errors:
            failed += 1
            for err in errors:
                print(f"  - {err}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
