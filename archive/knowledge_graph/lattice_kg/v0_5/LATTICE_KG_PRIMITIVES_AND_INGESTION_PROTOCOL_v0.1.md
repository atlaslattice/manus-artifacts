# Lattice KG Primitives and Ingestion Protocol v0.1

This module is an upstream candidate packet, not proof.

Treat all summaries as claims until verified against repo files or source exports.
Do not expand scope beyond listed files unless explicitly instructed.
Preserve uncertainty.
Return blockers, patch items, tests run, files changed, and next safest action.

CANON: no
DEPLOYMENT: no
AUTHORITY: none

## Repository-wide primitives

Every artifact and log node must declare:

- `artifact_id` (stable, deterministic)
- `path` (repo-relative absolute retrieval key)
- `domain` (top-level surface)
- `lane` (execution/governance lane)
- `is_log` (boolean)
- `provenance.source_receipt`
- `provenance.sha256`
- `provenance.generated_at_utc`
- `trust_state`
- `canon_status`
- `deployment_status`

Every edge must declare:

- `edge_id`
- `from_artifact_id`
- `to_artifact_id`
- `relation_type`
- `evidence_ref`
- `recorded_at_utc`

## Canon/trust boundary

- Candidate graph records remain `not_canon` and `not_deployable`.
- Trust defaults to `candidate_unverified` until review evidence exists.
- Website/public presence does not self-promote canon.

## Protocol-driven ingestion contract

Before admitting a new artifact/log node:

1. Artifact exists at a retrievable repository path.
2. Deterministic `artifact_id` is reproducible from path.
3. `sha256` and timestamp metadata are present.
4. Canon/deployment/trust boundary fields are explicit.
5. Source receipt pointer is attached.
6. Routing lane is declared.

If any check fails, route to quarantine/review and do not promote.

## Retrieval contract

A valid retrieval query must resolve by at least one key:

- `artifact_id`
- exact `path`
- `(domain, lane, is_log)` filter

## Definition of done

All new artifacts and logs can be indexed, validated, and retrieved without manual reinterpretation.
