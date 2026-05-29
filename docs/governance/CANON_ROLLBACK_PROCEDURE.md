# Canon Rollback Procedure

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #9
LAST_UPDATED: 2026-05-29
```

Defines how to safely roll back a ratified artifact when the ratification
must be reversed or a critical error is discovered post-canonization.

---

## When Rollback Is Appropriate

- A `CRITICAL` dispute reveals the ratification was invalid.
- The `ratification_event_id` is found to be fraudulent or improperly assigned.
- Content is later found to contain PII, secrets, or license violations.
- @atlaslattice explicitly revokes a ratification decision.

---

## What "Rollback" Means

Rollback does **not** delete history. It means:

1. The artifact's `trust_state` is downgraded (e.g. `AUTHORITATIVE` →
   `CANDIDATE` or `DEPRECATED`).
2. The `ratification_event_id` is preserved in the artifact's frontmatter but
   annotated as revoked.
3. A `ROLLBACK_REASON` field is added.
4. All downstream artifacts that cited this one are flagged for review.

Git history is never rewritten to remove the ratified artifact; GitHub provides
the immutable substrate.

---

## Rollback Steps

### Step 1 — Initiate

- Open a GitHub Issue with title `[CANON ROLLBACK] <artifact-path>`.
- Apply label `canon-rollback`.
- Tag @atlaslattice for immediate review.

### Step 2 — Immediate Suspension (if severity warrants)

For `CRITICAL` issues (e.g. PII, secrets):

```bash
# In a PR, update artifact frontmatter immediately:
TRUST_STATE: SUSPENDED
ROLLBACK_ISSUE: #<issue-number>
```

Merge as emergency override. Council review follows the merge.

### Step 3 — Impact Assessment

- [ ] Identify all artifacts that cite the rolled-back artifact.
- [ ] Identify all KG edges sourced from this artifact.
- [ ] Identify all external publications (website, mirrors) referencing it.
- [ ] Assess whether downstream artifacts are materially affected.

### Step 4 — Adjudication

@atlaslattice makes the binding rollback decision:

| Decision | Action |
|---|---|
| Full rollback | `trust_state: DEPRECATED`, `canon_status: DEPRECATED` |
| Partial rollback | Specific claims revoked; artifact amended and re-reviewed |
| Reinstatement | Dispute resolved; `trust_state` restored |

### Step 5 — Artifact Update

Update frontmatter:

```
STATUS: DEPRECATED  (or CANDIDATE if re-review path chosen)
RATIFICATION_EVENT_ID: GOV-2026-001  (preserved)
ROLLBACK_EVENT_ID: GOV-2026-002  (new event ID for rollback)
ROLLBACK_DATE: YYYY-MM-DD
ROLLBACK_REASON: <brief reason>
ROLLBACK_ADJUDICATOR: @atlaslattice
TRUST_STATE: DEPRECATED  (or CANDIDATE)
```

### Step 6 — Downstream Remediation

- File issues against each affected downstream artifact.
- Re-validate KG integrity: `python scripts/check_graph_link_integrity.py`.
- Update external publications to remove or qualify canon claims.
- Log the rollback event in `GOVERNANCE_CHANGELOG_TEMPLATE.md`.

---

## Invariants

- No Git history rewrite. Rollback is always a forward commit.
- `ratification_event_id` is never removed; it is annotated as revoked.
- Rollback events receive their own `GOV-<YYYY>-<NNN>` event ID.

---

## Related

- [CANON_DISPUTE_RESOLUTION.md](./CANON_DISPUTE_RESOLUTION.md)
- [GOVERNANCE_CHANGELOG_TEMPLATE.md](./GOVERNANCE_CHANGELOG_TEMPLATE.md)
- [TRUST_STATE_TAXONOMY.md](./TRUST_STATE_TAXONOMY.md)
