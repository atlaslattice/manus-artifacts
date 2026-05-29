# Canon Adjudication Checklist

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #6
LAST_UPDATED: 2026-05-29
```

Step-by-step checklist for @atlaslattice and the Aetherforge Council to use
when adjudicating an artifact for canon promotion.

---

## Pre-Adjudication (Before Session)

- [ ] Artifact is committed to `main` in `atlaslattice/manus-artifacts`
- [ ] Artifact carries `STATUS: CANDIDATE — NOT CANON` or `UNDER_REVIEW` header
- [ ] `docs/canon-candidate-register.md` contains an entry for this artifact
- [ ] No open `canon-dispute` issues against this artifact
- [ ] Artifact has passed metadata validation
  (`scripts/validate_artifact_metadata.py`)
- [ ] Artifact has passed graph link integrity check
  (`scripts/check_graph_link_integrity.py`)
- [ ] All inbound links to the artifact are valid
- [ ] All outbound citations in the artifact are valid and sourced

---

## Substance Review (During Session)

- [ ] Artifact content is accurate and internally consistent
- [ ] Claims are supported by cited evidence
- [ ] No PII or secrets present
- [ ] License is compatible with repository MIT license
- [ ] No contradictions with existing `AUTHORITATIVE` artifacts
  (or contradictions are explicitly flagged and scoped)
- [ ] Provenance chain is clear: source, transformation history, authorship

---

## Governance Mechanics (During Session)

- [ ] Council quorum present or asynchronous sign-off recorded
- [ ] Assign next sequential `ratification_event_id` (e.g. `GOV-2026-001`)
- [ ] Record session in governance changelog
- [ ] @atlaslattice provides explicit adjudication statement

---

## Post-Adjudication (After Session)

- [ ] Update artifact frontmatter:
  - `STATUS: RATIFIED`
  - `RATIFICATION_EVENT_ID: GOV-<YYYY>-<NNN>`
  - `CANON_STATUS: RATIFIED`
  - `TRUST_STATE: AUTHORITATIVE`
  - `RATIFIED_BY: @atlaslattice`
  - `RATIFICATION_DATE: <date>`
- [ ] Update `docs/canon-candidate-register.md` — move to Ratification Log
- [ ] Update `docs/LATTICE_GLOBAL_INDEX.md` entry if present
- [ ] Notify downstream dependents if any canonical references changed
- [ ] If website publication intended, apply `website-canon` label

---

## Rejection Path

If adjudication does not result in ratification:

- [ ] Record reason in candidate register under "Notes"
- [ ] Revert artifact `STATUS` to `CANDIDATE — NOT CANON` if it was changed
- [ ] File a follow-up issue with required remediation steps
- [ ] Artifact may be re-nominated after remediation is complete

---

## Related

- [CANDIDATE_TO_CANON_WORKFLOW.md](./CANDIDATE_TO_CANON_WORKFLOW.md)
- [RATIFICATION_EVENT_ID_STANDARD.md](./RATIFICATION_EVENT_ID_STANDARD.md)
- [CANON_DISPUTE_RESOLUTION.md](./CANON_DISPUTE_RESOLUTION.md)
- [docs/canon-candidate-register.md](../canon-candidate-register.md)
