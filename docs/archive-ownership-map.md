# Archive Section Ownership Map

Status: candidate ownership map (not canon)

## Ownership Model

- Human root authority: @atlaslattice
- Review ownership model: CODEOWNERS + governance policy
- Merge rights and canon adjudication: governed by `/GOVERNANCE.md`

## Domain-to-Owner Map

| Domain | Primary owner role | Secondary reviewers | Reference |
|---|---|---|---|
| `/.github/` | Repo governance maintainers | Security/process reviewers | `/.github/CODEOWNERS` |
| `/archive/` | Council archival stewards | GPTBrain/TIDELOCK lanes | `/GOVERNANCE.md` |
| `/projects/` | Program execution maintainers | Council reviewers | `/projects/*.md` |
| `/docs/` | Public-readiness/documentation maintainers | Governance and security reviewers | `/docs/index.md` |
| `/codebases/` | Implementation maintainers | Test and security reviewers | `/codebases/tests/` |
| `/reference_impl/` | Reference implementation maintainers | Schema/test reviewers | `/reference_impl/` |
| `/schemas/` | Schema maintainers | Validation reviewers | `/schemas/` |
| `/council/` | Council records maintainers | Governance reviewers | `/council/` |

## Operational Rule

- Ownership is enforced in practice through CODEOWNERS review and branch protection checks.
