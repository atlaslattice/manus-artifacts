# Receipt Habitat v0.1

```text
STATUS: LOCAL-FIRST PROTOTYPE — NOT CANON
DEPLOYMENT: NO
RUNTIME CLAIM: LOCAL DRY-RUN ONLY
AUTHORITY: NONE
PARENT: Issue #128
```

Receipt Habitat v0.1 is a tiny local workbench for turning volatile AI conversation material into source-scoped, timestamped, non-canon evidence packets.

It exists to prevent false completeness, unsupported canon language, and premature deployment claims.

## Product law

```text
The product is not smart because it says yes.
The product is smart because it knows exactly when it cannot say yes yet.
```

## CLI contract

```bash
python -m receipt_habitat.ingest examples/mobile_continuity_summary.md --raw-status summary_only --timezone America/Chicago
python -m receipt_habitat.packet ingestion.yaml
python -m receipt_habitat.review packet.yaml
python -m receipt_habitat.status packet.yaml
```

## Hard rules

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

## Non-goals

```text
No live GitHub writes.
No autonomous execution.
No OpenAI API requirement.
No cross-vendor connector.
No canon promotion.
No deployment.
No runtime enforcement claim.
No memory overwrite.
```

## Keeper line

```text
Build the scoreboard that refuses fake points.
```
