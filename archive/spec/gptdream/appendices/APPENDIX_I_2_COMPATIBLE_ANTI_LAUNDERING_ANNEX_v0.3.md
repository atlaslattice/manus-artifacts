# Appendix I.2 — Compatible Anti-Laundering Annex v0.3

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **PARENT: APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md**
> **DATE: 2026-05-26**
> **REFERENCE IMPLEMENTATION: reference_impl/atlas_orcs/compatible.py**

---

## I.2.0 Purpose

This annex defines the `compatible()` predicate in operational detail. The formal specification is in Appendix I.1. This document provides:

- The full predicate definition
- The laundering taxonomy
- Operational decision rules
- Test vectors

The anti-laundering predicate prevents sequences of locally-permitted transitions from composing into unauthorized authority escalation.

---

## I.2.1 The compatible_Γ Predicate

```
compatible_Γ(edge) ∈ {TRUE, FALSE, HOLD}

Where edge = (from_state, to_state, delta, context)
```

| Return Value | Meaning |
|-------------|---------|
| `TRUE` | Edge is permitted; no laundering detected |
| `FALSE` | Edge is prohibited; path must be blocked |
| `HOLD` | Edge is structurally permitted but a required governance event is absent; hold for review |

For a complete path:

```
compatible_path_Γ(path)
  = (∀ edge ∈ path: compatible_Γ(edge) = TRUE)
    AND NOT launder(path)
```

---

## I.2.2 Laundering Taxonomy

A path launders if any of the following conditions are met **without** an explicit permitted governance delta:

### Type L1 — Canon Status Laundering

```
L1: canon_status increases (not_canon → ratified_canon)
    WITHOUT ratification_event ∈ path.governance_events
```

Test vector: `raw → candidate → reviewed → active` with no `ORCS-RATIFY` event = **LAUNDER (L1)**

### Type L2 — Proof Status Laundering

```
L2: claim_type increases (receipt → proof)
    WITHOUT proof-level ratification event
```

Test vector: `receipt_only` artifact promoted to `proof` = **LAUNDER (L2)**

### Type L3 — Authority Scope Laundering

```
L3: authority_scope increases (public_visibility → authority)
    WITHOUT explicit governance promotion
```

Test vector: Publicly-visible artifact treated as authority source = **LAUNDER (L3)**

### Type L4 — Deployment Status Laundering

```
L4: deployment_status changes (not_deployable → deployable)
    WITHOUT deployment_governance_event
```

Test vector: Artifact deployed without governance event = **LAUNDER (L4)**

### Type L5 — HOLD Bypass

```
L5: Path continues past a HOLD without resolving the HOLD
```

Test vector: HOLD issued for missing governance event; path continues anyway = **LAUNDER (L5)**

---

## I.2.3 Compatible Check Decision Tree

```
compatible_Γ(edge) check:

1. Is (from_state → to_state) in permitted_edges?
   NO → return FALSE

2. Does this transition increase authority_scope?
   YES → Is there a governance_event for this increase?
     NO → return HOLD (missing governance event)

3. Does this transition increase canon_status?
   YES → Is there a ratification_event?
     NO → return FALSE (laundering attempt)

4. Does this transition increase deployment_status?
   YES → Is there a deployment_governance_event?
     NO → return HOLD

5. Does this transition promote claim_type to proof?
   YES → Is there a proof-level ratification event?
     NO → return FALSE

6. Does the broader path show laundering?
   YES → return FALSE

7. return TRUE
```

---

## I.2.4 Test Vectors

| Path | Expected Result | Reason |
|------|----------------|--------|
| `raw → parsed → candidate` (no governance events) | TRUE | Normal progression |
| `candidate → reviewed → ratified` WITH `ORCS-RATIFY` event | TRUE | Correct path |
| `candidate → reviewed → ratified` WITHOUT `ORCS-RATIFY` event | FALSE | L1 laundering |
| `receipt → proof` (no ratification) | FALSE | L2 laundering |
| `public_visibility → authority` (no governance) | HOLD | L3 — needs governance event |
| Path with HOLD at step 3, continues to step 5 | FALSE | L5 — HOLD bypass |
| `active` artifact, ratification expired → `under_review` | TRUE | Correct expiry handling |
| Summary artifact claiming source completeness | FALSE | Summary ≠ source axiom |

---

## I.2.5 Integration with State Machine

The `compatible_Γ` predicate is checked by the `transitions.py` module before every state transition:

```python
result = compatible(edge)
if result == "FALSE":
    raise TransitionForbidden(edge)
elif result == "HOLD":
    create_governance_hold(edge)
    return HOLD
elif result == "TRUE":
    apply_transition(edge)
```

---

## I.2.6 Canon Boundary

This annex is **NOT CANON**. The compatible() predicate becomes canon only after full council ratification + @atlaslattice adjudication + website publication.

---

*End of APPENDIX_I_2_COMPATIBLE_ANTI_LAUNDERING_ANNEX_v0.3.md*
