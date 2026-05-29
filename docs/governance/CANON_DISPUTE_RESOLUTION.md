# Canon Dispute Resolution Workflow

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #8
LAST_UPDATED: 2026-05-29
```

Defines the process for raising, reviewing, and resolving disputes about
canon status, content accuracy, or trust classification of artifacts.

---

## When to File a Dispute

File a dispute when:

- An artifact marked `RATIFIED` / `AUTHORITATIVE` contains factual errors.
- Two `AUTHORITATIVE` artifacts make contradictory claims.
- A ratification was made without meeting the minimum criteria.
- An artifact is being cited with higher trust than its state warrants.
- A `ratification_event_id` cannot be verified against session records.

---

## Dispute States

```
OPEN → UNDER_REVIEW → RESOLVED
               ↓
           ESCALATED (to @atlaslattice)
```

---

## Filing a Dispute

1. Open a GitHub Issue with title `[CANON DISPUTE] <artifact-path>`.
2. Apply label `canon-dispute`.
3. Include:
   - Artifact path and current `ratification_event_id` (if any)
   - Nature of the dispute (factual error / contradiction / process violation)
   - Evidence supporting the dispute
   - Proposed resolution

4. Set the disputed artifact's `trust_state` to `DISPUTED` in a PR:
   ```
   TRUST_STATE: DISPUTED
   DISPUTE_ISSUE: #<issue-number>
   ```

---

## Review Process

### Council Triage (≤ 5 business days)

A council member is assigned as dispute reviewer:

- [ ] Confirm the dispute is actionable (not a duplicate or out-of-scope)
- [ ] Identify all artifacts affected
- [ ] Assess severity: `MINOR` (wording/metadata) / `MAJOR` (factual) / `CRITICAL` (process violation)

### Resolution Paths

| Severity | Resolution |
|---|---|
| `MINOR` | PR to correct artifact; @atlaslattice approves; dispute closed |
| `MAJOR` | Council review session required; may require re-ratification |
| `CRITICAL` | Immediate escalation to @atlaslattice; artifact may be suspended |

### Escalation

If not resolved within 14 days, or if severity is `CRITICAL`, the dispute is
escalated to @atlaslattice for binding decision.

---

## Resolution

Upon resolution:

1. Update artifact frontmatter: remove `DISPUTE_ISSUE`; restore or update
   `TRUST_STATE` to appropriate value.
2. If re-ratification required, follow
   [CANDIDATE_TO_CANON_WORKFLOW.md](./CANDIDATE_TO_CANON_WORKFLOW.md).
3. Close the dispute issue with resolution summary.
4. Log outcome in `GOVERNANCE_CHANGELOG_TEMPLATE.md`.

---

## Anti-Patterns to Avoid

- Do **not** unilaterally change `trust_state` on an `AUTHORITATIVE` artifact
  without filing a dispute.
- Do **not** delete ratified artifacts; use `DEPRECATED` with lineage trace.
- Do **not** cite a `DISPUTED` artifact as authoritative in downstream work.

---

## Related

- [CANON_ROLLBACK_PROCEDURE.md](./CANON_ROLLBACK_PROCEDURE.md)
- [TRUST_STATE_TAXONOMY.md](./TRUST_STATE_TAXONOMY.md)
- [CANON_ADJUDICATION_CHECKLIST.md](./CANON_ADJUDICATION_CHECKLIST.md)
