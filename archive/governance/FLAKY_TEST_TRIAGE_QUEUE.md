---
artifact_id: TEST-POLICY-FLAKY-TEST-TRIAGE-001
title: Flaky Test Triage Queue
status: candidate
created: 2026-05-28
owner: council
tags: [testing, reliability, flaky-tests, triage]
---

# Flaky Test Triage Queue

> Defines the process for identifying, tracking, and resolving flaky tests.

status: candidate

---

## What Is a Flaky Test?

A **flaky test** is a test that produces different results (pass/fail) on the same code without any code changes. Flaky tests:
- Erode trust in the test suite
- Cause false CI failures that waste contributor time
- Hide real failures when developers start ignoring failures
- Are a smell for non-deterministic code or external dependencies in tests

---

## Flaky Test Registry

| Test | Flakiness type | Root cause | Status | Assignee |
|------|---------------|-----------|--------|---------|
| (none currently tracked) | — | — | — | — |

---

## Detection

Flaky tests are detected when:
1. A CI run fails and the test is unrelated to the PR's changes
2. A re-run of the same commit produces a different result
3. A test is quarantined as flaky by a contributor

Report a flaky test by opening a GitHub issue with the `flaky-test` label and including:
- Test name (pytest node ID)
- Failure rate (how often it fails, approximately)
- Failure output

---

## Triage Process

| Step | Action |
|------|--------|
| 1. Identify | Test fails on re-run of same commit |
| 2. Label | GitHub issue with `flaky-test` label |
| 3. Quarantine | Add `@pytest.mark.flaky(reruns=2)` using `pytest-rerunfailures` |
| 4. Investigate | Root cause analysis within 2 weeks |
| 5. Fix | Fix root cause; remove `flaky` mark |
| 6. Close | Close GitHub issue; update registry |

---

## Quarantine Implementation

Install: `pip install pytest-rerunfailures`

Mark a flaky test:
```python
import pytest

@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_something_occasionally_flaky():
    ...
```

**Quarantine SLA:** Tests may remain quarantined for a maximum of **30 days**. After 30 days, the test must either be fixed or deleted if the underlying behavior is not testable deterministically.

---

## Root Causes and Fixes

| Root cause | Fix |
|-----------|-----|
| Time-dependent test (uses `datetime.now()`) | Mock time with `freezegun` or use fixed timestamps |
| Random data without seed | Set random seed; use `hypothesis` for property-based testing |
| External service dependency | Mock the external service; use `responses` or `pytest-httpserver` |
| File system race condition | Use `tmp_path` pytest fixture; don't share state across tests |
| Test order dependency | Run with `pytest-randomly` to detect and fix ordering issues |

---

*Atlas Lattice Foundation · status: candidate*
