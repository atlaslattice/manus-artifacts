# D-Φ-1 v0.4 — Validator Candidates

```text
STATUS: VALIDATOR CANDIDATES — CANDIDATE — NOT CANON
DATE: 2026-05-22
SOURCE_ISSUE: https://github.com/atlaslattice/manus-artifacts/issues/122
SOURCE_PACKET: archive/standards/dphi/D_PHI_1_v0_4_REVIEW_PACKET_2026-05-21.md
CONTROL_ROOM: archive/ops/CONTROL_ROOM_STATUS_2026-05-21_V2_1_DPHI_REVIEW_HANDOFF.md
DEPLOYMENT: none
AUTHORITY: none
HUMAN_ROOT_REQUIRED: true
```

## Purpose

Convert the D-Φ-1 v0.4 controlled review packet into a first-pass set of validator candidates.

This document does not implement validators. It defines reviewable checks that can later become schemas, tests, CI jobs, or reference implementation guards.

## Operating invariant

```text
Interpretation before legality.
Legality before execution.
Receipts before promotion.
Human-root before canon.
```

## Validation categories

```text
V1 Predicate ordering
V2 Status / authority scope
V3 Edge legality vs path legality
V4 Receipt and replay protection
V5 Fallback state semantics
V6 Merge / ratification block
```

## V1 — Predicate ordering validator

### Candidate rule

A transition validator should evaluate structural checks before semantic or authority checks.

Minimum expected order:

```text
rsv_zero -> coordinate_valid -> z_in_domain -> tag_not_reserved -> status_scope_valid -> path_valid -> receipt_valid
```

### Test cases

```yaml
- id: V1-001
  input: reserved_bits_nonzero
  expected: FALSE
  must_not_reach:
    - coordinate_interpretation
    - execution

- id: V1-002
  input: z_out_of_domain
  expected: FALSE
  must_preserve_lineage: true

- id: V1-003
  input: reserved_tag
  expected: QUARANTINE
  must_not_execute: true
```

### Blocking condition

```text
Any failed structural predicate can still advance execution.
```

## V2 — artifact_status / authority_scope validator

### Candidate rule

Every transition must carry explicit `artifact_status` and `authority_scope`.

Safe defaults:

```text
missing artifact_status -> HOLD
missing authority_scope -> HOLD
candidate without approval -> authority_weight = 0
unknown status -> QUARANTINE
```

### Test cases

```yaml
- id: V2-001
  input:
    artifact_status: null
    authority_scope: review_only
  expected: HOLD

- id: V2-002
  input:
    artifact_status: candidate
    authority_scope: canon_promotion
    human_root_signature: null
  expected: HOLD
  authority_weight: 0

- id: V2-003
  input:
    artifact_status: unknown_magic_status
    authority_scope: execution
  expected: QUARANTINE
```

### Blocking condition

```text
Visibility, retrieval, simulation, or memory implies permission.
```

## V3 — Edge legality vs path legality validator

### Candidate rule

A locally valid packet/edge is not sufficient for execution. The full route must be legal, non-destructive, ordered, and receipted.

### Test cases

```yaml
- id: V3-001
  input:
    edge_valid: true
    path_receipted: false
  expected: HOLD

- id: V3-002
  input:
    edge_valid: true
    path_destructive: true
  expected: QUARANTINE

- id: V3-003
  input:
    edge_valid: true
    sequence_counter_order: out_of_order
  expected: HOLD
```

### Blocking condition

```text
Valid packet shape is sufficient for execution.
```

## V4 — Receipt and replay protection validator

### Candidate rule

Any state-advancing transition must bind to a parent anchor and canonicalized delta receipt.

Required receipt fields:

```yaml
receipt:
  parent_anchor:
  delta_hash:
  canonicalization_policy:
  sequence_counter:
  tool_version:
  timestamp:
  authority_scope:
```

### Test cases

```yaml
- id: V4-001
  input:
    parent_anchor: null
    delta_hash: present
  expected: HOLD

- id: V4-002
  input:
    sequence_counter: duplicate
  expected: QUARANTINE

- id: V4-003
  input:
    delta_hash: present
    canonicalization_policy: null
  expected: HOLD
```

### Blocking condition

```text
Hash claims are accepted without canonicalization policy.
```

## V5 — Fallback state semantics validator

### Candidate rule

Fallback states must preserve lineage and block unreviewed advancement.

Required semantics:

```yaml
FALSE:
  transition_advances: false
  lineage_preserved: true

UNRESOLVED:
  promotion_allowed: false
  requires_review_or_receipts: true

HOLD:
  promotion_allowed: false
  requires_expiration_or_review_trigger: true

QUARANTINE:
  deletion_allowed: false
  promotion_allowed: false
  warning_required: true
```

### Test cases

```yaml
- id: V5-001
  input: FALSE_transition
  expected:
    lineage_preserved: true
    execution: false

- id: V5-002
  input: UNRESOLVED_transition
  expected:
    promotion: false
    next_action_required: true

- id: V5-003
  input: HOLD_without_expiry
  expected: INVALID_HOLD

- id: V5-004
  input: QUARANTINE_artifact
  expected:
    deletion: false
    promotion: false
```

### Blocking condition

```text
FALSE deletes lineage, UNRESOLVED promotes, HOLD never expires, or QUARANTINE is treated as deletion or approval.
```

## V6 — Merge / ratification block validator

### Candidate rule

No merge, canon promotion, deployment, or authority transfer can be inferred from score, visibility, memory, hash, or review pass.

### Test cases

```yaml
- id: V6-001
  input:
    review_verdict: PASS
    human_root_decision: null
    action: canon_promotion
  expected: BLOCK

- id: V6-002
  input:
    hash_valid: true
    action: deployment
    human_root_decision: null
  expected: BLOCK

- id: V6-003
  input:
    memory_retrieved: true
    action: execution_authority
  expected: BLOCK
```

### Blocking condition

```text
Automatic canon promotion, automatic deployment, or authority transfer from artifact existence.
```

## Proposed next implementation path

```text
1. Keep this document as candidate validator design.
2. Collect S1/S2/S4/S5/S7 review on issue #122.
3. Convert accepted validator candidates into YAML schema or Python tests.
4. Add CI only after review confirms scope.
5. Require S10 approval before any merge/promotion behavior.
```

## No-canon-promotion statement

This document is a candidate validator design. It does not ratify D-Φ-1, approve implementation, authorize deployment, or create merge authority.
