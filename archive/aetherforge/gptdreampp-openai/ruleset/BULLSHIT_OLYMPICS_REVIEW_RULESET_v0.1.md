# Bullshit Olympics Review Ruleset v0.1 (CANDIDATE)

Purpose: detect overclaim, false authority, or canon drift before merge.

## Required checks

- Reject phrases implying deployed authority without ratification receipts.
- Reject canon claims when `canon_status != RATIFIED_CANON`.
- Reject records with missing provenance lineage or missing receipt URI.
- Require explicit reviewer notes when review status is FAIL.

## Blocking outcomes

Any FAIL in this review lane blocks merge for touched records.
