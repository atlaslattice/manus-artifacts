# GPTDream++ Provenance-First Ruleset v0.1

```text
STATUS: RULESET DRAFT — CANDIDATE — NOT CANON
```

## Core rules

1. No artifact promotion without source path + hash + attribution.
2. No dream/play delta treated as verified fact by default.
3. No canon claim without explicit ratification metadata.
4. No deployment claim without executable receipt evidence.
5. Claude-touched governance material must be explicitly flagged and reviewed.
6. Contradictions must be preserved and routed, not silently collapsed.
7. Public summary language must be translation-safe and non-overclaiming.

## Required metadata

- artifact_id
- source_system + source_path
- hash + hash_algo
- attribution (author + model lane)
- canon_status
- review flags

## Review gates

- Gate A: receipt completeness
- Gate B: contamination/authority drift check
- Gate C: overclaim and deployment-claim check
- Gate D: human-root adjudication for any promotion
