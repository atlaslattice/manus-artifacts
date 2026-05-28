---
artifact_id: CICD-POLICY-REPO-HYGIENE-001
title: Repository Hygiene Workflow Policy
status: candidate
created: 2026-05-28
owner: council
tags: [ci-cd, governance, hygiene, automation]
---

# Repository Hygiene Workflow Policy

> Defines automated and manual hygiene checks that keep the Atlas Lattice repository clean, organized, and healthy.

status: candidate

---

## What Is Repository Hygiene?

Repository hygiene covers the set of practices that prevent technical debt, structural rot, and discovery failures:

- No orphan artifacts
- No broken links
- No stale or undated content past its review window
- No incomplete frontmatter
- No duplicate documents without a deduplication plan
- No uncommitted work logs

---

## Automated Hygiene Checks (Current)

| Check | Tool | Frequency | Blocks merge? |
|-------|------|-----------|--------------|
| Markdown structure lint | `scripts/check_docs_layout_structure.py` | Every PR | Yes |
| AI evidence integrity | `scripts/check_ai_evidence_integrity.py` | Every PR | Yes |
| KG quality gates | `scripts/validate_lattice_quality_gates.py` | Every push to main | Yes |
| GPTBrain reference checks | `archive/boot/gptbrain/reference_impl/run_checks.sh` | Every PR touching gptbrain | Yes |
| Boring machine validation | Full pytest suite | Every push | Yes |

---

## Planned Hygiene Checks

| Check | Tool (planned) | Target | Description |
|-------|---------------|--------|-------------|
| Link integrity | `scripts/check_link_integrity.py` | Q3 2026 | Detect broken internal links |
| Metadata completeness | `scripts/check_metadata_completeness.py` | Q3 2026 | Flag missing `artifact_id`, `status`, `created` |
| Duplicate detection | `scripts/detect_duplicate_docs.py` | Q3 2026 | Hash-based near-duplicate finder |
| Schema validation | `scripts/validate_schemas.py` | Q3 2026 | Validate YAML schemas against JSON Schema meta-schema |
| Stale artifact scan | `scripts/scan_stale_artifacts.py` | Weekly schedule | Flag docs with `created` > 180 days and no `updated` |
| Orphan detection | Part of KG quality gates | Every push to main | Already partially active |

---

## Manual Hygiene Cadence

| Task | Frequency | Owner |
|------|-----------|-------|
| Review stale artifact quarantine | Monthly | Section owner |
| Triage duplicate docs backlog | Monthly | Section owner |
| Audit broken links | Monthly (until CI gate active) | Swarm agent |
| Review orphan node report | Quarterly | KG maintainer |
| Update CANONICAL_PATH_MAP.md | On any artifact rename/move | PR author |

---

## Hygiene Failure Response

| Failure type | Response time | Resolution |
|-------------|--------------|-----------|
| Broken CI gate | Immediate | PR author fixes before review |
| Orphan node > threshold | 72 hours | Link or quarantine orphan |
| Stale artifact flagged | 2 weeks | Update, quarantine, or deprecate |
| Duplicate detected | 1 month | Merge or link as "superseded_by" |
| Broken link in main | 48 hours | Fix or quarantine linking artifact |

---

## Hygiene Score

A quarterly hygiene score is computed as:

```
hygiene_score = 
  (1 - orphan_rate) * 0.30 +
  (1 - broken_link_rate) * 0.25 +
  frontmatter_coverage * 0.25 +
  (1 - stale_rate) * 0.20
```

**Target:** hygiene_score ≥ 0.90 by Q4 2026.

---

*Atlas Lattice Foundation · status: candidate*
