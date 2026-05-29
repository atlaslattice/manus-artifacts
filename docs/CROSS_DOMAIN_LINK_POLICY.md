# Cross-Domain Link Policy
Status: Candidate
Date: 2026-05-27

This policy sets minimum link density so "everything connects to everything" is implemented consistently.

## Scope

Applies to high-visibility artifacts in:

- `docs/`
- `projects/`
- `governance/`
- `archive/spec/gptdream/`
- `schemas/`
- `reference_impl/`
- `tests/`

## Minimum-link policy

For every new or materially updated flagship artifact:

1. Include at least **2 outbound links** to relevant artifacts in different domains.
2. Include at least **1 governance or validation link**.
3. Include at least **1 return-path link** from an index/board/map artifact where practical.
4. Prefer explicit relationship wording from [ARTIFACT_RELATIONSHIP_TYPES.md](./ARTIFACT_RELATIONSHIP_TYPES.md).

## "See also" block standard

Use a `## Related` or `## See also` section near the end of the file with:

- 1 doctrine/system link
- 1 execution/project link
- 1 governance/validation link

## Exceptions

Exceptions are allowed for leaf artifacts with narrow purpose, but must be noted in the artifact body with a short rationale.

## Validation

During review, verify:

- links resolve
- links are cross-domain
- authority boundaries are not misrepresented as canon

## Related

- [LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md](./LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md)
- [PUBLIC_ARCHIVE_MAP.md](./PUBLIC_ARCHIVE_MAP.md)
- [VALIDATION_PLAYBOOK.md](./VALIDATION_PLAYBOOK.md)
