# Lattice KG Query Cookbook v0.1

This module is an upstream candidate packet, not proof.

CANON: no
DEPLOYMENT: no
AUTHORITY: none

## Query goals

Use deterministic retrieval keys first:

1. `artifact_id`
2. exact path
3. `(domain, lane, is_log)` filters

## Example query intents

- Find artifact by ID in global index.
- Resolve exact path to artifact metadata.
- List candidate logs by lane.
- List artifacts missing contradiction links.
- List records blocked from promotion.

## Operator checklist

1. Confirm index freshness (`generated_at_utc`, fingerprint).
2. Confirm artifact exists at indexed path.
3. Confirm candidate boundary (`not_canon`, `not_deployable` unless ratified).
4. Confirm receipts exist for validation, blockers, and next safest action.
