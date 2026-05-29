# Archive Validators

```text
STATUS: VALIDATOR SCAFFOLD — NOT CANON — NON-DEPLOYABLE
AUTHORITY: none
PURPOSE: define candidate validator scripts for archive hygiene, status discipline, and knowledge graph ingestion checks
```

## Purpose

Validators are guardrails for archive hygiene. They are not canon engines and do not decide truth.

They may flag:

```text
missing artifact_status blocks
invalid raw_export_status values
canon-like language without ratification
runtime/deployment language in non-executable lanes
malformed KG node records
malformed KG edge records
missing receipt references
```

## Non-claims

```text
Passing validation does not mean canon.
Passing validation does not mean truth.
Passing validation does not mean deployment-ready.
Validation only means the artifact meets the checked formatting and boundary rules.
```

## Candidate validators

```text
validate_artifact_status.py
validate_raw_export_status.py
validate_source_inventory.py
validate_no_canon_language.py
validate_no_deployment_language.py
validate_kg_node_edge_seed.py
```

## Keeper

```text
Validation checks the lane markers.
Human-root decides the destination.
```