# APPENDIX I — ATLAS / ORCS EPISTEMIC PROFILE

**Version:** v0.3 — Patched Binder-Grade Draft  
**Status:** CANDIDATE — NOT CANON — NON-DEPLOYABLE  
**Authority:** Formalization only  
**Ratification:** Required for canon or deployment promotion  
**Date:** 2026-05-21

## Core System Definition

```math
\mathcal{A} = (\mathbb{S}, \Delta, \Pi, \Gamma, \kappa)
```

Where:

- `S` / `\mathbb{S}` = possible archive states
- `S_t` = archive state at time `t`
- `E(S_t)` = evidence entries contained in `S_t`
- `Δ` = append-only deltas
- `Π` = Atlas promotion operator
- `Γ_t` = ORCS governance profile at time `t`
- `κ` = CAS-001-A cryptographic receipt / anchor function

## 1. State Evolution

```math
S_{t+1} = S_t \oplus \delta_t
```

with:

```math
\delta_t \in \Delta
```

```math
parent(\delta_t) = \kappa(S_t)
```

### Retained Lineage Rule

```math
Lineage(S_t) \subseteq Lineage(S_{t+1})
```

Meaning: a later state must retain recoverable references to all evidence, receipts, and lineage present in the prior state. This is not literal set containment in every storage layout; it is provenance continuity. Compression, indexing, sealing, relocation, or tombstoning is allowed only if recoverability is preserved.

No overwrite. No destructive erasure.

## 2. Promotion Operator

```math
\Pi_{\Gamma_t}^{q}(S_t) = \{ e \in E(S_t) \mid \sigma(e; \Gamma_t) \ge \theta_t \}
```

Where `q` is the promotion target class:

- `review_candidate`
- `canon_candidate`
- `ratified_canon`
- `deployment_candidate`

### Candidate Scoring Function

```math
\sigma(e; \Gamma_t) = w_c C(e) + w_r R(e) + w_p P(e) + w_a A(e)
```

With:

- `C(e)` = Confidence / corroboration score
- `R(e)` = Receipt / provenance score
- `P(e)` = Policy / profile fit score
- `A(e)` = Audit / approval state score

All scores are candidate scoring functions unless and until independently validated under a named governance profile.

A high score produces promotion eligibility, not automatic ratification or truth.

### Promotion Rule

- Threshold crossing creates eligibility.
- Review constraints determine the promotion class.
- Ratification requires an explicit authority event.
- Deployment requires a separate deployment approval path.

## 3. Governance Profile

```math
\Gamma_t = (\Theta_t, W_t, \Phi_t, \mathcal{R}_t)
```

Governance transition with receipt:

```math
\Gamma_{t+1} = \Phi_t(\Gamma_t, g_t), \quad g_t \in \Delta_\Gamma
```

Governance-chain receipt:

```math
\kappa^\Gamma_{t+1} = H(
  "GOVv1" \parallel
  \kappa^\Gamma_t \parallel
  H("GOVDELTAv1" \parallel canon(g_t))
)
```

No silent governance drift. All governance changes must carry an explicit receipt.

## 4. Cryptographic Anchor — CAS-001-A

Chain anchor:

```math
\kappa_t = H(
  "STATEv1" \parallel
  \kappa_{t-1} \parallel
  H("DELTAv1" \parallel canon(\delta_t)) \parallel
  t \parallel
  policy_t
)
```

Full receipt tuple:

```math
CAS(S_t) = (\kappa_{raw}(S_t), \kappa_{canonical}(S_t), \rho_t)
```

Where `ρ_t` contains receipt metadata, canonicalization policy, tool version, timestamp, and parent anchor.

## 5. Cross-Vendor Interop

Adapters:

- `f_v` = vendor export adapter
- `r_v` = vendor reconstruction adapter
- `C` = canonicalization function

Lossless adapter criterion:

```math
\kappa_{canonical}(S) = \kappa_{canonical}(r_v(f_v(S)))
```

Lossless means canonical equivalence, not necessarily byte-identical raw equivalence. Raw exports may differ in formatting while canonicalized content matches.

Lossy adapters require an explicit loss receipt:

```yaml
projection_loss_declared: true
omitted_fields: []
round_trip_anchor_match: false
```

## 6. Core Invariant

```math
\Pi_{\Gamma_t}^{q}(S_t) \subseteq E(S_t)
```

Meaning:

Atlas promotes from retained evidence. Atlas does not create truth. It selects and elevates retained evidence under governance.

## 7. Non-Claims Block

This appendix does not claim:

- Atlas creates truth.
- Score threshold equals ratification.
- Vendor adapters are currently lossless.
- Cryptographic anchoring alone proves semantic correctness.
- Append-only storage means every record is public, promoted, or canon.
- Governance transitions are valid without review constraints.
- Ratified canon is automatically deployed.

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

## 9. Final Compressed Form

```math
S_{t+1} = S_t \oplus \delta_t
```

```math
S_t^* = \{ e \in E(S_t) \mid \sigma(e;\Gamma_t) \ge \theta_t \}
```

```math
\kappa_t = H("STATEv1" \parallel \kappa_{t-1} \parallel H("DELTAv1" \parallel canon(\delta_t)))
```

with the invariant:

```math
S_t^* \subseteq E(S_t)
```

## Keeper Line

```text
The ledger records.
Atlas promotes.
ORCS governs.
CAS anchors.
Nobody pretends the scoreboard created the game.
```

## Final Status

```text
Appendix I v0.3 — Patched Binder-Grade Draft
CANDIDATE — NOT CANON — NON-DEPLOYABLE
READY FOR REVIEW
NO RATIFICATION
NO DEPLOYMENT
B-LITE COMPLETE
RUNWAY PREPARED
NO LAUNCH
```
