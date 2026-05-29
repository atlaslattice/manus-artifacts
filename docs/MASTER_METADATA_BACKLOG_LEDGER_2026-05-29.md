---
artifact_id: DOC-MASTER-METADATA-BACKLOG-LEDGER-2026-05-29
title: Master Metadata Backlog Ledger (500+ IP Program)
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---

# Master Metadata Backlog Ledger (500+ IP Program)

> Wave 3 · Task 36 · Generated 2026-05-29

This ledger tracks the full backfill queue for the 500+ IP public program.
It maps every markdown artifact to its backfill tier, current metadata state, and queue status.

---

## Tier summary

| Tier | Description | Count | Status |
|---|---|---:|---|
| Tier 0 — Top 50 | Highest-value public surfaces | 50 | ✅ All complete |
| Tier 1 — Next 100 | Priority archive + spec + boot artifacts | 100 | ✅ Backfilled 2026-05-29 |
| Tier 2 — Next 200 | Governance, seats, culture, architecture | 200 | ✅ Backfilled 2026-05-29 |
| Tier 3 — Tail 26 | Research, health, manus-vault, misc | 26 | ✅ Backfilled 2026-05-29 |
| Exceptions | GitHub templates + quarantine-pending | 8 | ⏳ Owner action / template surface |
| **Total in repo** | | **384** | 376/384 complete |

> **Coverage rate after Wave 3 backfill: 98%**  
> Remaining 8 = exception/quarantine paths. No non-exception paths remain without metadata.

---

## 500+ IP ingestion queue

The following is the forward-looking ledger for IP artifacts not yet in the repository.
Each ingested source should be registered in `docs/MASTER_SOURCE_REGISTRY.md` before
any artifacts are committed.

| Priority | Source | Est. artifacts | Domain | Intake status |
|---:|---|---:|---|---|
| P0 | `atlaslattice/manus-artifacts` (this repo) | 384 | All | ✅ Indexed |
| P1 | Other git repos (atlaslattice org) | ~50 | Codebases, research | 🟨 Pending source registration |
| P2 | Notion workspace | ~200 | Projects, planning, logs | 🟨 Pending Notion export |
| P3 | Google Drive | ~150 | Docs, presentations, archives | 🟨 Pending Drive export |
| P4 | Local archives (Windows PC) | ~100+ | Raw IP, early work | 🟨 Pending owner upload |
| P5 | Additional archived gits | ~50 | Legacy codebases | 🟨 Pending discovery |
| — | **Total est.** | **~534+** | | |

---

## Tier 3 — Tail artifacts (26 files)

These 26 files were backfilled in the Wave 3 batch pass. They include research sweeps,
health-domain content, manus-vault session logs, and root-level summaries.

| Path | Domain | Notes |
|---|---|---|
| `archives/janus-checkpoints/latest-checkpoint.md` | Archive | Legacy checkpoint |
| `bazinga/v0.1-launch-decree.md` | Project | Launch artifact |
| `council/council-session-master-archive.md` | Council | Session archive |
| `council-reviews/council-review-copilot-output.md` | Council | Review artifact |
| `council-reviews/council-review-manus-artifacts.md` | Council | Review artifact |
| `final_manus_artifact_report.md` | Root | Manus session report |
| `health/austin-in-home-pt.md` | Health | Personal health data — review before public |
| `health/texas-neuro-rehab-patient-rights.md` | Health | Public health info |
| `health/texas-residential-facilities.md` | Health | Public health info |
| `health/texas-wellness-facilities.md` | Health | Public health info |
| `manus-vault/Digital_Noahs_Ark/01_architecture_spec.md` | Manus-vault | Architecture spec |
| `manus-vault/Digital_Noahs_Ark/02_invisible_interface_design.md` | Manus-vault | Design artifact |
| `manus-vault/Digital_Noahs_Ark/03_feature_absorption_engine.md` | Manus-vault | Feature spec |
| `manus-vault/Digital_Noahs_Ark/04_continuity_bridge_architecture.md` | Manus-vault | Architecture spec |
| `manus-vault/MVP_Architect_Session/copilot_message.md` | Manus-vault | Session log |
| `manus-vault/MVP_Architect_Session/mvp_proposal.md` | Manus-vault | Proposal |
| `manus-vault/MVP_Architect_Session/review.md` | Manus-vault | Review log |
| `manus-vault/MVP_Architect_Session/session_log.md` | Manus-vault | Session log |
| `manus-vault/session_summary.md` | Manus-vault | Summary |
| `research/intelligence-sweeps/2026-03-17_to_03-18_24hr-sweep.md` | Research | Intelligence sweep |
| `research/intelligence-sweeps/2026-03-18_to_03-19_24hr-expanded-sweep.md` | Research | Intelligence sweep |
| `research/shugs-microscopy-cross-reference-april-2026.md` | Research | Cross-reference |
| `research/tech-titans-convergence-report.md` | Research | Report |
| `research/workspace-briefing.md` | Research | Briefing |
| `sandbox_inventory_april_2026.md` | Root | Sandbox log |
| `synthesis_plan.md` | Root | Synthesis plan |

### Health domain note

`health/austin-in-home-pt.md` may contain personal health data. Recommend owner review
before promoting to canon or making the directory explicitly public. All other health files
appear to contain publicly available resource listings.

---

## Exception paths ledger

| Path | Reason | Action required |
|---|---|---|
| `.github/PULL_REQUEST_TEMPLATE.md` | GitHub workflow template | None — operational surface |
| `.github/ISSUE_TEMPLATE/artifact_proposal.md` | GitHub issue template | None — operational surface |
| `.github/ISSUE_TEMPLATE/bug_report.md` | GitHub issue template | None — operational surface |
| `.github/ISSUE_TEMPLATE/feature_request.md` | GitHub issue template | None — operational surface |
| `.github/ISSUE_TEMPLATE/graph_linking_quest.md` | GitHub issue template | None — operational surface |
| `.github/ISSUE_TEMPLATE/metadata_quest.md` | GitHub issue template | None — operational surface |
| `.github/ISSUE_TEMPLATE/evidence_quest.md` | GitHub issue template | None — operational surface |
| `projects/free-bank/banking-revolution-archive.md` | Quarantine-pending (bank content) | **Owner action**: route to private repo |

---

## Next backfill actions

1. **Owner**: route `projects/free-bank/banking-revolution-archive.md` to quarantine/private repo (Wave 1 blocker).
2. **Owner**: review `health/austin-in-home-pt.md` for any personally identifiable health data.
3. **Agent**: begin Wave 4 graph integrity sweep once Wave 3 checkpoint gate is closed.
4. **Automation**: monthly provenance drift workflow will keep this ledger current going forward.

---

*Generated by TIDELOCKBrain — Wave 3 · 2026-05-29*
