---
artifact_id: DOC-PROVENANCE-COMPLETENESS-REPORT-2026-05-29
title: Provenance Completeness Report v2
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---

# Provenance Completeness Report v2

Generated at: `2026-05-29T03:29:10+00:00`

> **Wave 3 post-backfill snapshot.**

## Required provenance signals

- `artifact_id`
- `owner`
- `created` / `last_updated`
- `status`
- `source_of_truth`

## Gap summary

- Files missing `artifact_id`: **8**
- Files missing `source_of_truth`: **9**
- Files with invalid status values: **4**
- Files with non-GitHub source values: **0**

## Highest-priority remaining gaps

| Path | Missing keys |
|---|---|
| `archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_WORK_LOG_WAVE7_TASK77_CI_OPTIMIZE_2026-05-29.md` | last_updated, source_of_truth |
| `archive/boot/gptbrain/variants/S1_VARIANT_A_INTERFACE_PALACE_2026-05-09.md` | artifact_id, created, last_updated, owner, source_of_truth, title |
| `archive/boot/gptbrain/variants/S1_VARIANT_B_COGNITIVE_ARCHIVE_2026-05-09.md` | artifact_id, created, last_updated, owner, source_of_truth, title |
| `archive/boot/gptbrain/variants/S1_VARIANT_C_CLAIM_CALIBRATION_POINTER_2026-05-08.md` | artifact_id, created, last_updated, owner, source_of_truth, title |
| `archive/boot/gptbrain/variants/S1_VARIANT_E_CONTINUITY_HABITAT_2026-05-09.md` | artifact_id, created, last_updated, owner, source_of_truth, title |
| `manus-vault/MVP_Architect_Session/mvp-architect-skill/SKILL.md` | artifact_id, created, last_updated, owner, source_of_truth, status, title |
| `manus-vault/Skills/ai-native-os-architect/SKILL.md` | artifact_id, created, last_updated, owner, source_of_truth, status, title |
| `manus-vault/Skills/mvp-architect/SKILL.md` | artifact_id, created, last_updated, owner, source_of_truth, status, title |
| `docs/ARTIFACT_ID_COLLISION_REPORT_2026-05-27.md` | none |
| `docs/LINEAGE_QUALITY_SCORE_PROPOSAL_v0_1.md` | none |
| `docs/MASTER_SOURCE_REGISTRY.md` | none |
| `docs/METADATA_BACKFILL_SCOPE_2026-05-27.md` | none |
| `docs/METADATA_COVERAGE_REPORT_2026-05-27.md` | none |
| `docs/METADATA_EXCEPTION_REGISTRY_2026-05-27.md` | none |
| `docs/PROVENANCE_COMPLETENESS_REPORT_2026-05-27.md` | none |
| `docs/SCHEMA_VERSION_MIGRATION_NOTES_v0_1.md` | none |
| `docs/closeout/CONDITIONAL_HISTORY_REWRITE_RUNBOOK_2026-05-28.md` | none |
| `docs/closeout/DUPLICATE_ARTIFACT_DETECTION_PASS_2026-05-28.md` | none |
| `docs/closeout/HISTORY_REWRITE_RECEIPT_RESCAN_PROOF_2026-05-28.md` | none |
| `docs/closeout/NEXT10_EXECUTION_CHECKPOINTS_2026-05-28.md` | none |
| `docs/closeout/PII_AUDIT_CLOSEOUT_2026-05-28.md` | none |
| `docs/closeout/PII_AUDIT_EVIDENCE_RECEIPT_2026-05-28.md` | none |
| `docs/closeout/PRE_RELEASE_SAFETY_SIGNOFF_2026-05-28.md` | none |
| `docs/closeout/PROVENANCE_FRONTMATTER_BACKFILL_CLOSEOUT_2026-05-28.md` | none |
| `docs/closeout/REDACTION_PROTOCOL_SAFE_PUBLICATION_EXCEPTIONS_2026-05-28.md` | none |

## Exception paths (excluded from gap count)

| Path | Reason |
|---|---|
| `.github/ISSUE_TEMPLATE/artifact_proposal.md` | GitHub issue template; operational intake surface. |
| `.github/ISSUE_TEMPLATE/bug_report.md` | GitHub issue template; operational intake surface. |
| `.github/ISSUE_TEMPLATE/evidence_quest.md` | GitHub issue template; Aetherforge contributor quest intake. |
| `.github/ISSUE_TEMPLATE/feature_request.md` | GitHub issue template; operational intake surface. |
| `.github/ISSUE_TEMPLATE/graph_linking_quest.md` | GitHub issue template; Aetherforge contributor quest intake. |
| `.github/ISSUE_TEMPLATE/metadata_quest.md` | GitHub issue template; Aetherforge contributor quest intake. |
| `.github/PULL_REQUEST_TEMPLATE.md` | GitHub PR template; contributor workflow surface, not canon source. |
| `projects/free-bank/banking-revolution-archive.md` | Quarantine-pending: primarily refers to banks; requires owner routing to private repo before public backfill. |
