# Directory Maturity Labels

Status: candidate maturity model (not canon)

## Maturity Levels

- **L0 Seed**: exploratory, unstable, minimal structure.
- **L1 Structured**: coherent structure and baseline documentation present.
- **L2 Operational**: repeatable workflows, validation checks, and ownership signals in place.
- **L3 Hardened**: governance/security controls and quality gates consistently enforced.
- **L4 Public-Ready**: clear navigation, provenance discipline, and launch-grade transparency.

## Initial Labels (Working Assignment)

| Directory | Label | Rationale |
|---|---|---|
| `/.github/` | L3 Hardened | templates, workflows, CODEOWNERS, security policy present |
| `/docs/` | L2 Operational | health dashboard and evidence docs; IA sprint now added |
| `/projects/` | L2 Operational | active execution boards and sprint artifacts |
| `/archive/` | L2 Operational | rich historical substrate, candidate-canon heavy |
| `/codebases/` | L1 Structured | heterogeneous implementations with partial testing |
| `/reference_impl/` | L2 Operational | reference logic + tests in selected surfaces |
| `/schemas/` | L2 Operational | structured schema repository with versioned dirs |

## Upgrade Rule

A directory can be promoted one level when its required controls for that level are continuously satisfied for at least one wave/sprint cycle.
