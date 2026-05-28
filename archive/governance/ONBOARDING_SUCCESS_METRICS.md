---
artifact_id: DX-POLICY-ONBOARDING-SUCCESS-METRICS-001
title: Onboarding Success Metrics
status: candidate
created: 2026-05-28
owner: council
tags: [developer-experience, onboarding, metrics, measurement, community]
---

# Onboarding Success Metrics

> Defines the metrics used to measure the health and effectiveness of the Atlas Lattice contributor onboarding experience.

status: candidate

---

## Why Measure Onboarding?

If the onboarding experience is unclear or frustrating, new contributors leave before making a contribution. Metrics help identify where the funnel breaks down.

---

## Onboarding Funnel

```
Repository visitors
    → README readers (GitHub traffic)
       → First issue openers
          → First PR openers
             → First PR merged
                → Second PR merged (retained contributor)
```

Each drop-off point is a potential area for improvement.

---

## Metrics Table

| Metric | Target | Source |
|--------|--------|--------|
| Time to first merged PR (median) | ≤ 14 days from first issue | GitHub API / manual tracking |
| First-PR merge rate | ≥ 60% of first PRs opened | GitHub API |
| Contributor retention (2nd PR rate) | ≥ 40% of first-time contributors open a 2nd PR | GitHub API |
| Fast Lane issue fill rate | ≥ 80% of Fast Lane issues claimed within 30 days | Manual |
| Welcome message response rate | ≥ 90% of welcome messages receive ≥ 1 follow-up action | Manual |
| Onboarding doc clarity rating | ≥ 4/5 stars in annual survey | Survey |

---

## Data Collection

| Metric | Method |
|--------|--------|
| Funnel drop-off | GitHub Insights → Traffic page + issue/PR analytics |
| Time to first PR merge | Export from GitHub API: `gh api repos/atlaslattice/manus-artifacts/pulls` |
| Retention | Cross-reference contributor list: new last quarter vs. active this quarter |

---

## Annual Onboarding Survey

Once/year, post a brief survey in GitHub Discussions:

1. How easy was it to make your first contribution? (1–5)
2. Which resources did you use? (README / FAQ / Glossary / other)
3. What was the biggest barrier? (free text)
4. What would you improve? (free text)

Results are published in the annual quality report.

---

## Improvement Cycle

1. Measure metrics quarterly
2. Identify the funnel step with the biggest drop-off
3. Hypothesize one improvement to that step
4. Ship the improvement (update docs, create Fast Lane issue, etc.)
5. Re-measure in the next quarter

---

*Atlas Lattice Foundation · status: candidate*
