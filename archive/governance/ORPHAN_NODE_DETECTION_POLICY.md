---
artifact_id: KG-POLICY-ORPHAN-DETECTION-001
title: Orphan Node Detection Policy
status: candidate
created: 2026-05-28
owner: council
tags: [knowledge-graph, orphan-detection, quality-gates, automation]
---

# Orphan Node Detection Policy

> Defines what constitutes an orphan artifact, how orphans are detected, and how they must be resolved.

status: candidate

---

## What Is an Orphan Node?

An **orphan node** is an artifact in the repository that:
1. Has **zero outbound links** to other repository artifacts, **and**
2. Has **zero inbound links** from other repository artifacts

An artifact with only outbound *or* only inbound links is **not** an orphan — it's a leaf or a root node, both of which are normal graph structures.

---

## Why Orphans Matter

Orphan artifacts are:
- **Undiscoverable** — no path leads to them from any entry point
- **Unvalidated** — no document vouches for their relevance
- **Unmaintained** — they won't appear in impact analysis when related docs change
- **Misleading** — they may contain stale or contradictory information

A world-class knowledge graph has no orphan artifacts.

---

## Detection

Orphan detection runs as part of the KG quality gates:

```bash
python scripts/validate_lattice_quality_gates.py
```

The script outputs:
```
ORPHAN CHECK:
  Total nodes: 142
  Orphan nodes: 3
  Threshold: 14 (10%)
  Status: PASS

  Orphan artifacts:
    - archive/governance/OLD_DRAFT.md (0 in, 0 out)
    - docs/UNTITLED.md (0 in, 0 out)
```

---

## Thresholds

| Metric | Soft threshold (warning) | Hard threshold (failure) |
|--------|--------------------------|--------------------------|
| Orphan count (absolute) | > 5 | > 15 |
| Orphan rate (% of all nodes) | > 5% | > 10% |

The hard threshold blocks PR merges to main.

---

## Resolution Process

When an orphan is detected:

1. **Determine cause:**
   - New document not yet linked from an index → add to relevant index
   - Stale document with no current value → move to `archive/quarantine/` per [Stale Artifact Quarantine Lane](./STALE_ARTIFACT_QUARANTINE_LANE.md)
   - Intentional standalone reference → add at least one outbound link and ensure it is linked from the closest index

2. **Fix the links:**
   - Add the orphan to the relevant section of [INDEX_OF_INDEXES.md](./INDEX_OF_INDEXES.md) or a domain index
   - Add at least one outbound link from the orphan to a related artifact
   - Add `relations:` frontmatter linking it to a parent or peer

3. **Verify:**
   - Re-run `python scripts/validate_lattice_quality_gates.py`
   - Confirm orphan count is below threshold

---

## Acceptable Orphan Types

A small set of artifacts are structurally expected to be orphans during active development:

| Type | Example | Acceptable period |
|------|---------|------------------|
| Active draft | A wave's first stub doc, not yet indexed | < 72 hours |
| Work log (just created) | A new TIDELOCKBrain log | < 24 hours (link to taskboard) |
| Template file | `*TEMPLATE*.md` (meant to be copied, not linked) | Always — templates are excluded from orphan checks |

---

## Exclusions from Orphan Checks

The following file patterns are excluded:

```
*TEMPLATE*.md
.github/**
*.yml
*.yaml
*.py
*.json
*.sh
CHANGELOG.md  (root level, structurally unlinked)
```

---

## Governance

| Role | Responsibility |
|------|---------------|
| PR author | Resolve orphan check failures before requesting review |
| Section owner | Review orphan reports in their domain quarterly |
| @atlaslattice | Approves exclusion list changes |

---

*Atlas Lattice Foundation · status: candidate*
