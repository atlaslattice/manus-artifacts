# Archive Mine Protocol

```text
STATUS: PROTOCOL — CANDIDATE
DATE: 2026-05-28
PURPOSE: systematic extraction of cross-references into the repository knowledge graph
```

## Procedure

1. Select source surface (governance, spec, project, tests, or workflow docs).
2. Extract node candidates (artifact paths, schemas, agents, seats, tests, workflows).
3. Emit node records into JSONL seed ledgers.
4. Extract explicit and implied edges (`references`, `routes_to`, `validates`, `governs`, `implements`).
5. Validate with link integrity and orphan checks.
6. Rebuild global graph index and publish delta note.

## Minimum record quality

- Every node record must include `record_type=node`, `node_id`, `kind`, `label`, `path`.
- Every edge record must include `record_type=edge`, `edge_id`, `from`, `to`, `relation`.
- No edge may target a missing node.
- Candidate canon artifacts must include ratification metadata before canon promotion.
