# Trust-State Glossary

## Summary

Authoritative definitions of trust and canon state terminology used across AtlasLattice.
All governance documents and artifact metadata MUST use these terms consistently.

---

## Trust states

| Term | Code | Definition |
|---|---|---|
| **Unverified** | `UNVERIFIED` | No review has occurred. Content may be AI-generated, imported, or draft. |
| **Reviewed** | `REVIEWED` | At least one human reviewer has assessed the artifact; not yet ratified. |
| **Ratified** | `RATIFIED` | Full council review + @atlaslattice adjudication complete. Canon-eligible. |

---

## Canon states

| Term | Code | Definition |
|---|---|---|
| **Draft** | `DRAFT` | Work in progress. Not ready for review. |
| **Candidate** | `CAND` | Submitted for review. Publicly visible. Explicitly NOT canon. |
| **Ratification pending** | `RAT_PEND` | Council review complete; awaiting @atlaslattice adjudication. |
| **Canon** | `CANON` | Authoritative. Requires `RATIFIED` trust state and `ratification_event_id`. |
| **Superseded** | `SUPERS` | Replaced by a newer canon artifact. Read-only archive. |
| **Rejected** | `REJECT` | Failed ratification. Archived for audit purposes. |
| **Archived** | `ARCH` | Withdrawn or obsolete. Retained for historical provenance. |

---

## Compound states

| Compound | Meaning |
|---|---|
| `is_canon()` | Returns true only when: `canon_status == CANON` AND `trust_state == RATIFIED` AND `ratification_event_id` is set. |
| `is_active_candidate()` | Returns true when: `canon_status == CAND` AND not archived. |
| `is_in_flight()` | Returns true when: `canon_status == RAT_PEND`. |

---

## Layered trust model

```
RATIFIED  ←── highest trust; backed by full council + human-root adjudication
REVIEWED  ←── intermediate; human eyes applied, governance not complete
UNVERIFIED ←── default; no trust claim made
```

---

## NOT-synonyms (common confusions)

| Term to avoid | Use instead | Why |
|---|---|---|
| "live" | `CANON` | "Live" implies deployment; canon is a governance state |
| "approved" | `RATIFIED` | Approval is vague; ratification is the specific act |
| "published" | `CANON + published_at set` | Publishing to a website ≠ ratification |
| "official" | `CANON` | "Official" lacks a traceable governance record |
| "verified" | `REVIEWED` or `RATIFIED` | Distinguish human review from full ratification |

---

## Cross-links

- [Canon Lifecycle State Machine](./CANON_LIFECYCLE_STATE_MACHINE.md)
- [Canon Metadata Standard](./CANON_METADATA_STANDARD.md)
- [Claim Verification Checklist](./CLAIM_VERIFICATION_CHECKLIST.md)
- [Governance Operations Handbook](./GOVERNANCE_OPERATIONS_HANDBOOK.md)

## Status

`candidate` — not canon until ratified.
