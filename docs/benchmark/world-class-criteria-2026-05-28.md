# World-Class Public Repository Criteria — 2026-05-28

> *Status: CANDIDATE — not canon until ratified by @atlaslattice*

## What This Document Is

This rubric defines what “world class” means for a public Atlas Lattice repository. The goal is not aesthetic polish alone; it is durable public trust, fast newcomer comprehension, strong governance legibility, and enough evidence that ambitious claims feel inspectable instead of theatrical.

## 1. README Quality

| Criterion | Description | What “world class” looks like |
|---|---|---|
| Clear mission | The landing page states why the repository exists and why an outsider should care. | A first-time visitor can explain the repo mission in one sentence after 30 seconds. |
| Navigation table | The README provides role-based or task-based pathways into the archive. | Newcomers, engineers, researchers, and contributors each have an obvious path without guesswork. |
| Trust badges | Public status badges show CI, license, security, and key repo health signals. | Badges are current, meaningful, and reinforce trust rather than act as decoration. |

## 2. Documentation Depth

| Criterion | Description | What “world class” looks like |
|---|---|---|
| Architecture docs | The repository explains how major systems fit together. | Core system boundaries, layers, and interactions are documented in diagrams and prose. |
| Glossary | Domain language is defined so newcomers are not forced to decode private jargon. | Specialized terms are consistently defined and cross-linked wherever they appear. |
| Decision records | Important choices and tradeoffs are documented over time. | Readers can trace why major structural decisions were made and what alternatives were rejected. |

## 3. Governance Rigor

| Criterion | Description | What “world class” looks like |
|---|---|---|
| Clear policies | Contribution, security, canon-boundary, and review policies are easy to find. | Governance docs are concise, public, and enforced through process rather than vibes. |
| Ratification flow | The path from candidate artifact to authoritative artifact is explicit. | Promotion rules are documented, reviewable, and difficult to game. |
| Transparency | Readers can see who made decisions, how they were reviewed, and what remains unresolved. | Open questions, review queues, and authority boundaries are surfaced publicly. |

## 4. Knowledge Graph

| Criterion | Description | What “world class” looks like |
|---|---|---|
| Stable IDs | Important artifacts have durable identifiers. | IDs are machine-readable, non-ambiguous, and used consistently across docs and tooling. |
| Cross-links | Artifacts link to adjacent context instead of existing as dead ends. | Readers and scripts can move easily between doctrine, implementation, evidence, and review. |
| Registry completeness | The graph covers enough of the repository to be operationally useful. | Most high-value artifacts are registered, typed, and linked with minimal orphaned content. |

## 5. Validation Automation

| Criterion | Description | What “world class” looks like |
|---|---|---|
| CI coverage | Continuous integration checks the claims the repo makes about itself. | Core docs, graphs, tests, and hygiene all run automatically on every relevant change. |
| Test suite | Executable systems have a meaningful, maintained test surface. | Tests cover core contracts and fail loudly when promises drift. |
| Validation scripts | Specialized repository rules are encoded, not just described. | Canon, provenance, link, and schema checks are reproducible locally and in CI. |

## 6. Contributor Experience

| Criterion | Description | What “world class” looks like |
|---|---|---|
| CONTRIBUTING guide | Contributors can understand the rules before they touch anything. | The guide is short, specific, and maps directly to validation commands and review flow. |
| Ownership signals | CODEOWNERS, reviewers, and maintainership expectations are visible. | Responsibility boundaries are explicit, making review routing predictable. |
| Templates & decision tree | Issue, PR, and routing templates reduce ambiguity. | Contributors know what kind of change they are making and which path to follow. |

## 7. Evidence & Provenance

| Criterion | Description | What “world class” looks like |
|---|---|---|
| AI-built claim evidence | AI-generated claims are paired with receipts and source paths. | Major claims can be audited without trusting narration alone. |
| Receipts | Build, review, and execution artifacts are preserved. | Receipts exist for consequential changes and are linked from summary docs. |
| Audit trail | Readers can trace how work moved from idea to candidate artifact. | Provenance is durable, queryable, and connected to review outcomes. |

## 8. Discoverability

| Criterion | Description | What “world class” looks like |
|---|---|---|
| Topic pages | Major domains have dedicated landing pages. | Every important domain has a clear overview page with start-here guidance. |
| Reading paths | Different audiences can find relevant entry points fast. | Persona-based reading paths exist at both repo and domain level. |
| Persona guides | Public docs acknowledge distinct user needs. | Engineers, researchers, policymakers, and contributors can each orient in minutes. |

## Related Documents

- [Benchmark Index](./README.md) — index of all benchmark artifacts.
- [Comparison Repositories](./comparison-repos-2026-05-28.md) — concrete public examples against this rubric.
- [Benchmark Scorecard](./scorecard-2026-05-28.md) — current Atlas Lattice scoring against these dimensions.

---
*Atlas Lattice Foundation · Austin, Texas*
