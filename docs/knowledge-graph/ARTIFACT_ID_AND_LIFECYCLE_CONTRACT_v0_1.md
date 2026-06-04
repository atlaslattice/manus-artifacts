# Artifact ID and Lifecycle Contract v0.1

> **Status:** CANDIDATE  
> **Artifact Type:** spec  
> **Stable ID:** AL-KG-003  
> **Date:** 2026-05-27

## Purpose

Define a shared ID grammar, relation vocabulary, and lifecycle progression contract for candidate artifacts in the Atlas Lattice knowledge graph.

## ID Grammar

`AL-<DOMAIN>-<SEQ>`

- Prefix: `AL`
- Domain: uppercase code (`MISSION`, `KG`, `AF`, `GP`, `RT`, `CI`, `EXEC`, `GOV`, `EVID`, `LOG`, `SYS`, `BRAIN`, `SCHEMA`, `TEST`, `ADR`, `HEALTH`)
- Sequence: three-digit zero-padded integer (`001`, `002`, ...)

### Domain Namespace (Current)

| Domain | Scope |
|---|---|
| MISSION | mission-level doctrine and alignment artifacts |
| KG | taxonomy, registry, and graph contracts |
| AF | Aetherforge gameplay/system artifacts |
| GP | GPTDream++ package/vault artifacts |
| RT | ratification and trust governance artifacts |
| CI | automation, validator, and CI workflow artifacts |
| EXEC | execution plans, sprints, and campaign artifacts |
| GOV | governance policy/baseline artifacts |
| EVID | machine-readable evidence artifacts |
| LOG | execution receipts and audit logs |
| SYS | subsystem documentation and implementation entrypoints |
| BRAIN | multi-agent manifests, protocols, and indexes |
| SCHEMA | schema bundles and suites |
| TEST | executable validation and adversarial suites |
| ADR | architecture decision records |
| HEALTH | generated health and coverage reports |

## Relation Vocabulary (v0.1)

Allowed relation verbs:

- `defines`
- `implements`
- `implemented_by`
- `extends`
- `operationalizes`
- `governs`
- `supports`
- `constrains`
- `validated_by`
- `indexes`
- `references`
- `referenced_by`
- `depends_on`
- `summarized_by`
- `prioritizes`
- `runs`
- `validates`
- `receipts_for`
- `evidence_for`
- `recorded_in`
- `part_of`
- `relates_to`
- `tested_by`
- `tests`
- `generated_by`
- `spec`

## Lifecycle Progression Contract

Canonical lifecycle states remain:

1. `DRAFT`
2. `CANDIDATE`
3. `RATIFIED`
4. `ARCHIVED`
5. `DEPRECATED`

### Allowed Forward Transitions

- `DRAFT -> CANDIDATE`
- `CANDIDATE -> RATIFIED`
- `CANDIDATE -> DEPRECATED`
- `RATIFIED -> ARCHIVED`
- `RATIFIED -> DEPRECATED`

### Transition Guards

- Promotion to `RATIFIED` requires council ratification and @atlaslattice adjudication.
- `ARCHIVED` artifacts are retained for provenance and must keep stable IDs.
- `DEPRECATED` artifacts remain addressable and must include an active replacement link when possible.

## Metadata Contract (v0.1)

Required metadata fields are defined in `artifact_taxonomy.v0_1.json`.
Recommended additions for graph quality:

- `provenance_origin`
- `created_date`
- `last_updated`
- `owner`
- `supersedes` (optional)

## Governance Boundary

All outputs in this contract are candidate-state semantics only; no canon promotion is implied by publication.
