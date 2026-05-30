# Deprecation Policy

*Atlas Lattice Foundation · Aetherforge Mission #9 · 2026-05-28*

status: candidate

> Defines how artifacts, schemas, scripts, and workflows are deprecated in Atlas Lattice — ensuring continuity of the knowledge graph while keeping the repository free of unmaintained dead weight.

---

## Deprecation Philosophy

Deprecation is **not deletion**. The Atlas Lattice knowledge graph must preserve provenance and historical state. Deprecated artifacts are quarantined, annotated, and archived — never silently removed without a trace.

---

## Lifecycle States

```
active → deprecated → quarantined → archived
                  ↘ (exceptional) → removed (with redirect pointer)
```

| State | Meaning |
|-------|---------|
| `active` | Current, maintained, in use |
| `deprecated` | Superseded; still readable but no longer updated |
| `quarantined` | Flagged for removal review; links may be broken |
| `archived` | Frozen historical record; read-only |
| `removed` | Deleted from live tree; redirect pointer left in place |

---

## Deprecation Triggers

An artifact may be deprecated when:
1. A newer version or successor document has been ratified.
2. The content is provably incorrect and correction is not feasible.
3. The owning section has been reorganized and the artifact no longer belongs.
4. The artifact was experimental and the experiment concluded.
5. Security or legal requirement demands removal of content.

---

## Deprecation Process

### Step 1 — Propose

Open a PR with classification label `[GOV]` and title pattern:  
`[GOV] Deprecate <artifact-name> — reason`

Include in the PR description:
- The deprecation trigger (from the list above)
- The successor document or canonical replacement (if any)
- Any downstream links that need updating

### Step 2 — Header Update

Add the following block to the top of the artifact file (below the title, before other content):

```markdown
> ⚠️ **DEPRECATED** as of YYYY-MM-DD.
> Superseded by: [successor link]
> Status: deprecated
> Scheduled quarantine: YYYY-MM-DD + 90 days
```

### Step 3 — Review & Approval

- Standard deprecations: Tier 2 SLA (72 hours), section owner approval.
- Canon artifact deprecations: require **@atlaslattice** ratification.

### Step 4 — Quarantine

After 90 days in `deprecated` state with no objections, move the artifact to the appropriate `_quarantine/` subfolder and update all inbound links.

### Step 5 — Archive or Remove

- Default: move to `archive/` with `status: archived` frontmatter.
- Exceptional removal: only for security/legal mandates. Leave a `_REDIRECT.md` stub with the artifact's original path, reason for removal, and date.

---

## Bulk Deprecation

For wave deprecations (e.g., after a major reorganization), a **Deprecation Batch Record** must be filed as `DEPRECATION_BATCH_YYYY-MM-DD.md` in `archive/governance/` and referenced in the council session notes.

---

## Prohibited Actions

- ❌ Silent deletion of any artifact with inbound links.
- ❌ Deprecation of canon-status artifacts without @atlaslattice ratification.
- ❌ Removing `_REDIRECT.md` stubs for at least 1 year post-removal.

---

## Related Documents

- [Change Classification Rules](./CHANGE_CLASSIFICATION_RULES.md)
- [Section Ownership Map](./SECTION_OWNERSHIP_MAP.md)
- [Council Review Cadence](./COUNCIL_REVIEW_CADENCE.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
