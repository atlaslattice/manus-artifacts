# Versioning and Release Policy

```text
STATUS: CANDIDATE GOVERNANCE POLICY — NOT CANON
```

```yaml
artifact_id: DOC-VERSIONING-RELEASE-POLICY-2026-05-28
title: Versioning and Release Policy
status: candidate
created_utc: 2026-05-28T18:27:53Z
updated_utc: 2026-05-28T18:27:53Z
owners:
  - @atlaslattice
domain: governance
source_uri:
  - https://github.com/atlaslattice/manus-artifacts/blob/main/docs/versioning-release-policy.md
provenance:
  extraction_method: human-authored
  evidence_links:
    - ../docs/governance-ratification-process.md
    - ../.github/CONTRIBUTING.md
    - ../projects/aetherforge-top50-taskboard-2026-05-26.md
  confidence: high
governance:
  canon_status: NOT_CANON
  ratification_event_id: null
  adjudicator: null
  trust_state: pending
```

## Executive Summary

This policy defines how repository artifacts should be versioned, released, and
superseded so the archive remains public, legible, and trustworthy. Governance
status and version status are separate: a document can be versioned without
being canon, and nothing becomes canon without the ratification flow in
[Governance and Ratification Process](./governance-ratification-process.md).

## Scope

This policy applies to:

- governance and policy docs under `docs/`
- specs, schemas, and contracts under `archive/`, `schemas/`, and related paths
- reference implementations and validation surfaces
- release-oriented project artifacts and public milestone bundles

Historical source material may remain date-stamped when that preserves original
context, but new structured artifacts should follow this policy.

## Core Rules

1. **Separate versioning from canon state.** Use version numbers for change
   tracking; use governance fields for candidate/reviewed/ratified state.
2. **Prefer explicit versions for living artifacts.** New standards, templates,
   schemas, contracts, and policy docs should include a visible version.
3. **Never erase lineage.** Replaced artifacts should be marked superseded or
   deprecated, not silently removed.
4. **Record scope of change.** Every meaningful release should describe what
   changed, why it changed, and what it affects.
5. **Keep filenames stable and readable.** Use short, human-readable names with
   embedded versions where practical.

## Version Format by Artifact Type

| Artifact type | Preferred format | Notes |
|---|---|---|
| Governance docs, policies, templates | `vMAJOR.MINOR` or `vMAJOR.MINOR.PATCH` | Use patch versions for clarifications that do not change intent. |
| Schemas and contracts | `vMAJOR_MINOR/` for directories plus semantic version in docs | Breaking changes require a new major version surface. |
| Reference implementations | Semantic versioning | Align with the schema/contract version they implement. |
| Historical imports and dated reports | ISO date in title or filename | Do not force-convert legacy historical artifacts. |
| Repository-wide milestones | Git tag or GitHub release title | Use for public release bundles, not every document update. |

## Change Classification

### Major

Use a major version bump when a change:

- breaks compatibility
- changes required governance or provenance fields
- alters schema shape or contract meaning
- replaces a previously recommended operating path

### Minor

Use a minor version bump when a change:

- adds a backward-compatible section, field, or capability
- expands guidance without invalidating prior conforming usage
- materially improves release criteria, examples, or coverage

### Patch

Use a patch version bump when a change:

- fixes errors, wording, or examples without changing meaning
- repairs links, formatting, or validation instructions
- adds clarity that does not alter the contract or governance path

## Release States

Use these release labels where relevant:

- `alpha` — early candidate shape, expected churn
- `beta` — broader review-ready candidate
- `rc` — release candidate pending final approval or validation
- stable version without suffix — default published version for active use

These labels do **not** imply canon status.

## Naming Guidance

- Prefer filenames like `topic-v0.1.md`, `policy-v1.0.md`, or versioned folders
  such as `v0_1/` for schemas.
- Keep human-readable titles inside documents even when filenames are compact.
- When an artifact is primarily historical, preserve original date-based naming
  and add version metadata inside the document only if needed.

## Minimum Release Contents

Every major new version or public release should include:

- declared artifact status (`candidate`, `reviewed`, `ratified`, etc.)
- version number or date-based release identity
- updated timestamp
- source or evidence links
- supersession note when replacing a prior artifact
- validation notes appropriate to the touched surface

Use the repository's
[Artifact Provenance Header Template](./artifact-provenance-header-template.md)
for major artifacts and the
[pull request template](https://github.com/atlaslattice/manus-artifacts/blob/main/.github/pull_request_template.md) for change review.

## Repository Release Policy

### Document and policy releases

- Release directly by merging the updated artifact and ensuring links resolve.
- Add or update cross-links in index/navigation docs when the artifact is
  intended for discovery.
- Use a changelog or change summary in the PR description for major revisions.

### Schema and contract releases

- Do not mutate a stable schema surface in place if the change is breaking.
- Create a new versioned directory or filename for breaking revisions.
- Keep prior stable versions available for lineage and migration.

### Repository-wide milestone releases

- Reserve GitHub releases or tags for meaningful public bundles such as
  "World-Class v1", major governance drops, or package-quality deliverables.
- A release bundle should summarize included artifacts, validation status, and
  known follow-up work.

## Supersession and Deprecation

When replacing an artifact:

1. keep the prior artifact in place when possible
2. add a note linking to the newer preferred version
3. update index docs to point to the preferred current artifact
4. mark deprecated materials clearly when retained only for lineage

## Review and Validation Expectations

- Validate touched paths before opening a PR.
- For markdown-heavy changes, at minimum confirm internal links still resolve.
- For code, schema, or pipeline changes, run the existing checks tied to that
  surface.
- Ratification-impacting releases must follow the governance flow and update any
  required logs or evidence links.

## Adoption Note

This policy is a candidate governance artifact intended to improve consistency
for future archive work. Existing legacy files do not need to be renamed
retroactively unless they are being actively modernized or promoted.
