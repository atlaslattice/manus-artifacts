# GitHub Adapter

```text
STATUS: ADAPTER SCAFFOLD — NOT CANON
MODE: WORK_OUTPUT
PURPOSE: make GitHub API access explicit, auditable, and mode-gated
HUMAN_ROOT_GATE: required before live write actions
```

## Summary

This directory defines a candidate GitHub adapter lane for GPTBrain / Council Brain work.

The adapter exists to prevent GitHub access from becoming invisible ambient authority.

## Default mode

```text
DRY_RUN_ONLY
```

## Modes

```text
REPO_TRACE_ONLY — repo metadata and references only
DRY_RUN_ONLY    — preview/receipt only, no mutation
MOCK_GITHUB     — deterministic fake responses for tests
LIVE_GITHUB     — blocked by default; requires explicit approval
```

## Files

```text
GITHUB_RUNTIME_ADAPTER_SPEC_2026-05-09.md
source_manifest.yaml
github_adapter.py          # proposed scaffold
test_github_adapter.py     # proposed tests
```

## One-line rule

```text
GitHub should be wired as an auditable adapter, not as invisible ambient authority.
```

## Guardrails

```text
GitHub readable is not GitHub writable.
Token present is not action authorized.
Configured API is not approved mutation.
```

## Minimum future tests

```text
- token missing -> clear blocked receipt
- DRY_RUN_ONLY write -> preview/blocked, no mutation
- MOCK_GITHUB -> deterministic fake output
- LIVE_GITHUB without approval -> blocked
- receipts never include token values
```
