---
artifact_id: GOV-RATIFICATION-LIFECYCLE-v0-1-2026-05-28
title: Ratification Lifecycle One-Pager
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Ratification Lifecycle One-Pager

> **Scope:** Defines the canonical pipeline an artifact travels from creation to ratified canon status.

## Pipeline Overview

```
DRAFT → CANDIDATE → UNDER_REVIEW → RATIFIED
                 ↘ REJECTED / ARCHIVED
```

### Stage Definitions

| Stage | Meaning | Entry Criteria | Exit Criteria |
|---|---|---|---|
| **DRAFT** | Work in progress; not yet publishable | Artifact created | Author marks ready for review |
| **CANDIDATE** | Published; eligible for council review | Author publishes to GitHub | Council opens review thread |
| **UNDER_REVIEW** | Active adjudication in progress | Council review opened | Vote completed or review closed |
| **RATIFIED** | Full council ratification; canon | Majority vote + @atlaslattice adjudication | Ratification event ID assigned |
| **REJECTED** | Failed review; not canon | Review closed with denial | Archived with rejection note |
| **ARCHIVED** | Superseded or withdrawn | Owner or council withdraws | Replaced by successor artifact |

## Mandatory Fields at Ratification

An artifact **cannot** move to `RATIFIED` without all three:

1. `ratification_event_id` — unique event reference (format: `RAT-YYYY-MM-DD-NNN`)
2. `canon_status: RATIFIED`
3. `trust_state: CANON`

## Adjudication Authority

Final adjudication always requires **@atlaslattice** sign-off. Council reviews are advisory until adjudication.

## Lifecycle Audit Trail

Every stage transition must produce a dated entry in the [Unresolved Decision Register](./UNRESOLVED_DECISION_REGISTER_2026-05-28.md) until the artifact is ratified or archived.

## Related Artifacts

- [Canon Promotion Checklist](./CANON_PROMOTION_CHECKLIST_v0_1.md)
- [Canon Demotion / Rollback Policy](./CANON_DEMOTION_ROLLBACK_POLICY_v0_1.md)
- [Adjudication Evidence Template](./ADJUDICATION_EVIDENCE_TEMPLATE_v0_1.md)
- [Canon-Candidate Register](../canon-candidate-register.md)
