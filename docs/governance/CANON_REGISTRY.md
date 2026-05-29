# Canon Registry

## Summary

Index of all artifacts that have achieved `CANON` status in the AtlasLattice repository.
Updated as ratification events are processed.

> **Note:** An artifact is canon only when `canon_status == CANON`, a `ratification_event_id` is set,
> and `trust_state == RATIFIED`. See the [Canon Lifecycle State Machine](./CANON_LIFECYCLE_STATE_MACHINE.md).

---

## Registry table

| Artifact ID | Title | Domain | Ratification Event | Ratified UTC | File path |
|---|---|---|---|---|---|
| _(none yet)_ | — | — | — | — | — |

---

## How to add an entry

1. Complete a full council review and obtain adjudication from @atlaslattice.
2. Set frontmatter: `canon_status: CANON`, `trust_state: RATIFIED`, `ratification_event_id: <id>`.
3. Add a row to the table above via PR.
4. Reference the ratification event file under `docs/governance/events/`.

---

## Cross-links

- [Candidate Registry](./CANDIDATE_REGISTRY.md)
- [Canon Lifecycle State Machine](./CANON_LIFECYCLE_STATE_MACHINE.md)
- [Ratification Event Template](./RATIFICATION_EVENT_TEMPLATE.md)
- [Adjudication Receipt Template](./ADJUDICATION_RECEIPT_TEMPLATE.md)
- [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md)

## Status

`candidate` — registry itself is not canon until ratified.
