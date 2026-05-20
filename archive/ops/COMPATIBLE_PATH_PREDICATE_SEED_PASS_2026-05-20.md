# COMPATIBLE_PATH PREDICATE — SEED PASS

```text
STATUS: OPS / FORMALIZATION SEED — NOT CANON
ISSUE: #67 — Stabilize canon access and extract useful work before new ratification
DATE: 2026-05-20
SOURCE: Dave / GPT live formalization thread
POSTURE: Reviewable operational predicate; no solo canon promotion
```

---

## 1. Purpose

This note preserves the seed-pass formalization of `compatible_path(σ_i → σ_j)` as a hard decision predicate over the current ontology container.

It is not a canon edit. It is a reviewable operational artifact prepared under Issue #67's continuity-stabilization posture.

The goal is to turn the ontology from a passive descriptive schema into a decidable decision surface for proposed state transitions, while preserving the core guardrails:

```text
No deletion.
No forced merge.
No silent overwrite.
No solo canon edits.
No GitHub-as-canon shortcut.
No model-memory-as-canon shortcut.
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

The path compatibility predicate is:

```text
compatible_path(Γ, O, G) ∈ {TRUE, FALSE}
```

It evaluates to TRUE only if every step clears the full validation conjunction.

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

## 5. Predicate Definition

The predicate is the conjunction of four sub-predicates:

```text
compatible_path(Γ, O, G)
:= Step(Γ, O)
 ∧ Boundary(Γ, O)
 ∧ NonEscalation(Γ, O)
 ∧ GraphClosed(Γ, G)
```

If any sub-predicate evaluates to FALSE, the full path is incompatible.

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

## 10. Decision Surface Outcomes

The decision surface should resolve into one of three operational classes.

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

---

## 11. Decidability Claim

The seed-pass predicate is intended to remain decidable because it reduces to:

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

Caution:

```text
This decidability claim assumes finite path length, finite receipt scope, bounded authority vectors, and concrete transition alphabets. Unbounded semantic interpretation is outside the predicate.
```

---

## 12. Issue #67 Guardrail Alignment

This note is aligned with Issue #67 because it stabilizes operational compatibility without ratifying new canon.

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
- authorize deletion.
```

---

## 13. Madden Board Compression

```text
BOOM — this installs the replay sensors across the whole field.
Every cleat, every yard line, every ball movement has to clear the Step gate, the Boundary receipt, the NonEscalation ceiling, and the GraphClosed tape archive.

If a dirty transition tries to sneak down the sideline, it is not a debate.
The predicate hits FALSE, the circuit breaker drops, and the play is quarantined with the tape preserved.

And if anyone tries to delete the tape?
Game over. Halt propagation. Preserve the wake. Replace with tombstone, quarantine, seal, revoke access, or archive.
Nobody burns the tape.
```

---

## 14. Next Engineering Move

Recommended next file under Issue #67:

```text
archive/ops/COMPATIBLE_PATH_SMT_SIGNATURE_2026-05-20.md
```

Purpose:

```text
Define the SMT-friendly variable domains, constraints, and expected solver outputs for compatible_path without binding to a specific implementation language.
```
