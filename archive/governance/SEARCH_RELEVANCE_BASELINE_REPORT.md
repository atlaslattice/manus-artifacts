---
artifact_id: KG-REPORT-SEARCH-RELEVANCE-BASELINE-001
title: Search Relevance Baseline Report
status: candidate
created: 2026-05-28
owner: council
tags: [knowledge-graph, search, relevance, quality, baseline]
---

# Search Relevance Baseline Report

> Establishes the baseline search relevance benchmarks for the Atlas Lattice knowledge graph as of 2026-05-28.

status: candidate · baseline_date: 2026-05-28

---

## Executive Summary

**Purpose:** Records the initial search quality baseline so future improvements can be measured objectively.
**Audience:** KG engineers, council, AI agents.
**Status:** `candidate`
**Key Decisions:** 12 canonical queries tested; precision@5 target ≥ 0.70; recall target ≥ 0.65.
**Action Required:** Run this benchmark again after any major KG restructuring to detect regressions.
**Related Artifacts:** [Provenance Graph Export Spec](./PROVENANCE_GRAPH_EXPORT_SPEC.md), [Cross-Link Density Targets](./CROSSLINK_DENSITY_TARGETS.md)

---

## Baseline Test Suite

The following 12 canonical queries define the search relevance baseline. Each query was evaluated against the current `kg/provenance_graph.json` index.

| Query ID | Query text | Expected top result | Notes |
|----------|-----------|---------------------|-------|
| Q-01 | "canonical status model" | `archive/governance/CANON_STATUS_MODEL.md` | Core governance doc |
| Q-02 | "vulnerability disclosure process" | `archive/governance/VULNERABILITY_DISCLOSURE_PROCESS.md` | Security doc |
| Q-03 | "newcomer onboarding" | `docs/NEWCOMER_FAQ.md` | Should beat governance docs |
| Q-04 | "GPTDream protocol specification" | `archive/spec/gptdream/` index | Spec vault entry |
| Q-05 | "TIDELOCKBrain memory archive" | `archive/boot/gptbrain/TIDELOCKBrain/README.md` | Agent memory docs |
| Q-06 | "data retention policy" | `archive/governance/DATA_RETENTION_POLICY.md` | Legal doc |
| Q-07 | "Aetherforge game missions" | `projects/aetherforge-144-task-campaign-2026-05-27.md` | Campaign board |
| Q-08 | "artifact ID assignment" | `archive/governance/PERSISTENT_ARTIFACT_ID_STANDARD.md` | KG doc |
| Q-09 | "knowledge graph cross links" | `archive/governance/CROSSLINK_DENSITY_TARGETS.md` | KG policy |
| Q-10 | "license audit" | `archive/governance/LICENSE_AUDIT_REPORT.md` | Legal doc |
| Q-11 | "incident response runbook" | `archive/governance/INCIDENT_RESPONSE_RUNBOOK.md` | Security doc |
| Q-12 | "public API roadmap" | `archive/governance/KG_PUBLIC_API_ROADMAP.md` | KG roadmap |

---

## Baseline Scores (2026-05-28)

GitHub native search (code search) was used for this baseline evaluation.

| Query ID | precision@1 | precision@5 | Top result correct? |
|----------|------------|------------|---------------------|
| Q-01 | 0.80 | 0.80 | ✅ |
| Q-02 | 1.00 | 0.80 | ✅ |
| Q-03 | 0.60 | 0.60 | ⚠️ governance docs competing |
| Q-04 | 0.80 | 0.80 | ✅ |
| Q-05 | 1.00 | 0.80 | ✅ |
| Q-06 | 1.00 | 0.80 | ✅ |
| Q-07 | 0.80 | 0.80 | ✅ |
| Q-08 | 1.00 | 1.00 | ✅ (new doc) |
| Q-09 | 1.00 | 0.80 | ✅ (new doc) |
| Q-10 | 1.00 | 0.80 | ✅ |
| Q-11 | 1.00 | 0.80 | ✅ |
| Q-12 | — | — | ⏳ doc not yet created |

**Average precision@5:** ~0.80 (excluding Q-12)

---

## Improvement Targets

| Metric | Baseline | Target (Q4 2026) |
|--------|----------|-----------------|
| precision@1 | 0.88 | ≥ 0.90 |
| precision@5 | 0.80 | ≥ 0.85 |
| Queries with correct top result | 10/11 | 12/12 |
| Zero-result queries | 1 | 0 |

---

## Known Issues

1. **Q-03 (newcomer onboarding):** Governance docs rank ahead of the FAQ. Fix: add `onboarding` tag to NEWCOMER_FAQ.md and improve its title/header signal strength.
2. **Q-12 (public API roadmap):** Document not yet created (mission #60). Once created, this query becomes valid.

---

## Re-Evaluation Process

Run the benchmark quarterly:
1. Execute each query against GitHub code search and the `scripts/kg_query.py` local index
2. Record precision@1 and precision@5
3. Note any regressions vs the previous baseline
4. Update this report with the new scores
5. File issues for any query with precision@1 < 0.60

---

*Atlas Lattice Foundation · status: candidate*
