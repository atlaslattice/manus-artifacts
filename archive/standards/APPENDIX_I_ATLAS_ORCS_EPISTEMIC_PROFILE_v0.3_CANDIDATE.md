# Appendix I — Atlas / ORCS Epistemic Profile

```text
VERSION: v0.3 — Patched Binder-Grade Draft
STATUS: CANDIDATE — NOT CANON — NON-DEPLOYABLE
AUTHORITY: none — formalization draft only
RATIFICATION: required by designated human/governance ratifier
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

## 1. State Evolution

\[
S_{t+1} = S_t \oplus \delta_t
\]

with:

\[
\delta_t \in \Delta
\]

\[
\text{parent}(\delta_t) = \kappa(S_t)
\]

### Retained Lineage Rule

\[
\text{Lineage}(S_t) \subseteq \text{Lineage}(S_{t+1})
\]

This is **not** literal set containment of every raw object in hot storage. It means provenance continuity: a later state must retain recoverable references to all evidence, receipts, and lineage present in the prior state. Compression, indexing, relocation, and cold archival are allowed only if recoverability is preserved.

No overwrite. No destructive erasure. No hidden termination.

---

## 2. Promotion — Atlas

\[
\Pi_{\Gamma_t}^{q}(S_t) = \{ e \in E(S_t) \mid \sigma(e; \Gamma_t) \ge \theta_t \}
\]

Where \(q\) is the promotion target class:

```text
review_candidate
canon_candidate
ratified_canon
deployment_candidate
```

### Candidate Scoring Function

\[
\sigma(e; \Gamma_t) = w_c C(e) + w_r R(e) + w_p P(e) + w_a A(e)
\]

with:

- \(C(e)\) = confidence / corroboration score
- \(R(e)\) = receipt / provenance score
- \(P(e)\) = policy / profile fit score
- \(A(e)\) = audit / approval state score

Scores are governance heuristics, not truth metrics. A high score produces promotion eligibility, not automatic ratification, truth, or authority.

### Promotion Rule

- Threshold crossing creates eligibility.
- Review constraints determine the promotion class.
- Ratification requires an explicit authority event by the designated human/governance ratifier.

---

## 3. Governance — ORCS

\[
\Gamma_t = (\Theta_t, W_t, \Phi_t, \mathcal{R}_t)
\]

### Governance Transition

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

No silent governance drift. All governance changes must carry an explicit receipt.

---

## 4. Cryptographic Anchor — CAS-001-A

Let \(H\) be the selected cryptographic hash function, for example SHA-256, with algorithm and version recorded in receipt metadata.

The canonicalization function \(\text{canon}(x)\) must be deterministic, versioned, and recorded in \(\rho_t\). Two systems must not claim the same canonical hash unless they used the same canonicalization policy and version.

### Chain Anchor

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

where \(\rho_t\) contains:

```text
receipt metadata
canonicalization policy and version
tool version
timestamp
parent anchor
hash algorithm and version
visibility class
review status
```

---

## 5. Cross-Vendor Interop

Adapters:

- \(f_v\) = vendor export adapter
- \(r_v\) = vendor reconstruction adapter
- \(C\) = canonicalization function

### Lossless Adapter Criterion

\[
\kappa_{\text{canonical}}(S) = \kappa_{\text{canonical}}(r_v(f_v(S)))
\]

Lossless means canonical equivalence, not necessarily byte-identical raw equivalence. Raw exports may differ in formatting while canonicalized content matches.

Lossy adapters require explicit loss receipt:

```yaml
projection_loss_declared: true
omitted_fields: []
round_trip_anchor_match: false
loss_notes: []
```

---

## 6. Core Invariant

\[
\Pi_{\Gamma_t}^{q}(S_t) \subseteq E(S_t)
\]

Meaning:

```text
Atlas promotes from retained evidence.
Atlas does not create truth.
Atlas only selects and elevates what already exists under governance.
```

---

## 7. Non-Claims Block

This appendix does **not** claim:

- Atlas creates truth.
- Score threshold equals ratification.
- Vendor adapters are currently lossless.
- Cryptographic anchoring alone proves semantic correctness.
- Append-only storage means every record is public, promoted, or canon.
- Governance transitions are valid without review constraints.
- Recorded material has authority merely because it is preserved.

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
Stored ≠ authoritative
Visible ≠ permitted
Retrieved ≠ verified
```

---

## 9. Final Compressed Form

\[
S_{t+1} = S_t \oplus \delta_t
\]

\[
S_t^* = \{ e \in E(S_t) \mid \sigma(e;\Gamma_t) \ge \theta_t \}
\]

\[
\kappa_t = H(\texttt{"STATEv1"} \parallel \kappa_{t-1} \parallel H(\texttt{"DELTAv1"} \parallel \text{canon}(\delta_t)))
\]

with the invariant:

\[
S_t^* \subseteq E(S_t)
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
READY FOR REVIEW
NO RATIFICATION
NO DEPLOYMENT
```
