# GitHub Mirror Publication Criteria

```
STATUS: CANDIDATE — NOT CANON
AXIS: 01 — Canon & Governance  Task: #2
LAST_UPDATED: 2026-05-29
```

Defines what it means for an artifact to be published to GitHub and what
trust level that confers.

---

## Governing Principle

GitHub (`atlaslattice/manus-artifacts`) is the **durable canonical substrate**.
All other surfaces (Drive, Notion, website, mirrors) are relay/working-vault
layers. Publication to GitHub is a necessary — but not sufficient — condition
for canon status.

---

## Mirror vs. Canon

| Surface | Role | Trust Level |
|---|---|---|
| Google Drive | Working vault / drafts | `WORKING` |
| Notion | Relay / notes layer | `WORKING` |
| GitHub (this repo) | Canonical substrate | `CANDIDATE` minimum |
| GitHub (ratified) | Canon record | `RATIFIED` |
| Website mirror | Public surface | Inherits from GitHub state |

---

## Minimum Criteria for GitHub Commit (CANDIDATE)

An artifact committed to `main` must satisfy:

1. **Filename slug** — Lowercase, hyphen-separated, ISO date suffix where
   applicable (e.g. `my-artifact-2026-05-29.md`).
2. **STATUS header** — Top of file must declare
   `STATUS: CANDIDATE — NOT CANON` until ratified.
3. **Metadata block** — Must include at minimum: `LAST_UPDATED`, `AXIS` or
   `PURPOSE`, and `RELATED` links where applicable.
4. **No PII / secrets** — Must pass pre-flight secret and PII scan.
5. **License** — Covered by repository MIT license; no conflicting license.

---

## Mirror Sync Policy

When an artifact already exists in a relay layer (Drive/Notion) and is being
mirrored to GitHub for the first time:

1. Apply filename normalization.
2. Add `STATUS: CANDIDATE — NOT CANON` header.
3. Preserve original source metadata in a `SOURCE` block.
4. Log in `docs/INGESTION_SOURCES_REGISTRY.md`.
5. Do NOT claim ratification or canon status in the mirrored copy.

---

## Promoting a GitHub CANDIDATE to RATIFIED

Follow [CANDIDATE_TO_CANON_WORKFLOW.md](./CANDIDATE_TO_CANON_WORKFLOW.md).

---

## Related

- [WEBSITE_CANON_CRITERIA.md](./WEBSITE_CANON_CRITERIA.md)
- [docs/INGESTION_SOURCES_REGISTRY.md](../INGESTION_SOURCES_REGISTRY.md)
- [docs/naming-conventions.md](../naming-conventions.md)
