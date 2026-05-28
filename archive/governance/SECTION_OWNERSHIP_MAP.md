# Section Ownership Map

*Atlas Lattice Foundation · Aetherforge Mission #4 · 2026-05-28*

status: candidate

> Mapping which council role or contributor owns each top-level section of the repository. Ownership means accountability for quality, review turnaround, and lifecycle decisions—not gating contributions.

---

## Ownership Model

Each section has:
- **Owner** — primary accountable party
- **Reviewer** — secondary review voice for PRs touching the section
- **Escalation** — ratification authority (always @atlaslattice for canon decisions)

---

## Top-Level Section Map

| Path | Section Name | Owner Role | Reviewer Role | Escalation |
|------|--------------|-----------|---------------|------------|
| `/archive/` | Artifact Archive | Archive Steward | Council Scribe | @atlaslattice |
| `/archive/boot/gptbrain/` | GPTBrain / TIDELOCKBrain | Brain-Keeper | CAS Auditor | @atlaslattice |
| `/archive/governance/` | Governance Spine | Governance Lead | Council Chair | @atlaslattice |
| `/archive/spec/` | Spec Vault | Spec Architect | Schema Guardian | @atlaslattice |
| `/archive/spec/gptdream/` | GPTDream++ Specs | Dream Architect | CAS Auditor | @atlaslattice |
| `/council/` | Council Records | Council Chair | Governance Lead | @atlaslattice |
| `/docs/` | Public Documentation | Docs Lead | Accessibility Rep | @atlaslattice |
| `/projects/` | Taskboards & Campaigns | Program Manager | Governance Lead | @atlaslattice |
| `/reference_impl/` | Reference Implementations | Engineering Lead | QA Lead | @atlaslattice |
| `/schemas/` | Schema Registry | Schema Guardian | Spec Architect | @atlaslattice |
| `/scripts/` | Automation Scripts | Automation Lead | Engineering Lead | @atlaslattice |
| `/tests/` | Test Suite | QA Lead | Engineering Lead | @atlaslattice |
| `.github/` | CI/CD Workflows | DevOps Lead | Security Champion | @atlaslattice |
| `README.md` | Public Entry Point | Docs Lead | Program Manager | @atlaslattice |
| `SECURITY.md` | Security Policy | Security Champion | Governance Lead | @atlaslattice |
| `CODE_OF_CONDUCT.md` | Community Standards | Community Lead | Council Chair | @atlaslattice |

---

## Sub-Archive Ownership

| Path | Owner Role |
|------|------------|
| `/archive/architecture/` | Systems Architect |
| `/archive/culture/` | Community Lead |
| `/archive/knowledge_graph/` | KG Engineer |
| `/archive/ops/` | DevOps Lead |
| `/archive/provenance/` | Archive Steward |
| `/archive/simulation/` | Dream Architect |
| `/archive/synthesis/` | Council Scribe |

---

## Role Roster Notes

Until the Atlas Lattice Foundation council is fully staffed, all roles are **held by @atlaslattice** as founding custodian. This map establishes the intended future ownership topology. As contributors join, ownership will be delegated following the ratification workflow.

---

## Related Documents

- [Ratification Workflow](./RATIFICATION_WORKFLOW.md)
- [Change Classification Rules](./CHANGE_CLASSIFICATION_RULES.md)
- [Governance Onboarding Guide](./GOVERNANCE_ONBOARDING_GUIDE.md)
- [Next-144 Taskboard](../../projects/aetherforge-next144-taskboard-2026-05-28.md)

---

*Maintained by Atlas Lattice Foundation · status: candidate until ratified*
