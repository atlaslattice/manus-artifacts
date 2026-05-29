# Governance Change Log Template

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #10
LAST_UPDATED: 2026-05-29
```

Template and running log for all governance events: ratifications, rollbacks,
disputes, and policy changes.

---

## Log Format

Each entry uses the following fields:

```
| Event ID | Date | Type | Artifact / Policy | Decision | Adjudicator | Notes |
```

**Event Types:**

| Code | Type |
|---|---|
| `RAT` | Ratification |
| `ROL` | Rollback |
| `DIS` | Dispute opened |
| `DRC` | Dispute resolved/closed |
| `POL` | Policy change |
| `AUD` | Audit event |

---

## Event ID Sequence Register

| Event ID | Date | Type | Summary |
|---|---|---|---|
| *(no events yet)* | — | — | — |

---

## How to Add an Entry

1. Assign the next sequential event ID (`GOV-<YYYY>-<NNN>`).
2. Record the event in the table below.
3. Update the artifact's frontmatter with the event ID.
4. Commit both changes in the same PR.

---

## Governance Event Log

> Authoritative record of all governance actions taken.

| Event ID | Date | Type | Artifact / Policy | Decision | Adjudicator | Notes |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

*First governance event pending first ratification session.*

---

## Annual Summary

| Year | Events | Ratifications | Rollbacks | Disputes | Policy Changes |
|---|---|---|---|---|---|
| 2026 | 0 | 0 | 0 | 0 | 0 |

---

## Related

- [RATIFICATION_EVENT_ID_STANDARD.md](./RATIFICATION_EVENT_ID_STANDARD.md)
- [CANON_ADJUDICATION_CHECKLIST.md](./CANON_ADJUDICATION_CHECKLIST.md)
- [CANON_ROLLBACK_PROCEDURE.md](./CANON_ROLLBACK_PROCEDURE.md)
- [GOVERNANCE_AUDIT_CADENCE.md](./GOVERNANCE_AUDIT_CADENCE.md)
