# CHANGELOG

All notable changes to the Atlas Lattice repository are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to a date-based versioning scheme (YYYY-MM-DD milestones rather than semver, as this is a knowledge archive rather than a software package).

status: candidate

---

## [Unreleased]

### Added

- Wave 3 Repository Architecture Pack: navigation standards, breadcrumb standards, index of indexes, archive taxonomy map, file placement decision tree, duplicate docs triage, stale artifact quarantine lane, canonical path map, role-based landing paths (#25–#36)
- Wave 2 Legal/Trust Pack: license audit, attribution inventory, trademark guide, PII redaction rubric, sensitive content review process, export control checklist, data retention policy, vulnerability disclosure process, incident response runbook, compliance evidence index, public risk register, quarterly audit template (#13–#24)
- Wave 1 Governance Completion: section ownership map, review SLA policy, council review cadence, change classification rules, deprecation policy, governance onboarding guide (#4–#12)
- Wave 5 Knowledge Graph Pack (tasks #50–#60): 10 new KG governance/spec artifacts completing the KG Layer wave
  - `archive/governance/PERSISTENT_ARTIFACT_ID_STANDARD.md` — artifact ID scheme (#50)
  - `archive/governance/CROSSLINK_DENSITY_TARGETS.md` — min link requirements (#51)
  - `archive/governance/ONTOLOGY_RELATION_TYPES.md` — 14 typed KG relations (#52)
  - `archive/governance/MACHINE_READABLE_CITATION_BLOCKS.md` — cite block standard (#53)
  - `archive/governance/PROVENANCE_GRAPH_EXPORT_SPEC.md` — JSON-LD/TSV/DOT export spec (#54)
  - `archive/governance/ORPHAN_NODE_DETECTION_POLICY.md` — orphan detection and resolution (#56)
  - `archive/governance/TAG_GOVERNANCE_RULES.md` — controlled tag vocabulary (#57)
  - `archive/governance/SEARCH_RELEVANCE_BASELINE_REPORT.md` — baseline benchmark (#58)
  - `archive/governance/KG_VISUALIZATION_SURFACE_DESIGN.md` — D3.js graph viz design (#59)
  - `archive/governance/KG_PUBLIC_API_ROADMAP.md` — public API phases (#60)
  - `archive/governance/METADATA_HEADERS_STANDARD.md` — YAML frontmatter schema standard (#37)
  - `archive/governance/EXECUTIVE_SUMMARIES_STANDARD.md` — when and how to write exec summaries (#38)
  - `docs/PROJECT_BRIEFS.md` — one-page briefs for all core projects (#39)
  - `docs/GLOSSARY.md` — expanded with Aetherforge, GPTDream++, KG, Lattice KG, Wave, TIDELOCKBrain, ORCS, Breadcrumb, Wake Report terms (#40)
  - `archive/governance/TERMINOLOGY_CONSISTENCY_REPORT.md` — 18-finding consistency audit (#41)
  - `archive/governance/EDITORIAL_STYLE_GUIDE.md` — prose and style rules (#42)
  - `archive/governance/DOCS_LINT_QUALITY_GATES.md` — 5 active CI quality gates documented (#43)
  - `archive/governance/READABILITY_QUALITY_THRESHOLDS.md` — Flesch targets by doc category (#44)
  - `CHANGELOG.md` — root changelog established; `archive/governance/CHANGELOG_DISCIPLINE_POLICY.md` (#45)
  - `archive/governance/RELEASE_NOTES_FORMAT_STANDARD.md` — wave release notes template (#46)
  - `docs/NEWCOMER_FAQ.md` — onboarding FAQ (#47)
  - `docs/TOP_ARTIFACTS.md` — curated artifact collection (#48)
- `scripts/README.md` — scripts directory index

---

## [2026-05-28] — Waves 1-3 Foundation Sprint

### Added

- Aetherforge Next-144 Execution Taskboard (`projects/aetherforge-next144-taskboard-2026-05-28.md`)
- Next-144 GitHub Issue Seeding Pack (`projects/aetherforge-next144-github-issue-seeding-pack-2026-05-28.md`)
- Naming conventions (#30) via `docs/NAMING_CONVENTIONS.md`
- TIDELOCK Children of the Swarm security pack work logs
- TIDELOCK Wave 2 governance spine work logs
- Lattice KG quality gates — CI workflow and validation scripts

### Completed (Missions)

- #1 Define canonical status model
- #2 Publish ratification workflow
- #3 Create canon decision ledger
- #5 Add RFC proposal template
- #10 Standardize provenance requirements
- #11 Track artifact lifecycle states
- #26 Complete missing folder READMEs
- #30 Define naming conventions
- #34 Drive broken links to zero
- #49 Adopt universal frontmatter schema
- #55 Add KG integrity validation
- #62 Add markdown lint workflow

---

## [2026-05-26] — GPTDream++ Vault Build

### Added

- GPTDream++ full spec vault: 10 appendix documents in `archive/spec/gptdream/`
- 15 Atlas/ORCS YAML schemas in `schemas/atlas_orcs/v0_1/`
- O_AI schemas in `schemas/o_ai/v0_1/`
- Native thread schema in `schemas/native_thread/v0_1/`
- Python reference implementations: `reference_impl/atlas_orcs/`, `reference_impl/execution_gate/`, `reference_impl/native_thread/`
- T01–T12 adversarial tests in `tests/adversarial/`
- 63 total tests, all passing
- TIDELOCKBrain 1000Y dream journal, wake report, delta extraction

---

## [2026-05-09] — Foundation Archive

### Added

- GPTBrain boot system: `archive/boot/gptbrain/`
- Initial governance spine, council session records
- KRAKOA Living Archive Charter
- S1 variant synthesis and ratification packets
- Aluminum OS v4.0 Unified Field (canonical)
- BAZINGA v0.1 launch decree
- SheldonBrain system architecture
- Initial README with full project overview

---

*CHANGELOG maintained by Atlas Lattice Foundation · status: candidate*
