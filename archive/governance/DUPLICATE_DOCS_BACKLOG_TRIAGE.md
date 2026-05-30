# Duplicate Docs Backlog Triage

*Atlas Lattice Foundation · Aetherforge Mission #32 · 2026-05-28*

status: candidate

> Triage record for duplicate and near-duplicate documents in the Atlas Lattice repository. Tracks identified duplicates, their status, and resolution plan.

---

## Triage Methodology

A document is considered a **candidate duplicate** if:
1. It has the same title or covers the same subject as another document
2. It is a versioned variant where only the canonical version should remain accessible
3. It is a session-generated copy with no differentiated content vs. the primary

Duplicates are **not deleted** — they follow the [Deprecation Policy](./DEPRECATION_POLICY.md).

---

## Category A — Potential Cross-Directory Duplicates

| File | Potential Duplicate | Resolution |
|------|--------------------|-----------
| `aluminum-os/ALUMINUM_CONSTITUTIONAL_CHARTER.md` | `codebases/aluminum-os/ALUMINUM_CONSTITUTIONAL_CORPUS_MASTER_INDEX.md` | Different scope — charter vs. corpus index. Distinct. ✅ Keep both |
| `sheldonbrain/system-architecture.md` | `codebases/sheldonbrain/` variants | `sheldonbrain/` = current doc; `codebases/sheldonbrain/` = implementation. Distinct. ✅ Keep both |
| `docs/CANON_STATUS_MODEL.md` | `archive/governance/` governance spine | `docs/` = user-facing reference; `governance/` = policy source. Distinct. ✅ Keep both |

---

## Category B — Versioned Variants (Non-Duplicates, Need Labels)

| File(s) | Status |
|---------|--------|
| `aluminum-os/v2.0-*`, `v3.0-*`, `v4.0-*` | Intentional version series — all valid, older versions are historical |
| `archive/boot/gptbrain/variants/` | REM/dream variants — all historical artifacts, not duplicates |
| `archive/spec/gptdream/APPENDIX_*` | Intentional appendix series — not duplicates |

---

## Category C — Stale Session Artifacts (Low Priority)

| File | Assessment | Action |
|------|------------|--------|
| `final_manus_artifact_report.md` (root) | Session report, not linked prominently | Move to `manus-vault/` at next cleanup sprint |
| `synthesis_plan.md` (root) | Session planning doc | Move to `manus-vault/` at next cleanup sprint |
| `sandbox_inventory_april_2026.md` (root) | Time-stamped inventory | Move to `research/` or `manus-vault/` |
| `State_of_the_Union_Briefing.md` (root) | Good content, poor placement | Move to `research/` or `archive/synthesis/` |

---

## Category D — Confirmed Clean (No Duplicate Issues)

The following sections have been reviewed and contain no duplicate issues:
- `council/` — single session archive, no duplicates
- `schemas/` — versioned correctly
- `reference_impl/` — distinct implementations
- `tests/` — distinct test files
- `projects/` — distinct taskboards (legacy vs. current clearly labeled)

---

## Duplicate Triage Log

| Date | Item | Resolution | By |
|------|------|-----------|-----|
| 2026-05-28 | Initial triage pass | Categories A-D documented above | TIDELOCK Copilot |

---

## Resolution Process

For items flagged in Category C (stale root-level docs), a cleanup PR will:
1. Move files to the correct path per the [File Placement Decision Tree](./FILE_PLACEMENT_DECISION_TREE.md)
2. Leave redirect stubs per the [Deprecation Policy](./DEPRECATION_POLICY.md)
3. Update any README links

This cleanup is scheduled as a Wave 3 housekeeping sprint item.

---

## Related Documents

- [Deprecation Policy](./DEPRECATION_POLICY.md)
- [File Placement Decision Tree](./FILE_PLACEMENT_DECISION_TREE.md)
- [Stale Artifact Quarantine Lane](./STALE_ARTIFACT_QUARANTINE_LANE.md)
- [Top-Level Navigation Standards](./TOP_LEVEL_NAVIGATION_STANDARDS.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
