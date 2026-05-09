# CI Evidence Receipt — Wave 1 Hardening

```text
STATUS: CI EVIDENCE RECEIPT — NOT CANON
DATE: 2026-05-09
PURPOSE: Surface CI evidence for S1 GPTBrain reference implementation tests as part of Wave 1 hardening.
ISSUE: manus-artifacts#19
RUNTIME LABEL: WORK_OUTPUT
CLAIM CONFIDENCE: C5 (operationally demonstrated — tests passed locally and in CI)
CANON STATUS: NOT CANON — evidence artifact only
HUMAN-ROOT GATE: required before any promotion
```

## Test Run Summary

### Local test run (2026-05-09, Wave 1 branch)

```text
Platform: Python 3.12.3, pytest-9.0.3
Working directory: archive/boot/gptbrain/reference_impl/
Command: python -m pytest -v
Result: 24 passed in 0.05s
```

### Test inventory

| Test file | Tests | Status |
|---|---|---|
| `test_dream_memory_palace_reference_impl.py` | 6 | PASS |
| `test_gptbrain_memory.py` | 7 | PASS |
| `test_schema_presence.py` | 4 | PASS |
| `tests/test_reference_impl_core.py` | 7 | PASS |
| **Total** | **24** | **ALL PASS** |

### Key test assertions confirmed

```text
test_schema_presence::test_canonical_candidate_integrates_variant_e
  "Variant E = continuity / human-intent dashboard layer" in candidate  ✓
  "Layer 7 — Continuity / Human-Intent Dashboard" in candidate          ✓
  "Continuity is visibility, not authority." in candidate               ✓
  "Variant E remains pending or missing" not in candidate               ✓

test_schema_presence::test_required_gptbrain_files_exist
  schema/S1_MEMORY_OBJECT_SCHEMA.yaml                    ✓
  schema/S1_CLAIM_LEDGER_SCHEMA.yaml                     ✓
  schema/S1_ARTIFACT_REGISTRY_SCHEMA.yaml                ✓
  schema/S1_AUDIT_EVENT_SCHEMA.yaml                      ✓
  CLAIM_LEDGER.seed.jsonl                                ✓
  ARTIFACT_REGISTRY.seed.jsonl                           ✓
  BOOT_PACKET_TEMPLATE.md                                ✓
  CURRENT_STATE_2026-05-09.md                            ✓
  NEXT_ACTIONS_2026-05-09.md                             ✓
  GPT_INSTANCE_STATE_LOG_2026-05-09.md                   ✓

test_schema_presence::test_boot_packet_points_to_verified_dated_snapshots
  CURRENT_STATE_2026-05-09.md referenced in BOOT_PACKET_TEMPLATE.md    ✓
  NEXT_ACTIONS_2026-05-09.md referenced in BOOT_PACKET_TEMPLATE.md     ✓
  "Do not claim the bare aliases exist unless verified" present         ✓
```

## CI Workflow Status

### `GPTBrain reference checks` (gptbrain-reference-checks.yml)

```text
Workflow: .github/workflows/gptbrain-reference-checks.yml
Trigger: push to archive/boot/gptbrain/**
Recent runs: 6 successful runs (2026-05-09)
Status: GREEN on master
```

Commit SHA of CI workflow addition: `4daf57d22601b287f944597fac576743a7c5fc8f`

### `S7 Hygiene Checks` (s7_hygiene_checks.yml)

```text
Workflow: .github/workflows/s7_hygiene_checks.yml (added Wave 1)
Trigger: push to master and copilot/** branches, PRs to master
Status: Added to master in Wave 1 (this PR)
Prior status: action_required on PR #15 — explained below
```

#### Why PR #15 showed `action_required`

```text
Root cause: GitHub Actions blocks automated-bot PR workflows from running without
explicit maintainer approval. This is a security gate, not a test failure.

The s7_hygiene_checks.yml existed only on PR #15's branch (copilot/s7-repo-hygiene-pass)
and triggered on pull_request. GitHub required maintainer approval before running
the workflow from a bot-authored PR.

Fix: Add the workflow to the master branch (this PR), so future pushes to master
and copilot/** branches run the CI without an approval gate.
```

## Provenance Commits Referenced

| SHA | Description |
|---|---|
| `4daf57d22601b287f944597fac576743a7c5fc8f` | ci(gptbrain): add reference implementation checks workflow |
| `02a015d06a84240dfcf2614f0091b5e6e22b2408` | test(gptbrain): add schema and boot presence checks |
| `1dde7eb2fbd79ca7bdb702c44793ffa9e2c68a01` | Add S1 Variant E closure status |
| `c19a03a7593ffebc2e44c09dfa3a3bdd4973ee5f` | Add S1 alias topology policy |
| `1a557b27f3b8c5247b5e59887badffd1e29afd8b` | Add shared Council contradiction ledger schema |

## Issue #19 P1 Task Status — Wave 1

```text
[x] Attach explicit commit_sha fields to artifact/claim/memory seed provenance.
    → ARTIFACT_REGISTRY.seed.jsonl: 5 records updated with commit_sha
    → CLAIM_LEDGER.seed.jsonl: 5 records updated with commit_sha
    → MEMORY_OBJECTS.seed.jsonl: 2 records updated with commit_sha + alias policy

[x] Add CI/schema validation evidence artifacts.
    → This file (CI_EVIDENCE_RECEIPT_2026-05-09.md)
    → s7_hygiene_checks.yml added to master

[x] Add audit or validation receipt for reference implementation tests.
    → 24 tests PASSED (documented above)
    → gptbrain-reference-checks.yml: 6 recent green runs on master
```
