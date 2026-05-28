# Governance Decision Index

## Summary

Chronological index of all formal governance decisions, adjudications, ratifications,
conflict resolutions, and policy changes in the AtlasLattice repository.

---

## Index table

| Decision ID | Date UTC | Type | Description | Record path | Decided by |
|---|---|---|---|---|---|
| GOV-2026-001 | 2026-05-28 | Policy | Governance operations handbook bootstrapped; Wave-1 candidate suite introduced | _this index_ | @atlaslattice |

---

## Decision types

| Type | Meaning |
|---|---|
| `Ratification` | Artifact elevated to CANON status |
| `Rejection` | Artifact ratification denied |
| `Policy` | New or updated governance policy |
| `Conflict resolution` | Formal resolution of an artifact conflict |
| `Supersession` | Existing canon artifact replaced |
| `Withdrawal` | Artifact voluntarily archived |
| `Adjudication` | Formal @atlaslattice ruling on a disputed artifact or claim |

---

## How to add an entry

1. After any governance event, add a row with a new `GOV-YYYY-NNN` ID.
2. Link to the detailed event record (ratification event, adjudication receipt, etc.).
3. Increment the sequence number within the year.

---

## Related record stores

- Ratification events: `docs/governance/events/RAT-YYYY-NNN.md`
- Adjudication receipts: `docs/governance/receipts/ADJ-YYYY-NNN.md`
- ADRs (Architecture Decision Records): `docs/decisions/`

---

## Cross-links

- [Canon Registry](./CANON_REGISTRY.md)
- [Candidate Registry](./CANDIDATE_REGISTRY.md)
- [Adjudication Receipt Template](./ADJUDICATION_RECEIPT_TEMPLATE.md)
- [Ratification Event Template](./RATIFICATION_EVENT_TEMPLATE.md)
- [Conflict-Resolution Playbook](./CONFLICT_RESOLUTION_PLAYBOOK.md)

## Status

`candidate` — not canon until ratified.
