# Artifact Provenance Header Template

```text
STATUS: CANDIDATE TEMPLATE — NOT CANON
```

Use this header for major artifacts to standardize governance, provenance, and
ratification metadata.

## Required header block

```yaml
artifact_id: ARTIFACT-UNIQUE-ID
title: Human-readable artifact title
status: candidate # candidate | reviewed | ratified | superseded | deprecated
created_utc: 2026-05-28T00:00:00Z
updated_utc: 2026-05-28T00:00:00Z
owners:
  - @atlaslattice
domain: governance # governance | spec | implementation | research | archive
source_uri:
  - https://github.com/atlaslattice/manus-artifacts/path/to/source
provenance:
  extraction_method: human-authored
  evidence_links:
    - path/or/url/to/supporting/evidence
  confidence: medium # low | medium | high
governance:
  canon_status: NOT_CANON
  ratification_event_id: null
  adjudicator: null
  trust_state: pending
```

## Required notes

- If `status: ratified`, `ratification_event_id` and `adjudicator` must be set.
- If artifact replaces another, include a supersession note and backlink.
- Deprecated artifacts are retained for lineage and must not be hard-deleted.

