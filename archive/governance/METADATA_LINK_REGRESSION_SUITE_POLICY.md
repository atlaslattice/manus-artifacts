---
artifact_id: TEST-POLICY-METADATA-LINK-REGRESSION-001
title: Metadata and Link Regression Suite Policy
status: candidate
created: 2026-05-28
owner: council
tags: [testing, regression, metadata, links]
---

# Metadata and Link Regression Suite Policy

> Defines the regression test suite that guards against metadata corruption and broken links across waves of development.

status: candidate

---

## Purpose

As the repository grows, changes in one document can silently break metadata or links in others. A regression suite catches these breaks automatically.

---

## Regression Test Categories

### Category 1: Frontmatter Regression

Checks that frontmatter fields that existed before the PR still exist after it:

- No `artifact_id` removed from a document that had one
- No `status` field removed
- Status cannot regress from `ratified` to `candidate` without explicit deprecation
- `created` date cannot change on an existing document

**Tool (planned):** `tests/test_frontmatter_regression.py`

---

### Category 2: Cross-Link Regression

Checks that documents linked from other documents still exist:

- No document referenced by another document was deleted without replacement
- No anchor (`#section`) in a link was removed from the target file
- No canonical path in `CANONICAL_PATH_MAP.md` now 404s

**Tool:** `scripts/check_link_integrity.py` (planned Q3 2026)

---

### Category 3: KG Index Regression

Checks that the KG index doesn't regress:

- Total node count does not decrease (documents cannot be removed without archiving)
- Total edge count does not decrease significantly (cross-link density is maintained)
- No artifact that was in the index is missing after a PR

**Tool:** `tests/test_lattice_kg_hypercube_program.py` (extends existing suite)

---

### Category 4: Schema Regression

Checks that schema changes don't break existing valid examples:

- All existing valid examples in `tests/examples/` still validate against their schemas
- No schema removal (schemas may only be deprecated, not deleted)

**Tool:** Existing `tests/test_schema_parsing.py`

---

## Running the Full Regression Suite

```bash
# All regression-related tests
python -m pytest -q \
  tests/test_schema_parsing.py \
  tests/test_lattice_kg_hypercube_program.py \
  tests/test_frontmatter_regression.py \  # planned
  --tb=short
```

---

## Regression Failure Response

| Category | Failure type | Response |
|----------|-------------|---------|
| Frontmatter | Missing field | PR author must restore or explicitly migrate |
| Cross-link | Broken internal link | Fix the link or create a redirect stub |
| KG Index | Node count decreased | Verify deletion was intentional; add quarantine record |
| Schema | Previously valid example now fails | Schema change is breaking — bump version |

---

*Atlas Lattice Foundation · status: candidate*
