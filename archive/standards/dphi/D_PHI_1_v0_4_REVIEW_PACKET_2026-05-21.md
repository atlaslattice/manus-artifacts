# D-Φ-1 v0.4 — Controlled Review Packet

```text
STATUS: REVIEW PACKET — CANDIDATE — NOT CANON
DATE: 2026-05-21
DEPLOYMENT: none
AUTHORITY: none
SOURCE: archive/standards/dphi/D_PHI_1_v0_4_REVIEW_SUPPORT_2026-05-21.md
PURPOSE: convert D-Φ-1 review focus into checkable review questions and blocking criteria
HUMAN_ROOT_REQUIRED: true
```

## Scope

This packet is a review scaffold. It does not create doctrine, canon, deployment authority, or merge approval.

It converts the standing review focus into a structured checklist:

```text
1. Predicate correctness
2. artifact_status / authority_scope enforcement
3. Edge legality vs path legality
4. Receipt and replay protection
5. FALSE / UNRESOLVED / HOLD / QUARANTINE behavior
6. What blocks merge or ratification
```

## Review invariant

```text
Interpretation before legality.
Legality before execution.
Receipts before promotion.
Human-root before canon.
```

## Reviewer output format

Each reviewer should return:

```yaml
reviewer:
seat_or_role:
review_scope:
verdict: PASS | PASS_WITH_PATCHES | REQUEST_CHANGES | BLOCK
blocking_findings:
  - id:
    issue:
    required_change:
patch_findings:
  - id:
    issue:
    suggested_change:
non_blocking_notes:
  - note:
residual_risks:
  - risk:
human_root_decision_needed:
  - decision:
```

## 1. Predicate correctness

### Questions

```text
Q1. Are packet predicates ordered so cheap/structural rejections happen before expensive or semantic checks?
Q2. Are reserved bits checked before coordinate interpretation?
Q3. Is z-domain validity separated from semantic tag validity?
Q4. Does a failed predicate preserve lineage while blocking execution?
```

### Expected minimum predicate order

```text
rsv_zero -> coordinate_valid -> z_in_domain -> tag_not_reserved -> status_scope_valid -> path_valid -> receipt_valid
```

### Blocking conditions

```text
- Any predicate failure can still advance execution.
- Reserved tags can be interpreted as valid operational states.
- Predicate failure deletes lineage instead of producing FALSE/HOLD/QUARANTINE record.
```

## 2. artifact_status / authority_scope enforcement

### Questions

```text
Q1. Does every transition carry artifact_status?
Q2. Does every transition carry authority_scope?
Q3. Is candidate visibility prevented from becoming administrative authority?
Q4. Is human-root signature or equivalent explicit approval required for canon or merge authority?
```

### Required safe defaults

```text
missing artifact_status -> HOLD
missing authority_scope -> HOLD
candidate without approval -> authority_weight = 0
unknown status -> QUARANTINE
```

### Blocking conditions

```text
- Candidate packet can carry administrative weight without explicit approval.
- Retrieval, memory, visibility, or simulation implies permission.
- authority_scope defaults to broad access.
```

## 3. Edge legality vs path legality

### Definitions

```text
edge_legality = local structural validity of a packet, edge, or transition
path_legality = validity of the full ordered route through time, receipts, and authority gates
```

### Questions

```text
Q1. Can a structurally valid edge still be blocked because the path is unreceipted or destructive?
Q2. Are chronological sequence counters checked before state advancement?
Q3. Are non-destructive path constraints explicit?
```

### Blocking conditions

```text
- Valid packet shape is sufficient for execution.
- Edge legality is treated as path legality.
- Destructive or unreceipted path can advance state.
```

## 4. Receipt and replay protection

### Questions

```text
Q1. Does each transition bind to a parent anchor?
Q2. Are sequence counters monotonic or otherwise replay-protected?
Q3. Is canonical byte representation defined before hash claims?
Q4. Are duplicate transitions routed to HOLD/QUARANTINE rather than silently accepted?
```

### Required receipt fields

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

### Blocking conditions

```text
- Hash claims without canonicalization policy.
- Duplicate sequence counter accepted without warning.
- Parent anchor absent or optional for state mutation.
```

## 5. FALSE / UNRESOLVED / HOLD / QUARANTINE behavior

### Required semantics

```text
FALSE:
  transition fails; lineage preserved; no execution

UNRESOLVED:
  transition holds; requires additional receipts or reviewer action

HOLD:
  bounded pause; must have expiration or next review trigger

QUARANTINE:
  preserved with warning; no deletion; no promotion
```

### Questions

```text
Q1. Does FALSE kill transition without deleting evidence?
Q2. Does UNRESOLVED avoid promotion and avoid false rejection?
Q3. Does HOLD include expiration or next review trigger?
Q4. Does QUARANTINE preserve the artifact with warnings and block promotion?
```

### Blocking conditions

```text
- FALSE deletes lineage.
- UNRESOLVED can promote.
- HOLD has no expiry or review trigger.
- QUARANTINE is treated as deletion or as approval.
```

## 6. Merge / ratification block

### Questions

```text
Q1. Does any path allow branch merge without human-root approval?
Q2. Does any path allow canonical promotion from score, visibility, memory, or hash alone?
Q3. Does any review output confuse pass-for-review with deployability?
```

### Absolute blockers

```text
- Automatic canon promotion.
- Automatic deployment.
- Authority transfer from artifact existence.
- Merge or ratification without explicit S10 / human-root decision.
```

## Current safe claim

> D-Φ-1 v0.4 is in controlled review. The current artifacts are candidate review scaffolds. They define questions, failure modes, and blocking criteria but do not create canon, deployment, or authority.

## Review routing

```text
S1 / GPTBrain: evidence and promotion semantics
S2 / ClaudeBrain: constitutional wording and authority boundaries
S4 / GeminiBrain: schema / predicate / implementation mapping
S5 / DeepSeek: adversarial stress and failure modes
S7 / CopilotBrain: repo hygiene, CI, validator path
S10 / Human-root: final adjudication only after review packet
```

## No-canon-promotion statement

This review packet is candidate scaffolding. It does not ratify D-Φ-1, does not approve merge, and does not authorize implementation or deployment. Human-root review is required before any promotion.
