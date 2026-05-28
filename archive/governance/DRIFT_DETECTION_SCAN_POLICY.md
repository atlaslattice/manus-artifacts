---
artifact_id: CICD-POLICY-DRIFT-DETECTION-001
title: Drift Detection Scan Policy
status: candidate
created: 2026-05-28
owner: council
tags: [ci-cd, drift, detection, automation, schedule]
---

# Drift Detection Scan Policy

> Defines scheduled scans that detect when the repository has drifted from its documented standards.

status: candidate

---

## What Is Drift?

**Repository drift** occurs when the actual state of the repository no longer matches its documented standards. Examples:

- Frontmatter fields missing on new files
- Cross-link density below targets
- Orphan artifacts accumulating
- Schema files out of sync with reference implementations
- Stale artifacts past their review window
- CHANGELOG.md not updated in > 30 days

Drift is inevitable in active repositories. The solution is **scheduled detection** — regular automated scans that surface drift before it compounds.

---

## Scheduled Scans

| Scan | Tool | Schedule | Output |
|------|------|---------|--------|
| Orphan node scan | `scripts/validate_lattice_quality_gates.py` | Weekly (Sunday 00:00 UTC) | GitHub issue if orphan_rate > 5% |
| Stale artifact scan | `scripts/scan_stale_artifacts.py` (planned) | Weekly (Sunday 00:00 UTC) | GitHub issue listing stale artifacts |
| Metadata completeness | `scripts/check_metadata_completeness.py` (planned) | Weekly (Sunday 00:00 UTC) | GitHub issue if coverage < threshold |
| External link check | `scripts/check_external_links.py` (planned) | Weekly (Monday 06:00 UTC) | GitHub issue listing broken URLs |
| CHANGELOG staleness | Built-in check | Monthly | Warning if CHANGELOG not updated in 30 days |
| Schema drift | `scripts/validate_schemas.py` (planned) | On push to main | Blocks merge if schema drift detected |

---

## Drift Severity Levels

| Level | Definition | Response time |
|-------|-----------|--------------|
| **Critical** | KG quality gate fails; CI blocked | Immediate (blocks all PRs to main) |
| **High** | Orphan rate > 10%; metadata coverage < 50% | 48 hours |
| **Medium** | Stale artifacts > 20; external links broken | 2 weeks |
| **Low** | Minor frontmatter gaps; single broken external link | Rolling backlog |

---

## Drift Report

Each weekly scan run produces a drift report committed to `kg/drift_report_YYYY-MM-DD.json`:

```json
{
  "date": "2026-05-28",
  "orphan_count": 2,
  "orphan_rate": 0.014,
  "stale_count": 0,
  "metadata_coverage": 0.92,
  "broken_external_links": 1,
  "overall_drift_level": "low"
}
```

---

## Drift Budget

A healthy repository maintains:

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Orphan rate | < 3% | 3–10% | > 10% |
| Stale artifacts | < 5 | 5–20 | > 20 |
| Metadata coverage | > 90% | 70–90% | < 70% |
| Broken ext. links | 0 | 1–5 | > 5 |
| CHANGELOG staleness | < 14 days | 14–30 days | > 30 days |

---

*Atlas Lattice Foundation · status: candidate*
