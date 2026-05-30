---
artifact_id: GOV-DOCS-LINT-QUALITY-GATES-001
title: Docs Lint Quality Gates Policy
status: candidate
created: 2026-05-28
owner: council
tags: [documentation, quality-gates, lint, ci, automation]
---

# Docs Lint Quality Gates Policy

> Defines the automated lint checks applied to all documentation in the repository.

status: candidate

---

## Overview

Consistent, well-structured documentation is enforced through automated quality gates in CI. This policy defines the gates, their thresholds, how to interpret failures, and how to request exceptions.

---

## Active Quality Gates

### Gate 1: Markdown Structure Lint

**Tool:** `scripts/check_docs_layout_structure.py`
**CI Workflow:** `.github/workflows/lattice-kg-quality-gates.yml`
**Trigger:** Every pull request touching `docs/`, `archive/`, or `*.md` files

**Checks performed:**
- All `archive/governance/` documents have YAML frontmatter with `title`, `status`, `artifact_id`, `created`
- All top-level `docs/` files have at least one `##` section header
- No document in `archive/` is completely empty (0 bytes or whitespace only)
- README.md in each top-level folder is present and non-empty

**Failure action:** PR blocked until resolved.

---

### Gate 2: AI Evidence Integrity

**Tool:** `scripts/check_ai_evidence_integrity.py`
**CI Workflow:** `.github/workflows/lattice-kg-quality-gates.yml`
**Trigger:** Every pull request touching `archive/` files

**Checks performed:**
- AI evidence artifacts contain required provenance fields
- No AI evidence file references a future date
- AI evidence logs follow the TIDELOCKBrain naming convention

**Failure action:** PR blocked until resolved.

---

### Gate 3: GPTBrain Reference Checks

**Tool:** `archive/boot/gptbrain/reference_impl/run_checks.sh`
**CI Workflow:** `.github/workflows/gptbrain-reference-checks.yml`
**Trigger:** Push or PR on any branch touching `archive/boot/gptbrain/`

**Checks performed:**
- Full pytest suite passes (`python -m pytest -q`)
- Schema presence validated
- Reference implementation compatible tests pass

**Failure action:** PR blocked until resolved.

---

### Gate 4: KG Quality Gates

**Tools:** `scripts/build_lattice_global_index.py`, `scripts/validate_lattice_quality_gates.py`, `python -m pytest -q tests/test_lattice_kg_hypercube_program.py`
**CI Workflow:** `.github/workflows/lattice-kg-quality-gates.yml`
**Trigger:** Every pull request on the main branch

**Checks performed:**
- Global KG index can be built without errors
- Quality gate thresholds met (link density, orphan artifact count, frontmatter coverage)
- KG hypercube test suite passes

**Failure action:** PR blocked until resolved.

---

### Gate 5: Boring Machine Validation

**Tools:** `python -m pytest -q tests/test_schema_parsing.py tests/adversarial/ tests/test_oai_packet_examples.py tests/test_native_thread_packet_examples.py reference_impl/atlas_orcs/tests/test_compatible.py archive/boot/gptbrain/reference_impl/test_schema_presence.py archive/product/receipt_habitat_v0_1/tests/test_receipt_habitat_v0_1.py`
**CI Workflow:** `.github/workflows/boring-machine-validation.yml`
**Trigger:** Every push and PR

**Checks performed:**
- Schema parsing tests
- Adversarial protocol tests (T01–T12)
- Native thread and OAI packet format validation
- Receipt habitat reference tests

**Failure action:** PR blocked until resolved.

---

## Planned Future Gates

| Gate | Description | Target |
|------|-------------|--------|
| Gate 6 | Readability threshold scan (Flesch-Kincaid) | Q3 2026 |
| Gate 7 | Cross-link density enforcement | Q3 2026 |
| Gate 8 | Terminology consistency scanner (per TERMINOLOGY_CONSISTENCY_REPORT.md) | Q4 2026 |
| Gate 9 | CHANGELOG update enforcement | Q4 2026 |

---

## Running Gates Locally

```bash
# Gate 1 + 2: Docs layout and AI evidence
python scripts/check_docs_layout_structure.py
python scripts/check_ai_evidence_integrity.py

# Gate 3: GPTBrain reference checks
cd archive/boot/gptbrain/reference_impl && bash run_checks.sh

# Gate 4: KG quality gates
python scripts/build_lattice_global_index.py
python scripts/validate_lattice_quality_gates.py
python -m pytest -q tests/test_lattice_kg_hypercube_program.py

# Gate 5: Full boring machine validation
python -m pytest -q tests/test_schema_parsing.py tests/adversarial tests/test_oai_packet_examples.py tests/test_native_thread_packet_examples.py reference_impl/atlas_orcs/tests/test_compatible.py archive/boot/gptbrain/reference_impl/test_schema_presence.py archive/product/receipt_habitat_v0_1/tests/test_receipt_habitat_v0_1.py
```

---

## Exception Process

| Scenario | Process |
|----------|---------|
| Intentional empty stub file | Add `<!-- stub: intentional -->` comment; PR description must explain |
| Prototype branch (not targeting main) | Gate 4 may be waived; Gates 1, 2, 3, 5 remain required |
| Emergency hotfix | Any gate may be bypassed with `[HOTFIX]` in PR title + @atlaslattice approval |

---

## Governance

| Role | Responsibility |
|------|---------------|
| PR author | Resolve all blocking gate failures before requesting review |
| Reviewers | Never approve PRs with unresolved gate failures without an exception |
| @atlaslattice | Approves gate policy changes; sole authority for emergency bypass |

---

*Atlas Lattice Foundation · status: candidate*
