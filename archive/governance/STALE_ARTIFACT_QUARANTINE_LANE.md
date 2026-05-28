# Stale Artifact Quarantine Lane

*Atlas Lattice Foundation · Aetherforge Mission #33 · 2026-05-28*

status: candidate

> Defines the process and structure of the quarantine lane — the holding state for artifacts awaiting deprecation, cleanup, or removal before they are formally archived or deleted.

---

## Purpose

The quarantine lane prevents stale artifacts from cluttering the active repository while ensuring they are never silently deleted. It provides a 90-day review window and full audit trail.

---

## Quarantine Criteria

An artifact enters the quarantine lane when:
1. It has had no meaningful commits in **24 months**
2. It has been superseded by a newer canonical version
3. It failed a duplication triage review (see [Duplicate Docs Backlog Triage](./DUPLICATE_DOCS_BACKLOG_TRIAGE.md))
4. It was placed incorrectly and is awaiting relocation

---

## Quarantine Directory Structure

Quarantined artifacts are moved to `_quarantine/` subdirectories within their source section:

```
archive/governance/_quarantine/
archive/spec/_quarantine/
archive/boot/_quarantine/
docs/_quarantine/
projects/_quarantine/
```

A `_quarantine/` directory at the root is NOT used — quarantine is section-scoped to preserve context.

---

## Quarantine Header

When an artifact is moved to quarantine, prepend this header:

```markdown
> ⚠️ **QUARANTINED** as of YYYY-MM-DD.
> Original path: <original/path/to/file.md>
> Reason: <stale / superseded / misplaced / duplicate>
> Scheduled review: YYYY-MM-DD (90 days)
> Disposition: archive / delete / restore
> Approved by: @username
```

---

## Quarantine Process

### Step 1 — Nomination

Any contributor may nominate an artifact for quarantine by opening a PR with label `[CHORE] quarantine-candidate`.

Include in PR description:
- Original path
- Quarantine reason
- Proposed disposition (archive, delete, restore, relocate)

### Step 2 — Review Window

Nominated artifacts have a **30-day public comment window** (tracked in the PR). Any contributor may object with justification.

### Step 3 — Move

After 30 days with no blocking objections:
1. Move file to `_quarantine/` subfolder
2. Add quarantine header to the file
3. Leave a redirect stub at the original path:

```markdown
# [Artifact Name] — Redirected

This document has been moved to quarantine.

> Original path: <this file's path>
> Quarantined location: <new path>
> Date: YYYY-MM-DD
> Reason: <reason>
```

### Step 4 — 90-Day Disposition Review

At the next quarterly council session after the 90-day mark:
- **Archive:** Move to frozen archive with `status: archived`
- **Delete:** Remove with full post-mortem in incident log (exceptional only)
- **Restore:** Move back to active path, remove quarantine header

---

## Current Quarantine Queue

*(Empty at 2026-05-28 — quarantine process newly established)*

| Artifact | Nominated | Reason | Disposition |
|----------|----------|--------|------------|
| — | — | — | — |

Candidates from [Duplicate Docs Backlog Triage](./DUPLICATE_DOCS_BACKLOG_TRIAGE.md) (Category C) will be formally nominated in the next housekeeping sprint.

---

## Related Documents

- [Deprecation Policy](./DEPRECATION_POLICY.md)
- [Duplicate Docs Backlog Triage](./DUPLICATE_DOCS_BACKLOG_TRIAGE.md)
- [Data Retention Policy](./DATA_RETENTION_POLICY.md)
- [File Placement Decision Tree](./FILE_PLACEMENT_DECISION_TREE.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
