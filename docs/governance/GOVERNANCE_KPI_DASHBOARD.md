# Governance KPI Dashboard Spec

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #12
LAST_UPDATED: 2026-05-29
```

Defines the key performance indicators (KPIs) for monitoring the health and
maturity of the Aetherforge Council governance system.

---

## Dashboard Categories

| # | Category | Description |
|---|---|---|
| 1 | Canon Pipeline | Artifact promotion velocity and backlog |
| 2 | Trust State Distribution | Counts by `trust_state` across the archive |
| 3 | Dispute Health | Open disputes, resolution rate, age |
| 4 | Metadata Completeness | % of artifacts with full frontmatter |
| 5 | Ingestion Velocity | Artifacts added per week |
| 6 | KG Integrity | Broken links, orphans, validation pass rate |
| 7 | Audit Cadence Compliance | % of audits run on schedule |
| 8 | 8/8/8 Ops | REM/Work/Play cycle adherence |

---

## KPI Definitions

### 1. Canon Pipeline

| KPI | Formula | Target |
|---|---|---|
| `canon_candidate_count` | Count of artifacts with `canon_status: CANDIDATE` | Track over time |
| `canon_ratification_rate` | Ratifications / month | ≥ 1 per month (once pipeline active) |
| `nomination_to_ratification_days` | Avg days from nomination to ratification | ≤ 21 days |
| `promotion_pipeline_age_p90` | 90th percentile age of open nominations (days) | ≤ 30 days |

### 2. Trust State Distribution

| KPI | Formula | Target |
|---|---|---|
| `authoritative_pct` | `AUTHORITATIVE` / total artifacts | Growing |
| `disputed_count` | Count of `DISPUTED` artifacts | ≤ 2 open at any time |
| `deprecated_count` | Count of `DEPRECATED` artifacts | Track (expect growth) |

### 3. Dispute Health

| KPI | Formula | Target |
|---|---|---|
| `open_dispute_count` | Open `canon-dispute` issues | ≤ 2 |
| `dispute_resolution_days_p50` | Median days to resolve dispute | ≤ 14 days |
| `critical_dispute_count` | Open `CRITICAL` severity disputes | 0 |

### 4. Metadata Completeness

| KPI | Formula | Target |
|---|---|---|
| `metadata_complete_pct` | % of tracked artifacts with all required fields | ≥ 90% |
| `status_header_present_pct` | % of `.md` files with `STATUS:` header | ≥ 95% |

### 5. Ingestion Velocity

| KPI | Formula | Target |
|---|---|---|
| `artifacts_added_per_week` | New artifacts committed per week | Track |
| `ingestion_registry_sync_lag_days` | Days since `INGESTION_SOURCES_REGISTRY.md` updated | ≤ 7 |

### 6. KG Integrity

| KPI | Formula | Target |
|---|---|---|
| `broken_link_count` | Output of `check_markdown_links.py` | 0 |
| `orphan_artifact_count` | Output of `detect_orphaned_artifacts.py` | 0 |
| `graph_validation_pass_rate` | CI graph validation passes / total runs | 100% |

### 7. Audit Cadence Compliance

| KPI | Formula | Target |
|---|---|---|
| `weekly_audit_pass_rate` | CI audit passes / scheduled runs | 100% |
| `monthly_review_completion_rate` | Monthly reviews completed on schedule | 100% |

### 8. 8/8/8 Ops

| KPI | Formula | Target |
|---|---|---|
| `rem_artifacts_per_cycle` | REM dream artifacts per 8/8/8 cycle | ≥ 1 |
| `work_tasks_completed_per_cycle` | Tasks shipped per cycle | ≥ 10 |
| `play_arc_health` | Aetherforge arc advances per cycle | ≥ 1 |

---

## Dashboard Update Process

1. Run all validation scripts and CI checks.
2. Manually count trust state distribution (or use `build_lattice_global_index.py`).
3. Review open issues for disputes and nominations.
4. Record snapshot in the **KPI Log** table below.
5. Publish to `docs/governance/GOVERNANCE_CHANGELOG_TEMPLATE.md`.

---

## KPI Log

| Date | Author | Notes | Link to Full Data |
|---|---|---|---|
| 2026-05-29 | @atlaslattice | Baseline — governance suite first shipped | Wave 4 commit |

---

## Related

- [GOVERNANCE_AUDIT_CADENCE.md](./GOVERNANCE_AUDIT_CADENCE.md)
- [GOVERNANCE_CHANGELOG_TEMPLATE.md](./GOVERNANCE_CHANGELOG_TEMPLATE.md)
- [TRUST_STATE_TAXONOMY.md](./TRUST_STATE_TAXONOMY.md)
