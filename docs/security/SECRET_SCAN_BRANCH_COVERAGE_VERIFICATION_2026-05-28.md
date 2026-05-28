---
artifact_id: DOC-SECRET-SCAN-BRANCH-COVERAGE-2026-05-28
title: Secret Scan Workflow Branch Coverage Verification
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---
# Secret Scan Workflow Branch Coverage Verification

## Summary

The repository's secret-scan workflow currently triggers on both `push` and `pull_request` without branch filters, which means it covers all branches by default.

## Evidence

Source workflow: [`/.github/workflows/secret-scan.yml`](../../.github/workflows/secret-scan.yml)

```yaml
on:
  push:
  pull_request:
```

## Coverage Interpretation

| Event | Branch coverage | Notes |
|---|---|---|
| `push` | All branches | No `branches` or `paths-ignore` filter present |
| `pull_request` | All PR base branches | No branch restriction present |

## Operational Notes

- `actions/checkout@v4` is configured with `fetch-depth: 0`, enabling full-history scanning.
- `gitleaks/gitleaks-action@v2` runs on every push/PR event under current config.
- No scheduled scan exists yet; this verification covers branch/event scope only.

## Recommendation

Current branch coverage is sufficient for baseline protection. A future hardening pass may add `schedule` or `workflow_dispatch` if periodic full-repo rescans are desired.
