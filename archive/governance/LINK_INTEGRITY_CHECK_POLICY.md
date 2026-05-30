---
artifact_id: CICD-POLICY-LINK-INTEGRITY-001
title: Link Integrity Check Policy
status: candidate
created: 2026-05-28
owner: council
tags: [ci-cd, links, integrity, quality-gates]
---

# Link Integrity Check Policy

> Defines the automated and manual processes for detecting and resolving broken links in the repository.

status: candidate

---

## Scope

This policy covers:
- Internal links (relative paths between repository files)
- Anchor links (`#section-name` within files)
- External links to public web resources (checked on a schedule, not per-PR)

---

## Broken Link Categories

| Category | Definition | Severity |
|----------|-----------|---------|
| Dead internal link | Links to a file that no longer exists | Critical |
| Wrong anchor | Links to a `#section` that doesn't exist in the target file | High |
| Dead external link | Links to a URL that returns 4xx/5xx | Medium |
| Redirecting external link | Links that redirect (301/302) — destination should be used instead | Low |

---

## CI Gate (Planned: Q3 2026)

`scripts/check_link_integrity.py` will run on every PR:

1. Extract all markdown links from modified files
2. For internal links: verify the target file exists and the anchor (if any) is present
3. Report all broken internal links
4. Fail the gate if any critical or high-severity broken links are found in files modified by the PR

External link checking is **not** run per-PR (too slow). See scheduled check below.

---

## Scheduled External Link Check

A weekly GitHub Actions workflow will:
1. Extract all external URLs from all markdown files in the repository
2. HTTP HEAD request each URL (with a 10-second timeout)
3. Open a GitHub issue listing all 4xx/5xx URLs if any are found
4. Label the issue `broken-link` and assign to the section owner

**Workflow file:** `.github/workflows/external-link-check.yml` (planned Q3 2026)

---

## Resolution Process

| Category | Owner | SLA |
|----------|-------|-----|
| Dead internal link (blocks PR) | PR author | Before merge |
| Wrong anchor (blocks PR) | PR author | Before merge |
| Dead external link (issue) | Section owner | 2 weeks |
| Redirecting link (issue) | Any contributor | Rolling |

---

## Link Move Protocol

When renaming or moving a file:
1. Search the entire repository for links to the old path: `grep -r "old/path" . --include="*.md"`
2. Update all found links to the new path
3. Update `archive/governance/CANONICAL_PATH_MAP.md` with the new path
4. Add an entry to CHANGELOG.md noting the rename

---

## Current Status

As of 2026-05-28, link integrity is maintained manually. The CI gate will be implemented as part of the Q3 2026 hygiene sprint.

Drive to zero broken internal links is tracked as mission #34 (complete per Wave 3).

---

*Atlas Lattice Foundation · status: candidate*
