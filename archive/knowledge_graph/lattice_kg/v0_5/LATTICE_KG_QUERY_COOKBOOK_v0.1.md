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

## v1.0 query recipes

1. Build the v1.0 index and inspect completeness:
   - `python3 scripts/build_lattice_global_index_v2.py --repo-root .`
2. Find under-linked artifacts with JSON output:
   - `python3 scripts/detect_underlinked_artifacts.py --repo-root . --output json`
3. Detect missing metadata fields:
   - `python3 scripts/detect_missing_metadata.py --repo-root .`
4. Validate lineage and contradiction integrity:
   - `python3 scripts/validate_lineage_chain.py --repo-root .`
   - `python3 scripts/validate_contradiction_pairs.py --repo-root .`
5. Generate the reverse index and query by path:
   - `python3 scripts/build_reverse_index.py --repo-root .`
6. Run the full compliance sweep:
   - `python3 scripts/run_full_compliance_sweep.py`
