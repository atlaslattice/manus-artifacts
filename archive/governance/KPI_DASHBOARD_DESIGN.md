---
artifact_id: LAUNCH-POLICY-KPI-DASHBOARD-001
title: KPI Dashboard Design
status: candidate
created: 2026-05-28
owner: council
tags: [launch, kpi, dashboard, metrics, monitoring]
---

# KPI Dashboard Design

> Defines the key performance indicators and dashboard design for Atlas Lattice operational visibility.

status: candidate

---

## Dashboard Vision

A public KPI dashboard shows the health, growth, and world-class progress of Atlas Lattice in real time. Initially, it will be a markdown table updated quarterly; ultimately, a live dashboard rendered from the KG and GitHub APIs.

---

## KPI Categories

### Tier 1: Mission Progress KPIs

| KPI | Current value | Target |
|-----|-------------|--------|
| Missions complete | 144/144 | 144/144 ✅ |
| World-class scorecard | ~475/720 | ≥ 600/720 |
| KG nodes | TBD (pending index rebuild) | ≥ 500 |
| KG edges | TBD | ≥ 2000 |

---

### Tier 2: Quality KPIs

| KPI | Current value | Target |
|-----|-------------|--------|
| CI pass rate | ≥ 98% (target) | ≥ 98% |
| Test count | 63+ | ≥ 100 by v1.0 |
| Metadata coverage | TBD | ≥ 95% |
| Orphan node rate | TBD | ≤ 5% |
| Broken internal links | 0 target | 0 |

---

### Tier 3: Community KPIs

| KPI | Current value | Target |
|-----|-------------|--------|
| Stars | TBD | ≥ 100 by v1.0 |
| External contributors | 0 (solo project) | ≥ 5 by v1.0 |
| Forks | TBD | ≥ 10 by v1.0 |
| Issues opened by community | 0 | ≥ 20 by v1.0 |

---

### Tier 4: Security KPIs

| KPI | Current value | Target |
|-----|-------------|--------|
| Open critical/high Dependabot alerts | 0 | 0 |
| Open CodeQL alerts | 0 | 0 |
| Days since last security review | TBD | ≤ 365 |

---

## Dashboard Rendering Plan

**Phase 1 (now):** Markdown table in `docs/KPI_DASHBOARD.md`, updated quarterly.

**Phase 2 (post M5):** GitHub Pages site rendering live data from:
- `kg/global_index.json` for KG metrics
- GitHub API for community/repo metrics
- CI badge API for quality metrics

---

## Dashboard Publishing

The KPI Dashboard is published at:
- `docs/KPI_DASHBOARD.md` (always current, updated quarterly)
- Referenced in `README.md` in the Progress section

---

*Atlas Lattice Foundation · status: candidate*
