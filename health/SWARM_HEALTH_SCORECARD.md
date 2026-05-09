# SWARM HEALTH SCORECARD

**Status:** Operational monitoring template (periodic reporting artifact)  
**Cadence:** Weekly (recommended) or per sprint/phase

## Instructions

1. Fill one row per reporting period.
2. Use task packet logs and backlog transitions as data sources.
3. Flag regressions in notes and link incident IDs from the failure ledger.
4. Review scorecard in council/review cycle; escalate repeated failures.

## Core Metrics

- **task_throughput:** tasks completed in period
- **handoff_latency_avg_hours:** average hours between lane handoffs
- **provenance_completeness_pct:** % tasks with complete source/evidence metadata
- **approval_gated_task_count:** number of tasks requiring human approval gate
- **quarantine_rate_pct:** % tasks moved to `quarantined`
- **repeated_failure_classes:** count of failure classes with repeat incidents
- **recovery_success_rate_pct:** % recovery-mode tasks successfully resumed
- **ratification_rate_pct:** % reviewed tasks ratified

## Blank Template

| Period | Tasks Opened | task_throughput | handoff_latency_avg_hours | provenance_completeness_pct | approval_gated_task_count | quarantine_rate_pct | repeated_failure_classes | recovery_success_rate_pct | ratification_rate_pct | Notes / Incident Links |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| YYYY-WW |  |  |  |  |  |  |  |  |  |  |
| YYYY-WW |  |  |  |  |  |  |  |  |  |  |
| YYYY-WW |  |  |  |  |  |  |  |  |  |  |

## Interpretation Guide

- Rising throughput with falling provenance completeness indicates speed-over-governance drift.
- Rising quarantine rate with repeated failures indicates guardrail or handoff contract gaps.
- Low ratification with high review volume indicates approval bottlenecks needing escalation.
