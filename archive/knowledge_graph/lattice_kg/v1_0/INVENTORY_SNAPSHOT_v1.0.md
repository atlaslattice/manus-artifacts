---
STATUS: CANDIDATE — NOT CANON
AUTHORITY: NONE
DEPLOYMENT: NONE
artifact_id: KNOWLEDGE_GRAPH-KG-20260603-inventory-snapshot-v1-0
path: archive/knowledge_graph/lattice_kg/v1_0/INVENTORY_SNAPSHOT_v1.0.md
domain: knowledge_graph
lane: inventory
generated_at_utc: 2026-06-03T00:00:00Z
author: Copilot
version: "1.0"
---
# Inventory Snapshot v1.0

## Source run
- Command: `python3 scripts/build_lattice_global_index.py --repo-root /tmp/workspace/atlaslattice/manus-artifacts`
- Snapshot file: `archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json`

## Findings
- Indexed artifacts (v0.5 snapshot): 1288
- Indexed artifacts (v1.0 snapshot): 1209
- Indexed edges (v1.0 snapshot): 216
- Average completeness score (v1.0): 0.069

## Notes
- The repository now includes explicit v1.0 contract, governance, quest, parity, adversarial, CI, contributor, and release-readiness surfaces.
- Reverse indexing and badge generation were added for machine consumption.
- Metadata and backlink debt remain visible through the new validators and reports.
