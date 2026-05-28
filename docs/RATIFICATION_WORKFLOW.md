---
title: Ratification Workflow
artifact_id: GOVERNANCE-RATIFICATION-WORKFLOW-2026-05-28
status: candidate
canon_status: candidate
lifecycle_state: review
ratification_event_id: pending
trust_state: WORK
owner: Atlas Lattice Foundation
last_updated: 2026-05-28
provenance: Created from Aetherforge Mission #2 execution in repository governance layer.
---

# Ratification Workflow

## Scope

Defines the minimum workflow to move an artifact from candidate state to canonical state.

## Workflow Stages

1. **Draft + Candidate Registration**
   - Artifact enters repository with candidate metadata.
   - Provenance block and source evidence are required.
2. **RFC / Issue Review**
   - Governance, process, or architecture deltas must reference an RFC proposal issue.
3. **Council Review Window**
   - Designated reviewers record approvals, concerns, or request changes.
4. **Ratification Event**
   - Decision receives a dated `ratification_event_id`.
5. **Human Root Adjudication**
   - Final canon eligibility adjudicated by @atlaslattice.
6. **Status Transition**
   - `canon_status` is updated to `ratified` or `canonical`.
7. **Ledger Entry**
   - Decision logged in `docs/CANON_DECISION_LEDGER.md`.

## Required Evidence

- Source provenance and creation context
- Review notes and decision summary
- Adjudicator identity and timestamp
- Link to superseding artifact when applicable

## Failure Conditions

Promotion is blocked if any required governance field is missing, if provenance is absent, or if trust state is `BLOCKED`.
