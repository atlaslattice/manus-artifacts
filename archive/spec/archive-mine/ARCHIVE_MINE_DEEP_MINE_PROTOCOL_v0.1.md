# Archive Mine — Deep Mine / Fossilbranch Excavation Protocol v0.1

```text
STATUS: CANDIDATE WORKING SPEC — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
ROLE: Aetherforge Deep Mine / Fossilbranch Excavation
```

## Purpose
Ingest old Notion/Drive/GitHub/website source piles without allowing stale or contaminated material to become authority.

## Scope
This protocol covers:
- source inventory construction
- artifact status assignment
- contamination and quarantine controls
- candidate delta extraction
- website canon recoverability package assembly

## Required status classes
Every ingested artifact must be assigned exactly one primary status:
- raw
- parsed
- candidate
- quarantined
- superseded
- ratified

## Contamination boundary
- Contaminated artifacts must be preserved.
- Contaminated artifacts must be blocked from authority effects.
- Ratification cannot be inferred from ingestion, parsing, or indexing.

## Candidate delta boundary
Candidate deltas are review artifacts only and must not self-promote to canon or deploy authority.

## Canon recoverability boundary
Website canon must be reconstructable via receipts and hashes with a complete audit trail.

## Definition of done mapping
- Old material is searchable: source inventory and index artifacts exist.
- Old material is not automatically trusted: default non-ratified status and explicit trust fields.
- Contaminated material is preserved but blocked from authority: contamination flags + authority_blocked guardrail.
- Website canon is recoverable and auditable: recoverability package requires snapshot receipts and audit events.
