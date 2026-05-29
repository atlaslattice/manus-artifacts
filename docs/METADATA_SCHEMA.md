# Metadata Schema
Status: Candidate
Date: 2026-05-26

This document defines the unified frontmatter schema for markdown artifacts in the archive.
The schema is intentionally compact: it carries the minimum governance data required for navigation, lineage, and auditability.

## Required YAML frontmatter block

```yaml
---
title: Canon Lifecycle
status: Candidate
domain: Governance
steward: Governance Steward
created: 2026-05-26
updated: 2026-05-26
version: v1.0.0-2026-05-26
supersedes: []
superseded_by: []
---
```

## Field definitions

| Field | Required | Type | Notes |
| --- | --- | --- | --- |
| `title` | Yes | string | Human-readable artifact title |
| `status` | Yes | string | One of Draft, Candidate, Canon, Archived, Deprecated |
| `domain` | Yes | string | Systems, Projects, Governance, Research, Health, or Vault |
| `steward` | Yes | string | Named role, team, or acting steward |
| `created` | Yes | date | First publication date in `YYYY-MM-DD` |
| `updated` | Yes | date | Most recent substantive update date |
| `version` | Yes | string | Prefer `vX.Y.Z-YYYY-MM-DD` |
| `supersedes` | Yes | array | Paths or artifact IDs replaced by this artifact |
| `superseded_by` | Yes | array | Paths or artifact IDs that replace this artifact |

## Optional extension fields

Use sparingly when the artifact requires them.

- `artifact_id`
- `review_cadence`
- `website_ready`
- `decision_log`
- `tags`
- `summary`

## Example: doctrine artifact

```yaml
---
title: Aluminum OS Primer
status: Candidate
domain: Systems
steward: Systems Steward
created: 2026-05-26
updated: 2026-05-26
version: v1.0.0-2026-05-26
supersedes: []
superseded_by: []
artifact_id: AF-SYS-AOS-0101
review_cadence: quarterly
tags: [aluminum-os, primer, onboarding]
---
```

## Example: superseding artifact

```yaml
---
title: Unified Field v4.0
status: Candidate
domain: Systems
steward: Systems Steward
created: 2026-05-26
updated: 2026-05-26
version: v4.0.0-2026-05-26
supersedes:
  - aluminum-os/v3.0-unified-field.md
superseded_by: []
decision_log: AF-GOV-CDL-0042
---
```

## Application rules

1. Frontmatter should be the first content in the file when used.
2. The visible header should still include `Status: Candidate` or the current lifecycle label for human readers.
3. `updated` should change only for substantive changes, not for cosmetic formatting alone.
4. Arrays may be empty but should still be present for schema consistency.
5. If metadata is not yet retrofitted onto a legacy artifact, the header note remains the minimum requirement.

## Why this schema matters

The schema allows the archive to support integrity checks, lineage maps, quality dashboards, and public website publication gates without overfitting to any one toolchain.
It is the structural grammar that lets the Aetherforge archive remain inspectable at scale.

## Related documents

- [NAMING_CONVENTIONS.md](./NAMING_CONVENTIONS.md)
- [ARTIFACT_LINEAGE.md](./ARTIFACT_LINEAGE.md)
- [VALIDATION_PLAYBOOK.md](./VALIDATION_PLAYBOOK.md)
