---
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
artifact_id: KNOWLEDGE_GRAPH-KG-20260603-lattice-artifact-lifecycle-v1-0
path: archive/knowledge_graph/lattice_kg/v1_0/LATTICE_ARTIFACT_LIFECYCLE_v1.0.md
domain: knowledge_graph
lane: contracts
generated_at_utc: 2026-06-03T00:00:00Z
author: Copilot
version: "1.0"
---

# Lattice Artifact Lifecycle v1.0

## States
- `raw`
- `candidate`
- `under_review`
- `approved`
- `quarantined`
- `superseded`
- `ratified`

## ASCII state diagram
```text
raw -> candidate -> under_review -> approved -> ratified
  \         \            \            \-> superseded
   \         \-> quarantined -> under_review
    \-> quarantined
candidate -> superseded
approved -> quarantined
ratified -> superseded
```

## Transition guards
- Promotion never happens by self-assertion.
- `approved` and `ratified` require explicit review evidence.
- `ratified` requires `ratification_event_id`, signatures, and adjudication date.
- `candidate` and `under_review` remain `not_deployable`.

## Required fields by state
| State | Required fields |
|---|---|
| raw | path, source_receipt, generated_at_utc |
| candidate | artifact_id, status, authority, deployment, path, domain, lane |
| under_review | reviewer, review_lane, evidence_refs |
| approved | adjudication_summary, review_receipt |
| quarantined | quarantine_reason, next_safest_action |
| superseded | supersedes, effective_date |
| ratified | ratification_event_id, council_signatures, adjudication_date |
