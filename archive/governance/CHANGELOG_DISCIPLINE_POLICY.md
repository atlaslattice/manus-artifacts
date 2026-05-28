---
artifact_id: GOV-CHANGELOG-DISCIPLINE-POLICY-001
title: Changelog Discipline Policy
status: candidate
created: 2026-05-28
owner: council
tags: [documentation, changelog, discipline, policy]
---

# Changelog Discipline Policy

> Defines the rules for maintaining CHANGELOG.md and enforcing changelog updates as a required contribution step.

status: candidate

---

## Purpose

A well-maintained CHANGELOG is a first-class artifact. It preserves institutional memory, helps contributors understand the project's evolution, and signals professional-grade repo discipline. This policy enforces that every meaningful change to the repository is reflected in CHANGELOG.md.

---

## The Rule

**Any pull request that adds, modifies, or removes documentation or artifacts must include a CHANGELOG.md update.**

Exceptions:
- Typo fixes (1–3 characters, no semantic change)
- Pure whitespace/formatting only
- Automated bot commits (dependency bumps, CI config by bots)
- Changes to `.github/` only (CI config, templates — these are logged as "CI" in CHANGELOG)

---

## What Goes in CHANGELOG.md

The repository CHANGELOG.md is at the root: `/CHANGELOG.md`.

Use the following top-level categories within the `[Unreleased]` section:

| Category | When to use |
|----------|-------------|
| `### Added` | New files, new sections, new features |
| `### Changed` | Modifications to existing artifacts |
| `### Deprecated` | Artifacts moved to deprecated status |
| `### Removed` | Artifacts deleted or moved |
| `### Fixed` | Corrections (broken links, wrong frontmatter, errors) |
| `### Security` | Any security-relevant change |

**Format for each entry:**

```
- `path/to/file.md` — short description of what was added/changed/why
```

If a single PR adds many files, group them logically:

```
- Wave 4 Documentation Pack (tasks #37–#48): 8 new governance and docs artifacts
  - `archive/governance/EXECUTIVE_SUMMARIES_STANDARD.md`
  - `archive/governance/DOCS_LINT_QUALITY_GATES.md`
  - (etc.)
```

---

## Release Versioning

This repository uses **date-based milestones**, not semver. When a wave is completed:

1. Move all items from `[Unreleased]` into a new dated section `## [YYYY-MM-DD] — Wave N Label`
2. Keep `[Unreleased]` at the top as an empty bucket for the next wave
3. Add a CHANGELOG entry referencing any release notes file produced

---

## CHANGELOG.md Location and Format

The CHANGELOG lives at the repository root:

```
/CHANGELOG.md
```

It follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) formatting. The header at the top of the file must link to the standard and state the versioning scheme.

---

## Enforcement

| Phase | Mechanism |
|-------|-----------|
| Now | PR review checklist — reviewer checks that CHANGELOG was updated |
| Q4 2026 | Gate 9 in CI — automated check that CHANGELOG.md was touched in any PR touching `archive/`, `docs/`, `schemas/` |

---

## Who Maintains CHANGELOG.md

- **PR author** adds their own entries before requesting review
- **Swarm agents** (TIDELOCK and others) must include CHANGELOG entries in every execution wave
- **@atlaslattice** reviews CHANGELOG quality at milestone ratifications

---

## Example Entry (Good)

```markdown
### Added

- `archive/governance/DOCS_LINT_QUALITY_GATES.md` — defines all automated documentation lint gates (#43)
- `archive/governance/READABILITY_QUALITY_THRESHOLDS.md` — sets Flesch score targets by doc category (#44)
- `CHANGELOG.md` — root changelog established per Keep a Changelog standard (#45)
- `archive/governance/CHANGELOG_DISCIPLINE_POLICY.md` — policy for changelog enforcement (#45)
- `archive/governance/RELEASE_NOTES_FORMAT_STANDARD.md` — template for wave release notes (#46)
```

---

## Example Entry (Bad — do not do this)

```markdown
### Added

- updated docs
- some new files
- fixes
```

Entries must have file paths and meaningful descriptions.

---

*Atlas Lattice Foundation · status: candidate*
