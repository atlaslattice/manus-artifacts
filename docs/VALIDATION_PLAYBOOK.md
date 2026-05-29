# Validation Playbook
Status: Candidate
Date: 2026-05-26

This playbook consolidates validation standards for the archival repository.
It is intentionally documentation-centric: the goal is not software release validation, but trustable archive integrity.
In the Aetherforge program, validation is the quality ring that keeps ambitious doctrine from outrunning governance.

## Validation objectives

Validation should answer the following questions for any public artifact set:

1. Is the artifact structurally complete?
2. Is its status visible and accurate?
3. Can readers navigate links and lineage without dead ends?
4. Does CI check the same things contributors are expected to check locally?
5. Are high-impact claims traceable enough for public scrutiny?

## Validation layers

### 1. Header and metadata integrity

Every new or materially changed markdown file should include:

- a title
- a visible `Status:` note
- a current date line
- metadata frontmatter when the artifact is part of the normalized schema rollout

### 2. Link integrity

Contributors should verify that:

- all relative markdown links resolve
- referenced canon artifacts exist at the cited paths
- directory links point to real repository locations
- supersession chains do not terminate in missing files

### 3. Lifecycle correctness

Validation should check whether the labeled lifecycle state matches the actual governance condition.
A file may be polished and still remain Candidate if ratification has not occurred.

### 4. GPTBrain parity

Local checks and CI checks should stay aligned for archive automation and reference logic.
If a parity check exists in CI, contributors should be able to run an equivalent local command or script before proposing changes.

### 5. Metadata completeness

For documents using frontmatter, verify required fields from [METADATA_SCHEMA.md](./METADATA_SCHEMA.md):

- `title`
- `status`
- `domain`
- `steward`
- `created`
- `updated`
- `version`
- `supersedes`
- `superseded_by`

## Local validation checklist

- Confirm the file opens with title, status, and date
- Review links manually or with script support
- Confirm referenced paths exist
- Check domain assignment and steward ownership
- Check changelog, lineage, and dashboard impacts for major additions
- Confirm no artifact is described as canon without authority

## CI validation checklist

CI should prioritize fast, legible checks that fail loudly and explain why.
Current or target checks include:

- metadata presence on changed markdown files
- visible status header check
- existence of linked markdown targets for changed files
- canon-reference existence checks
- stale artifact reporting on schedule
- GPTBrain reference parity workflow where applicable

## Release-context validation

### Candidate publication

Candidate publication requires structural completeness, readable framing, and basic link integrity.

### Canon promotion

Canon promotion adds governance evidence, vote record, adjudication, and decision logging requirements.

### Public website publication

Website publication adds readability, summary quality, and public trust framing requirements on top of archive correctness.

## Failure handling

When a validation failure appears:

1. classify it as structural, governance, provenance, or freshness-related
2. assign the relevant steward
3. document whether the artifact remains publishable as Candidate
4. escalate to incident response if public trust or canon integrity is affected

## Evidence posture

Validation is not a substitute for truth, but it is the operating discipline that keeps the archive auditable.
Every Aetherforge improvement should make future validation cheaper, clearer, and more reliable.

## Related documents

- [QUALITY_GATES.md](./QUALITY_GATES.md)
- [QUALITY_DASHBOARD.md](./QUALITY_DASHBOARD.md)
- [../governance/PROVENANCE_REQUIREMENTS.md](../governance/PROVENANCE_REQUIREMENTS.md)
