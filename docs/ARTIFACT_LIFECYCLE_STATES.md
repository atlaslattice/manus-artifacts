---
title: Artifact Lifecycle States
artifact_id: GOVERNANCE-ARTIFACT-LIFECYCLE-STATES-2026-05-28
status: candidate
canon_status: candidate
lifecycle_state: active
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-28
provenance: Created from Aetherforge Mission #11 execution in repository governance layer.
---

# Artifact Lifecycle States

## Lifecycle Enumeration

- `draft` — actively authored; not ready for formal review
- `review` — in RFC/council review path
- `active` — approved for current use within declared status
- `maintenance` — active but stable, low-frequency updates
- `deprecated` — scheduled retirement; still retained
- `archived` — retained for provenance; not active execution

## Transition Rules

- `draft -> review` requires provenance completeness.
- `review -> active` requires ratification event record.
- `active -> maintenance` is optional and used for stable surfaces.
- `active|maintenance -> deprecated` requires replacement or rationale.
- `deprecated -> archived` requires historical retention note.

## Notes

Lifecycle state does not override canon status; both must be tracked together.
