# Artifact Relationship Types (v0.1)

> **Status:** Candidate  
> **Purpose:** Standardize how artifacts connect in the lattice knowledge graph.

## Core relationship types

| Relationship | Meaning | Example |
|---|---|---|
| `frames` | Defines mission or context for downstream artifacts | `README.md` `frames` `projects/aetherforge-top10-taskboard-2026-05-26.md` |
| `indexes` | Serves as a navigation hub | `docs/ARCHIVE_INDEX.md` `indexes` `archive/boot/gptbrain/` |
| `implements` | Executes a planned or protocol-defined action | `archive/boot/gptbrain/reference_impl/run_checks.sh` `implements` `gptbrain-reference-checks.yml` behavior |
| `derives_from` | Built from source context or prior artifact lineage | Wake report `derives_from` dream/play log |
| `validates` | Provides test/check evidence for a target artifact | `python -m pytest -q` run `validates` reference implementation |
| `routes_to` | Sends work to a review/decision lane | Taskboard item `routes_to` council review |
| `supersedes` | Replaces prior variant while preserving lineage | New index version `supersedes` old index |
| `constrains` | Imposes policy boundaries on output | `.github/CONTRIBUTING.md` `constrains` canon claims |

## Minimum linking guidance

- Every high-visibility artifact should include at least one inbound and one outbound relation.
- Protocol outputs should explicitly include `derives_from` and `routes_to` semantics.
- Workboard tasks should include a `routes_to` or `validates` destination before marked complete.
