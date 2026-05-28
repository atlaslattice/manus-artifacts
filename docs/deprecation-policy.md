# Deprecation and Supersession Policy

> **Status:** CANDIDATE  
> **Artifact Type:** policy  
> **Date:** 2026-05-28  
> **Related:** [Ratification and Trust Flow](./RATIFICATION_AND_TRUST_FLOW.md), [Contributor decision tree](./contributor-decision-tree.md), [Artifact quality rubric](./artifact-quality-rubric.md)

## When to deprecate vs delete

- **Deprecate** when an artifact has historical, governance, research, or provenance value but should no longer be treated as current.
- **Delete** only when the file is a clear mistake, duplicate with no archival value, or contains material that cannot remain published.
- Default to deprecation over deletion.

## Required deprecation notice format

Add a notice near the top of the artifact:

```markdown
> **Status:** DEPRECATED
> **Deprecated On:** YYYY-MM-DD
> **Replacement:** [Ratification and Trust Flow](./RATIFICATION_AND_TRUST_FLOW.md)
> **Reason:** One-sentence explanation.
```

## How to add replacement links

1. add a direct replacement link in the deprecation notice
2. update any nearby index or README that routes readers to the old file
3. update registry or evidence references if the old file is machine-tracked
4. preserve the deprecated file so incoming links still resolve

## How deprecated artifacts appear in registry

If the artifact is represented in a machine-readable registry, retain the same stable ID unless the object identity itself changed. Update lifecycle state to `DEPRECATED` and add a link that points to the replacement artifact.

## Timeline requirements

- Deprecation notice should be added in the same change that introduces the replacement when possible.
- Deprecated artifacts should keep working links for at least one review cycle.
- Governance-critical artifacts should not be deleted without explicit adjudication.
- Evidence-bearing artifacts should preserve their receipts and evidence links indefinitely.
