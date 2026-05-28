---
artifact_id: GOV-ADJUDICATION-EVIDENCE-TEMPLATE-v0-1-2026-05-28
title: Adjudication Evidence Template
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Adjudication Evidence Template

> Copy this template when recording a ratification, demotion, or conflict-resolution adjudication decision.

---

## Adjudication Record

**Adjudication Event ID:** `ADJ-YYYY-MM-DD-NNN`  
**Date:** YYYY-MM-DD  
**Adjudicator:** @atlaslattice  
**Artifact(s) Under Review:**

| Artifact ID | Title | File Path |
|---|---|---|
| `ARTIFACT-ID` | Title here | `path/to/artifact.md` |

**Type of Adjudication:**

- [ ] Ratification (CANDIDATE → RATIFIED)
- [ ] Demotion (RATIFIED → lower status)
- [ ] Conflict resolution
- [ ] Emergency security/PII action
- [ ] Other: ___

---

## Summary of Evidence Reviewed

1. _Council review thread link or reference_
2. _Objections raised and responses_
3. _Supporting artifacts or external references_

---

## Council Vote Summary

| Council Member | Vote | Notes |
|---|---|---|
| @member | APPROVE / REJECT / ABSTAIN | |

**Vote result:** PASS / FAIL / DEFERRED

---

## Adjudicator Decision

**Decision:** RATIFIED / REJECTED / DEFERRED / DEMOTED / ARCHIVED

**Rationale:**

> _State the reason for the decision, including any conditions or caveats._

---

## Conditions and Follow-up Actions

| Action | Owner | Due | Status |
|---|---|---|---|
| | | | |

---

## Frontmatter Directives

Fields to update on the adjudicated artifact:

```yaml
canon_status: RATIFIED      # or REJECTED / ARCHIVED / CANDIDATE
trust_state: CANON          # or NON_CANON / CANDIDATE
ratification_event_id: RAT-YYYY-MM-DD-NNN   # if ratifying
demotion_event_id: DEM-YYYY-MM-DD-NNN       # if demoting
adjudication_event_id: ADJ-YYYY-MM-DD-NNN
last_updated: YYYY-MM-DD
```

---

## Related Artifacts

- [Ratification Lifecycle](./RATIFICATION_LIFECYCLE_v0_1.md)
- [Canon Promotion Checklist](./CANON_PROMOTION_CHECKLIST_v0_1.md)
- [Governance Decision Index](./GOVERNANCE_DECISION_INDEX_2026-05-28.md)
