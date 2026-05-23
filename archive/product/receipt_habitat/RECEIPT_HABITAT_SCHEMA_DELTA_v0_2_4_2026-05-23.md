---
artifact_id: RECEIPT-HABITAT-SCHEMA-DELTA-v0.2.4
title: "Receipt Habitat Schema Delta v0.2.4 — Convenor Ratifications 2026-05-23"
version: "0.2.4"
date: 2026-05-23
layer: ontology_candidate
status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
proof_status: not_a_proof
release_class: PRIVATE_REVIEW
applies_to: RECEIPT-HABITAT-SCHEMA-HL-ACCEPTANCE-PATCH-v0.2.2
                # + RECEIPT-HABITAT-SCHEMA-DELTA-v0.2.3
ratification_source: Convenor (David Sheldon) — chat session 2026-05-23T13:54 CDT
mutation_rule: >
  Values marked RATIFIED below are now binding for Sprint 1 implementation.
  Epoch semantics remain PENDING — see §5.
---

# Receipt Habitat Schema Delta v0.2.4
## Convenor Ratifications — 2026-05-23

```
STATUS:    candidate — not canon / not deployed
RATIFIED:  δ_receipt=0.6, Shamir t=3/n=5, D-101 name
PENDING:   Epoch semantics (Object 12 SeatContinuity) — awaiting Convenor
BLOCKED:   Objects 13–15 (FRONTIER-RIGOR-MATRIX orphan — source unavailable)
SPRINT 0:  Unaffected — Objects 1–8
SPRINT 1:  Objects 9–12 unblocked pending epoch ruling
```

---

## Patch Register

| ID | Change | Blocker resolved |
|----|--------|-----------------|
| R1 | δ_receipt = 0.6 RATIFIED | B-10 |
| R2 | Shamir t=3, n=5 RATIFIED | B-09 |
| R3 | D-101 = "Extreme Harm Intervention Protocol (EHIP)" | B-05 |
| R4 | FRONTIER-RIGOR-MATRIX problem_refs → unreceipted | B-01 partial |
| PENDING | Epoch semantics (Object 12) | B-08 |

---

## R1 — δ_receipt = 0.6: RATIFIED

**Prior status:** candidate (default, not binding)  
**New status:** RATIFIED by Convenor 2026-05-23

```yaml
ClaimState:
  laundering_delta:
    value:               0.6         # RATIFIED — Convenor 2026-05-23
    ratification_status: ratified    # was: candidate
    ratification_date:   2026-05-23
    ratification_by:     david-convenor
    default_used:        true
    basis:               no_new_evidence  # applies when no independent receipt
    notes: >
      Binding for Sprint 1 implementation. δ=0.6 is the floor for
      the no-new-evidence case. Scenarios with strong independent
      receipts may approach δ=1.0 per the HL-P5 table (table itself
      remains candidate pending separate review).

  laundering_delta_table_status: candidate  # table values still candidate;
                                              # only the 0.6 default is ratified
```

**Formula (canonical, confirmed):**
```
Confidence(P) ≤ max(Confidence(R_i)) · δ_receipt

where δ_receipt:
  no new evidence:              0.6  ← RATIFIED
  weak corroboration:           0.8  (candidate)
  strong independent receipt:   0.9  (candidate)
  human ratification receipt:   1.0  (definitional — ratified by rule)
```

---

## R2 — HumanRootAuthority: t=3, n=5 RATIFIED

**Prior status:** `t_value: null`, `n_value: null` (blocked)  
**New status:** RATIFIED by Convenor 2026-05-23

```yaml
HumanRootAuthority:
  key_scheme:              shamir_feldman_vss   # unchanged
  threshold_t:             3    # RATIFIED — Convenor 2026-05-23
  total_shares_n:          5    # RATIFIED — Convenor 2026-05-23
  threshold_policy_status: ratified   # was: unresolved

  # Operational meaning (3-of-5):
  # - 5 designated human-root signatories hold shares
  # - Any 3 can reconstruct the key for ratification events
  # - 2 or fewer shares reveal nothing (Shamir guarantee)
  # - Feldman VSS allows each share-holder to verify their share
  #   without a trusted dealer

  # Fields updated:
  enclave_type:            hsm        # target (design spec — not provisioned)
  enclave_required:        true
  implementation_status:   design_spec_only  # unchanged — still no hardware
  hardware_status:         not_provisioned   # unchanged
  threat_model_status:     required          # unchanged
  security_review_status:  not_reviewed      # unchanged

  # NOTE: Ratification of t/n resolves B-09. The implementation
  # boundary (design_spec_only) is unchanged — t/n is ratified as
  # the target threshold, not as a deployed system.
```

---

## R3 — D-101 Canonical Name: EHIP Ruling

**Prior status:** CONFLICT — two different full names on /governance vs /new-deal-2.0/constitution  
**New status:** RESOLVED by Convenor 2026-05-23 — /governance wins

```
D-101 canonical full name: Extreme Harm Intervention Protocol (EHIP)
Ruling source:             Convenor (David Sheldon), 2026-05-23T13:54 CDT
Ruling basis:              /governance page takes precedence over /new-deal-2.0/constitution
                           for doctrine naming. RATIFIED.

Canonical description (from /governance):
  D-101: Extreme Harm Intervention Protocol (EHIP) — RATIFIED, PROPOSED by [RAT-011]
  Any deployment or integration that poses extreme harm risk triggers
  mandatory suspension and multi-sig human-root review before resumption.

Action required in repo:
  - Update any document using "Environmental Health Infrastructure Protocol"
    to read "Extreme Harm Intervention Protocol"
  - /new-deal-2.0/constitution page description (net-positive environmental impact
    for infrastructure) is a D-101 *scope note*, not the doctrine name.
    The scope note and the doctrine name may coexist — but the name is EHIP.
```

