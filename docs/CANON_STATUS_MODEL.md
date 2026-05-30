---
title: Canon Status Model
artifact_id: GOVERNANCE-CANON-STATUS-MODEL-2026-05-28
status: candidate
canon_status: candidate
lifecycle_state: draft
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-28
provenance: Created from Aetherforge Mission #1 execution in repository governance layer.
---

# Canon Status Model

## Purpose

Define the canonical status model used across this repository so canon decisions are machine-checkable and human-auditable.

## Canon Fields

Every governance-managed artifact must track:

- `canon_status`: `candidate`, `ratified`, `canonical`, `deprecated`, `superseded`, `archived`
- `ratification_event_id`: stable event ID or `pending`
- `trust_state`: `WORK`, `CANDIDATE`, `VERIFIED`, `BLOCKED`
- `lifecycle_state`: lifecycle stage from `docs/ARTIFACT_LIFECYCLE_STATES.md`

## Status Definitions

### candidate
- Default state for new artifacts.
- Not authoritative for execution.

### ratified
- Council review has approved the artifact in a dated event.
- Pending publication promotion or canon adjudication.

### canonical
- Explicitly adjudicated by human root authority.
- Approved for normative reference.

### deprecated
- No longer recommended for active use.
- Kept for historical provenance and traceability.

### superseded
- Replaced by a newer artifact.
- Must include a `superseded_by` pointer.

### archived
- Retained for historical integrity only.
- Not an active execution surface.

## Enforcement Rule

No artifact is canon by implication. Canon requires explicit `ratification_event_id`, `canon_status`, and `trust_state` alignment.
