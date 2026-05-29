# State Snapshot Staleness Policy

```text
STATUS: STALENESS POLICY — NOT CANON
DATE: 2026-05-26
CANON STATUS: candidate
AUTHORITY: freshness signaling policy
```

## Policy

- State snapshot docs must declare `DATE` and `STALE AFTER`.
- If current UTC date is past `STALE AFTER`, mark doc as review-required.
- Prefer weekly refresh for operational snapshots and monthly refresh for strategy snapshots.

## Review-required marker

Use this marker when stale:

```text
FRESHNESS: STALE — REVIEW REQUIRED
```
