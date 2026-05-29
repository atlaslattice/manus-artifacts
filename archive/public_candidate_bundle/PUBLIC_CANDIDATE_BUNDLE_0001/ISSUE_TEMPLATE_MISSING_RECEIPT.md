# Missing Receipt Issue Template — Candidate

```text
STATUS: ISSUE TEMPLATE CANDIDATE — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
```

## Missing receipt report

```yaml
missing_receipt_report:
  target_artifact:
  target_surface:
  missing:
    - source_url
    - raw_export
    - hash
    - timestamp
    - author/source
    - review_packet
  consequence: hold | quarantine | review_only | block
  suggested_review_lane:
  public_safe_summary:
```

## Checklist

- [ ] Missing item is specific
- [ ] Target artifact is identified
- [ ] Consequence is declared
- [ ] No accusation implied
- [ ] Missing receipt can become a graph node

## Keeper

```text
Missing is not failure. Missing is a node.
```
