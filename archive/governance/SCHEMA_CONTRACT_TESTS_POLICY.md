---
artifact_id: TEST-POLICY-SCHEMA-CONTRACT-TESTS-001
title: Schema Contract Tests Policy
status: candidate
created: 2026-05-28
owner: council
tags: [testing, schema, contracts, compatibility]
---

# Schema Contract Tests Policy

> Defines how schema contract tests ensure that producers and consumers of schemas remain compatible.

status: candidate

---

## What Are Contract Tests?

A **schema contract test** verifies that:
1. A producer (something that creates data conforming to a schema) produces valid output
2. A consumer (something that reads schema-conforming data) correctly processes it
3. The schema itself matches what both sides expect

This is distinct from unit tests (which test isolated functions) — contract tests focus on the interface boundary.

---

## Contracts in This Repository

| Schema | Producer | Consumer | Contract test file |
|--------|---------|---------|------------------|
| `schemas/atlas_orcs/v0_1/session_packet.yml` | Reference impl encoder | Reference impl decoder | `reference_impl/atlas_orcs/tests/test_compatible.py` |
| `schemas/o_ai/v0_1/message.yml` | OAI message builder | Schema parser | `tests/test_oai_packet_examples.py` |
| `schemas/native_thread/v0_1/thread_packet.yml` | Thread encoder | Thread decoder | `tests/test_native_thread_packet_examples.py` |
| YAML frontmatter schema | Contributor (document author) | `check_docs_layout_structure.py` | `tests/test_schema_parsing.py` |

---

## Contract Test Requirements

Every schema in `schemas/` must have:

1. **At least one valid example** — a JSON/YAML file in `tests/examples/` that conforms to the schema
2. **At least one invalid example** — a JSON/YAML file in `tests/examples/invalid/` that should fail validation
3. **A contract test** — a pytest test that validates the valid example passes and the invalid example fails

---

## Adding a New Schema Contract

When adding a new schema:

1. Create the schema at `schemas/{namespace}/{version}/{name}.yml`
2. Create `tests/examples/{name}_valid.json` with a valid example
3. Create `tests/examples/invalid/{name}_invalid.json` with an invalid example
4. Add a test in `tests/test_schema_parsing.py`:

```python
def test_{name}_valid():
    schema = load_schema("schemas/{namespace}/{version}/{name}.yml")
    example = load_example("tests/examples/{name}_valid.json")
    assert validate(example, schema) == True

def test_{name}_invalid():
    schema = load_schema("schemas/{namespace}/{version}/{name}.yml")
    example = load_example("tests/examples/invalid/{name}_invalid.json")
    assert validate(example, schema) == False
```

---

## Breaking Change Policy

A **breaking change** to a schema is any change that causes previously valid data to become invalid.

| Change type | Breaking? | Required action |
|------------|---------|----------------|
| Adding an optional field | No | Update examples; add contract test for new field |
| Adding a required field | Yes | Bump schema version; migration guide required |
| Removing a field | Yes | Bump schema version; deprecate old version |
| Changing field type | Yes | Bump schema version; migration guide required |
| Renaming a field | Yes | Bump schema version; migration guide required |

---

*Atlas Lattice Foundation · status: candidate*
