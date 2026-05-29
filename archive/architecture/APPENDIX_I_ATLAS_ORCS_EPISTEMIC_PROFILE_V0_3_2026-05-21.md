# APPENDIX I — ATLAS / ORCS EPISTEMIC PROFILE

```text
VERSION: v0.3 — Patched Binder-Grade Draft
STATUS: CANDIDATE — NOT CANON — NON-DEPLOYABLE
AUTHORITY: Formalization only
RATIFICATION: Required — Human-root / S10
DATE: 2026-05-21
POSTURE: B-LITE complete; runway prepared; no launch
```

---

## Core System Definition

```text
A = (S, Δ, Π, Γ, κ)
```

Where:

```text
S = possible archive states
S_t = archive state at time t
E(S_t) = evidence entries contained in S_t
Δ = append-only deltas
Π = Atlas promotion operator
Γ_t = ORCS governance profile at time t
κ = CAS-001-A cryptographic receipt / anchor function
```

---

## 1. State Evolution — Patched

```text
S_{t+1} = S_t ⊕ δ_t
```

With:

```text
δ_t ∈ Δ
parent(δ_t) = κ(S_t)
```

### Retained Lineage Rule — Clarified

```text
Lineage(S_t) ⊆ Lineage(S_{t+1})
```

Meaning:

```text
A later state must retain recoverable references to all evidence, receipts, and lineage present in the prior state.
This is not literal set containment. It is provenance continuity.
Compression, indexing, or relocation is allowed only if recoverability is preserved.
```

Hard boundary:

```text
No overwrite.
No destructive erasure.
```

---

## 2. Promotion / Atlas — Patched

```text
Π^q_{Γ_t}(S_t) = { e ∈ E(S_t) | σ(e; Γ_t) ≥ θ_t }
```

Where `q` is the promotion target class:

```text
review_candidate
canon_candidate
ratified_canon
deployment_candidate
```

### Scoring Function — Defined

```text
σ(e; Γ_t) = w_c C(e) + w_r R(e) + w_p P(e) + w_a A(e)
```

With:

```text
C(e) = Confidence / Corroboration score
R(e) = Receipt / Provenance score
P(e) = Policy / Profile fit score
A(e) = Audit / Approval state score
```

Important boundary:

```text
All scores are candidate scoring functions.
A high score produces promotion eligibility, not automatic ratification or truth.
```

### Promotion Rule

```text
Threshold crossing creates eligibility.
Review constraints determine the promotion class.
Ratification requires an explicit authority event: human-root / S10 decision.
```

---

## 3. Governance / ORCS — Patched

```text
Γ_t = (Θ_t, W_t, Φ_t, R_t)
```

Governance transition with receipt:

```text
Γ_{t+1} = Φ_t(Γ_t, g_t),   g_t ∈ Δ_Γ
```

### Governance-Chain Receipt

```text
κ^Γ_{t+1} = H(
  "GOVv1" ||
  κ^Γ_t ||
  H("GOVDELTAv1" || canon(g_t))
)
```

Boundary:

```text
No silent governance drift.
All governance changes must carry an explicit receipt.
```

---

## 4. Cryptographic Anchor / CAS-001-A — Patched

### Chain Anchor / State Progression

```text
κ_t = H(
  "STATEv1" ||
  κ_{t-1} ||
  H("DELTAv1" || canon(δ_t)) ||
  t ||
  policy_t
)
```

### Full Receipt Tuple

```text
CAS(S_t) = (
  κ_raw(S_t),
  κ_canonical(S_t),
  ρ_t
)
```

Where:

```text
ρ_t contains receipt metadata, canonicalization policy, tool version, timestamp, and parent anchor.
```

---

## 5. Cross-Vendor Interop — Patched

Adapters:

```text
f_v = vendor export adapter
r_v = vendor reconstruction adapter
C = canonicalization function
```

### Lossless Adapter Criterion

```text
κ_canonical(S) = κ_canonical(r_v(f_v(S)))
```

Note:

```text
Lossless means canonical equivalence, not necessarily byte-identical raw equivalence.
Raw exports may differ in formatting while canonicalized content matches.
```

### Lossy Adapter Requirements

Lossy adapters require explicit loss receipt:

```yaml
projection_loss_declared: true
omitted_fields: listed
round_trip_anchor_match: false
```

---

## 6. Core Invariant — Load-Bearing

```text
Π^q_{Γ_t}(S_t) ⊆ E(S_t)
```

Meaning:

```text
Atlas promotes from retained evidence.
Atlas does not create truth.
Atlas only selects and elevates what already exists under governance.
```

---

## 7. Non-Claims Block

This appendix does not claim:

```text
- Atlas creates truth
- Score threshold equals ratification
- Vendor adapters are currently lossless
- Cryptographic anchoring alone proves semantic correctness
- Append-only storage means every record is public, promoted, or canon
- Governance transitions are valid without review constraints
```

---

## 8. Must-Not-Infer Block

Do not infer:

```text
Recorded ≠ promoted
Promoted ≠ ratified
Ratified ≠ deployed
Canonicalized ≠ true
Hashed ≠ meaningful
Receipt-bearing ≠ approved
```

---

## 9. Final Compressed Form

```text
S_{t+1} = S_t ⊕ δ_t
```

```text
S_t* = { e ∈ E(S_t) | σ(e; Γ_t) ≥ θ_t }
```

```text
κ_t = H(
  "STATEv1" ||
  κ_{t-1} ||
  H("DELTAv1" || canon(δ_t))
)
```

with the invariant:

```text
S_t* ⊆ E(S_t)
```

---

## 10. Keeper Line

```text
The ledger records.
Atlas promotes.
ORCS governs.
CAS anchors.
Nobody pretends the scoreboard created the game.
```

---

## 11. Final Status

```text
Appendix I v0.3 — Patched Binder-Grade Draft
CANDIDATE — NOT CANON — NON-DEPLOYABLE
Ready for review.
No ratification.
No deployment.
```

```text
B-LITE complete.
Runway prepared.
No launch.
```
