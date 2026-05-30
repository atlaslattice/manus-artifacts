---
artifact_id: CICD-POLICY-WORKFLOW-METRICS-001
title: Workflow Runtime Metrics Policy
status: candidate
created: 2026-05-28
owner: council
tags: [ci-cd, metrics, performance, workflow]
---

# Workflow Runtime Metrics Policy

> Defines how CI/CD workflow runtime metrics are collected, reviewed, and acted upon.

status: candidate

---

## Why Track Workflow Metrics?

Slow CI pipelines discourage frequent commits and degrade developer experience. Tracking runtime metrics enables:
- Early detection of workflow bloat
- Informed decisions about caching and parallelization
- Cost tracking (GitHub Actions minutes)
- SLO setting for CI performance

---

## Metrics to Track

| Metric | Description | Target |
|--------|-------------|--------|
| P50 wall-clock time | Median time from push to final job complete | ≤ 3 minutes |
| P95 wall-clock time | 95th percentile run time | ≤ 5 minutes |
| Failure rate (7-day rolling) | % of runs that fail | ≤ 5% |
| Flaky test rate | % of reruns needed | ≤ 2% |
| Cache hit rate | % of runs using cached dependencies | ≥ 80% |
| Action minutes consumed (monthly) | GitHub Actions billing minutes | Track; alert if > 500/month |

---

## Current Benchmarks (2026-05-28)

| Workflow | Typical runtime | Status |
|----------|----------------|--------|
| `boring-machine-validation.yml` | ~2 min | ✅ Within target |
| `gptbrain-reference-checks.yml` | ~1 min | ✅ Within target |
| `lattice-kg-quality-gates.yml` | ~1 min | ✅ Within target |

---

## Collection Method

GitHub Actions run data is accessible via the GitHub API. A quarterly pull of run durations from the past 90 days is performed using:

```bash
gh run list --limit 200 --json workflowName,createdAt,updatedAt,conclusion \
  | python scripts/analyze_workflow_metrics.py
```

(Script planned: `scripts/analyze_workflow_metrics.py`, Q3 2026)

---

## Review Cadence

| Review | Frequency | Owner |
|--------|-----------|-------|
| P50/P95 runtime check | Quarterly | Engineering |
| Failure rate trend | Monthly (from CI dashboard) | Engineering |
| Cost review | Quarterly | @atlaslattice |

---

## Optimization Triggers

If any metric exceeds its target:

| Issue | Response |
|-------|---------|
| P50 > 3 min | Profile jobs; add caching; parallelize |
| Failure rate > 5% | Investigate flaky tests; fix root cause |
| Cache hit rate < 80% | Review cache keys; ensure dependency lock files are committed |
| > 500 Action minutes/month | Review trigger conditions; add `paths` filters |

---

*Atlas Lattice Foundation · status: candidate*
