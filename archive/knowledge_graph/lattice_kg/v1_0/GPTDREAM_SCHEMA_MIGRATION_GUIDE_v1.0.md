---
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
artifact_id: GPTDREAM-GPTDREAM-20260603-gptdream-schema-migration-guide-v1-0
path: archive/knowledge_graph/lattice_kg/v1_0/GPTDREAM_SCHEMA_MIGRATION_GUIDE_v1.0.md
domain: gptdream
lane: parity
generated_at_utc: 2026-06-03T00:00:00Z
author: Copilot
version: "1.0"
---

# GPTDream Schema Migration Guide v1.0

1. Freeze old packet receipts.
2. Map `schema_version: 0.1` records into v1.0 field names.
3. Re-emit provenance receipts with explicit `tool_chain`.
4. Update wake, dream, and delta triplets to mutual links.
5. Re-run strict-mode validation and parity CI.
