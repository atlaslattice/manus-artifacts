# Schema Patch Issue Template — Candidate

```text
STATUS: ISSUE TEMPLATE CANDIDATE — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
```

## Schema patch request

```yaml
schema_patch_request:
  schema_name:
  schema_path:
  field_or_rule:
  proposed_change:
  reason:
  compatibility_risk: low | medium | high
  migration_needed: true | false | unknown
  example_before:
  example_after:
  review_lane:
```

## Checklist

- [ ] Existing schema path identified
- [ ] Proposed field/rule is explicit
- [ ] Compatibility risk declared
- [ ] Example before/after included when possible
- [ ] Patch does not imply canon/deployment/authority

## Keeper

```text
Patch the schema without crowning the schema.
```
