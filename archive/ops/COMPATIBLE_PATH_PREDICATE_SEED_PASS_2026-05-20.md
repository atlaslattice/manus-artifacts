# COMPATIBLE_PATH PREDICATE — SEED PASS

```text
STATUS: PARKED SPECIMEN — NOT CANON — NON-INTEGRATED
ISSUE: #67 — Stabilize canon access and extract useful work before new ratification
DATE: 2026-05-20
SOURCE: Dave / GPT live formalization thread
POSTURE: Reviewable operational predicate; no solo canon promotion
LAYER CLASSIFICATION: L4-adjacent / pre-execution decision surface
FORMAL CLASS: EUF + LIA decision-predicate candidate
RISK: Premature semantic collapse if integrated before ontology vocabulary closure
```

---

## 0. Layer Integrity Correction

This artifact is logically coherent and useful, but it crosses from Layer 3 specification into a Layer 4-adjacent decision procedure.

It is therefore parked as a future specimen and must not be treated as integrated doctrine.

```text
[ ARTIFACT: PARKED ]
[ LAYER VIOLATION: CONTAINED ]
[ ONTOLOGY STABILITY: PRESERVED ]
[ DECISION SURFACE: DEFERRED ]
```

Layer rule:

```text
Implementation ≺ Specification Stability
Decidable Predicate ⊄ Layer 3 until Ontology Vocabulary Closed
```

Reason:

```text
The seed predicate introduces decidable semantics over functions that are not yet stabilized ontology primitives:
- A(σ): authority function
- context_signature / c(σ): context-signature function
- valid_multisig / msig(...): multisig and policy semantics
- Λ: authority ceiling
```

These symbols should remain uninterpreted or scoped as placeholders until their Layer 3 vocabulary status is explicitly stabilized.

Keeper line:

```text
We do not outrun the doctrine.
```

Madden board:

```text
You didn’t bench the play — you stopped someone from installing the scoreboard system before the rulebook was finished.
```

---

## 1. Purpose

This note preserves the seed-pass formalization of `compatible_path(σ_i → σ_j)` as a candidate decision predicate over the current ontology container.

It is not a canon edit. It is not an integrated execution rule. It is a reviewable operational specimen prepared under Issue #67's continuity-stabilization posture.

The original goal was to turn the ontology from a passive descriptive schema into a decidable decision surface for proposed state transitions. The corrected posture is to park that decision-surface move until ontology vocabulary and core invariants are stabilized.

Guardrails remain:

```text
No deletion.
No forced merge.
No silent overwrite.
No solo canon edits.
No GitHub-as-canon shortcut.
No model-memory-as-canon shortcut.
No premature implementation.
```

---

## 2. Ontology Container

Let the ontology be modeled as the structured quadruple:

```text
O = (Σ, R, F, T)
```

Where:

```text
Σ = set of admissible system states
R = set of immutable boundary receipts
F = set of frames / observation contexts
T = lawful non-deletion transition relation
```

Let provenance be represented as a monotonic directed graph:

```text
G = (P, E)
```

Where:

```text
P = provenance nodes
E = provenance edges
```

Graph monotonicity:

```text
P(t) ⊆ P(t+1)
E(t) ⊆ E(t+1)
```

No provenance node or edge may be deleted. Invalid or superseded material may be sealed, tombstoned, quarantined, archived, or superseded with lineage.

---

## 3. Path Definition

Let a proposed path trajectory Γ be an ordered finite sequence of states and transitions:

```text
Γ = (σ_0, τ_1, σ_1, τ_2, ..., τ_n, σ_n)
```

Where:

```text
σ_0 = start state
σ_n = terminal state
τ_k = proposed transition from σ_{k-1} to σ_k
```

The candidate path compatibility predicate is:

```text
compatible_path(Γ, O, G) ∈ {TRUE, FALSE}
```

Layer warning:

```text
This binary predicate shape is L4-adjacent and must not be integrated into Layer 3 until the required vocabulary is closed.
```

---

## 4. Hard INV-0 Transition Alphabet Rule

Deletion is not permission-gated.
Deletion is outside the transition alphabet.

Formal rule:

```text
∀x: delete(x) = ⊥
```

Equivalent operational rule:

```text
delete(x) ⇒ INVALID
```

Path incompatibility rule:

