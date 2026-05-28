# Canon Lifecycle State Machine

## Summary

Defines the authoritative state transitions for any artifact in the AtlasLattice repository.
No artifact advances without human-root adjudication by @atlaslattice and full council ratification.

---

## States

| State | Code | Meaning |
|---|---|---|
| `draft` | DRAFT | Work-in-progress. Not yet ready for review. |
| `candidate` | CAND | Submitted for council review. Publicly visible but explicitly NOT canon. |
| `ratification_pending` | RAT_PEND | Council review complete; awaiting @atlaslattice adjudication. |
| `canon` | CANON | Ratified by full council + adjudicated by @atlaslattice. Authoritative. |
| `superseded` | SUPERS | Replaced by a newer canon artifact. Archived, read-only. |
| `rejected` | REJECT | Failed ratification. Archived for audit trail. |
| `archived` | ARCH | Withdrawn or obsolete. Retained for historical provenance. |

---

## Transitions

```
[draft] ──submit──► [candidate] ──council_review_complete──► [ratification_pending]
                                                                        │
                                         ┌──────────────────────────────┤
                                         ▼                              ▼
                                      [canon]                       [rejected]
                                         │
                             ┌───────────┴───────────┐
                             ▼                       ▼
                        [superseded]            [archived]
```

### Transition rules

| From | To | Actor | Required evidence |
|---|---|---|---|
| `draft` | `candidate` | Contributor | PR opened; frontmatter `canon_status: CAND` |
| `candidate` | `ratification_pending` | Council seat | Council review sign-off recorded |
| `ratification_pending` | `canon` | @atlaslattice | `ratification_event_id` set; `trust_state: RATIFIED` |
| `ratification_pending` | `rejected` | @atlaslattice | Rejection note recorded in adjudication receipt |
| `canon` | `superseded` | @atlaslattice | Successor canon artifact linked |
| `canon` | `archived` | @atlaslattice | Withdrawal rationale recorded |
| `candidate` | `archived` | Contributor | Voluntary withdrawal |

---

## Invariants

- `is_canon()` returns `true` only when: `canon_status == CANON` AND `ratification_event_id` is set AND `trust_state == RATIFIED`.
- Artifacts at `draft` or `candidate` MUST display a not-canon banner.
- State regressions (e.g., `canon` → `candidate`) are not permitted; use `superseded` + new candidate.
- Every transition produces an adjudication receipt or governance event record.

---

## Cross-links

- [Canon Metadata Standard](./CANON_METADATA_STANDARD.md)
- [Adjudication Receipt Template](./ADJUDICATION_RECEIPT_TEMPLATE.md)
- [Ratification Event Template](./RATIFICATION_EVENT_TEMPLATE.md)
- [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md)
- [Governance Operations Handbook](./GOVERNANCE_OPERATIONS_HANDBOOK.md)

## Status

`candidate` — not canon until ratified by full council and adjudicated by @atlaslattice.
