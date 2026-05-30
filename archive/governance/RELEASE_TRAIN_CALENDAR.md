---
artifact_id: LAUNCH-POLICY-RELEASE-TRAIN-001
title: Release Train Calendar
status: candidate
created: 2026-05-28
owner: council
tags: [launch, release, calendar, versioning, cadence]
---

# Release Train Calendar

> Defines the Atlas Lattice release cadence and version scheme.

status: candidate

---

## Version Scheme

Atlas Lattice uses **calendar versioning** (CalVer):

```text
v[YEAR].[QUARTER].[PATCH]
v2026.Q3.0  — first release of Q3 2026
v2026.Q3.1  — patch release within Q3 2026
v2027.Q1.0  — first release of Q1 2027
```

Special releases:
- `v1.0.0` — the formal v1.0 milestone release (overrides CalVer for historical clarity)

---

## Release Types

| Type | Frequency | Trigger |
|------|-----------|---------|
| Quarterly release | Every 3 months | Wave completion + scorecard update |
| Milestone release | When milestone criteria met | v1.0, v2.0, etc. |
| Hotfix release | As needed | Critical bug or security fix |
| Open Data Pack | Quarterly | Aligned with quarterly release |

---

## Release Train Calendar (2026–2027)

| Release | Target date | Expected contents |
|---------|------------|------------------|
| v2026.Q3.0 | 2026-09-01 | Wave 12 artifacts + CI implementations M1–M2 |
| v2026.Q4.0 | 2026-12-01 | KG API beta + community contributions |
| v2027.Q1.0 | 2027-03-01 | Scorecard Q4 update + translations start |
| v2027.Q2.0 | 2027-06-01 | Pre-launch final prep |
| v1.0.0 | 2027-06-01 | Full v1.0 launch |

---

## Release Process

| Step | Action |
|------|--------|
| 1. Branch freeze | Create `release/vYYYY.QN.X` branch |
| 2. Final testing | Run full test suite; validate quality gates |
| 3. CHANGELOG update | Finalize CHANGELOG.md for this release |
| 4. Tag | `git tag v2026.Q3.0 -m "Release v2026.Q3.0"` |
| 5. GitHub Release | Create release with signed artifacts; attach Open Data Pack |
| 6. Announce | Post in Discussions → Announcements |

---

*Atlas Lattice Foundation · status: candidate*
