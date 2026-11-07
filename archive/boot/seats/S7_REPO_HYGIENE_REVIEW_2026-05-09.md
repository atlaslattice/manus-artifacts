# S7 CopilotBrain — Repo Hygiene Review
# `archive/boot/seats/S7_REPO_HYGIENE_REVIEW_2026-05-09.md`

```
STATUS:    CANDIDATE REVIEW NOTE — NOT CANON
PURPOSE:   Document S7 repo-hygiene findings for human-root review and swarm handoff
SEAT:      S7 / CopilotBrain — Code Integrator / PR Swarm
PROMOTION: Requires human-root review; no auto-ratification
DATE:      2026-05-09
RUNTIME:   WORK_OUTPUT
```

> **Guardrail:** This document is a candidate/non-canon artifact. It must not be treated as
> ratified canon. No files are renamed, deleted, or finalized without human-root approval.
> Variants are preserved; path changes are documented in the path registry, not silently applied.

---

## 1. Scope

This review covers the `archive/boot/` subtree as of 2026-05-09, including:

- `archive/boot/council/` — Council-wide boot packets and schemas
- `archive/boot/gptbrain/` — S1 GPTBrain variants, synthesis artifacts, reference implementation
- `archive/boot/seats/` — Per-seat specs and credential files

Coordination issue: https://github.com/atlaslattice/manus-artifacts/issues/11

---

## 2. Summary of Findings

| Area | Finding | Severity | Action |
|------|---------|----------|--------|
| Path drift | S1 Variant C naming mismatch between index and spec | Medium | Log in path registry; do not rename |
| Missing index | `archive/boot/README.md` absent | Low | Add (additive) |
| Missing index | `archive/boot/council/README.md` absent | Low | Add (additive) |
| Missing index | `archive/boot/gptbrain/README.md` absent | Low | Add (additive) |
| Missing index | `archive/boot/seats/README.md` absent | Low | Add (additive) |
| Schema machine-readability | YAML schemas are descriptive templates, not formal validators | Medium | Add note; propose companion JSON Schema files |
| Reference impl tests | Tests existed in `reference_impl/`; adding `tests/` subdirectory for repo-root import style | Low | Add tests |
| Status enforcement | No CI to enforce STATUS headers or block accidental RATIFIED CANON language | Medium | Add CI workflow |
| PR/issue templates | No `.github/` templates | Low | Add templates |
| SUPERSEDED terminology | `DEPRECATED_SUPERSEDED` (code) vs `SUPERSEDED` (docs) inconsistency | Low | Document in path registry; harmonize in future pass |

---

## 3. Detailed Findings

### 3.1 Path Drift

`COUNCIL_BRAIN_INDEX.md` references:
```
archive/boot/gptbrain/variants/S1_VARIANT_C_CLAIM_CALIBRATION_2026-05-08.md
```

`GPTBRAIN_S1_CANONICAL_CANDIDATE_SPEC_2026-05-09.md` references:
```
archive/boot/gptbrain/variants/S1_VARIANT_C_CLAIM_CALIBRATION_POINTER_2026-05-08.md
```

Both files exist in the repo. The naming mismatch is logged in
`archive/boot/gptbrain/S1_PATH_REGISTRY_2026-05-09.md` without silent rename.

**Action taken:** No rename. Path registry is the source of truth for alias tracking.

### 3.2 Missing Directory Indexes

The following directories lacked human/machine-navigable README files:

- `archive/boot/` — root boot directory
- `archive/boot/council/` — council artifacts
- `archive/boot/gptbrain/` — S1 GPTBrain subtree
- `archive/boot/seats/` — per-seat specs

**Action taken:** README files added to each directory (additive only).

### 3.3 Schema Machine-Readability

The three YAML schema files in `archive/boot/council/schemas/`:
```
COUNCIL_PACKET_SCHEMA_2026-05-09.yaml
ROUTE_TO_SEAT_PACKET_SCHEMA_2026-05-09.yaml
CONTRADICTION_LEDGER_SCHEMA_2026-05-09.yaml
```

These are structured descriptive templates, not formal JSON Schema / OpenAPI / pykwalify validators.
They are machine-readable as YAML documents but cannot be used directly for automated validation.

**Specific inconsistency:** `required_fields` lists flat names (e.g., `source_seat`) while the
actual structure nests them under sub-objects (e.g., `source.source_seat`).

**Action taken:**
- No rewrite of existing schemas.
- Schema README added documenting purpose, validation status, and proposed companion JSON Schema path.
- CI YAML parse check added to catch malformed YAML.

**Proposed next step (S2/S4 route):** Add formal JSON Schema files beside each template.

### 3.4 Reference Implementation Tests

`dream_memory_palace_reference_impl.py` had 6 tests in `test_dream_memory_palace_reference_impl.py`.
All pass. A `tests/` subdirectory has been added with additional coverage:

- `test_reference_impl_core.py` — validation, recall/source filtering, diff, synthesize

**Existing coverage:**
- `test_remember_and_recall_project_claim` — recall + audit
- `test_contradiction_links_both_claims_and_creates_unresolved_object` — contradiction
- `test_challenge_flags_c0_unsourced_unratified_claim` — challenge report
- `test_canon_promotion_requires_human_root_approval` — canon gate
- `test_sealed_sensitive_memory_is_not_readable` — permissions
- `test_save_json_writes_memories_and_audit_log` — serialization

