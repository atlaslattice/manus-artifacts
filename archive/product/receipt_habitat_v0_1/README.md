# Receipt Habitat v0.1

```text
STATUS: LOCAL IMPLEMENTATION SCAFFOLD — NOT CANON
DEPLOYMENT: no
AUTHORITY: none
RUNTIME: local_dry_run_only
ISSUE: #128
```

## Purpose

Receipt Habitat v0.1 is a boring local workbench that turns volatile AI conversation material into source-scoped, reviewable, non-canon evidence packets.

It exists to prevent false completeness.

```text
Visibility is not authorization.
Receipt is not approval.
Simulation is not execution.
Memory is not permission.
Archive is not canon.
```

## MVP Flow

```text
ingest raw/partial/summary/unavailable input
→ create ingestion packet
→ validate required status fields
→ review overclaim and authority language
→ emit review packet
→ render status/next safest action
```

No network calls.  
No live repo mutation.  
No deployment claim.  
No canon promotion.

## CLI Contract

Target commands:

```bash
python -m receipt_habitat.ingest input.md --raw-status summary_only --timezone America/Chicago
python -m receipt_habitat.packet ingestion.yaml
python -m receipt_habitat.review packet.yaml
python -m receipt_habitat.status packet.yaml
```

The first pass is intentionally test-first. The schema and tests define the behavior before any richer CLI is promoted.

## Required Defaults

```yaml
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
runtime_status: local_dry_run_only
```

## Hard Rules

```text
R1. Missing raw_export_status -> fail.
R2. Missing thread_time_range -> fail.
R3. Missing access_scope -> fail.
R4. canon_status must be not_canon in v0.1.
R5. deployment_status must be not_deployable in v0.1.
R6. summary_only packets cannot create public claims.
R7. unavailable raw exports must list unavailable_sources.
R8. any claim without evidence_ref cannot exceed C1_SIGNAL.
R9. any deployment/runtime phrase without receipt returns block.
R10. any canon/ratification phrase without receipt returns patch or block.
```

## Directory

```text
archive/product/receipt_habitat_v0_1/
  README.md
  schemas/
  examples/
  src/receipt_habitat/
  tests/
```

## Keeper

```text
Build the scoreboard that refuses fake points.
```
