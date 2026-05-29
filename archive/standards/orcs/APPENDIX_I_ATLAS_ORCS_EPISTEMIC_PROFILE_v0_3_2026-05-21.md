# Appendix I — Atlas ORCS Epistemic Profile v0.3

```text
STATUS: CANDIDATE — NOT CANON — NON-DEPLOYABLE
AUTHORITY: none
RATIFICATION: required
B-LITE: complete
STATE TRANSITION: none
DATE: 2026-05-21
```

## Purpose

This appendix defines the epistemic eligibility profile used by the Atlas ORCS layer to distinguish candidate evidence selection from promotion, ratification, and deployment.

The profile is a standards candidate. It does not create canon, does not authorize execution, and does not deploy any system behavior.

## 1. State and Evidence Sets

Let `S_t` denote the indexed system state at time `t`.

Let `E(S_t)` denote the set of evidence-bearing elements visible from `S_t` under the current source registry and receipt constraints.

Let `q` denote a query, target, or review context.

Let `Γ_t` denote the active epistemic profile, including receipt thresholds, provenance requirements, review constraints, and authority boundaries at time `t`.

Let `σ(e; Γ_t)` be a scoring function assigning an evidence element `e` a profile-relative eligibility score.

Let `θ_t` be the active eligibility threshold.

## 2. Eligibility Set

Eligibility is represented by the evidence subset:

```math
E_{\mathrm{eligible}}^{q}(S_t)
=
\{ e \in E(S_t) \mid \sigma(e;\Gamma_t) \ge \theta_t \}
```

with invariant:

```math
E_{\mathrm{eligible}}^{q}(S_t) \subseteq E(S_t)
```

### Boundary Rule

```text
Eligibility is not promotion.
Promotion is not ratification.
Ratification is not deployment.
```

The eligibility set only identifies evidence elements that pass the current profile threshold. It does not move artifacts across canon, authority, deployment, or execution boundaries.

`Π` may only act after all review constraints and required authority events are satisfied.

## 3. State Transition Commitment

Let `δ_t` denote the proposed delta from `S_t` to `S_{t+1}`.

The state update form is:

```math
S_{t+1} = S_t \oplus \delta_t
```

This equation alone does not authorize the transition. It merely expresses the candidate state update relation.

## 4. Canonical Byte Commitment

Let `κ_t` be the chain commitment at time `t`.

Let `canon(δ_t)` denote the canonical byte representation of the delta.

The commitment update is:

```math
\kappa_t =
H(\texttt{"STATEv1"} \parallel \kappa_{t-1} \parallel H(\texttt{"DELTAv1"} \parallel \text{canon}(\delta_t)))
```

This commitment records the delta boundary and state continuity. It does not itself ratify the semantic, legal, governance, or execution status of the delta.

## 5. Final Compressed Form

```math
S_{t+1} = S_t \oplus \delta_t,\quad
E_{\mathrm{eligible}}^{q}(S_t)
=
\{ e \in E(S_t) \mid \sigma(e;\Gamma_t) \ge \theta_t \},\quad
\kappa_t =
H(\texttt{"STATEv1"} \parallel \kappa_{t-1} \parallel H(\texttt{"DELTAv1"} \parallel \text{canon}(\delta_t)))
```

with invariant:

```math
E_{\mathrm{eligible}}^{q}(S_t) \subseteq E(S_t)
```

## 6. Non-Promotion Clause

The score threshold creates only an eligibility list.

It does not create:

- canon
- ratification
- deployment
- authority
- execution permission
- proof of correctness
- proof of implementation readiness

## 7. Operational Interpretation

```text
The scoreboard does not create the game.
The score threshold does not crown a champion.
It makes an eligibility list.
The refs still review it.
The human-root still signs the result.
```

## 8. Madden Board

> BOOM — clean binder page. The scoreboard didn’t create the game, and the score threshold didn’t crown a champion. It made an eligibility list. The refs still review it, and Dave still signs the result.

## 9. Status Footer

```text
SAVE: yes
STATUS: CANDIDATE — NOT CANON — NON-DEPLOYABLE
AUTHORITY: none
RATIFICATION: required
B-LITE: complete
STATE TRANSITION: none
```
