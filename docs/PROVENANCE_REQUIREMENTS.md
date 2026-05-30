---
title: Provenance Requirements
artifact_id: GOVERNANCE-PROVENANCE-REQUIREMENTS-2026-05-28
status: candidate
canon_status: candidate
lifecycle_state: active
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-28
provenance: Created from Aetherforge Mission #10 execution in repository governance layer.
---

# Provenance Requirements

## Objective

Standardize provenance metadata so artifact lineage is queryable and auditable.

## Minimum Required Provenance Fields

- `artifact_id`: stable identifier
- `owner`: accountable steward or team
- `last_updated`: ISO date (`YYYY-MM-DD`)
- `provenance`: source context statement
- `canon_status`
- `ratification_event_id`
- `trust_state`

## Optional Provenance Fields

- `source_refs`: issue IDs, PR IDs, council session IDs
- `supersedes`: prior artifact ID/path
- `superseded_by`: replacement artifact ID/path
- `reviewers`: named reviewers or council group

## Enforcement

- Governance-managed markdown artifacts must include YAML frontmatter with required fields.
- Legacy files using only `status:` remain valid, but should be migrated incrementally.
- Automated checks run through `scripts/validate_artifact_metadata.py`.
