---
artifact_id: RECEIPT-HABITAT-SCHEMA-DELTA-v0.2.4
title: "Receipt Habitat Schema Delta v0.2.4 — Convenor Ratifications"
version: "0.2.4"
date: 2026-05-23
layer: ontology_candidate
status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
proof_status: not_a_proof
release_class: PRIVATE_REVIEW
applies_to: RECEIPT-HABITAT-SCHEMA-HL-ACCEPTANCE-PATCH-v0.2.2 + RECEIPT-HABITAT-SCHEMA-DELTA-v0.2.3
raw_export_status: uploaded_text
ratification_source: Convenor David Sheldon — chat session 2026-05-23T13:54 CDT
mutation_rule: >
  Values marked RATIFIED below are binding for Sprint 1 implementation. Epoch semantics remain pending.
  Canon promotion of the full schema still requires later consolidation and explicit human-root ratification.
---

# Receipt Habitat Schema Delta v0.2.4

## Convenor Ratifications — 2026-05-23

```text
STATUS: candidate — not canon / not deployed
RATIFIED: delta_receipt=0.6, Shamir t=3/n=5, D-101 name
PENDING: Epoch semantics for Object 12 SeatContinuity
BLOCKED: Objects 13–15 until Frontier Rigor Matrix source is resolved or replaced
SPRINT 0: Unaffected — Objects 1–8
SPRINT 1: Objects 9–12 unblocked pending epoch ruling
```

## Patch Register

| ID | Change | Blocker resolved |
|---|---|---|
| R1 | delta_receipt = 0.6 RATIFIED | B-10 |
| R2 | Shamir t=3, n=5 RATIFIED | B-09 |
| R3 | D-101 = Extreme Harm Intervention Protocol / EHIP | B-05 |
| R4 | Frontier Rigor Matrix problem_refs downgraded to unreceipted | B-01 partial |
| PENDING | Epoch semantics | B-08 |

## R1 — delta_receipt = 0.6 RATIFIED

```yaml
ClaimState:
  laundering_delta:
    value: 0.6
    ratification_status: ratified
    ratification_date: 2026-05-23
    ratification_by: david-convenor
    default_used: true
    basis: no_new_evidence
    notes: >
      Binding for Sprint 1 implementation. delta=0.6 is the floor for the no-new-evidence case.
      Other table values remain candidate pending separate review.
```

Canonical confirmed formula:

```text
Confidence(P) <= max(Confidence(R_i)) * delta_receipt
```

with:

```text
no new evidence: 0.6 RATIFIED
weak corroboration: 0.8 candidate
strong independent receipt: 0.9 candidate
human ratification receipt: 1.0 definitional / ratified by rule
```

## R2 — HumanRootAuthority t=3, n=5 RATIFIED

```yaml
HumanRootAuthority:
  key_scheme: shamir_feldman_vss
  threshold_t: 3
  total_shares_n: 5
  threshold_policy_status: ratified
  enclave_type: hsm
  enclave_required: true
  implementation_status: design_spec_only
  hardware_status: not_provisioned
  threat_model_status: required
  security_review_status: not_reviewed
```

Boundary:

```text
t/n is ratified as the target threshold, not as a deployed system.
```

## R3 — D-101 Canonical Name: EHIP

Ruling:

```text
D-101 canonical full name: Extreme Harm Intervention Protocol (EHIP)
Ruling source: Convenor David Sheldon, 2026-05-23T13:54 CDT
Ruling basis: /governance page takes precedence over /new-deal-2.0/constitution for doctrine naming.
```

Required repo action:

```text
Update any document using Environmental Health Infrastructure Protocol to read Extreme Harm Intervention Protocol.
The /new-deal-2.0/constitution environmental description is a D-101 scope note, not doctrine name.
```

## R4 — Frontier Rigor Matrix Problem References Downgraded

Finding:

```text
GANGASEEK-FRONTIER-RIGOR-MATRIX-v1.0.0 not found in confirmed chain.
Closest artifact is an Atlas Prime response candidate, not the matrix itself.
```

Ruling:

```text
Problem references on Sprint 2 objects are downgraded to unreceipted_source_unavailable.
```

Apply to:

```text
Object 13 ExecutionRiskTier
Object 14 StressTestRecord
Object 15 ArtifactClassifierMatrix
```

## Pending — Epoch Semantics

```yaml
SeatContinuity:
  epoch_type: PENDING
  epoch_type_status: pending_convenor_ruling
  epoch_type_notes: >
    Convenor instinct = per_model_context_reset. Context briefing delivered 2026-05-23. Awaiting explicit ratification.
```

## Blocker Registry — Post-v0.2.4

| Blocker | New Status |
|---|---|
| B-01 Frontier Rigor Matrix | Downgraded to labeled orphan — Sprint 2 still blocked |
| B-02 CLM-007/009 | Unchanged — no canonical anchor |
| B-03 GangaSeek namespace | Unchanged — Convenor reviewing packet |
| B-04 GangaSeek INV/CLM catalog v0.2 | Ready to produce — waiting on namespace |
| B-05 D-101 name conflict | Resolved — EHIP confirmed |
| B-06 RAT-011 D-101 proposer | Unverified — /governance re-fetch needed |
| B-07 6-tuple ClaimState | Resolved prior |
| B-08 Epoch semantics | Pending ruling |
| B-09 Shamir t/n | Resolved — t=3, n=5 ratified |
| B-10 delta_receipt | Resolved — 0.6 ratified |
| B-11 vector_basis calibration | Uncalibrated informational only |
| B-12 RAT-010 DL-IN | 3 for / 7 abstain — not yet passed |

## Updated Read Stack

```text
v0.1   → Objects 1–8
v0.2   → Objects 9–12 + Linkage delta
v0.2.1 → Precision patch
v0.2.2 → HL acceptance patch
v0.2.3 → Q46–Q60 additions
v0.2.4 → Convenor ratifications
PENDING → v0.3 consolidated schema
```

## Final Status

```text
DOCUMENT: RECEIPT-HABITAT-SCHEMA-DELTA-v0.2.4
STATUS: candidate — not canon / not deployed / not fully ratified
RATIFIED: delta=0.6, t=3/n=5, D-101=EHIP
PENDING: Epoch semantics, namespace signature
BLOCKED: Sprint 2 Frontier Rigor Matrix orphan
SPRINT 0: Objects 1–8 unblocked — begin now
NEXT: Epoch ruling → v0.3 consolidation → Sprint 0 execution
```

## Keeper

```text
Some constants are now ratified.
The schema is still candidate.
Sprint 0 can begin.
Sprint 1 awaits epoch ruling.
Sprint 2 waits for the missing matrix.
```