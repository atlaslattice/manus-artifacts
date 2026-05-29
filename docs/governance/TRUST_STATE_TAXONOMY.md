# Trust State Taxonomy

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #5
LAST_UPDATED: 2026-05-29
```

Defines all allowed values for the `trust_state` field and their semantics
within the Aetherforge knowledge graph and canon lifecycle.

---

## Taxonomy Table

| `trust_state` | Code | Meaning | Allowed `canon_status` |
|---|---|---|---|
| `WORKING` | `TW` | Relay/working-vault layer content; not used for formal trust decisions | `DRAFT`, `CANDIDATE` |
| `CANDIDATE` | `TC` | Committed, under review; may be cited but not authoritative | `CANDIDATE` |
| `UNDER_REVIEW` | `TU` | Nominated for ratification; citations should note pending status | `UNDER_REVIEW` |
| `AUTHORITATIVE` | `TA` | Ratified; acts as source of truth for downstream citations | `RATIFIED` |
| `DISPUTED` | `TD` | Active contradiction or challenge is open; use with caution | Any |
| `SUPERSEDED` | `TS` | A newer ratified version exists; cites its successor | `DEPRECATED` |
| `DEPRECATED` | `TX` | Retired from active use; preserved for traceability | `DEPRECATED` |

---

## State Transition Diagram

```
                ┌──────────┐
                │  WORKING │  (relay layer, not tracked in canon pipeline)
                └──────────┘
                     │ commit to main
                     ▼
                ┌───────────┐
                │ CANDIDATE │ ──── dispute filed ──→ DISPUTED
                └───────────┘
                     │ nominated
                     ▼
              ┌──────────────┐
              │ UNDER_REVIEW │ ──── dispute filed ──→ DISPUTED
              └──────────────┘
                     │ ratified
                     ▼
              ┌───────────────┐
              │ AUTHORITATIVE │ ──── dispute filed ──→ DISPUTED
              └───────────────┘       │ superseded
                                      ▼
                               ┌────────────┐
                               │ SUPERSEDED │
                               └────────────┘
                                      │ final retirement
                                      ▼
                               ┌────────────┐
                               │ DEPRECATED │
                               └────────────┘
```

---

## Usage Rules

1. `AUTHORITATIVE` requires a valid `ratification_event_id`.
2. `DISPUTED` may be applied to any state; it does not remove other fields.
3. A `DISPUTED` artifact that resolves its dispute reverts to its prior state
   (or advances if resolution involved a ratification).
4. `SUPERSEDED` artifacts must carry a `superseded_by` field pointing to the
   successor artifact path.
5. `DEPRECATED` artifacts retain all prior metadata fields for traceability.

---

## KG Edge Semantics

In the knowledge graph, `trust_state` drives edge weighting:

| Edge type | `trust_state` modifier |
|---|---|
| Citation | Full weight only from `AUTHORITATIVE` sources |
| Reference | Allowed from `CANDIDATE`+ but annotated |
| Contradiction | Triggers `DISPUTED` on conflicting nodes |
| Provenance chain | Traces through `SUPERSEDED` edges |

---

## Related

- [CANON_STATUS_FRONTMATTER.md](./CANON_STATUS_FRONTMATTER.md)
- [RATIFICATION_EVENT_ID_STANDARD.md](./RATIFICATION_EVENT_ID_STANDARD.md)
- [CANON_DISPUTE_RESOLUTION.md](./CANON_DISPUTE_RESOLUTION.md)