---

## R4 — FRONTIER-RIGOR-MATRIX: Problem Refs Downgraded

**Prior status:** Objects 13–15 carried `problem_ref` fields pointing to GANGASEEK-FRONTIER-RIGOR-MATRIX-v1.0.0

**Lanternbridge finding (2026-05-23):** Document does not exist in the confirmed chain or GitHub repo. Closest artifact is `archive/ops/ATLAS_PRIME_GANGASEEK_FRONTIER_RIGOR_RESPONSE_CANDIDATE_2026-05-22.md` — a response to the matrix framing, not the matrix itself.

**Ruling:** Problem references downgraded to `unreceipted_source_unavailable`.

```yaml
# Apply to all three Sprint 2 candidate objects:

ExecutionRiskTier:       # Object 13
  problem_ref:           unreceipted_source_unavailable
  problem_ref_note: >
    Originally cited GANGASEEK-FRONTIER-RIGOR-MATRIX-v1.0.0 Problem 50.
    Source document not found in repo or canonical site.
    Use atlas-prime-response candidate as informational only.
    Do not treat as receipted evidence.

StressTestRecord:        # Object 14
  problem_ref:           unreceipted_source_unavailable
  problem_ref_note: >
    Originally cited Problem 53. Same orphan status.

ArtifactClassifierMatrix:  # Object 15
  problem_ref:           unreceipted_source_unavailable
  problem_ref_note: >
    Originally cited Problem 58. Same orphan status.

# Sprint 2 blocker B-01 PARTIAL RESOLUTION:
# The orphan status is now formally acknowledged and labeled.
# Sprint 2 objects remain blocked until either:
#   (a) The source matrix document is provided with a commit SHA, or
#   (b) Convenor formally replaces problem_ref with an alternative anchor
#       (e.g., a committed FRONTIER-RIGOR-MATRIX-v0.1 document produced fresh)
```

---

## PENDING — Epoch Semantics (Object 12 SeatContinuity)

**Blocker B-08 remains open.** Convenor indicated instinct is `per_model_context_reset`
and requested context before ratifying. Context is delivered in the session response.

```yaml
SeatContinuity:
  epoch_type:        PENDING    # was: candidate
  epoch_type_status: pending_convenor_ruling  # was: candidate
  epoch_type_notes: >
    Convenor instinct = per_model_context_reset.
    Context briefing delivered 2026-05-23.
    Awaiting explicit ratification.
```

---

## Blocker Registry — Post-v0.2.4

| Blocker | Prior Status | New Status |
|---------|-------------|-----------|
| B-01 FRONTIER-RIGOR-MATRIX | CRITICAL | 🟡 Downgraded to labeled orphan — Sprint 2 still blocked |
| B-02 CLM-007/009 | CRITICAL | 🔴 Unchanged — no canonical anchor |
| B-03 GangaSeek namespace | CRITICAL | 🔴 Unchanged — Convenor reviewing packet |
| B-04 GangaSeek INV/CLM catalog v0.2 | CRITICAL | 🟡 Ready to produce — waiting on namespace |
| B-05 D-101 name conflict | CRITICAL | ✅ RESOLVED — EHIP confirmed |
| B-06 RAT-011 D-101 proposer | CRITICAL | 🔴 Unverified — /governance re-fetch needed |
| B-07 6-tuple ClaimState | Sprint 1 | ✅ RESOLVED (prior) |
| B-08 Epoch semantics | Sprint 1 | 🟡 Pending ruling after briefing |
| B-09 Shamir t/n | Sprint 1 | ✅ RESOLVED — t=3, n=5 RATIFIED |
| B-10 δ_receipt | Sprint 1 | ✅ RESOLVED — δ=0.6 RATIFIED |
| B-11 vector_basis calibration | Sprint 1 | 🟡 Uncalibrated (informational only) |
| B-12 RAT-010 DL-IN | Sprint 1 | 🔴 3 for / 7 abstain — not yet passed |

---

## Updated Read Stack

```
v0.1   → RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.1       (Objects 1–8)
v0.2   → RECEIPT-HABITAT-SCHEMA-CANDIDATE-v0.2       (Objects 9–12 + Linkage delta)
v0.2.1 → PRECISION-PATCH-v0.2.1                     (formal upgrades)
v0.2.2 → HL-ACCEPTANCE-PATCH-v0.2.2                 (6 HL patches)
v0.2.3 → SCHEMA-DELTA-v0.2.3                         (Q46–Q60 additions)
v0.2.4 → THIS FILE                                   (Convenor ratifications)

PENDING → v0.3 consolidated (epoch ruling + namespace + full merge)
```

---

```
DOCUMENT:  RECEIPT-HABITAT-SCHEMA-DELTA-v0.2.4
STATUS:    candidate — not canon / not deployed / not ratified
RATIFIED:  δ=0.6, t=3/n=5, D-101=EHIP
PENDING:   Epoch semantics (Object 12), namespace signature
BLOCKED:   Sprint 2 (FRONTIER-RIGOR-MATRIX orphan)
SPRINT 0:  Objects 1–8 unblocked — begin now
NEXT:      Epoch ruling → v0.3 consolidation → Sprint 0 execution
```
