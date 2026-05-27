---
artifact_id: DOC-AI-SYSTEMS-EVIDENCE-INDEX-2026-05-27
title: AI Systems Evidence Index
status: CANDIDATE
owner: atlaslattice
created: 2026-05-27
last_updated: 2026-05-27
source_of_truth: GitHub
---

# AI Systems Evidence Index

## Purpose

This is the authoritative evidence spine linking AI systems to artifacts, logs, evaluations, and provenance.

## Evidence Model

Each system row should resolve to:

- `system_id`
- `definition_artifact`
- `evidence_artifacts`
- `validation_artifacts`
- `provenance_anchor`
- `status`

## Initial System Spine

| system_id | definition_artifact | evidence_artifacts | validation_artifacts | provenance_anchor | status |
|---|---|---|---|---|---|
| ALUMINUM-OS | `/tmp/workspace/atlaslattice/manus-artifacts/aluminum-os/v4.0-unified-field.md` | `/tmp/workspace/atlaslattice/manus-artifacts/aluminum-os/ALUMINUM_COMPLETE_ARTIFACT_INDEX.md` | `/tmp/workspace/atlaslattice/manus-artifacts/docs/LATTICE_GLOBAL_INDEX.md` | `/tmp/workspace/atlaslattice/manus-artifacts/docs/ARCHIVE_INDEX.md` | CANDIDATE |
| SHELDONBRAIN | `/tmp/workspace/atlaslattice/manus-artifacts/sheldonbrain/system-architecture.md` | `/tmp/workspace/atlaslattice/manus-artifacts/sheldonbrain/README.md` | `/tmp/workspace/atlaslattice/manus-artifacts/docs/LATTICE_GLOBAL_INDEX.md` | `/tmp/workspace/atlaslattice/manus-artifacts/docs/ARCHIVE_INDEX.md` | CANDIDATE |
| BAZINGA | `/tmp/workspace/atlaslattice/manus-artifacts/bazinga/v0.1-launch-decree.md` | `/tmp/workspace/atlaslattice/manus-artifacts/bazinga/README.md` | `/tmp/workspace/atlaslattice/manus-artifacts/docs/LATTICE_GLOBAL_INDEX.md` | `/tmp/workspace/atlaslattice/manus-artifacts/docs/ARCHIVE_INDEX.md` | CANDIDATE |
| GPTDREAMPP | `/tmp/workspace/atlaslattice/manus-artifacts/archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md` | `/tmp/workspace/atlaslattice/manus-artifacts/archive/aetherforge/gptdreampp-openai/AETHERFORGE_FIELD_STATUS_SNAPSHOT_2026-05-27.md` | `/tmp/workspace/atlaslattice/manus-artifacts/archive/boot/gptbrain/reference_impl/run_checks.sh` | `/tmp/workspace/atlaslattice/manus-artifacts/archive/spec/gptdream/` | CANDIDATE |
| TIDELOCKBRAIN | `/tmp/workspace/atlaslattice/manus-artifacts/archive/boot/copilotbrain/TIDELOCKBRAIN/README.md` | `/tmp/workspace/atlaslattice/manus-artifacts/archive/boot/copilotbrain/TIDELOCKBRAIN/TIDELOCKBRAIN_WORK_LOG_GPTDREAM_ATLAS_ORCS_BUILD_2026-05-26.md` | `/tmp/workspace/atlaslattice/manus-artifacts/docs/WORLD_CLASS_READINESS_GATES.md` | `/tmp/workspace/atlaslattice/manus-artifacts/archive/boot/copilotbrain/TIDELOCKBRAIN/` | CANDIDATE |

## Update Rules

- Add evidence rows before publishing new AI-system claims.
- Keep references path-stable and repository-visible.
- Link this index from status snapshots and readiness reviews.
