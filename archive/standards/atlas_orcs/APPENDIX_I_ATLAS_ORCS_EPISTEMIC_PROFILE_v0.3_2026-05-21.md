# APPENDIX I — ATLAS / ORCS EPISTEMIC PROFILE

```text
Version: v0.3 — Patched Binder-Grade Draft
STATUS: CANDIDATE — NOT CANON — NON-DEPLOYABLE
AUTHORITY: Formalization only
RATIFICATION: Required (Human-root / S10)
DATE: 2026-05-21
```

## Core System Definition

\[
\mathcal{A} = (\mathbb{S}, \Delta, \Pi, \Gamma, \kappa)
\]

Where:

- \(\mathbb{S}\) = possible archive states
- \(S_t\) = archive state at time \(t\)
- \(E(S_t)\) = evidence entries contained in \(S_t\)
- \(\Delta\) = append-only deltas
- \(\Pi\) = Atlas promotion operator
- \(\Gamma_t\) = ORCS governance profile at time \(t\)
- \(\kappa\) = CAS-001-A cryptographic receipt / anchor function

---

## 1. State Evolution (Patched)

\[
S_{t+1} = S_t \oplus \delta_t
\]

With:

\[
\delta_t \in \Delta
\]

\[
\text{parent}(\delta_t) = \kappa(S_t)
\]

### Retained Lineage Rule (Clarified)

\[
\text{Lineage}(S_t) \subseteq \text{Lineage}(S_{t+1})
\]

Meaning:

A later state must retain recoverable references to all evidence, receipts, and lineage present in the prior state. This is **not** literal set containment — it is **provenance continuity**. Compression, indexing, or relocation is allowed only if recoverability is preserved.

```text
No overwrite.
No destructive erasure.
```

---

## 2. Promotion (Atlas) — Patched

\[
\Pi_{\Gamma_t}^{q}(S_t) = \{ e \in E(S_t) \mid \sigma(e; \Gamma_t) \ge \theta_t \}
\]

Where \(q\) is the **promotion target class**:

- `review_candidate`
- `canon_candidate`
- `ratified_canon`
- `deployment_candidate`

### Scoring Function (Defined)

\[
\sigma(e; \Gamma_t) = w_c C(e) + w_r R(e) + w_p P(e) + w_a A(e)
\]

With:

- \(C(e)\) = Confidence / Corroboration score
- \(R(e)\) = Receipt / Provenance score
- \(P(e)\) = Policy / Profile fit score
- \(A(e)\) = Audit / Approval state score

All scores are candidate scoring functions.

A high score produces **promotion eligibility**, not automatic ratification or truth.

### Promotion Rule

- Threshold crossing creates **eligibility**.
- Review constraints determine the **promotion class**.
- **Ratification** requires an explicit authority event (human-root decision).

---

## 3. Governance (ORCS) — Patched

\[
\Gamma_t = (\Theta_t, W_t, \Phi_t, \mathcal{R}_t)
\]

### Governance Transition (with receipt)

\[
\Gamma_{t+1} = \Phi_t(\Gamma_t, g_t), \quad g_t \in \Delta_\Gamma
\]

### Governance-Chain Receipt

\[
\kappa^\Gamma_{t+1} = H(
\texttt{"GOVv1"} \parallel
\kappa^\Gamma_t \parallel
H(\texttt{"GOVDELTAv1"} \parallel \text{canon}(g_t))
)
\]

```text
No silent governance drift.
```

All governance changes must carry an explicit receipt.

---

## 4. Cryptographic Anchor (CAS-001-A) — Patched

### Chain Anchor (state progression)

\[
\kappa_t = H(
\texttt{"STATEv1"} \parallel
\kappa_{t-1} \parallel
H(\texttt{"DELTAv1"} \parallel \text{canon}(\delta_t)) \parallel
t \parallel
\text{policy}_t
)
\]

### Full Receipt Tuple

\[
\text{CAS}(S_t) =
(
\kappa_{\text{raw}}(S_t),
\kappa_{\text{canonical}}(S_t),
\rho_t
)
\]

Where \(\rho_t\) contains receipt metadata, canonicalization policy, tool version, timestamp, and parent anchor.

---

## 5. Cross-Vendor Interop — Patched

### Adapters

- \(f_v\) = vendor export adapter
- \(r_v\) = vendor reconstruction adapter
- \(C\) = canonicalization function

### Lossless Adapter Criterion

\[
\kappa_{\text{canonical}}(S) = \kappa_{\text{canonical}}(r_v(f_v(S)))
\]

Note:

Lossless means **canonical equivalence**, not necessarily byte-identical raw equivalence. Raw exports may differ in formatting while canonicalized content matches.

Lossy adapters require explicit loss receipt:

- `projection_loss_declared = true`
- `omitted_fields` listed
- `round_trip_anchor_match = false`

---

## 6. Core Invariant (Unchanged — Load-Bearing)

\[
\Pi_{\Gamma_t}^{q}(S_t) \subseteq E(S_t)
\]

Meaning:

Atlas **promotes from retained evidence**.

Atlas does **not** create truth.

It only selects and elevates what already exists under governance.

---

## 7. Non-Claims Block

This appendix does **not** claim:

- Atlas creates truth
- Score threshold equals ratification
- Vendor adapters are currently lossless
- Cryptographic anchoring alone proves semantic correctness
- Append-only storage means every record is public, promoted, or canon
- Governance transitions are valid without review constraints

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

## Final Compressed Form

\[
S_{t+1} = S_t \oplus \delta_t,\quad
S_t^{*,q} = \{ e \in E(S_t) \mid \sigma(e;\Gamma_t) \ge \theta_t \},\quad
\kappa_t = H(\texttt{"STATEv1"} \parallel \kappa_{t-1} \parallel H(\texttt{"DELTAv1"} \parallel \text{canon}(\delta_t)))
\]

with the invariant:

\[
S_t^{*,q} \subseteq E(S_t)
\]

---

## Keeper Line

> The ledger records.  
> Atlas promotes.  
> ORCS governs.  
> CAS anchors.  
> Nobody pretends the scoreboard created the game.

---

## Final Status

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