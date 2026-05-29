# Adjudication Receipt Template

## Summary

Captures the formal record of @atlaslattice's adjudication decision on an artifact.
One receipt is required per ratification or rejection event.

---

## Template

```yaml
---
receipt_id: "ADJ-YYYY-NNN"
artifact_id: "<artifact_id>"
artifact_title: "<title>"
artifact_path: "<path/to/artifact.md>"
adjudicated_by: "@atlaslattice"
adjudication_utc: "YYYY-MM-DDTHH:MM:SSZ"
decision: RATIFIED | REJECTED | DEFERRED
prior_status: CAND | RAT_PEND
new_status: CANON | REJECT | CAND
trust_state_after: RATIFIED | UNVERIFIED | REVIEWED
ratification_event_id: "RAT-YYYY-NNN"   # required if decision == RATIFIED
council_review_ids: []                   # list of council sign-off record IDs
---
```

## Decision rationale

```text
[Concise rationale for the decision. Include any conditions or caveats.]
```

## Conditions / follow-up actions

- [ ] _Condition 1 (if any)_
- [ ] _Condition 2 (if any)_

## Source lineage reviewed

```text
- [list of sources, prior artifacts, or evidence reviewed during adjudication]
```

## Audit trail

```text
This receipt is the durable record of the adjudication event.
Do not alter after @atlaslattice signature. Corrections require a new receipt.
```

---

## Filing instructions

1. Copy this template to `docs/governance/receipts/ADJ-YYYY-NNN.md`.
2. Fill all YAML fields.
3. Link from the artifact's frontmatter: `adjudication_receipt_id: ADJ-YYYY-NNN`.
4. Link from the [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md).

---

## Cross-links

- [Ratification Event Template](./RATIFICATION_EVENT_TEMPLATE.md)
- [Canon Lifecycle State Machine](./CANON_LIFECYCLE_STATE_MACHINE.md)
- [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md)

## Status

`candidate` — not canon until ratified.
