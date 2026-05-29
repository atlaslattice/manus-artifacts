# Governance Audit Cadence

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #11
LAST_UPDATED: 2026-05-29
```

Defines the schedule, scope, and ownership of recurring governance audits
for the `atlaslattice/manus-artifacts` repository.

---

## Audit Schedule

| Cadence | Trigger | Scope | Owner |
|---|---|---|---|
| **Weekly** | Monday 00:00 UTC (auto-CI) | KG integrity, broken links, metadata completeness | CI pipeline |
| **Monthly** | First Monday of month | Candidate register review, open disputes, KPI check | @atlaslattice |
| **Quarterly** | Q1/Q2/Q3/Q4 | Full governance health review, KPI dashboard update | @atlaslattice + council |
| **Annual** | Jan 1 | Comprehensive archive audit, protocol optimization | @atlaslattice + council |
| **Ad hoc** | On critical dispute or rollback | Targeted scope | @atlaslattice |

---

## Weekly Automated Audit (CI)

CI runs the following on every push to `main` and on schedule:

```bash
python scripts/validate_artifact_metadata.py
python scripts/check_graph_link_integrity.py
python scripts/check_markdown_links.py
python scripts/detect_orphaned_artifacts.py
python scripts/validate_lattice_quality_gates.py
```

Failures block merge. Results are logged to the CI run summary.

---

## Monthly Governance Review

Agenda:

1. **Candidate register** — Review all `UNDER_REVIEW` artifacts; clear or
   advance stale nominations (> 30 days).
2. **Open disputes** — Status check on all `canon-dispute` issues.
3. **KPI dashboard** — Review [GOVERNANCE_KPI_DASHBOARD.md](./GOVERNANCE_KPI_DASHBOARD.md).
4. **Policy drift** — Check for implicit governance practice drift vs. docs.
5. **Action items** — Record in governance changelog.

---

## Quarterly Health Review

In addition to monthly agenda:

1. Review all `RATIFIED` artifacts for continued accuracy.
2. Run full archive scan for new orphans, broken links, metadata gaps.
3. Review 8/8/8 ops cycle performance.
4. Update `GOVERNANCE_KPI_DASHBOARD.md` with quarterly metrics.
5. Publish quarterly summary to `docs/governance/GOVERNANCE_CHANGELOG_TEMPLATE.md`.

---

## Annual Protocol Optimization

In addition to quarterly agenda:

1. Review all governance docs for accuracy and completeness.
2. Review all 144-task campaign progress.
3. Update trust taxonomy, frontmatter standard, and event ID sequence if needed.
4. Archive prior-year governance log to `archive/governance/<year>/`.
5. Publish annual state-of-the-lattice summary.

---

## Audit Output Artifacts

| Output | Location | Frequency |
|---|---|---|
| CI quality gate report | GitHub Actions run log | Weekly |
| Monthly review notes | `docs/governance/GOVERNANCE_CHANGELOG_TEMPLATE.md` | Monthly |
| Quarterly KPI snapshot | `docs/governance/GOVERNANCE_KPI_DASHBOARD.md` | Quarterly |
| Annual archive | `archive/governance/<year>/` | Annual |

---

## Related

- [GOVERNANCE_KPI_DASHBOARD.md](./GOVERNANCE_KPI_DASHBOARD.md)
- [GOVERNANCE_CHANGELOG_TEMPLATE.md](./GOVERNANCE_CHANGELOG_TEMPLATE.md)
- [CANON_ADJUDICATION_CHECKLIST.md](./CANON_ADJUDICATION_CHECKLIST.md)
