---
title: Universal Frontmatter Schema
artifact_id: GOVERNANCE-UNIVERSAL-FRONTMATTER-SCHEMA-2026-05-28
status: candidate
canon_status: candidate
lifecycle_state: active
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-28
provenance: Created from Aetherforge Mission #49 execution in repository governance layer.
---

# Universal Frontmatter Schema

## Required Keys

```yaml
---
title: <string>
artifact_id: <string>
status: candidate|canonical|deprecated|superseded|archived
canon_status: candidate|ratified|canonical|deprecated|superseded|archived
lifecycle_state: draft|review|active|maintenance|deprecated|archived
ratification_event_id: <string|pending>
trust_state: WORK|CANDIDATE|VERIFIED|BLOCKED
owner: <string>
last_updated: YYYY-MM-DD
provenance: <string>
---
```

## Compatibility Policy

- Legacy artifacts with a `status:` header line are accepted.
- New governance-managed artifacts should use full frontmatter.
- Metadata validation runs through `scripts/validate_artifact_metadata.py`.
