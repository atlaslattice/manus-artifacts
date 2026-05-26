# AtlasBrain Evidence Vault (candidate)

```text
STATUS: CANDIDATE WORKFLOW — NOT CANON — NOT DEPLOYABLE
```

## Layout

- `raw_exports/` = immutable source tape objects (hash required)
- `parsed_packets/` = derived packets linked to source raw export id

## Guardrails

- Parsed packets must declare `derived_from_raw: true` as a top-level field inside the parsed packet `.yaml` or `.json` file (not markdown/frontmatter), alongside `raw_export_id`.
  - Example:
    - `derived_from_raw: true`
    - `raw_export_id: raw-export-2026-05-26-001`
- Benchmark claims remain review-gated.
- Public claims remain quarantined until source is complete.
