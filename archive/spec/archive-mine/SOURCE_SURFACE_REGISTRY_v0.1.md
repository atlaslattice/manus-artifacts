# SOURCE_SURFACE_REGISTRY v0.1

STATUS: CANDIDATE BUILD PLAN — NOT CANON  
DEPLOYMENT: NO  
AUTHORITY: NONE

## Purpose
Machine-checkable registry for Archive Mine reconciliation across Notion fossils, Drive reports, GitHub archive lanes, and website canon surfaces.

## Source gravity
- Mass ingestion parent: #160
- Reconciliation lanes: #158, #159, #163, #165, #168, #169, #171, #173, #175

## Required inventory domains
1. Notion roots
2. Drive roots
3. GitHub archive lanes
4. Website canon surfaces
5. Claude-touch contamination labels
6. Candidate deltas (Notion fossils)
7. Candidate deltas (Drive reports)
8. Canon recoverability manifest
9. Fossil → current GitHub receipt crosswalk

## Machine-readable contract
- Schema: `/tmp/workspace/atlaslattice/manus-artifacts/schemas/archive_mine/v0_1/source-surface-registry.schema.yaml`
- Sample packet: `/tmp/workspace/atlaslattice/manus-artifacts/fixtures/archive_mine/source_surface_registry_v0_1.sample.yaml`
- Reference validator: `/tmp/workspace/atlaslattice/manus-artifacts/reference_impl/archive_mine/registry.py`

## Canon boundary
GitHub remains canonical substrate. Notion/Drive are relay and fossil extraction surfaces until explicit ratification workflow is complete.
