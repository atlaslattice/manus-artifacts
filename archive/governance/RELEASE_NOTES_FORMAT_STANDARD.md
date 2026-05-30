---
artifact_id: GOV-RELEASE-NOTES-FORMAT-STANDARD-001
title: Release Notes Format Standard
status: candidate
created: 2026-05-28
owner: council
tags: [documentation, release-notes, changelog, standards]
---

# Release Notes Format Standard

> Defines the required format, content, and process for release notes in the Atlas Lattice repository.

status: candidate

---

## Overview

Release notes communicate what changed, why it matters, and how to adapt. This standard governs the format for all releases, wave completions, and significant milestones.

---

## Release Types

| Type | Trigger | Format |
|------|---------|--------|
| **Wave Release** | Completion of a 12-mission Aetherforge wave | Full release notes per this standard |
| **Hotfix** | Emergency correction to a canonical artifact | Abbreviated release notes (sections: Summary, Changed, Action Required) |
| **Minor Update** | Non-breaking additions (new docs, minor spec updates) | CHANGELOG.md entry only (no standalone release notes required) |
| **Schema Version Bump** | New schema version in `schemas/` | Full release notes with migration guide |

---

## Release Notes Template

```markdown
# Release Notes — [Wave/Version Label]
*Atlas Lattice Foundation · [YYYY-MM-DD]*

## Summary

One paragraph summarizing what this release covers and its significance.

## Highlights

- **[Highlight 1]:** Short description of most important change.
- **[Highlight 2]:** Short description.
- **[Highlight 3]:** Short description.

## Added

- `path/to/file.md` — what it is and why it was added
- ...

## Changed

- `path/to/file.md` — what changed (before → after if helpful)
- ...

## Deprecated

- `path/to/file.md` — deprecated in favor of [X]; will be removed on [date]
- ...

## Removed

- `path/to/file.md` — removed; see [replacement] for migration

## Fixed

- `path/to/file.md` — what was broken; what was corrected

## Security

- Any security-relevant changes (vulnerability fixes, policy updates, etc.)

## Migration Guide

*(Omit if no migration is required)*

Steps for contributors, agents, or integrations to adapt to this release.

## Metrics

| Metric | Before | After |
|--------|--------|-------|
| Missions complete | X | Y |
| Total docs | X | Y |
| Test coverage | X | Y |

## What's Next

Brief description of the next wave/milestone.

## Contributors

- @username — contributed [X]
- TIDELOCK — execution agent for this wave

---
*status: candidate · [Link to CHANGELOG.md](../CHANGELOG.md)*
```

---

## Placement

| Release type | File location |
|-------------|--------------|
| Wave releases | `archive/governance/RELEASE_NOTES_WAVE_NN_[DATE].md` |
| Schema versions | `archive/governance/RELEASE_NOTES_SCHEMA_vX_Y_[DATE].md` |
| CHANGELOG entries | Root `CHANGELOG.md` (always) |

---

## Process

1. **Draft** release notes during the wave sprint (not after)
2. **Review** with section owner before merging the wave PR
3. **Add** a CHANGELOG.md entry referencing the release notes file
4. **Tag** the relevant commit with `wave-NN-complete` (or equivalent)

---

## Section Completeness Requirements

| Section | When required |
|---------|--------------|
| Summary | Always |
| Highlights | Always (≥ 2 highlights) |
| Added | If any files added |
| Changed | If any files changed |
| Deprecated | If anything deprecated |
| Removed | If anything removed |
| Fixed | If anything corrected |
| Security | If any security-relevant change |
| Migration Guide | If any breaking change or schema bump |
| Metrics | For wave releases (highly recommended) |
| What's Next | Always |
| Contributors | Always |

Omit empty sections entirely — do not leave empty headers.

---

## Quality Check

Before publishing release notes:
- [ ] Summary is one paragraph (no more)
- [ ] All Added/Changed/Removed items have file paths
- [ ] No empty sections remain
- [ ] Metrics are accurate
- [ ] CHANGELOG.md has been updated
- [ ] status is `candidate` (release notes are never auto-ratified)

---

*Atlas Lattice Foundation · status: candidate*
