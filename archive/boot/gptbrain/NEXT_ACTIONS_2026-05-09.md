---
artifact_id: ARTIFACT-ARCHIVE-BOOT-GPTBRAIN-NEXT-ACTIONS-2026-05-09-MD-2026-05-29
title: S1 GPTBrain — Next Actions
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# S1 GPTBrain — Next Actions

```text
STATUS: NEXT ACTIONS — NOT CANON
ISSUE: manus-artifacts#12
DATE: 2026-05-09
SEAT: S1 GPTBrain
```

## Priority 0 — preserve boundaries

```text
Do not ratify canon by code.
Do not delete variants.
Do not silently overwrite lineage.
Do not treat memory as execution authority.
```

## Priority 1 — patch canonical candidate

Patch:

```text
archive/boot/seats/GPTBRAIN_S1_CANONICAL_CANDIDATE_SPEC_2026-05-09.md
```

to integrate Variant E as:

```text
Continuity / Human-Intent Dashboard layer
```

and replace any stale language implying Variant E is missing.

## Priority 2 — validate scaffold

Run the reference implementation against seed ledgers:

```bash
cd archive/boot/gptbrain/reference_impl
python gptbrain_memory.py claims --confidence C3
python gptbrain_memory.py trace --claim-id S1-CLAIM-2026-0509-0001
python gptbrain_memory.py challenge --claim-id S1-CLAIM-2026-0509-0001
```

Expected behavior:

```text
- claims load from CLAIM_LEDGER.seed.jsonl
- trace returns evidence_refs and missing_evidence
- challenge refuses overclaim paths and routes to review where needed
```

## Priority 3 — add tests

Create a small test file after the first local run:

```text
archive/boot/gptbrain/reference_impl/test_gptbrain_memory.py
```

Minimum tests:

```text
[ ] C0 claims cannot be asserted as facts
[ ] ratified_canon without ratified review is challenged
[ ] missing evidence appears in ChallengeReport
[ ] diff identifies added/removed/changed records
[ ] empty/missing ledgers fail softly where appropriate
```

## Priority 4 — update Issue #12

After scaffold validation, update Issue #12 with:

```text
- files created
- tests passed / not yet run
- remaining gaps
- next implementation target
```

## Priority 5 — choose storage path

After scaffold is stable, decide whether the next substrate should be:

```text
A. JSONL-only for archive portability
B. SQLite for local runnable memory
C. Postgres + pgvector for production substrate
D. Kuzu / Neo4j for claim graph traversal
```

Recommended next step:

```text
JSONL + tests first, SQLite second, graph/database later.
```
