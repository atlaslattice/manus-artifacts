# Quest-to-Task Map

> **Status:** CANDIDATE  
> **Artifact Type:** planning map  
> **Date:** 2026-05-28  
> **Related:** [Aetherforge Top-50 Taskboard](../../projects/aetherforge-top50-taskboard-2026-05-26.md), [Archive Health Status](../archive-health-status-2026-05-28.md), [Metadata Coverage Report](../metadata-coverage-report-2026-05-28.md)

## Active Mapping

<!-- METADATA
stable_id: AL-AF-103
lifecycle_state: CANDIDATE
owner: @atlaslattice
date_created: 2026-05-28
canon_status: candidate
-->

| Quest Type | Real Task | Acceptance Criteria | Priority |
| --- | --- | --- | --- |
| `BACKFILL` | Backfill stable semantic IDs and provenance blocks into high-value `docs/` and `projects/` artifacts missing metadata (taskboard #3, #36). | Target files include stable ID, lifecycle, owner, and date fields; `python3 scripts/validate_metadata_completeness.py` passes for touched paths. | P0 |
| `BACKFILL` | Add lifecycle states to legacy artifacts that are still implicitly candidate-only (taskboard #5). | Artifact surface explicitly states candidate/draft/deprecated posture and links the trust flow. | P1 |
| `CROSSLINK` | Connect Aluminum OS concept docs to `aluminum-os-core/README.md` and related implementation surfaces (taskboard #8, #25). | A newcomer can traverse concept → implementation → tests in two clicks or fewer. | P0 |
| `CROSSLINK` | Add related-artifact links between mission, game loop, trust flow, and knowledge-graph docs. | Each touched artifact has bidirectional or hub-based navigation to adjacent surfaces. | P1 |
| `INTAKE` | Import external Notion/Drive archive drops using the new intake standards and receipt template. | Imported file is kebab-case, provenance is preserved, triage class is recorded, and the receipt is complete. | P0 |
| `EVIDENCE` | Backfill evidence entries for AI-built governance/KG artifacts called out in the evidence dashboard. | New `docs/evidence/*.json` record references the target artifact, claim, and validation source. | P1 |
| `POLISH` | Create standard landing pages for top-level domains flagged in the normalization matrix (`docs/`, `projects/`, `archive/`, `aluminum-os/`). | README exists, uses standard structure, and is cross-linked from navigation hubs. | P0 |
| `DEPRECATE` | Mark superseded artifacts with replacement links under the deprecation policy (taskboard #35). | Deprecated artifact keeps its path, states the replacement, and preserves provenance. | P2 |
| `VALIDATE` | Run artifact graph validation after graph or registry-adjacent work. | `python3 .github/scripts/validate_artifact_graph.py` passes and the run is logged in a receipt. | P0 |
| `VALIDATE` | Capture weekly metadata/provenance validation receipts for archive hygiene (taskboard #18, #20). | Validator outputs are recorded with date, command, outcome, and follow-up note. | P1 |
| `RATIFY` | Prepare a packet for `AL-MISSION-001` with evidence, validation, and checklist completion. | Packet contains all required fields and an adjudication request to `@atlaslattice`. | P0 |
| `RATIFY` | Prepare a packet for `AL-KG-003` so the ID/lifecycle contract can move to review. | Packet includes schema links, validator evidence, and trust-state recommendation. | P0 |
| `RATIFY` | Prepare queue items for `AL-RT-001`, `AL-AF-001`, and `AL-GOV-002`. | Each candidate has blockers, next step, and packet completeness clearly stated. | P1 |
| `POLISH` | Publish themed reading lists, explainers, and spotlight pages needed for launch packaging (taskboard #46, #49, #50). | Public navigation surfaces exist and point readers to real repo artifacts. | P1 |
