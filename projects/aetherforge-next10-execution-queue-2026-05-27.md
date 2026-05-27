---
artifact_id: PROJECT-AETHERFORGE-NEXT10-QUEUE-2026-05-27
title: Aetherforge Next-10 Execution Queue (Mapped to Top-50)
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-27
source_of_truth: GitHub
---
# Aetherforge Next-10 Execution Queue (Mapped to Top-50)

## Prioritization Rule

Order by:
1. Public value impact
2. Graph centrality impact
3. Evidence completeness impact

## Queue

| Priority | Top-50 Task # | Task | Why now |
|---|---:|---|---|
| 1 | 2 | Secret history audit closeout | Hard public launch blocker |
| 2 | 3 | PII audit closeout | Hard public launch blocker |
| 3 | 4 | Public scope decision record | Hard public launch blocker |
| 4 | 5 | Conditional history rewrite decision | Required if blocker findings exist |
| 5 | 21 | Provenance/frontmatter backfill for top artifacts | Unlocks graph trust + evidence quality |
| 6 | 22 | ADR archive bootstrap in `docs/decisions/` | Governance traceability |
| 7 | 23 | Convert tribal knowledge to docs | Reduces single-point knowledge risk |
| 8 | 33 | Taxonomy normalization follow-up | Improves discoverability and indexing |
| 9 | 40 | Duplicate artifact detection pass | Improves retrieval quality |
| 10 | 50 | Formal world-class readiness review | Final go/no-go control point |

## Milestone Checkpoints

- **Checkpoint A (50%)**: blockers tracked with at least one closure artifact drafted.
- **Checkpoint B (75%)**: safety blockers closed and evidence coverage improved.
- **Checkpoint C (Pre-release)**: all hard blockers closed and readiness gates green.


## Related campaign

- `/tmp/workspace/atlaslattice/manus-artifacts/projects/aetherforge-144-task-campaign-2026-05-27.md`
