# Raw Export Is Not Summary

```text
STATUS: STANDARD CANDIDATE — NOT CANON — NON-DEPLOYABLE
AUTHORITY: none
PURPOSE: prevent summaries, parser outputs, and model interpretations from being mistaken for raw lineage
```

## Rule

A summary is not a raw transcript.

A parser output is not a raw transcript.

A model interpretation is not a raw transcript.

A memory packet is not a raw transcript.

## Required distinction

Every source packet should declare:

```yaml
raw_export_status:
  allowed:
    - not_exported
    - partial_export
    - full_raw_export_attached
    - full_raw_export_hashed
    - redacted_raw_export_attached
    - unavailable
```

## Fossilization rule

No artifact may claim full fossilization unless it has:

```text
raw export
stable source path
capture timestamp
hash or stable ID
privacy/status review
source manifest
```

## Keeper

```text
Raw if possible.
Summary if necessary.
Receipts always.
Canon never without review.
```