**New coverage (tests/ subdirectory):**
- `test_validate_empty_title_raises` — validation error
- `test_validate_empty_summary_raises` — validation error
- `test_validate_sealed_sensitive_requires_consent` — sealed permission guard
- `test_recall_require_sources_filters_uncited` — source filtering
- `test_recall_include_archived_flag` — archive inclusion toggle
- `test_diff_returns_period_summary` — diff output shape
- `test_synthesize_returns_model_not_canon_status` — synthesis output guardrail

### 3.5 Status Enforcement / CI

No CI pipeline existed to enforce:
- STATUS/PURPOSE/PROMOTION headers in candidate markdown files
- Prohibition on accidental `RATIFIED CANON` language in PR diffs
- YAML parse validity for schema files
- Reference implementation test pass

**Action taken:** `.github/workflows/s7_hygiene_checks.yml` added with:
1. Status header check on changed `.md` files in `archive/boot/`
2. Forbidden canon language check on PR diff
3. YAML parse check on all `.yaml`/`.yml` files in `archive/boot/`
4. pytest run for reference implementation

### 3.6 PR and Issue Templates

No `.github/pull_request_template.md` or issue templates existed.

**Action taken:** Added:
- `.github/pull_request_template.md` with standard checklist
- `.github/ISSUE_TEMPLATE/candidate_artifact.yml` — for new candidate artifacts
- `.github/ISSUE_TEMPLATE/review_route.yml` — for routing to review seats

### 3.7 Terminology Inconsistency

Code uses `DEPRECATED_SUPERSEDED` (in `CanonStatus` enum).
Documentation often uses `SUPERSEDED`.

**Action taken:** Logged in path registry. No code changes; harmonization is a future pass
requiring human-root review of canon status vocabulary.

---

## 4. Files That Must Remain Candidate Artifacts

These must not be ratified without human-root approval:

- `archive/boot/council/COUNCIL_WIDE_BOOT_PACKET_2026-05-09.md`
- `archive/boot/gptbrain/COUNCIL_WIDE_BRAIN_SYNTHESIS_2026-05-09.md`
- `archive/boot/gptbrain/S1_VARIANT_SYNTHESIS_MATRIX_2026-05-09.md`
- `archive/boot/gptbrain/S1_PROMOTION_CHECKLIST_2026-05-09.md`
- `archive/boot/seats/GPTBRAIN_S1_CANONICAL_CANDIDATE_SPEC_2026-05-09.md`
- All files under `archive/boot/gptbrain/variants/`
- All three YAML schema files
- `archive/boot/gptbrain/reference_impl/dream_memory_palace_reference_impl.py`

---

## 5. Routing Recommendations

### Route to S2 (Constitutional Scribe)
- Ratification language in PR/issue templates
- Canon-status wording in schema files
- CI wording around forbidden canon language
- Any GPTBRAIN_S1_CANONICAL_CANDIDATE_SPEC content before promotion

### Route to S6 (ManusBrain / Execution Agent)
- Path registry maintenance
- Contradiction ledger workflow
- Continuity/handoff decisions
- Archive hygiene passes

### Route to S4 (GeminiBrain / Engineering Simulation)
- Formal JSON Schema companion files
- Validator scripts for YAML schemas
- Test coverage expansions

---

## 6. Files Added in This Pass

All additions are additive and non-destructive:

| File | Purpose |
|------|---------|
| `archive/boot/README.md` | Boot root index |
| `archive/boot/council/README.md` | Council directory index |
| `archive/boot/gptbrain/README.md` | GPTBrain subtree index |
| `archive/boot/seats/README.md` | Seats directory index |
| `archive/boot/seats/S7_REPO_HYGIENE_REVIEW_2026-05-09.md` | This review note |
| `archive/boot/seats/S7_EXECUTION_LOG_2026-05-09.md` | Execution log |
| `.github/pull_request_template.md` | PR checklist template |
| `.github/ISSUE_TEMPLATE/candidate_artifact.yml` | Issue template |
| `.github/ISSUE_TEMPLATE/review_route.yml` | Issue template |
| `.github/workflows/s7_hygiene_checks.yml` | CI hygiene checks |
| `archive/boot/gptbrain/reference_impl/tests/conftest.py` | pytest path setup |
| `archive/boot/gptbrain/reference_impl/tests/test_reference_impl_core.py` | Additional tests |

---

## 7. No-Ratification Guardrail

```
This review note is a CANDIDATE artifact.
Nothing in this document ratifies any spec, variant, or reference implementation.
Canon promotion requires explicit human-root approval through the Council workflow.
No files were renamed or deleted.
No variants were removed.
All changes are additive and reviewable.
```

---

## 8. References

- Coordination issue: https://github.com/atlaslattice/manus-artifacts/issues/11
- S7 spec: `archive/boot/seats/COPILOTBRAIN_S7_CODE_INTEGRATOR_SPEC_2026-05-08.md`
- Path registry: `archive/boot/gptbrain/S1_PATH_REGISTRY_2026-05-09.md`
- Reference impl: `archive/boot/gptbrain/reference_impl/dream_memory_palace_reference_impl.py`
