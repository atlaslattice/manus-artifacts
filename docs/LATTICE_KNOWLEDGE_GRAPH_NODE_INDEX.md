# Lattice Knowledge Graph Node Index
Status: Candidate
Date: 2026-05-27

This index seeds the functional lattice knowledge graph so repository navigation is explicit, relational, and auditable.

## Node classes

- **Doctrine nodes**: systems-level conceptual artifacts.
- **Program nodes**: project execution artifacts and boards.
- **Governance nodes**: authority, review, and adjudication controls.
- **Validation nodes**: quality checks, tests, and scoreboards.
- **Protocol nodes**: GPTDream++ specifications, schemas, and implementations.

## Seed nodes (v0.1)

| Node ID | Type | Path | Primary links |
| --- | --- | --- | --- |
| N-README | Program | [../README.md](../README.md) | N-ROADMAP, N-TOP50, N-START |
| N-ROADMAP | Program | [./ROADMAP.md](./ROADMAP.md) | N-TOP50, N-QUEST, N-MISSION |
| N-START | Program | [./START_HERE.md](./START_HERE.md) | N-KG-POLICY, N-MAP, N-QUEST |
| N-TOP50 | Program | [../projects/aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md](../projects/aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md) | N-TOP10, N-QUEST, N-QUALITY |
| N-TOP10 | Program | [../projects/aetherforge-top10-taskboard-2026-05-26.md](../projects/aetherforge-top10-taskboard-2026-05-26.md) | N-TOP50, N-QUALITY |
| N-QUEST | Program | [../projects/AETHERFORGE_PUBLIC_QUESTBOARD_v0.1.md](../projects/AETHERFORGE_PUBLIC_QUESTBOARD_v0.1.md) | N-TOP50, N-WEEKLY, N-QUALITY |
| N-KG-POLICY | Governance | [./CROSS_DOMAIN_LINK_POLICY.md](./CROSS_DOMAIN_LINK_POLICY.md) | N-MAP, N-REL-TYPES |
| N-REL-TYPES | Governance | [./ARTIFACT_RELATIONSHIP_TYPES.md](./ARTIFACT_RELATIONSHIP_TYPES.md) | N-LINEAGE, N-KG-POLICY |
| N-MAP | Program | [./PUBLIC_ARCHIVE_MAP.md](./PUBLIC_ARCHIVE_MAP.md) | N-TAXONOMY, N-KG-POLICY |
| N-TAXONOMY | Doctrine | [./ARCHIVE_TAXONOMY.md](./ARCHIVE_TAXONOMY.md) | N-MAP, N-START |
| N-LINEAGE | Governance | [./ARTIFACT_LINEAGE.md](./ARTIFACT_LINEAGE.md) | N-REL-TYPES, N-CANON-LIFECYCLE |
| N-CANON-LIFECYCLE | Governance | [./CANON_LIFECYCLE.md](./CANON_LIFECYCLE.md) | N-CANON-BOUNDARY, N-QUALITY |
| N-CANON-BOUNDARY | Governance | [./CANON_BOUNDARY.md](./CANON_BOUNDARY.md) | N-CANON-LIFECYCLE, N-MISSION |
| N-QUALITY | Validation | [./QUALITY_GATES.md](./QUALITY_GATES.md) | N-VALIDATION, N-WEEKLY |
| N-VALIDATION | Validation | [./VALIDATION_PLAYBOOK.md](./VALIDATION_PLAYBOOK.md) | N-QUALITY, N-GPTDREAM-SURFACE |
| N-WEEKLY | Governance | [./WEEKLY_DELTA_DIGEST_TEMPLATE.md](./WEEKLY_DELTA_DIGEST_TEMPLATE.md) | N-QUEST, N-MISSION |
| N-GPTDREAM-SURFACE | Protocol | [../archive/spec/gptdream/README.md](../archive/spec/gptdream/README.md) | N-SCHEMAS, N-REFERENCE, N-TESTS |
| N-SCHEMAS | Protocol | [../schemas/README.md](../schemas/README.md) | N-GPTDREAM-SURFACE, N-REFERENCE |
| N-REFERENCE | Protocol | [../reference_impl/README.md](../reference_impl/README.md) | N-GPTDREAM-SURFACE, N-TESTS |
| N-TESTS | Validation | [../tests/README.md](../tests/README.md) | N-REFERENCE, N-VALIDATION |
| N-MISSION | Governance | [../governance/MISSION_CONTROL_CADENCE.md](../governance/MISSION_CONTROL_CADENCE.md) | N-WEEKLY, N-TOP50 |

## Operational rule

Any new flagship artifact should attach at least one inbound and one outbound link using relationship types from [ARTIFACT_RELATIONSHIP_TYPES.md](./ARTIFACT_RELATIONSHIP_TYPES.md).

## Related

- [CROSS_DOMAIN_LINK_POLICY.md](./CROSS_DOMAIN_LINK_POLICY.md)
- [PUBLIC_ARCHIVE_MAP.md](./PUBLIC_ARCHIVE_MAP.md)
