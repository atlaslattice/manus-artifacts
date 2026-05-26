# Naming Conventions
Status: Candidate
Date: 2026-05-26

This specification standardizes naming, versioning, and identifier formats across the archive.
Consistent naming is essential for Aetherforge-scale navigation, lineage tracking, and public trust.

## Core principles

- Prefer human-readable names over opaque labels.
- Keep filenames stable after publication unless supersession requires a new file.
- Encode date and version only when they clarify authority or sequence.
- Align file names, artifact IDs, and metadata fields wherever possible.

## File naming rules

### Markdown files

Use `kebab-case` for new general-purpose markdown files.

Examples:

- `canon-lifecycle.md`
- `trust-charter.md`
- `mission-control-cadence.md`

Existing historical filenames may remain as-is when renaming would break provenance.
New files added after 2026-05-26 should follow the current standard unless preserving an established series.

### Date suffixes

Add a date suffix when the artifact is time-bound, release-bound, or part of a recurring series.

Format:

- `YYYY-MM-DD`

Example:

- `aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md`

Use date suffixes for:

- taskboards
- audit reports
- decision logs published as snapshots
- batch reports and public state-of-archive releases

### Directory names

Use lowercase kebab-case for directories.
Prefer stable domain containers over topical sprawl.

## Version string standard

The archive standard version string is:

`vX.Y.Z-YYYY-MM-DD`

Rules:

- `X` = major doctrinal or structural break
- `Y` = meaningful additive revision
- `Z` = minor corrective revision
- date = publication or adjudication date of that version snapshot

Examples:

- `v1.0.0-2026-05-26`
- `v4.0.0-2026-05-26`
- `v4.1.2-2026-07-03`

If a historic artifact already uses a simpler in-file version such as `v4.0`, preserve the historic label and map it to the normalized version string in metadata when needed.

## Artifact ID format

Use the following archive-wide artifact ID pattern for new high-governance records:

`AF-{DOMAIN}-{SERIES}-{NNNN}`

Components:

- `AF` = Aetherforge / archive program prefix
- `{DOMAIN}` = three-letter domain code
- `{SERIES}` = short series code
- `{NNNN}` = zero-padded sequence number

Examples:

- `AF-SYS-AOS-0001` — Systems / Aluminum OS
- `AF-PRJ-AFG-0007` — Projects / Aetherforge program artifact
- `AF-GOV-CDL-0012` — Governance / canon decision log
- `AF-RSH-SWP-0003` — Research / sweep report

## Domain prefixes

| Domain | Prefix | Use case |
| --- | --- | --- |
| Systems | `SYS` | Aluminum OS, GPTBrain, SheldonBrain, BAZINGA |
| Projects | `PRJ` | Free Bank, Chinook Guardian, Three-Tier Autonomy, Aetherforge |
| Governance | `GOV` | Council records, policies, audits, decision logs |
| Research | `RSH` | Intelligence sweeps, synthesis, studies |
| Health | `HLT` | Patient rights and wellness artifacts |
| Vault | `VLT` | Continuity, checkpoint, and memory preservation surfaces |

## Recommended series codes

- `AOS` — Aluminum OS
- `GPB` — GPTBrain
- `SHB` — SheldonBrain
- `BZG` — BAZINGA
- `AFG` — Aetherforge
- `FBK` — Free Bank
- `CHG` — Chinook Guardian
- `TTA` — Three-Tier Autonomy
- `CDL` — Canon decision log
- `AUD` — Audit output

## Practical rules

- Prefer new file creation over silent overwrite when doctrine materially changes.
- Use lineage fields such as `supersedes` and `superseded_by` to connect versions.
- Avoid spaces, ambiguous abbreviations, and unstable nicknames in filenames.
- Preserve historical filenames when they are already part of the provenance chain.

## Related documents

- [METADATA_SCHEMA.md](./METADATA_SCHEMA.md)
- [ARTIFACT_LINEAGE.md](./ARTIFACT_LINEAGE.md)
- [../governance/RETENTION_POLICY.md](../governance/RETENTION_POLICY.md)
