# Artifact Lineage
Status: Candidate
Date: 2026-05-26

Artifact lineage is the archive mechanism for showing how one document evolves into another over time.
It prevents context loss, clarifies supersession, and preserves the history that public readers need to interpret doctrine correctly.

## Lineage model

Use two directional fields and one narrative rule:

- `supersedes` points backward to prior artifacts or versions.
- `superseded_by` points forward to the current successor.
- The narrative header should explain the reason for the transition when the shift is materially important.

## What counts as a lineage relationship

A lineage relationship exists when one artifact:

- formally replaces another
- consolidates multiple predecessors
- forks into separate successor tracks
- preserves a historical concept while changing operational guidance

Mere topical similarity is not enough.

## Major known lineage chains

### Aluminum OS progression

| Stage | Artifact | Notes |
| --- | --- | --- |
| v1 antecedent | Historical conceptual precursor | Referenced as an antecedent in archive narratives; not yet normalized in-repo as a formal file |
| v2 | [v2.0 Integrated Constitutional Substrate](../aluminum-os/v2.0-integrated-constitutional-substrate.md) | First visible repository-era integrated systems baseline |
| v3 | [v3.0 Unified Field](../aluminum-os/v3.0-unified-field.md) | Expanded synthesis and unification layer |
| v4 | [v4.0 Unified Field](../aluminum-os/v4.0-unified-field.md) | Current high-signal systems synthesis artifact |
| companion | [v4.0 Socratic OS Integration Report](../aluminum-os/v4.0-socratic-os-integration-report.md) | Adjacent implementation and integration context |

### BAZINGA launch lineage

| Stage | Artifact | Notes |
| --- | --- | --- |
| v0.1 | [v0.1 Launch Decree](../bazinga/v0.1-launch-decree.md) | Foundational BAZINGA launch and framing artifact |
| next step | Future protocol or execution supplements | Should point back to the launch decree when formalized |

### Project lineage surfaces

| Project | Current visible anchor | Likely lineage pattern |
| --- | --- | --- |
| Aetherforge | [Metatron Top 50 Taskboard](../projects/aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md) | time-stamped program board series |
| Free Bank | [Banking Revolution Archive](../projects/free-bank/banking-revolution-archive.md) | doctrine -> roadmap -> execution reports |
| Chinook Guardian | [v1.0](../projects/chinook-guardian/v1.0.md) | doctrine -> review -> release packages |
| Three-Tier Autonomy | [Doctrine](../projects/three-tier-autonomy/doctrine.md) | versioned policy lineage |

## Tracking format

Use a short lineage note whenever supersession occurs.

Example:

```text
Lineage note: This artifact supersedes aluminum-os/v3.0-unified-field.md
because it consolidates doctrine, implementation framing, and public-facing synthesis.
```

## Lineage review rules

- Every canon promotion should check for predecessor links.
- Archived artifacts should point to successors when one exists.
- Deprecated artifacts should point to both a successor and a warning rationale.
- Dashboards and maturity maps should prefer the latest non-deprecated artifact in a chain.

## Why lineage matters

Without lineage, a public archive looks like a pile of documents.
With lineage, it becomes a navigable historical system that shows how Aetherforge concepts mature across the five rings.

## Related documents

- [METADATA_SCHEMA.md](./METADATA_SCHEMA.md)
- [CANON_LIFECYCLE.md](./CANON_LIFECYCLE.md)
- [../governance/RETENTION_POLICY.md](../governance/RETENTION_POLICY.md)
