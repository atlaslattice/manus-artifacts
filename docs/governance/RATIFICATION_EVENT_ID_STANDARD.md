# `ratification_event_id` Field Standard

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #4
LAST_UPDATED: 2026-05-29
```

Defines the format, assignment process, and required usage of the
`ratification_event_id` field for canon artifacts.

---

## Purpose

The `ratification_event_id` is the primary immutable link between a ratified
artifact and its governance session record. It is the minimum proof that a
full council ratification event occurred.

---

## Format

```
GOV-<YYYY>-<NNN>
```

Where:
- `GOV` — fixed prefix (Governance)
- `<YYYY>` — four-digit year of the ratification session
- `<NNN>` — zero-padded three-digit sequence number, starting at `001` per year

**Examples:**
```
GOV-2026-001   (first ratification event of 2026)
GOV-2026-002
GOV-2026-015
```

---

## Assignment Process

1. A council session is scheduled for ratification.
2. @atlaslattice assigns the next sequential ID for the year.
3. The ID is recorded in the council session log.
4. The artifact's frontmatter is updated to include the ID.
5. The ID is logged in `docs/governance/GOVERNANCE_CHANGELOG_TEMPLATE.md`.

---

## Required Accompanying Fields

When `ratification_event_id` is set, all of the following must also be present:

```yaml
ratification_event_id: GOV-2026-001
canon_status: RATIFIED
trust_state: AUTHORITATIVE
ratified_by: "@atlaslattice"
ratification_date: "YYYY-MM-DD"
```

---

## Invariants

- IDs are **immutable** once assigned. They may not be reused or reassigned.
- If an artifact is deprecated after ratification, the `ratification_event_id`
  is preserved in its frontmatter as a historical record.
- Draft or candidate artifacts must **not** carry a `ratification_event_id`.

---

## Sequence Register

The authoritative sequence register is maintained in
[docs/governance/GOVERNANCE_CHANGELOG_TEMPLATE.md](./GOVERNANCE_CHANGELOG_TEMPLATE.md).

---

## Related

- [CANON_STATUS_FRONTMATTER.md](./CANON_STATUS_FRONTMATTER.md)
- [TRUST_STATE_TAXONOMY.md](./TRUST_STATE_TAXONOMY.md)
- [CANDIDATE_TO_CANON_WORKFLOW.md](./CANDIDATE_TO_CANON_WORKFLOW.md)
