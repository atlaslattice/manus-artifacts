# Appendix I.2 — Compatible Anti-Laundering Annex v0.3

```text
STATUS: CANDIDATE SPEC — NOT CANON
VERSION: 0.3
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
RUNTIME_LABEL: WORK_OUTPUT
DATE: 2026-05-26
PARENT: APPENDIX_I_1_FORMAL_MATH_SPINE_v0.2.md
IMPLEMENTATION: reference_impl/atlas_orcs/compatible.py
```

---

## I.2.0 Purpose

This annex defines the `compatible()` anti-laundering predicate that prevents local allowed transitions from composing into unauthorized authority.

## I.2.1 The laundering problem

A sequence of individually permitted transitions can compose into an unauthorized elevation of:
- authority (e.g., summary → authoritative source)
- canon status (e.g., candidate → canon without ratification)
- deployment status (e.g., not_deployable → deployed)
- proof status (e.g., receipt → proof of truth)
- public-claim status (e.g., private note → public assertion)

Each step may be locally valid. The composed path is not.

## I.2.2 Edge predicate

```text
compatible_Γ(edge) ∈ {TRUE, FALSE, HOLD}

where edge = (artifact, from_state, to_state, delta)

TRUE  — edge is permitted and does not begin a laundering path
FALSE — edge is not permitted; block transition
HOLD  — edge is locally permitted but requires review before proceeding
```

## I.2.3 Path predicate

```text
compatible_path_Γ(path)
=
  all_edges_TRUE(path)
  AND NOT launder(path, Γ)

where path = [edge₁, edge₂, ..., edgeₙ]
```

A path with ANY `FALSE` edge is blocked.
A path with ANY `HOLD` edge is blocked pending review.
A path where `launder(path, Γ)` is true is blocked even if all edges are TRUE.

## I.2.4 Launder definition

```text
launder(path, Γ) = true  iff  any of the following hold:

L-1. AUTHORITY_INFLATION
     Path increases authority_scope without explicit ratification_event in Γ

L-2. CANON_INFLATION
     Path increases canon_status without explicit ratification_event in Γ

L-3. DEPLOYMENT_INFLATION
     Path increases deployment_status without explicit governance_event in Γ

L-4. PROOF_INFLATION
     Path increases epistemic_weight from receipt to proof
     without independent verification event in Γ

L-5. PUBLIC_CLAIM_INFLATION
     Path increases public visibility
     without explicit publicity_authorization_event in Γ
```

## I.2.5 Key rules

```text
R-1. Path with all locally valid edges STILL FAILS if canon status
     increases without ratification_event.

R-2. Path with receipt only CANNOT become proof.
     (receipt ≠ truth; see Appendix I.1, §I.1.6)

R-3. Path with public visibility CANNOT become authority.
     (visibility ≠ authority)

R-4. HOLD blocks promotion until review resolves.

R-5. FALSE blocks path entirely.
```

## I.2.6 Implementation

See `reference_impl/atlas_orcs/compatible.py`.

The implementation provides:
```python
def compatible_edge(edge: Edge, context: GovernanceContext) -> Literal["TRUE", "FALSE", "HOLD"]
def compatible_path(path: List[Edge], context: GovernanceContext) -> bool
def launder(path: List[Edge], context: GovernanceContext) -> bool
```

## I.2.7 Test coverage

See `reference_impl/atlas_orcs/tests/test_compatible.py`.

---

```text
NOT CANON. NOT DEPLOYABLE.
```
