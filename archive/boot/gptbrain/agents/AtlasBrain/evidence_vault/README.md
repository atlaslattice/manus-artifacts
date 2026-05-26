# AtlasBrain Evidence Vault (candidate)

```text
STATUS: CANDIDATE WORKFLOW — NOT CANON — NOT DEPLOYABLE
```

## Layout

- `raw_exports/` = immutable source tape objects (hash required)
- `parsed_packets/` = derived packets linked to source raw export id

## Guardrails

- Parsed packets must declare `derived_from_raw: true` in packet metadata (YAML/JSON payload field), alongside `raw_export_id`.
- Benchmark claims remain review-gated.
- Public claims remain quarantined until source is complete.
