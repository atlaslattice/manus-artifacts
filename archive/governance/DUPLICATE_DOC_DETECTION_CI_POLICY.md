---
artifact_id: CICD-POLICY-DUPLICATE-DOC-DETECTION-001
title: Duplicate Document Detection in CI
status: candidate
created: 2026-05-28
owner: council
tags: [ci-cd, duplicates, automation, quality-gates]
---

# Duplicate Document Detection in CI

> Defines how duplicate documents are automatically detected, classified, and resolved.

status: candidate

---

## Why Automated Duplicate Detection?

Duplicate documents cause:
- Conflicting information (readers see different versions of truth)
- Maintenance burden (changes must be applied to N places)
- KG confusion (the graph has ambiguous edges)
- Discovery failure (users find the wrong copy)

---

## Detection Approach

Duplicate detection uses a multi-level similarity check:

### Level 1: Exact duplicate (hash match)
Two files with identical byte content → immediate flag as "exact duplicate"

### Level 2: Near-duplicate (Jaccard similarity)
Two files with ≥ 85% word-level Jaccard similarity → flagged as "near-duplicate"

### Level 3: Title collision
Two files with identical `title:` frontmatter field → flagged as "title collision"

### Level 4: Artifact ID collision
Two files claiming the same `artifact_id` → flagged as "ID collision" (critical)

---

## Thresholds

| Similarity level | Action |
|-----------------|--------|
| Exact duplicate (100%) | Block PR; must resolve before merge |
| Near-duplicate (≥ 85%) | Warn in PR; must acknowledge or resolve |
| Title collision | Warn in PR; annotate with intended distinction |
| Artifact ID collision | Block PR; IDs must be unique |

---

## Resolution Options

| Scenario | Resolution |
|----------|-----------|
| True duplicate (same content, same purpose) | Delete one; update all links to point to survivor; log in [DUPLICATE_DOCS_BACKLOG_TRIAGE.md](./DUPLICATE_DOCS_BACKLOG_TRIAGE.md) |
| Historical version (old replaced by new) | Keep both; add `superseded_by` frontmatter to old; deprecate old |
| Same topic, different scope/audience | Add a clear differentiator to both titles; add a "See also" link between them |
| False positive (similarity is coincidental) | Add `duplicate_check_exempt: true` to frontmatter of both files with a note explaining |

---

## CI Gate (Planned: Q3 2026)

`scripts/detect_duplicate_docs.py` will run on every PR:

```bash
python scripts/detect_duplicate_docs.py --paths archive/ docs/ --threshold 0.85
```

Output:
```
DUPLICATE CHECK:
  Exact duplicates: 0
  Near-duplicates (≥85%): 1
    - archive/governance/CANON_STATUS_MODEL.md
    - archive/governance/STATUS_MODEL_DRAFT.md (87% similarity)
  Title collisions: 0
  Artifact ID collisions: 0
  Status: WARN (near-duplicate requires acknowledgment)
```

---

## Existing Duplicate Backlog

See [DUPLICATE_DOCS_BACKLOG_TRIAGE.md](./DUPLICATE_DOCS_BACKLOG_TRIAGE.md) for the current tracked list of known duplicates and their resolution status.

---

*Atlas Lattice Foundation · status: candidate*
