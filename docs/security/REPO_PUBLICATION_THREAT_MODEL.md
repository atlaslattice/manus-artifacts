# Repository Publication Threat Model

Status: candidate threat model (not canon)

## Scope

Threat model for publishing and operating this repository as a public,
provenance-first open-source artifact surface.

## Assets

- Source artifacts and governance records
- CI workflows and automation paths
- Release artifacts and metadata
- Contributor trust + provenance trails

## Primary Threats

1. **Credential leakage**
   - Exposure in history, docs, workflow logs, or generated artifacts.
2. **Supply chain compromise**
   - Malicious dependency updates or compromised build actions.
3. **Integrity tampering**
   - Unauthorized artifact changes without clear provenance.
4. **Governance confusion**
   - Misinterpretation of candidate artifacts as canon.
5. **Overclaim/reliability drift**
   - AI evidence assertions without sufficient lineage.

## Existing Controls

- SECURITY.md reporting path
- CodeQL + repo hygiene workflows
- Link/metadata/orphan quality gates
- Canon candidate tracking and governance policy docs
- Explicit candidate/non-canon labels across governance surfaces

## Planned Controls

- Branch protection + required checks (settings)
- Signed release tags
- License compliance checks
- Artifact checksum publishing
- AI evidence integrity checker in CI

## Residual Risks

- Legacy artifact quality variance in deep archive layers
- Manual settings drift if owner actions are not completed
- False confidence from partial scans without periodic review
