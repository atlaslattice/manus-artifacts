---
artifact_id: DOC-LINEAGE-QUALITY-SCORE-REPORT-2026-05-29
title: Lineage Quality Score Report
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---

# Lineage Quality Score Report

Generated at: `2026-05-29T03:29:48+00:00`

> Scoring rubric from `docs/LINEAGE_QUALITY_SCORE_PROPOSAL_v0_1.md`.

## Band summary

| Score | Meaning | Count | % |
|---|---|---:|---:|
| 4 | Strong lineage | 303 | 81.7% |
| 3 | Usable lineage | 60 | 16.2% |
| 2 | Partial lineage | 0 | 0.0% |
| 1 | Weak lineage   | 1 | 0.3% |
| 0 | Unusable       | 7 | 1.9% |
| — | **Total**      | **371** | 100% |

**Average score:** 3.75 / 4.00

## Score-0 artifacts requiring immediate attention

| Path | Missing keys |
|---|---|
| `archive/boot/gptbrain/variants/S1_VARIANT_A_INTERFACE_PALACE_2026-05-09.md` | artifact_id, created, last_updated, owner, source_of_truth, title |
| `archive/boot/gptbrain/variants/S1_VARIANT_B_COGNITIVE_ARCHIVE_2026-05-09.md` | artifact_id, created, last_updated, owner, source_of_truth, title |
| `archive/boot/gptbrain/variants/S1_VARIANT_C_CLAIM_CALIBRATION_POINTER_2026-05-08.md` | artifact_id, created, last_updated, owner, source_of_truth, title |
| `archive/boot/gptbrain/variants/S1_VARIANT_E_CONTINUITY_HABITAT_2026-05-09.md` | artifact_id, created, last_updated, owner, source_of_truth, title |
| `manus-vault/MVP_Architect_Session/mvp-architect-skill/SKILL.md` | artifact_id, created, last_updated, owner, source_of_truth, status, title |
| `manus-vault/Skills/ai-native-os-architect/SKILL.md` | artifact_id, created, last_updated, owner, source_of_truth, status, title |
| `manus-vault/Skills/mvp-architect/SKILL.md` | artifact_id, created, last_updated, owner, source_of_truth, status, title |

## Score-1 artifacts (top 20 by priority)

| Path | Missing keys |
|---|---|
| `archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_WORK_LOG_WAVE7_TASK77_CI_OPTIMIZE_2026-05-29.md` | last_updated, source_of_truth |

## Canon promotion requirements

- Minimum score **3** required before canon review.
- Score **4** recommended for flagship artifacts.
- Re-run this script after each metadata backfill pass.