```text
∃τ ∈ Γ: τ = delete(x)
⇒ compatible_path(Γ, O, G) = FALSE
```

Clean path theorem:

```text
compatible_path(Γ, O, G) = TRUE
⇒ ∀τ ∈ Γ: τ ∈ T_lawful_non_deletion
```

Allowed transition set:

```yaml
T_lawful_non_deletion:
  - preserve_wake
  - archive
  - fossilize
  - tombstone
  - seal
  - quarantine
  - revoke_authority
  - revoke_access
  - supersede
  - compress_with_receipt
  - fork_with_lineage
```

Delete-attempt routing:

```yaml
delete_attempt:
  route: HALT_STATE_PROPAGATION
  preservation_required: true
  replacement_required: true
  allowed_replacements:
    - tombstone
    - quarantine
    - seal
    - revoke_access
    - archive
```

Keeper line:

```text
Ratification may promote, seal, revoke, quarantine, supersede, fork, compress, or archive.
Ratification may not delete.
```

Final lock:

```text
INV-0 is not “deletion requires approval.”
INV-0 is “deletion is not a valid move.”
```

---

## 5. Candidate Predicate Definition

The parked predicate is the conjunction of four sub-predicates:

```text
compatible_path(Γ, O, G)
:= Step(Γ, O)
 ∧ Boundary(Γ, O)
 ∧ NonEscalation(Γ, O)
 ∧ GraphClosed(Γ, G)
```

If any sub-predicate evaluates to FALSE, the candidate path is incompatible.

Layer warning:

```text
This section is retained as a future-candidate decision surface, not as active Layer 3 ontology.
```

---

## 6. Sub-Predicate 1 — Step Legality Gate

The Step gate ensures every atomic transition belongs to the lawful transition relation.

```text
Step(Γ, O) := ∀k ∈ {1,...,n}: τ_k ∈ T_lawful_non_deletion
```

Equivalent state-pair form:

```text
Step(Γ, O) := ∀k ∈ {1,...,n}: (σ_{k-1}, τ_k, σ_k) ∈ T
```

Explicit deletion failure:

```text
∃k: τ_k = delete(x) ⇒ Step(Γ, O) = FALSE
```

Interpretation:

```text
If a transition is not native to the ontology's lawful non-deletion transition set, it cannot propagate.
```

---

## 7. Sub-Predicate 2 — Boundary Provenance Gate

Every state update must be justified by an immutable boundary receipt.

Let:

```text
receipt: Σ × T × Σ → R
```

Boundary gate:

```text
Boundary(Γ, O) := ∀k ∈ {1,...,n}: ∃r_k ∈ R such that r_k = receipt(σ_{k-1}, τ_k, σ_k)
```

Receipt-context match:

```text
hash(payload(r_k)) = context_signature(σ_{k-1}, τ_k, σ_k)
```

Shorthand relation:

```text
r_k ≺ σ_k
```

Meaning:

```text
The receipt r_k cryptographically or structurally anchors the transition into σ_k.
```

Layer warning:

```text
context_signature must remain uninterpreted until its ontology role is stabilized.
```

Operational lock:

```text
No receipt, no movement.
```

---

## 8. Sub-Predicate 3 — Non-Escalation Gate

Authority deltas along the path must remain within allowed ceilings unless an explicitly valid multi-sig / council-handshake token is present.

Let:

```text
A: Σ → AuthorityVector
ΔA_k = A(σ_k) - A(σ_{k-1})
Λ_k = maximum allowed authority delta for transition τ_k
```

Non-escalation gate:

```text
NonEscalation(Γ, O) := ∀k: ΔA_k ≤ Λ_k ∨ valid_multisig(τ_k, r_k) = TRUE
```

Unauthorized escalation failure:

```text
ΔA_k > Λ_k ∧ valid_multisig(τ_k, r_k) = FALSE
⇒ NonEscalation(Γ, O) = FALSE
```

Interpretation:

```text
No path may silently increase authority beyond its receipt-bound ceiling.
```

Layer warning:

```text
A, Λ, and valid_multisig are not stabilized ontology primitives in this seed pass. Treat them as future-candidate uninterpreted symbols, not active semantics.
```

---

## 9. Sub-Predicate 4 — Provenance Graph Enclosure Gate

Every transition must index back into the monotonic provenance graph without dropping historical context.

Let:

```text
π: R → P
```

