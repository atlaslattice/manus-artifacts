---
artifact_id: TEST-POLICY-RELIABILITY-SLOS-001
title: Reliability SLOs
status: candidate
created: 2026-05-28
owner: council
tags: [testing, reliability, slo, quality]
---

# Reliability SLOs

> Defines Service Level Objectives (SLOs) for the reliability of the Atlas Lattice repository's systems and processes.

status: candidate

---

## SLO Framework

An **SLO (Service Level Objective)** is a measurable target for a system's reliability. For a knowledge archive, reliability means:
- Tests pass consistently
- KG index is available and accurate
- CI pipelines run to completion
- Links and references are valid

---

## SLO Table

| SLO | Metric | Target | Measurement window |
|-----|--------|--------|-------------------|
| CI Reliability | % of CI runs completing successfully on non-broken code | ≥ 98% | 30-day rolling |
| Flaky Test Rate | % of CI failures attributable to flaky tests | ≤ 2% | 30-day rolling |
| KG Index Freshness | Hours since last successful KG index build on main | ≤ 24 hours | Real-time |
| Orphan Rate | % of repository artifacts with 0 inbound + 0 outbound links | ≤ 5% | Weekly scan |
| Metadata Coverage | % of `archive/governance/` files with complete required frontmatter | ≥ 95% | Weekly scan |
| Broken Internal Links | Count of broken internal links in main | 0 | Weekly scan |
| Test Suite Runtime (P95) | 95th percentile total test suite wall-clock time | ≤ 5 minutes | 30-day rolling |

---

## Error Budget

For CI Reliability (98% target, 30-day window):
- **Total allowed failures:** 2% × 30 days × ~10 CI runs/day ≈ 6 failures/month
- When the error budget is depleted: freeze new features; focus on reliability improvements

---

## SLO Measurement

SLOs are measured and reported quarterly as part of the [Monthly Quality Report](./MONTHLY_QUALITY_REPORT_TEMPLATE.md). Between formal reports, the security champion monitors CI health informally.

---

## SLO Review Cadence

| Action | Frequency |
|--------|-----------|
| Measure all SLOs | Quarterly |
| Report on SLO health | Quarterly (quality report) |
| Tighten SLO targets | Annually (when consistently met) |
| Investigate missed SLO | Within 1 week of miss |

---

## SLO Miss Response

When an SLO is missed:
1. Log in [PUBLIC_RISK_REGISTER.md](./PUBLIC_RISK_REGISTER.md) as an operational risk
2. Identify root cause within 2 weeks
3. Define remediation action
4. Re-evaluate target if miss was due to an invalid benchmark (SLO too tight)

---

*Atlas Lattice Foundation · status: candidate*
