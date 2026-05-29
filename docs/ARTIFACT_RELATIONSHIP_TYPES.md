# Artifact Relationship Types
Status: Candidate
Date: 2026-05-27

This specification defines relationship labels for the lattice knowledge graph.
Use these labels in prose, tables, indexes, and future metadata automation.

## Core relationship set

| Relationship | Meaning | Direction |
| --- | --- | --- |
| `supersedes` | Replaces a predecessor artifact in lineage. | successor -> predecessor |
| `superseded_by` | Points to the current successor artifact. | predecessor -> successor |
| `supports` | Provides evidence, implementation context, or reinforcement. | supporting -> supported |
| `depends_on` | Requires the target artifact to be interpreted or executed correctly. | dependent -> dependency |
| `governs` | Defines authority constraints for another artifact. | governance artifact -> governed artifact |
| `implements` | Converts doctrine/spec into executable or operational form. | implementation -> doctrine/spec |
| `summarizes` | Provides compressed interpretation of a larger source artifact. | summary -> source |
| `indexes` | Organizes or maps a set of artifacts for navigation. | index -> collection |
| `tests` | Validates behavior or structure of another artifact/spec. | test artifact -> target artifact |
| `publishes` | Announces or exposes content to a public-facing surface. | publication surface -> published artifact |

## Required use

- Use `supersedes` and `superseded_by` whenever formal lineage changes occur.
- Use at least one of `supports`, `depends_on`, or `governs` when cross-domain links are added.
- Use `implements` from reference code or protocol docs to their governing specs.
- Use `tests` from test files or suites to reference implementations or schema packs.

## Canon boundary reminder

Relationship labels describe structure, not authority.
An artifact may have rich relationships and still remain Candidate until formal ratification and adjudication.

## Related

- [ARTIFACT_LINEAGE.md](./ARTIFACT_LINEAGE.md)
- [CROSS_DOMAIN_LINK_POLICY.md](./CROSS_DOMAIN_LINK_POLICY.md)
