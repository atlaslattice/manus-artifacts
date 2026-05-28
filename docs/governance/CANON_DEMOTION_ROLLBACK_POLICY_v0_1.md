---
artifact_id: GOV-CANON-DEMOTION-ROLLBACK-POLICY-v0-1-2026-05-28
title: Canon Demotion and Rollback Policy
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Canon Demotion and Rollback Policy

> **Purpose:** Define the process for downgrading a `RATIFIED` artifact back to `CANDIDATE` or `ARCHIVED`, and for rolling back changes that were incorporated during ratification.

## When Demotion Is Appropriate

| Trigger | Action |
|---|---|
| Factual error discovered post-ratification | Demotion to `CANDIDATE` pending correction |
| New conflicting evidence invalidates artifact | Demotion to `UNDER_REVIEW`; conflict process initiated |
| Artifact superseded by a newer ratified version | Demotion to `ARCHIVED` |
| Security/PII issue found in ratified content | Emergency demotion to `DRAFT`; sensitive content handling applied |
| Owner withdraws artifact | Demotion to `ARCHIVED` |

## Emergency Demotion (Security/PII Path)

1. @atlaslattice or designated security officer initiates emergency demotion immediately.
2. Artifact status set to `DRAFT`; content redacted if required.
3. Incident logged in [Unresolved Decision Register](./UNRESOLVED_DECISION_REGISTER_2026-05-28.md) with timestamp.
4. Affected artifacts (those linking to the demoted artifact) reviewed within 48 hours.
5. History rewrite decision made per [Conditional History Rewrite Runbook](../closeout/CONDITIONAL_HISTORY_REWRITE_RUNBOOK_2026-05-28.md).

## Standard Demotion Process

1. Council member or @atlaslattice opens a demotion proposal with:
   - Artifact ID and current ratification event ID
   - Reason for demotion
   - Proposed new status
2. @atlaslattice adjudicates within the [Governance SLA](./GOVERNANCE_SLA_TARGETS_v0_1.md).
3. Frontmatter updated: `canon_status` and `trust_state` changed; `demotion_event_id` added.
4. Governance Decision Index entry created.

## Rollback (Content Correction)

A rollback restores a previous content state:

1. Open a PR reverting the artifact content to the desired prior state.
2. PR linked to demotion event.
3. New ratification cycle run on corrected content before re-promoting to `RATIFIED`.

## Immutable Audit Trail Rule

Demoted artifacts retain their original `ratification_event_id` plus a new `demotion_event_id`. These fields are never deleted — only new fields added.

## Related Artifacts

- [Ratification Lifecycle](./RATIFICATION_LIFECYCLE_v0_1.md)
- [Adjudication Evidence Template](./ADJUDICATION_EVIDENCE_TEMPLATE_v0_1.md)
- [Canon Conflict Resolution Process](./CANON_CONFLICT_RESOLUTION_PROCESS_v0_1.md)
