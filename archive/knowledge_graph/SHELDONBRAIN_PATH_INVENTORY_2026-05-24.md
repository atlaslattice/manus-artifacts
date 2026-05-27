# Sheldonbrain Path Inventory — 2026-05-24

```text
STATUS: FIRST PASS INVENTORY — NOT CANON
MODE: AETHERFORGE / SHELDONBRAIN GRAPH INGESTION
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PURPOSE: identify repo-visible Sheldonbrain paths for graph source-node creation and adversarial review routing
```

## Method

Repo search over `atlaslattice/manus-artifacts` for `SHELDONBRAIN` and related code-path markers.

This is a path inventory, not a claim that the contents are current, complete, deployed, or canon.

## Repo-visible Sheldonbrain paths found

```text
archive/ops/SHELDONBRAIN_WORKSPACE_RECOVERY_NOTE_2026-05-11.md
archive/provenance/SHELDONBRAIN_PRODUCT_OWNER_NOT_ENGINEER_NOTE_2026-05-08.md
archive/boot/gptbrain/reference_impl/sheldonbrain_gptbrain_adapter.py
archive/boot/seats/S2_CLAUDE_BOOT_FRAGMENT_SHELDONBRAIN_AUTODREAM_2026-05-09.md
archive/boot/gptbrain/SWARM_UPDATE_SHELDONBRAIN_WORKSPACE_RECOVERED_2026-05-11.md
archive/boot/council/SHELDONBRAIN_WORKSPACE_RECOVERY_ORIENTATION_NOTE_2026-05-11.md
codebases/sheldonbrain/sheldonbrain-omega-v1/README.md
codebases/sheldonbrain/sheldonbrain-omega-v1/claude_review_report.md
codebases/sheldonbrain/sheldonbrain-omega-v1/MANUS_DEPLOYMENT_SUMMARY.md
codebases/sheldonbrain/sheldonbrain-omega-v1/core/janus_protocol.py
sheldonbrain/system-architecture.md
codebases/sheldonbrain/sheldonbrain-omega-v1/simulation/simulation_engine.py
codebases/sheldonbrain/sheldonbrain-omega-v1/core/chronos_fold_integration.py
manus-vault/notion/index/notion_edges.ndjson
codebases/other/drive_sync.py
manus-vault/notion/index/notion_objects.ndjson
codebases/sheldonbrain/sheldonbrain-omega-v1/core/CHRONOS_FOLD_README.md
codebases/other/upload_to_notion.py
codebases/sheldonbrain/sheldonbrain-omega-v1/claude_chronos_fold_artifacts/01_unified_codebase_architecture.md
archive/architecture/SHELDONBRAIN_MISSING_PARSER_MODULE_DISCOVERY_2026-05-08.md
```

## Initial graph source-node candidates

```yaml
source_nodes:
  - node_id: KG-SRC-SHELDONBRAIN-OMEGA-README
    path: codebases/sheldonbrain/sheldonbrain-omega-v1/README.md
    source_class: repo_visible
    raw_export_status: repo_file_visible
    review_priority: high
  - node_id: KG-SRC-SHELDONBRAIN-GPTBRAIN-ADAPTER
    path: archive/boot/gptbrain/reference_impl/sheldonbrain_gptbrain_adapter.py
    source_class: repo_visible_code
    raw_export_status: repo_file_visible
    review_priority: high
  - node_id: KG-SRC-SHELDONBRAIN-NOTION-OBJECTS
    path: manus-vault/notion/index/notion_objects.ndjson
    source_class: repo_visible_index
    raw_export_status: repo_file_visible
    review_priority: high
  - node_id: KG-SRC-SHELDONBRAIN-NOTION-EDGES
    path: manus-vault/notion/index/notion_edges.ndjson
    source_class: repo_visible_index
    raw_export_status: repo_file_visible
    review_priority: high
  - node_id: KG-SRC-SHELDONBRAIN-MISSING-PARSER-DISCOVERY
    path: archive/architecture/SHELDONBRAIN_MISSING_PARSER_MODULE_DISCOVERY_2026-05-08.md
    source_class: repo_visible_review_note
    raw_export_status: repo_file_visible
    review_priority: high
```

## High-risk review triggers

```text
MANUS_DEPLOYMENT_SUMMARY.md may contain deployment language.
S2_CLAUDE_BOOT_FRAGMENT_* may contain boot / authority language.
Claude chronos fold artifacts should route to Claude adversarial review queue.
Notion index files should be treated as source indices, not canon.
Adapter files require code-path inspection before implementation claims.
```

## Next actions

```text
1. Fetch and inspect sheldonbrain_gptbrain_adapter.py.
2. Fetch and inspect notion_objects.ndjson and notion_edges.ndjson schema shape.
3. Add graph source inventory rows for confirmed paths.
4. Route Claude-origin Sheldonbrain artifacts to Claude adversarial review queue.
5. Identify parser/adapter/ingestion modules without claiming deployment.
```

## Keeper

```text
Sheldonbrain ingests lineage.
The graph maps relationships.
Review extracts deltas.
Human-root ratifies canon.
```