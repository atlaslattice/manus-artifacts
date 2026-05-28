---
artifact_id: GOV-CANON-PROMOTION-CHECKLIST-v0-1-2026-05-28
title: Canon Promotion Checklist
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Canon Promotion Checklist

> Use this checklist before moving any artifact from `CANDIDATE` → `RATIFIED`.

## Pre-Review Readiness (Author Responsibility)

- [ ] Frontmatter complete: `artifact_id`, `title`, `status`, `owner`, `created`, `last_updated`, `source_of_truth`
- [ ] Artifact content is complete and internally consistent
- [ ] All referenced artifacts exist and are reachable
- [ ] No secrets, PII, or sensitive unredacted content present
- [ ] Artifact passes lint/metadata validation scripts (if applicable)
- [ ] Artifact linked from at least one index or parent artifact

## Council Review (Council Responsibility)

- [ ] Review thread opened and linked to artifact
- [ ] At least one council member besides author has reviewed
- [ ] All objections documented in review thread or adjudication evidence
- [ ] Vote recorded per [Council Vote Recording Format](./COUNCIL_VOTE_RECORDING_FORMAT_v0_1.md)

## Adjudication (Owner: @atlaslattice)

- [ ] @atlaslattice has reviewed council vote and objections
- [ ] Final adjudication decision documented
- [ ] Ratification event ID assigned (`RAT-YYYY-MM-DD-NNN`)
- [ ] Artifact frontmatter updated: `canon_status: RATIFIED`, `trust_state: CANON`, `ratification_event_id`
- [ ] Entry added to [Governance Decision Index](./GOVERNANCE_DECISION_INDEX_2026-05-28.md)

## Post-Ratification Housekeeping

- [ ] Unresolved Decision Register entry closed
- [ ] Any superseded CANDIDATE versions archived or flagged
- [ ] README or index links updated if needed

## Notes

Checklist is to be completed in order. Do not skip adjudication even when council vote is unanimous — this preserves the audit trail requirement.
