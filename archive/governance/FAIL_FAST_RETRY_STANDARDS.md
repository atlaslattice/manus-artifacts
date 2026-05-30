---
artifact_id: CICD-POLICY-FAIL-FAST-RETRY-001
title: Fail-Fast and Retry Standards
status: candidate
created: 2026-05-28
owner: council
tags: [ci-cd, reliability, fail-fast, retry, standards]
---

# Fail-Fast and Retry Standards

> Defines how CI/CD workflows handle failures — when to fail immediately vs retry, and how to prevent cascading failures.

status: candidate

---

## Fail-Fast Policy

### Default: fail-fast enabled for test matrices

For test matrices (e.g., testing across multiple Python versions), the `fail-fast: true` setting stops all matrix jobs as soon as any one job fails. This is the default and preferred setting — it saves CI minutes and gives faster feedback.

```yaml
strategy:
  fail-fast: true
  matrix:
    python-version: ["3.11", "3.12"]
```

**Exception:** If matrix jobs are truly independent and all results are needed for a complete report (e.g., cross-platform compatibility testing), use `fail-fast: false` with an explanatory comment.

---

### Step-level fail-fast

All shell steps run with `-e` semantics by default (exit on first error). Explicitly override with `|| true` only when a step failure is acceptable and documented:

```yaml
# Good: explicit intent documented
- run: python scripts/check_optional_tool.py || true  # optional check; failure is non-blocking

# Bad: silent error suppression without documentation
- run: rm -f /tmp/cache || true
```

---

## Retry Policy

### When to retry

| Scenario | Retry? | Max retries |
|----------|--------|------------|
| Network timeout (pip install, git fetch) | Yes | 3 |
| External API call in test | Yes | 2 |
| Transient GitHub API rate limit | Yes | 3 (with exponential backoff) |
| Test failure (deterministic) | No | 0 |
| Script logic error | No | 0 |

### Retry implementation

Use the `nick-fields/retry` action or inline retry loops for transient failures:

```yaml
- name: Install dependencies (with retry)
  uses: nick-fields/retry@ce71cc2b4483a0b79e04b5d79b4d67e2bae18ae3  # v3.0.0
  with:
    timeout_minutes: 5
    max_attempts: 3
    command: pip install -r requirements.txt
```

---

## Cascading Failure Prevention

### Job dependency ordering

Use `needs:` to express job dependencies and prevent downstream jobs from running on upstream failure:

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps: ...

  test:
    needs: lint
    runs-on: ubuntu-latest
    steps: ...
```

### Required status checks

All jobs that block merge must be configured as required status checks in branch protection settings. Skipped jobs should not count as passing.

---

## Notification Policy

| Failure type | Notification |
|-------------|-------------|
| Main branch CI failure | GitHub check failure visible on commit |
| Scheduled scan failure | GitHub issue auto-opened (see Drift Detection Policy) |
| Security gate failure | GitHub check failure + label `security` on PR |

No email or Slack notifications are configured — GitHub UI is the notification surface.

---

*Atlas Lattice Foundation · status: candidate*
