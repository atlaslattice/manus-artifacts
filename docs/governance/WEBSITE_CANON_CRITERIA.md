# Website Canon Publication Criteria

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #1
LAST_UPDATED: 2026-05-29
```

Defines the conditions under which content published on the Atlas Lattice
website surface is considered **canonical**.

---

## Governing Principle

Website publication does **not** automatically confer canon status. Content is
canonical on the website only when it has been explicitly ratified through the
full council process and published with that intent.

See [canon-trust-hierarchy.md](../canon-trust-hierarchy.md) and
[GOVERNANCE.md](../../GOVERNANCE.md).

---

## Publication Tiers

| Tier | Label | Criteria |
|---|---|---|
| **Exploratory** | `website-draft` | Published for feedback; no canon claim |
| **Candidate Mirror** | `website-candidate` | GitHub-committed candidate mirrored to web |
| **Canon Surface** | `website-canon` | Explicitly ratified; carries `ratification_event_id` |

---

## Minimum Requirements for `website-canon` Designation

An artifact published on the website may only carry the `website-canon`
designation when ALL of the following are true:

1. **GitHub commit exists** — The artifact is committed to `main` in
   `atlaslattice/manus-artifacts`.
2. **Ratification event recorded** — A `ratification_event_id` is present in
   the artifact frontmatter (e.g. `GOV-2026-001`).
3. **`canon_status: RATIFIED`** — Frontmatter field is set.
4. **`trust_state: AUTHORITATIVE`** — Frontmatter field is set.
5. **Council sign-off** — At least one council session record references the
   artifact by its ratification event ID.
6. **@atlaslattice adjudication** — Explicit adjudication on record.
7. **No open disputes** — No active canon dispute issues filed against the
   artifact.

---

## What Website Publication Does NOT Grant

- It does not upgrade `CANDIDATE` to `RATIFIED`.
- It does not substitute for `ratification_event_id`.
- It does not override GitHub as the canonical substrate.
- Mirroring to web does not imply council review has occurred.

---

## Process Summary

```
GitHub commit (CANDIDATE)
    → Council nomination
    → Council ratification session + event ID assigned
    → @atlaslattice adjudication
    → Frontmatter updated: canon_status=RATIFIED, trust_state=AUTHORITATIVE
    → Website published with website-canon label
```

---

## Related

- [CANDIDATE_TO_CANON_WORKFLOW.md](./CANDIDATE_TO_CANON_WORKFLOW.md)
- [CANON_STATUS_FRONTMATTER.md](./CANON_STATUS_FRONTMATTER.md)
- [RATIFICATION_EVENT_ID_STANDARD.md](./RATIFICATION_EVENT_ID_STANDARD.md)
