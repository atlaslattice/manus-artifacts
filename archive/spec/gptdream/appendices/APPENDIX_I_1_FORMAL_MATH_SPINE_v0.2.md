# Appendix I.1 — Formal Math Spine v0.2

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **PARENT: APPENDIX_I_ATLAS_ORCS_EPISTEMIC_GOVERNANCE_PROFILE_v0.1.md**
> **DATE: 2026-05-26**

---

## I.1.0 Purpose

This appendix provides the formal mathematical foundations for the Atlas/ORCS governance system. It defines:

- The state space Σ for artifacts
- The delta function Δ for state transitions
- The compatible predicate Γ for anti-laundering
- The proof ordering ≤_P for epistemic authority

This is intentionally boring math. The goal is machine-checkable structure, not philosophy.

---

## I.1.1 Artifact State Space

Let **A** be the set of all artifacts in the system.

For each artifact `a ∈ A`, define:

```
σ(a) ∈ Σ = {
  raw, parsed, candidate, reviewed,
  ratified, active, under_review,
  superseded, revoked, quarantined, rejected
}
```

The state space Σ is a **directed acyclic graph** with the following permitted edges:

```
raw → parsed
parsed → candidate
parsed → quarantined
candidate → reviewed
candidate → rejected
candidate → quarantined
reviewed → ratified
reviewed → rejected
ratified → active
ratified → under_review
active → under_review
active → superseded
active → revoked
under_review → reviewed
under_review → revoked
quarantined → reviewed  (after remediation)
quarantined → revoked
```

All other transitions are **prohibited**. The `compatible_Γ` predicate enforces this.

---

## I.1.2 Governance Delta Function

For each state transition, define:

```
Δ: A × Σ × Event → A × Σ

Δ(a, σ(a), e) = (a', σ') 
```

Where `e` is a governance event (ORCS operation), `a'` is the updated artifact, and `σ'` is the new state.

**Constraints on Δ:**

1. `Δ(a, reviewed, RATIFY(e)) = (a', ratified)` only if `e.ratifier_id ≠ a.author_id` (no self-ratification)
2. `Δ(a, σ, PROMOTE(*))` is only valid if `σ = ratified`
3. `Δ(a, active, EXPIRE(e)) = (a', under_review)` if `e.timestamp > ratification_expiry(a)`
4. `Δ(a, *, QUARANTINE(e)) = (a', quarantined)` preserves `a.lineage` — lineage is never modified

---

## I.1.3 Epistemic Authority Ordering

Define a partial order ≤_P on epistemic authority levels:

```
none <_P local <_P council <_P ratified_canon
```

And a separate ordering for claim types:

```
assumption <_P context <_P receipt <_P reviewed_claim <_P ratified_claim <_P proof
```

**Key invariants:**

- `receipt ≠_P proof` — a receipt does not imply proof
- `summary ≠_P source` — a summary does not inherit source authority
- `ratified_canon` is unreachable without an explicit `ORCS-RATIFY` event

---

## I.1.4 Compatible Predicate (preview)

Full specification in Appendix I.2. Preview:

```
compatible_Γ: Edge → {TRUE, FALSE, HOLD}

compatible_Γ(σ, σ') = 
  TRUE  if (σ, σ') ∈ permitted_edges AND NOT launder(σ, σ')
  FALSE if (σ, σ') ∉ permitted_edges
  HOLD  if (σ, σ') ∈ permitted_edges AND requires_governance_event_not_present(σ, σ')
```

For a path `π = [σ_0, σ_1, ..., σ_n]`:

```
compatible_path_Γ(π) = 
  ∀ i: compatible_Γ(σ_i, σ_{i+1}) = TRUE
  AND NOT launder(π)
```

---

## I.1.5 Laundering Definition (formal)

A path `π` launders if there exists any position `i` in the path such that:

```
launder(π) ⟺ ∃ i such that:
  authority_level(σ_{i+1}) > authority_level(σ_i)
  AND NOT ∃ governance_event(ORCS-RATIFY | ORCS-PROMOTE) at position i
```

Equivalently, any increase in:
- `authority_scope` (none → local → council → ratified_canon)
- `canon_status` (not_canon → ratified_canon)
- `deployment_status` (not_deployable → deployable)
- `claim_type` (receipt → proof)
- `public_claim_status` (internal → public)

...without a corresponding explicit permitted governance event = **laundering**.

---

## I.1.6 Proof System Requirements

For a claim to reach `proof` level:

```
claim c is_proof iff:
  ∃ ratification_event e such that:
    e.artifact_id = c.id
    AND e.ratification_scope ⊇ {proof}
    AND e.ratifier_id ≠ c.author_id
    AND NOT expired(e)
    AND @atlaslattice_adjudicated(e) = true
```

Note: GitHub receipts satisfy none of these conditions on their own.

---

## I.1.7 Canon Boundary

This appendix is **NOT CANON**. The formal math spine becomes canon only after full council ratification + @atlaslattice adjudication + website publication.

---

*End of APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md*
