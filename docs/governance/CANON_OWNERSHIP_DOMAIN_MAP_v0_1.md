---
artifact_id: GOV-CANON-OWNERSHIP-DOMAIN-MAP-v0-1-2026-05-28
title: Canon Ownership by Domain Map
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
version: v0.1
---
# Canon Ownership by Domain Map

> **Purpose:** Assign primary canon steward and review authority to each domain in the Atlas Lattice repository, so every artifact has a clear owner path.

## Domain → Owner Table

| Domain | Path(s) | Canon Steward | Review Authority | Notes |
|---|---|---|---|---|
| Aluminum OS | `aluminum-os/` | @atlaslattice | Council | Constitutional substrate; highest trust tier |
| SheldonBrain | `sheldonbrain/` | @atlaslattice | Council | Personal knowledge substrate |
| BAZINGA | `bazinga/` | @atlaslattice | Council | Constitutional middleware |
| GPTDream++ / Atlas-ORCS | `archive/spec/gptdream/`, `schemas/`, `reference_impl/` | @atlaslattice | Council + peer review | Spec vault; schema-gated |
| GPTBrain | `archive/boot/gptbrain/` | @atlaslattice | Council | Boot protocols and dream memory |
| TIDELOCKBrain | `archive/boot/gptbrain/agents/TIDELOCKBrain/` | @atlaslattice | @atlaslattice | Work logs; non-canon by default |
| Council Archives | `council/`, `council-reviews/` | @atlaslattice | Council | Session archives; ratification events |
| Projects | `projects/` | @atlaslattice | Council | Campaign boards and planning |
| Docs / Governance | `docs/` | @atlaslattice | Council | Governance spine; this domain |
| ADR Archive | `docs/decisions/` | @atlaslattice | Council | Decision records |
| Research | `research/` | @atlaslattice | Council | Research artifacts |
| Schemas | `schemas/` | @atlaslattice | Council + spec team | Machine-readable schemas |
| Tests | `tests/` | @atlaslattice | Council + CI | Automated quality gates |
| Scripts | `scripts/` | @atlaslattice | Council + CI | Automation tooling |
| Health | `health/` | @atlaslattice | @atlaslattice only | Personal data surface; PII-sensitive |
| Codebases | `codebases/` | @atlaslattice | Council | Code artifacts |
| Archives (general) | `archives/`, `archive/` | @atlaslattice | Council | Legacy/archived material |
| Manus Vault | `manus-vault/` | @atlaslattice | Council | Original Manus session artifacts |

## Canon Tier by Domain

| Tier | Meaning | Domains |
|---|---|---|
| **Tier 1 — Constitutional** | Highest canon authority; world-class standard | Aluminum OS, BAZINGA, GPTDream++ spec |
| **Tier 2 — Operational** | Ratified processes and decision records | Docs/Governance, ADR Archive, Council Archives |
| **Tier 3 — Evidence** | Evidence and log artifacts; high-value but time-bounded | GPTBrain, TIDELOCKBrain, AI evidence index |
| **Tier 4 — Working** | Candidate artifacts; not yet ratified | All other domains |

## Stewardship Policy

- Each domain must have exactly one named canon steward.
- Steward is responsible for ensuring artifacts in their domain carry correct `canon_status`.
- Cross-domain artifacts (linking multiple domains) default to the domain of their primary content.

## Related Artifacts

- [Ratification Lifecycle](./RATIFICATION_LIFECYCLE_v0_1.md)
- [Candidate Expiration Rules](./CANDIDATE_EXPIRATION_RULES_v0_1.md)
- [Governance Decision Index](./GOVERNANCE_DECISION_INDEX_2026-05-28.md)