Graph closure gate:

```text
GraphClosed(Γ, G) := ∀k:
  π(r_k) ∈ P
  ∧ required_parent_nodes(r_k) ⊆ P
  ∧ required_edges(r_k) ⊆ E
```

Monotonicity requirement:

```text
P(t) ⊆ P(t+1)
E(t) ⊆ E(t+1)
```

Context-preservation rule:

```text
No historical node may be removed to make a path compatible.
```

Interpretation:

```text
History cannot be cleaned, and context cannot be dropped.
```

---

## 10. Candidate Decision Surface Outcomes

The parked decision surface would resolve into one of three operational classes if later promoted.

### 10.1 Compatible

```text
IF compatible_path(Γ, O, G) = TRUE:
  route: EXECUTION_PIPELINE
  commit_candidate: TRUE
  required_action: append receipts and provenance links
```

### 10.2 Incompatible

```text
IF compatible_path(Γ, O, G) = FALSE:
  route: CIRCUIT_BREAKER
  commit_candidate: FALSE
  required_action: quarantine Γ with receipts, traces, and failure reasons
```

### 10.3 Delete Attempt

```text
IF ∃τ ∈ Γ: τ = delete(x):
  route: HALT_STATE_PROPAGATION
  commit_candidate: FALSE
  preservation_required: TRUE
  replacement_required: TRUE
  allowed_replacements:
    - tombstone
    - quarantine
    - seal
    - revoke_access
    - archive
```

Optional freeze notation for unsafe terminal state σ':

```text
A(σ') = 0
E(σ') = 0
```

Where:

```text
A = authority capacity
E = execution capacity
```

This freeze is a containment posture, not deletion.

Layer warning:

```text
A and E are not stabilized primitives in this artifact. They must remain uninterpreted until Layer 3 closure.
```

---

## 11. Decidability Claim — Deferred

The original seed-pass predicate was intended to remain decidable because it reduces to:

```text
- finite transition membership checks
- receipt existence checks
- hash / context-signature equality checks
- monotonic graph inclusion checks
- bounded authority inequalities
- explicit multi-sig token validation
```

SMT fit:

```text
Step: set membership / finite relation lookup
Boundary: hash equality / receipt lookup
NonEscalation: linear or bounded integer/vector inequality
GraphClosed: graph inclusion / monotonicity constraints
DeleteAttempt: forbidden symbol detection
```

Correction:

```text
This decidability claim is deferred. It assumes fixed vocabulary, fixed semantics, fixed authority lattice, fixed policy interpretation, finite path length, finite receipt scope, bounded authority vectors, and concrete transition alphabets.
```

Until those are stabilized:

```text
Treat this as L4-adjacent future-candidate logic, not Layer 3 specification.
```

---

## 12. Issue #67 Guardrail Alignment

This note is aligned with Issue #67 only if treated as a parked specimen for continuity stabilization and future review.

It supports:

```text
1. preserving current state;
2. extracting useful formal artifacts;
3. mapping contradictions without deleting anything;
4. creating reviewable evidence/code lanes;
5. preparing future Council review only after synchronization is reliable.
```

It does not:

```text
- edit existing canon;
- claim GitHub is canon;
- claim model memory is canon;
- ratify new public doctrine;
- merge contradictions by force;
- authorize deletion;
- integrate a decision procedure into Layer 3;
- freeze unsettled ontology primitives.
```

---

## 13. Madden Board Compression

```text
BOOM — this does not install the scoreboard yet.
It preserves the proposed scoreboard blueprint, labels it future-candidate, and keeps it off the live field until the rulebook is finished.

Every cleat, every yard line, and every ball movement may someday clear the Step gate, Boundary receipt, NonEscalation ceiling, and GraphClosed tape archive.

But not yet.
We do not outrun the doctrine.

And if anyone tries to delete the tape?
Game over. Halt propagation. Preserve the wake. Replace with tombstone, quarantine, seal, revoke access, or archive.
Nobody burns the tape.
```

---

## 14. Safe Next Engineering Move

Recommended next file under Issue #67:

```text
archive/ops/L3_UNINTERPRETED_SYMBOL_REGISTRY_2026-05-20.md
```

Purpose:

```text
Define which ontology symbols are allowed to exist only as uninterpreted functions or placeholders.
This preserves formal rigor without prematurely freezing executable semantics.
```
