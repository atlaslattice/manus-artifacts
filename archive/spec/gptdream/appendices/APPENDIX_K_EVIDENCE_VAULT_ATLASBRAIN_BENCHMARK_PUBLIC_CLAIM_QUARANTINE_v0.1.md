# Appendix K — Evidence Vault (AtlasBrain / benchmark / public-claim quarantine) v0.1

```text
STATUS: CANDIDATE APPENDIX — NOT CANON — NOT DEPLOYABLE
```

## Purpose

Separate raw evidence, evaluator reactions, benchmark claims, and public claims.

## Required mechanics

- Store raw exports separately from parsed packets.
- Hash raw exports.
- Create evidence packets.
- Route benchmark claims to review.
- Quarantine public claims until source complete.

## Definition of done

- Raw tape is preserved.
- Parsed packet is labeled as derived.
- Benchmark claim cannot publish without evidence packet + review.
- Public claim remains quarantined until `source_completeness = complete`.
