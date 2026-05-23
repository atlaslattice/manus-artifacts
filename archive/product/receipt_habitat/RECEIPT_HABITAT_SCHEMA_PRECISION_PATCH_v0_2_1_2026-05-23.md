---
artifact_id: RECEIPT-HABITAT-SCHEMA-PRECISION-PATCH-v0.2.1
title: "Receipt Habitat Schema — Precision Patch v0.2.1"
version: "0.2.1"
date: 2026-05-23
layer: ontology_candidate
status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
proof_status: not_a_proof
release_class: PRIVATE_REVIEW
applies_to: RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.2
raw_export_status: uploaded_text
receipt_status: >
  Derived from second Atlas Prime pass on Horizon Ledger Q41-Q45, ingested 2026-05-23.
  Richer formal source than first pass. Adds ClaimState vector tuple, SynthesisResult meet-semilattice,
  HumanRootAuthority Shamir/VSS/enclave, SeatContinuity epoch verification,
  and Q45 delta_receipt multiplicative formula. Q46-Q60 still truncated at this patch stage.
mutation_rule: >
  No field mutation without receipted change request. No canon promotion without human-root ratification.
---

# Receipt Habitat Schema — Precision Patch v0.2.1

```text
STATUS: candidate — not canon / not deployed / not ratified
RELEASE: PRIVATE_REVIEW
APPLIES: v0.2 delta on delta — read v0.1 + v0.2 + v0.2.1 together
SCOPE: Precision refinements only — no new objects, count stays at 12
PENDING: Q46–Q60 full text — Object 13 may follow
```

## Patch Register

| ID | Object | v0.2 form | v0.2.1 upgrade | Source |
|---|---|---|---|---|
| P1 | ClaimState | 5 named fields | Formal tuple with vector components | Q41 |
| P2 | SynthesisResult | highest_severity_wins prose | Gamma = meet(v_i); paraconsistent | Q42 |
| P3 | HumanRootAuthority | revocable authority object | Shamir t-of-n + Feldman VSS + hardware enclave | Q43 |
| P4 | SeatContinuity | persistent_identity=false | Epoch-step verification; ephemeral record | Q44 |
| P5 | ClaimState invariant | Confidence(P) <= Confidence(R) | Confidence(P) <= Confidence(R) * delta_receipt | Q45 |

## P1 — ClaimState Formal Tuple

```text
ClaimState = < C_semantic_vector, E_epistemic, R_evidence_vector, A_authority, P_operation >
```

Semantic content and evidence become vectors. Epistemic status, authority, and operational permission remain scalar enums.

Required implementation caution:

```text
Vector basis and calibration status must be explicit before implementation.
No vector may be treated as calibrated merely because it is typed.
```

## P2 — SynthesisResult Meet-Semilattice

Verdict ordering:

```text
BLOCK < PATCH < APPROVE
```

Aggregation:

```text
Gamma = meet(v_i)
```

Meaning:

```text
One BLOCK returns BLOCK overall. Majority signal is informational only.
Gamma is the binding routing verdict.
```

## P3 — HumanRootAuthority Cryptographic Design Target

The patch specifies Shamir threshold sharing, Feldman VSS, hardware-isolated reconstruction, and time-locked delegates.

Boundary:

```text
CRYPTOGRAPHIC PROTOCOL SPECIFICATION — not a deployed implementation.
No HSM, TEE, or key material exists until built and receipted.
Shamir/Feldman are standard protocols; implementation remains open blocker.
```

## P4 — SeatContinuity Epoch-Step Verification

At each epoch boundary:

```text
1. Prior epoch seat record expires.
2. New epoch record is created.
3. Seat must re-establish continuity credentials.
4. Authority does not carry forward without explicit receipt.
5. epoch_verified=false means no active seat.
```

Open blocker:

```text
Epoch definition requires convenor/human-root ratification.
```

## P5 — Epistemic Laundering Multiplicative Formula

```text
Confidence(P) <= Confidence(R) * delta_receipt
```

where:

```text
delta_receipt in (0,1]
```

Boundary:

```text
At this patch stage, default delta values remain candidate unless separately ratified.
Only human ratification receipt permits delta_receipt = 1.0.
```

## Sprint Impact

```text
Sprint 0: unaffected. Objects 1–8 only.
Sprint 1: Objects 9–12 use this precision patch.
```

## Keeper

```text
Vectors prevent scalar lies.
Meet-semilattice preserves blockers.
Human-root crypto is design until provisioned.
Seat continuity expires unless re-receipted.
Derived confidence decays unless evidence renews it.
Sprint 0 stays boring.
```