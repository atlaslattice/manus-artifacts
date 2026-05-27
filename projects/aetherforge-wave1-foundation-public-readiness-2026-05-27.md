# Aetherforge Wave 1 Foundation Pack — Public Readiness (2026-05-27)

Status: `active implementation artifact` (candidate)

This pack implements Wave 1 tasks (1–12) from the 144-task campaign board.

## 1) Public-readiness rubric

Use this rubric before publishing any artifact:

- **Audience clarity**: purpose and intended reader are explicit.
- **Source traceability**: claims link to source artifact(s).
- **Safety check**: sensitive data and private identifiers removed.
- **Governance fit**: canon/candidate status is explicitly labeled.
- **Reproducibility**: validation path exists (tests/checks/manual steps).
- **Discoverability**: artifact is linked from at least one index.

## 2) World-class quality bar

An artifact is "world-class" when it is:

- Accurate and internally consistent.
- Well-structured, navigable, and cross-linked.
- Verifiable through documented checks.
- Durable (clear ownership, update cadence, and changelog path).
- Useful to both first-time readers and maintainers.

## 3) Repo-wide visibility policy

Visibility tiers:

- **Public**: default tier; safe for open publication.
- **Review-required**: needs manual review before publication.
- **Restricted**: do not publish until explicitly cleared.

Policy rule: new artifacts should declare their tier in a short metadata header.

## 4) Folder audience classification

Top-level audience classes:

- **Public readers**: `README.md`, `projects/`, `about/`, `docs/`, `research/`.
- **Builders/contributors**: `.github/`, `scripts/`, `tests/`, `schemas/`, `fixtures/`.
- **Operational/archive lanes**: `archive/`, `archives/`, `manus-vault/`, `council/`, `council-reviews/`.

## 5) Sensitive vs public-safe artifact marking

Required labels for markdown artifacts:

- `Sensitivity: public-safe`
- `Sensitivity: review-required`
- `Sensitivity: restricted`

Default behavior: if missing, treat as `review-required`.

## 6) Release-readiness checklist

Before publishing a release batch:

- [ ] Rubric passed
- [ ] Sensitivity labels present
- [ ] Canon/candidate status present
- [ ] Links validated
- [ ] Relevant tests/checks passed
- [ ] Changelog/reference updates completed

## 7) Canonical terminology glossary

- **Canon**: ratified artifact approved by council process.
- **Candidate**: non-ratified artifact under active iteration.
- **Mirror**: synchronized representation, not authority by default.
- **Provenance**: evidence trail for claims and decisions.
- **Trust state**: confidence and adjudication status for an artifact.

## 8) Contributor mission statement

Build a transparent, verifiable, public knowledge graph artifact repository that is useful, auditable, and continuously improvable.

## 9) Repository north-star KPIs

Track monthly:

- Percent of artifacts with explicit sensitivity labels.
- Percent of top-level lanes with index/navigation coverage.
- Link integrity pass rate.
- Test/check pass rate on main validation workflows.
- Candidate-to-ratified progression count.

## 10) Operating principles

- Public-by-default with explicit safety gates.
- Provenance over assertion.
- Canon clarity over ambiguity.
- Reproducibility over implied correctness.
- Incremental delivery with visible status.

## 11) Publication cadence

- **Weekly**: campaign board updates and completed-task links.
- **Biweekly**: documentation quality and navigation refresh.
- **Monthly**: KPI snapshot and governance transparency summary.

## 12) Public launch roadmap (Wave 1 perspective)

- **Phase A**: establish policy + rubric + glossary (this pack).
- **Phase B**: classify and label critical top-level artifacts.
- **Phase C**: publish KPI baseline and first transparency report.
- **Phase D**: begin Wave 2 IA/navigation execution.

## Linked campaign source

- `/tmp/workspace/atlaslattice/manus-artifacts/projects/aetherforge-144-task-campaign-2026-05-27.md`
