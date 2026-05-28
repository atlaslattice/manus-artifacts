---
artifact_id: CICD-POLICY-SCHEMA-VALIDATION-001
title: Schema Validation in CI Policy
status: candidate
created: 2026-05-28
owner: council
tags: [ci-cd, schema, validation, quality-gates]
---

# Schema Validation in CI Policy

> Defines how YAML and JSON schemas are validated in CI to prevent malformed artifacts from entering the repository.

status: candidate

---

## Schemas to Validate

| Schema set | Location | Validates |
|-----------|---------|----------|
| Atlas/ORCS schemas | `schemas/atlas_orcs/v0_1/` | Session and artifact packets |
| O_AI schemas | `schemas/o_ai/v0_1/` | OpenAI-compatible payloads |
| Native thread schema | `schemas/native_thread/v0_1/` | Thread packet format |
| YAML frontmatter | Inline in check script | Artifact frontmatter fields |

---

## Current Validation (Active)

The boring machine validation suite already validates schemas:

```bash
python -m pytest -q tests/test_schema_parsing.py tests/adversarial tests/test_oai_packet_examples.py tests/test_native_thread_packet_examples.py reference_impl/atlas_orcs/tests/test_compatible.py
```

This runs on every push via `.github/workflows/boring-machine-validation.yml`.

---

## Planned Additional Validation (Q3 2026)

`scripts/validate_schemas.py` will add:

1. **JSON Schema meta-validation** — verify that each schema in `schemas/` is itself a valid JSON Schema (draft-07)
2. **Cross-schema reference check** — verify that `$ref` references within schemas resolve
3. **Frontmatter schema validation** — validate all `archive/governance/` frontmatter against the YAML frontmatter schema defined in `schemas/atlas_orcs/v0_1/frontmatter.yml`
4. **Example file validation** — validate all files in `tests/examples/` against their declared schema

---

## Schema Versioning Policy

| Rule | Detail |
|------|--------|
| Schemas are versioned | `v0_1`, `v0_2`, etc. — directory-versioned |
| Breaking changes require new version | Any change that invalidates existing valid documents is a breaking change |
| Old versions are kept | Previous versions remain in `schemas/` with a `deprecated: true` field |
| Version bumps require changelog entry | Breaking and minor changes both get CHANGELOG entries |

---

## Adding a New Schema

1. Create the schema YAML in the appropriate versioned directory
2. Add at least one valid example and one invalid example to `tests/`
3. Add a pytest test that validates both examples
4. Add the schema to `schemas/README.md`
5. Run `python scripts/validate_schemas.py` locally to verify

---

## Failure Response

| Failure | Owner | SLA |
|---------|-------|-----|
| Schema meta-validation failure | Schema author | Before merge |
| Example file fails validation | Example author | Before merge |
| Frontmatter validation failure | Doc author | Before merge |

---

*Atlas Lattice Foundation · status: candidate*
