# Source-of-Truth Mirror Policy

## Summary

Defines the authoritative source of truth for AtlasLattice content and the role of mirror/relay layers.

---

## Hierarchy

```
GitHub (atlaslattice/manus-artifacts)
    └── CANONICAL SUBSTRATE — durable source of truth for all ratified artifacts

Google Drive / Notion / other working vaults
    └── RELAY LAYER — working drafts, notes, sync targets; NOT authoritative

Website / published surfaces
    └── PUBLICATION LAYER — canon only when explicitly ratified/published there
                            (website ≠ canon by default; ratification is required)
```

---

## Rules

### Rule 1 — GitHub is the single canonical substrate

All canon artifacts are governed from the GitHub repository.
A claim is not canon because it appears on a website, in a Notion doc, or in a Google Drive file.

### Rule 2 — Mirror layers are read-relay, not write-authority

Working vaults (Drive, Notion, etc.) may receive exported snapshots of canon content but
have no write-authority over the canonical state. Changes must flow back through GitHub PRs.

### Rule 3 — Publication requires explicit ratification

Publishing content to an external surface (website, API, public doc) requires:
1. The artifact must be at `canon_status: CANON` in GitHub.
2. A publication event must be recorded in the [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md).
3. The published URL or surface must be noted in the artifact's frontmatter under `published_at`.

### Rule 4 — Conflicts default to GitHub

If a relay or publication layer diverges from GitHub, the GitHub version prevails.
Discrepancies must be resolved via a sync PR within one sprint.

### Rule 5 — Sensitive content is never mirrored without approval

Content marked `sensitive: true` or `audience: private` must not be exported to public-facing mirrors.

---

## Drift detection

Run `python scripts/validate_artifact_metadata.py` to detect frontmatter drift.
Mirror sync state should be audited at each quarterly review per the
[Governance Operations Handbook](./GOVERNANCE_OPERATIONS_HANDBOOK.md).

---

## Cross-links

- [Canon Lifecycle State Machine](./CANON_LIFECYCLE_STATE_MACHINE.md)
- [Governance Operations Handbook](./GOVERNANCE_OPERATIONS_HANDBOOK.md)
- [Governance Decision Index](./GOVERNANCE_DECISION_INDEX.md)
- [Canon Metadata Standard](./CANON_METADATA_STANDARD.md)

## Status

`candidate` — not canon until ratified.
