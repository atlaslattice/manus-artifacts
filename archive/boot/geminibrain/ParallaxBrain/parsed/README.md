# ParallaxBrain parsed/

```text
STATUS: CANDIDATE DERIVED-VIEW LANE — NOT CANON
DEPLOYMENT: no
AUTHORITY: none
RUNTIME: not implemented
```

## Purpose

This lane stores derived views, chunk summaries, and structured parses from raw ParallaxBrain source material.

## Rule

```text
Parsed views derive from raw.
Parsed views may not replace raw.
Every parsed view must point back to a raw source or source receipt.
```

## Required fields

```text
raw_source_ref
derivation_method
section_summary
schema_alignment_status
review_hold_flag
```
