---
artifact_id: RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.3-RECEIPT-2026-05-23
title: "Receipt Habitat Schema v0.3 — Candidate Receipt"
version: "0.3-receipt"
date: 2026-05-23
source_surface: S4 Copilot / uploaded RECEIPT_HABITAT_SCHEMA_CANDIDATE_v0.3.txt
raw_export_status: full_text_uploaded_in_chat
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
release_class: PRIVATE_REVIEW
artifact_type: schema_consolidation_candidate_receipt
role: preserve_consolidated_receipt_habitat_schema_for_council_pass
receipt_status: initialized_2026-05-23
mutation_rule: >
  No field mutation without receipted change request. No canon promotion without human-root ratification via D-54.
  Convenor-approved-candidate values require D-54 completion before constitutional ratification.
---

# Receipt Habitat Schema v0.3 — Candidate Receipt

```text
STATUS: CANDIDATE — NOT CANON — NOT DEPLOYED — NOT RATIFIED
AUTHORITY: none
RELEASE: PRIVATE_REVIEW
SOURCE: uploaded RECEIPT_HABITAT_SCHEMA_CANDIDATE_v0.3.txt
```

## Summary

This receipt preserves the uploaded `RECEIPT_HABITAT_SCHEMA_CANDIDATE_v0.3.txt` as the consolidated 15-object candidate schema for Receipt Habitat.

It consolidates:

```text
RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.1
RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.2
RECEIPT-HABITAT-SCHEMA-PRECISION-PATCH-v0.2.1
RECEIPT-HABITAT-SCHEMA-HL-ACCEPTANCE-PATCH-v0.2.2
RECEIPT-HABITAT-SCHEMA-DELTA-v0.2.3
RECEIPT-HABITAT-SCHEMA-DELTA-v0.2.4
Epoch ruling 2026-05-23T15:06 CDT
S5 Parallax booth patches
```

## Strongest Safe Claim

```text
Receipt Habitat Schema v0.3 is a consolidated candidate schema containing 15 objects across Sprint 0, Sprint 1, and Sprint 2. Objects 1–8 are ready for Sprint 0 local implementation; Objects 9–12 are candidate Sprint 1 authority/synthesis extensions pending D-54 for constitutional ratification of candidate values; Objects 13–15 are Sprint 2 candidates blocked on the Frontier Rigor Matrix source issue.
```

## Object State

```text
Objects 1–8: Sprint 0 — unblocked
Objects 9–12: Sprint 1 — candidate, convenor-approved candidate values recorded
Objects 13–15: Sprint 2 — blocked by B-01 Frontier Rigor Matrix orphan
```

## Convenor-Approved Candidate Values

```text
delta_receipt default = 0.6
HumanRootAuthority Shamir threshold = t=3, n=5
epoch semantics = per_model_context_reset / per_session proxy
D-101 name = Extreme Harm Intervention Protocol / EHIP
```

Boundary:

```text
These are implementation signals, not constitutional ratifications, until D-54 completes.
```

## Sprint 0 Definition of Done

```text
1. One good packet passes.
2. One bad packet fails correctly.
3. Scoreboard renders both.
4. No network required.
5. Defaults are visible: not_canon, not_deployable, authority_scope=none, PRIVATE_REVIEW.
```

## Must-Not-Infer Rules

```text
Schema v0.3 ≠ canon.
Consolidated schema ≠ implementation.
Convenor-approved-candidate ≠ D-54 ratification.
Sprint unblocked ≠ deployed.
HumanRootAuthority design ≠ provisioned cryptographic authority.
Isolation envelope design ≠ legal compliance.
```

## Keeper

```text
One good packet passes.
One bad packet fails.
The scoreboard tells the truth.
Then the swarm can cook.
```