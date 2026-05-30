---
artifact_id: TEST-POLICY-MONTHLY-QUALITY-REPORT-001
title: Monthly Quality Report Template
status: candidate
created: 2026-05-28
owner: council
tags: [testing, quality, reporting, metrics]
---

# Monthly Quality Report Template

> Template for the monthly quality report tracking test health, coverage, and reliability metrics.

status: candidate

---

## Report Template

```markdown
# Monthly Quality Report — [Month YYYY]

**Report date:** YYYY-MM-DD
**Prepared by:** [Agent/Person]
**Period:** YYYY-MM-01 to YYYY-MM-DD

---

## SLO Summary

| SLO | Target | Actual | Status |
|-----|--------|--------|--------|
| CI Reliability | ≥ 98% | X% | 🟢 / 🟡 / 🔴 |
| Flaky Test Rate | ≤ 2% | X% | 🟢 / 🟡 / 🔴 |
| KG Index Freshness | ≤ 24h | Xh avg | 🟢 / 🟡 / 🔴 |
| Orphan Rate | ≤ 5% | X% | 🟢 / 🟡 / 🔴 |
| Metadata Coverage | ≥ 95% | X% | 🟢 / 🟡 / 🔴 |
| Broken Internal Links | 0 | N | 🟢 / 🟡 / 🔴 |
| Test Suite Runtime (P95) | ≤ 5 min | X min | 🟢 / 🟡 / 🔴 |

---

## Test Suite Health

| Metric | Count/Value |
|--------|------------|
| Total tests | N |
| Tests passing | N |
| Tests failing | N |
| Tests skipped | N |
| Tests quarantined (flaky) | N |
| New tests added this month | N |

---

## Coverage Summary

| Domain | Coverage | Delta vs last month |
|--------|---------|---------------------|
| `reference_impl/atlas_orcs/` | X% | +/- X% |
| `reference_impl/execution_gate/` | X% | +/- X% |
| `scripts/` | X% | +/- X% |

---

## Security Health

| Metric | Count |
|--------|-------|
| Open Dependabot alerts | N |
| Open CodeQL alerts | N |
| Open secret scanning alerts | N |
| CVEs resolved this month | N |

---

## Repository Health

| Metric | Value |
|--------|-------|
| Total artifacts | N |
| Orphan nodes | N |
| Stale artifacts (> 180 days) | N |
| Broken internal links | N |
| Frontmatter coverage | X% |

---

## Incidents and Issues

List any notable incidents, test failures, or process issues from this month:

- (none / list items)

---

## Action Items

| Item | Owner | Due |
|------|-------|-----|
| (list action items) | | |

---

## Notes

(Any other observations for this period)
```

---

## Report Cadence

| Report | Frequency | Owner |
|--------|-----------|-------|
| Monthly Quality Report | Monthly (first week of month) | Security Champion / Engineering |
| Annual Summary | Annually | @atlaslattice |

Reports are stored at: `archive/governance/QUALITY_REPORT_YYYY_MM.md`

---

*Atlas Lattice Foundation · status: candidate*
