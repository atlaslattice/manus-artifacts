# CLAIM_LEDGER_SCHEMA_v0.1

```text
STATUS: CANDIDATE SCHEMA
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
PURPOSE: convert claims into inspectable units linked to artifacts, receipts, MissingReceipts, and review lanes
```

## Claim record

```yaml
claim_id:
claim_text:
claim_type: factual | operational_metric | symbolic | mathematical | governance | deployment | public_release | vendor_alignment | rights_license | other
source_artifacts: []
linked_receipts: []
linked_missing_receipts: []
evidence_required:
evidence_present:
receipt_status: missing | search_hit_only | partial_content | full_export_present | hash_present | independently_verified | blocked | superseded
overclaim_risk: low | medium | high | critical
unsafe_wording: []
safe_wording:
forbidden_claims: []
review_lane:
owner_lane:
status: open | review_needed | receipt_needed | verified_limited | superseded | blocked
```

## Claim type guide

```yaml
factual:
  example: "Issue #233 exists."
  evidence_required: source link or fetched issue

operational_metric:
  example: "63 tests passing."
  evidence_required: CI/test log, commit SHA, reproducible command

symbolic:
  example: "The lattice hums."
  evidence_required: none unless converted into factual/operational claim

mathematical:
  example: "1728 nodes are indexed."
  evidence_required: graph export/query if measured; definition if theoretical target

governance:
  example: "This is canon."
  evidence_required: human-root/website governance receipt

deployment:
  example: "This is live."
  evidence_required: runtime/deployment receipt

vendor_alignment:
  example: "OpenAI-first workflow."
  evidence_required: design artifact; avoid endorsement implication
```

## Overclaim risk levels

```yaml
low: wording is clearly candidate or symbolic
medium: wording may imply stronger support than receipts show
high: wording implies verified/canon/deployed without receipt
critical: wording implies external endorsement, public release, safety status, or proof without receipt
```

## Sample claim

```yaml
claim_id: CLAIM-P0-001
claim_text: "GPTDream++ spec vault has 63 tests passing."
claim_type: operational_metric
source_artifacts:
  - MISSING_RECEIPTS_P0_2026-05-30
linked_receipts: []
linked_missing_receipts:
  - MR-P0-001-GPTDREAM-63-TESTS
evidence_required: "CI/test log, commit SHA, test suite path, reproducible command"
evidence_present: "P0 missing receipt ledger only"
receipt_status: missing
overclaim_risk: high
unsafe_wording:
  - "63 tests passing"
  - "tests verified"
safe_wording: >
  GPTDream++ candidate artifacts exist, but the “63 tests passing” metric is pending CI/test receipt.
forbidden_claims:
  - "verified"
  - "all tests pass"
  - "production-ready"
review_lane: Module 12 Validation / CI / Red-Team Harness
owner_lane: Validation / CI
status: receipt_needed
```

## Acceptance rule

A claim may be repeated publicly only if it has safe wording and visible receipt status.

## Keeper

```text
A claim is not a crown.
It is a handle for review.
```
