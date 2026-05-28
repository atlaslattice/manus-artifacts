# Quality Dashboard
Status: Candidate
Date: 2026-05-26

This page is the single-page view of archive health.
It should help contributors, reviewers, and public readers see whether the repository is becoming more trustworthy over time.

## At-a-glance signals

- Canon integrity workflow: ![Canon Integrity](https://github.com/atlaslattice/manus-artifacts/actions/workflows/canon-integrity-check.yml/badge.svg)
- Stale artifact workflow: ![Stale Artifact Check](https://github.com/atlaslattice/manus-artifacts/actions/workflows/stale-artifact-check.yml/badge.svg)
- GPTBrain parity workflow: ![GPTBrain Reference Checks](https://github.com/atlaslattice/manus-artifacts/actions/workflows/gptbrain-reference-checks.yml/badge.svg)

## Domain coverage snapshot

| Domain | Coverage estimate | Current posture |
| --- | --- | --- |
| Systems | 85% | strong flagship visibility |
| Projects | 75% | good public anchor coverage |
| Governance | 80% | rapidly improving process completeness |
| Research | 60% | visible but still uneven |
| Health | 45% | under-structured, higher review sensitivity |
| Vault | 55% | continuity-rich, public framing still maturing |

## Open quality tasks

- retrofit metadata frontmatter onto legacy flagship documents
- expand lineage links on older systems artifacts
- review stale pages older than 90 days
- tighten provenance on sensitive research and health materials
- publish recurring hygiene sprint summaries through mission control cadence

## Recent hygiene runs

| Date | Run type | Outcome |
| --- | --- | --- |
| 2026-05-26 | Top-50 governance and navigation batch | Major archive guidance expanded |
| 2026-05-26 | Newcomer-path review | Onboarding, doctrine map, and best-of list added |
| 2026-05-26 | Quality instrumentation pass | Integrity and stale-content workflows added |

## Auto-refresh data snapshot

- Data artifact: [generated/QUALITY_DASHBOARD_DATA.json](./generated/QUALITY_DASHBOARD_DATA.json)
- Pipeline command: `python /tmp/workspace/atlaslattice/manus-artifacts/scripts/build_quality_dashboard_data.py`
- CI guards: `ring3-validation-hardening.yml` and `quality-dashboard-auto-refresh.yml`

## How to read this dashboard

Coverage percentages are directional estimates, not legal guarantees.
They are intended to make gaps visible and to keep Aetherforge quality work legible to outside observers.

## Related documents

- [VALIDATION_PLAYBOOK.md](./VALIDATION_PLAYBOOK.md)
- [ARTIFACT_SCORECARDS.md](./ARTIFACT_SCORECARDS.md)
- [RELEASE_CADENCE.md](./RELEASE_CADENCE.md)
