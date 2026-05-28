---
artifact_id: DOC-GOOD-FIRST-ISSUES-2026-05-27
title: Good First Issues — Public Contribution Lanes
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-28
source_of_truth: GitHub
---
# Good First Issues — Public Contribution Lanes

## Lane A — Metadata Backfill

- Add missing frontmatter fields on high-value legacy artifacts.
- Verify status labels are explicit (`DRAFT`, `CANDIDATE`, `CANONICAL`, `ARCHIVED`).
- Link updated files into `docs/ARCHIVE_INDEX.md`.
- Start a scoped intake with the [Metadata Quest template](https://github.com/atlaslattice/manus-artifacts/issues/new?template=metadata_quest.md).

## Lane B — Graph Linking

- Add missing relationship links using `docs/ARTIFACT_RELATIONSHIP_TYPES.md`.
- Resolve orphan artifacts by adding at least one index and one lineage link.
- Report duplicate or weakly differentiated artifacts with citation paths.
- Launch a contributor lane with the [Graph Linking Quest template](https://github.com/atlaslattice/manus-artifacts/issues/new?template=graph_linking_quest.md).

## Lane C — Evidence Hardening

- Add missing evidence links for AI system claims in `docs/AI_SYSTEMS_EVIDENCE_INDEX.md`.
- Add or update validation artifact references (tests/check scripts/workflows).
- Propose blocker-closure evidence additions in `docs/LAUNCH_BLOCKERS_TRACKER.md`.
- Route new work through the [Evidence Quest template](https://github.com/atlaslattice/manus-artifacts/issues/new?template=evidence_quest.md).

## Contributor Rule

Every issue/PR should include: objective, touched paths, validation run, and provenance citations.
