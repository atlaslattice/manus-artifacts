# Canon Decision Log Format
Status: Candidate
Date: 2026-05-26

This document defines the standard structure for logging canon decisions.
A durable decision log is required for ratifications, deprecations, major adjudications, and material canon conflicts.

## Record structure

Each canon decision entry should contain the following fields in order.

| Field | Required | Description |
| --- | --- | --- |
| Decision ID | Yes | Stable identifier such as `AF-GOV-CDL-0012` |
| Date | Yes | Decision publication date in `YYYY-MM-DD` |
| Artifact | Yes | Title and repository path of the affected artifact |
| Domain | Yes | One of the six taxonomy domains |
| Lifecycle change | Yes | Example: `Candidate -> Canon` |
| Decision | Yes | Short summary of what was approved or denied |
| Rationale | Yes | Why the decision was made |
| Evidence reviewed | Yes | Citations, links, and review inputs considered |
| Vote record | Yes for council decisions | Vote result, attendance, recusals, abstentions |
| Adjudicator | Yes for canon authority decisions | Name or role of final adjudicator |
| Effective version | Recommended | Version string or release label |
| Supersession notes | Recommended | What this replaces or what replaces it |
| Publication actions | Recommended | Website, changelog, index, and archival updates |

## Canonical entry template

```text
Decision ID: AF-GOV-CDL-0001
Date: 2026-05-26
Artifact: docs/TRUST_CHARTER.md
Domain: Governance
Lifecycle change: Candidate -> Canon
Decision: Approved as public trust charter v1
Rationale: Establishes transparent trust commitments for public archive readers
Evidence reviewed:
  - Canon promotion checklist packet
  - Domain steward recommendation
  - Council review notes
Vote record: 5-0-0, no recusals
Adjudicator: @atlaslattice
Effective version: v1.0.0-2026-05-26
Supersession notes: None
Publication actions:
  - Update governance index
  - Add website canon link
```

## Formatting rules

- One decision should map to one log entry.
- Use plain language in `Decision` and `Rationale`.
- Avoid ambiguous pronouns; name the exact artifact.
- Link to the artifact path, review record, and any superseded entries when published in markdown.
- If a decision is provisional, state the expiration or re-review condition.

## Vote record standard

Record the following when a council vote occurs:

- total eligible voters
- votes in favor
- votes opposed
- abstentions
- recusals
- quorum confirmation

## When a log entry is required

- candidate to canon promotion
- canon deprecation
- canon conflict adjudication
- exception approval to standard governance process
- public trust incident with canon authority implications

## Related documents

- [CANON_PROMOTION_CHECKLIST.md](./CANON_PROMOTION_CHECKLIST.md)
- [CANON_LIFECYCLE.md](./CANON_LIFECYCLE.md)
- [../governance/COUNCIL_REVIEW_WORKFLOW.md](../governance/COUNCIL_REVIEW_WORKFLOW.md)
