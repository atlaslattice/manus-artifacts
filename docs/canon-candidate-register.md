# Canon Candidate Register

```
STATUS: CANDIDATE — NOT CANON
PURPOSE: lightweight tracking of artifacts in the candidate→canon promotion pipeline
GOVERNANCE: GOVERNANCE.md, docs/canon-trust-hierarchy.md
LAST_UPDATED: 2026-05-28
```

All artifacts in this repository start as **candidates**. This register tracks
each artifact's movement through the canon pipeline. No artifact is canon until
ratified by full council and adjudicated by @atlaslattice.

---

## Pipeline States

```
DRAFT → CANDIDATE → UNDER_REVIEW → RATIFIED
                  ↘ DEPRECATED
```

| State | Meaning |
|---|---|
| DRAFT | In local branch, issue, or PR — not yet committed |
| CANDIDATE | Committed to `main`, under informal review |
| UNDER_REVIEW | Nominated for full council ratification session |
| RATIFIED | Canonized; requires `ratification_event_id` |
| DEPRECATED | Superseded; preserved for traceability |

---

## Minimum Fields for Promotion to RATIFIED

Each artifact seeking promotion must carry:

```yaml
ratification_event_id: <event-id>   # e.g. "GOV-2026-001"
canon_status: RATIFIED
trust_state: AUTHORITATIVE
```

---

## Active Candidate Register

> Maintainer: update this table when nominiting artifacts for review.

| # | Artifact Path | Status | Nominated By | Target Review Date | Notes |
|---|---|---|---|---|---|
| C-001 | `archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md` | CANDIDATE | @atlaslattice | TBD | Full spec vault |
| C-002 | `archive/spec/gptdream/REHYDRATION_BOOT_CARD.md` | CANDIDATE | @atlaslattice | TBD | Rehydration protocol |
| C-003 | `GOVERNANCE.md` | CANDIDATE | @atlaslattice | TBD | Core governance doc |
| C-004 | `PHILOSOPHY.md` | CANDIDATE | @atlaslattice | TBD | Vision document |
| C-005 | `docs/canon-trust-hierarchy.md` | CANDIDATE | @atlaslattice | TBD | Trust hierarchy ref |
| C-006 | `archive/boot/COUNCIL_BRAIN_INDEX.md` | CANDIDATE | @atlaslattice | TBD | Brain map |
| C-007 | `aluminum-os/v4.0-unified-field.md` | CANDIDATE | @atlaslattice | TBD | Aluminum OS canonical spec |

---

## Ratification Log

> Completed ratification events. Each entry requires a governance session record.

| Event ID | Date | Artifact | Council Session | Adjudicator |
|---|---|---|---|---|
| — | — | — | — | — |

*No artifacts have been formally ratified yet. First ratification session pending.*

---

## How to Nominate an Artifact

1. Open a [Governance Review Request](https://github.com/atlaslattice/manus-artifacts/issues/new?template=mission_intake.yml) issue.
2. Add a row to the **Active Candidate Register** table above in a PR.
3. Ensure the artifact carries all minimum metadata fields.
4. Tag @atlaslattice for adjudication scheduling.

---

## Related Documents

- [GOVERNANCE.md](../GOVERNANCE.md)
- [docs/canon-trust-hierarchy.md](./canon-trust-hierarchy.md)
- [.github/CONTRIBUTING.md](../.github/CONTRIBUTING.md)
