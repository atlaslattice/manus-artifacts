# CHANGELOG

All notable changes to the Atlas Lattice repository are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to a date-based versioning scheme (YYYY-MM-DD milestones rather than semver, as this is a knowledge archive rather than a software package).

status: candidate

---

## [Unreleased]

### Added

- Wave 12 Launch & World-Class Operations Pack (tasks #133–#144): 12 new launch/operations governance artifacts
  - `archive/governance/WORLDCLASS_SCORECARD_FRAMEWORK.md` — 144-mission scoring rubric and world-class threshold (#133)
  - `archive/governance/WORLDCLASS_SCORECARD_BASELINE.md` — initial 144-category baseline and gap-to-target summary (#134)
  - `archive/governance/V1_MILESTONE_PLAN.md` — milestone path and acceptance criteria for v1.0 (#135)
  - `archive/governance/RELEASE_TRAIN_CALENDAR.md` — CalVer release rhythm and launch timetable (#136)
  - `archive/governance/KPI_DASHBOARD_DESIGN.md` — KPI board layout and operating metrics (#137)
  - `archive/governance/TOP_OSS_BENCHMARK_REPORT.md` — comparator benchmark against exemplar OSS repositories (#138)
  - `archive/governance/QUARTERLY_OBJECTIVE_REVIEW.md` — quarterly review loop for objectives and launch readiness (#139)
  - `archive/governance/STATE_OF_LATTICE_REPORT_TEMPLATE.md` — recurring state-of-project report template (#140)
  - `archive/governance/PUBLIC_CHANGELOG_DIGEST_TEMPLATE.md` — public digest format derived from the root changelog (#141)
  - `archive/governance/ARCHIVAL_DURABILITY_POLICY.md` — durability, backup drill, and archive strategy (#142)
  - `archive/governance/PRESS_MEDIA_KIT.md` — public-facing media summary and key facts (#143)
  - `archive/governance/V1_LAUNCH_RETROSPECTIVE_PLAYBOOK.md` — launch-day sequence and retrospective template (#144)
- Wave 8 Testing & Reliability Pack (tasks #85–#96): 12 new testing governance artifacts
  - `archive/governance/TEST_STRATEGY_BY_DOMAIN.md` — 5-domain test strategy map (#85)
  - `archive/governance/COVERAGE_BASELINES.md` — minimum coverage thresholds by module (#86)
  - `archive/governance/GOLDEN_TESTS_STRATEGY.md` — snapshot/golden file testing approach (#87)
  - `archive/governance/SCHEMA_CONTRACT_TESTS_POLICY.md` — contract test requirements (#88)
  - `archive/governance/METADATA_LINK_REGRESSION_SUITE_POLICY.md` — regression test categories (#89)
  - `archive/governance/FLAKY_TEST_TRIAGE_QUEUE.md` — flaky test detection and triage (#90)
  - `archive/governance/RELIABILITY_SLOS.md` — SLO table with error budget (#91)
  - `archive/governance/RECOVERY_DRILLS_POLICY.md` — 4 recovery drill types and schedule (#92)
  - `archive/governance/FIXTURE_QUALITY_STANDARDS.md` — fixture naming and scope rules (#93)
  - `archive/governance/MUTATION_TESTING_PILOT.md` — mutmut pilot for reference_impl (#94)
  - `archive/governance/MONTHLY_QUALITY_REPORT_TEMPLATE.md` — report template and cadence (#95)
  - `archive/governance/TEST_OWNERSHIP_MATRIX.md` — test domain ownership assignments (#96)
- Wave 3 Repository Architecture Pack: navigation standards, breadcrumb standards, index of indexes, archive taxonomy map, file placement decision tree, duplicate docs triage, stale artifact quarantine lane, canonical path map, role-based landing paths (#25–#36)
- Wave 2 Legal/Trust Pack: license audit, attribution inventory, trademark guide, PII redaction rubric, sensitive content review process, export control checklist, data retention policy, vulnerability disclosure process, incident response runbook, compliance evidence index, public risk register, quarterly audit template (#13–#24)
- Wave 1 Governance Completion: section ownership map, review SLA policy, council review cadence, change classification rules, deprecation policy, governance onboarding guide (#4–#12)
- Wave 7 Security Pack (tasks #73–#84): 12 new security/supply-chain governance artifacts
  - `archive/governance/SECRET_SCANNING_PATTERNS_POLICY.md` — custom patterns + alert SLAs (#73)
  - `archive/governance/VULNERABILITY_TRIAGE_SLAS.md` — CVSS-based response times (#74)
  - `archive/governance/SBOM_GENERATION_POLICY.md` — SPDX + CycloneDX generation (#75)
  - `archive/governance/SIGNED_RELEASE_POLICY.md` — Sigstore/cosign signing (#76)
  - `archive/governance/BRANCH_PROTECTION_DEFAULTS.md` — required branch rules (#77)
  - `archive/governance/CODEOWNERS_COVERAGE_POLICY.md` — ownership map (#78)
  - `archive/governance/TOKEN_LEAST_PRIVILEGE_POLICY.md` — PAT/token scoping rules (#79)
  - `archive/governance/GITHUB_ACTION_PERMISSIONS_POLICY.md` — `permissions:` minimization (#80)
  - `archive/governance/SECURITY_CHAMPION_ROTATION_POLICY.md` — quarterly rotation (#81)
  - `archive/governance/SUBSYSTEM_THREAT_MODELS.md` — STRIDE threat model (#82)
  - `archive/governance/SECURITY_TRAINING_PLAYBOOK.md` — 5-module training guide (#83)
  - `archive/governance/ANNUAL_EXTERNAL_SECURITY_REVIEW_POLICY.md` — annual review process (#84)
- Wave 6 CI/CD Pack (tasks #61–#72): 11 new CI/CD governance artifacts
  - `archive/governance/REPO_HYGIENE_WORKFLOW_POLICY.md` — hygiene checks and cadence (#61)
  - `archive/governance/METADATA_COMPLETENESS_CHECK_POLICY.md` — required frontmatter fields (#63)
  - `archive/governance/LINK_INTEGRITY_CHECK_POLICY.md` — broken link detection (#64)
  - `archive/governance/DUPLICATE_DOC_DETECTION_CI_POLICY.md` — similarity-based duplicate finder (#65)
  - `archive/governance/SCHEMA_VALIDATION_CI_POLICY.md` — JSON Schema meta-validation (#66)
  - `archive/governance/DOCS_PREVIEW_BUILDS_POLICY.md` — PR preview build phases (#67)
  - `archive/governance/DRIFT_DETECTION_SCAN_POLICY.md` — weekly scheduled drift scans (#68)
  - `archive/governance/GITHUB_ACTIONS_VERSION_PINNING_POLICY.md` — SHA pinning rules (#69)
  - `archive/governance/DEPENDABOT_POLICY.md` — auto-merge and review rules (#70)
  - `archive/governance/WORKFLOW_RUNTIME_METRICS_POLICY.md` — P50/P95 runtime targets (#71)
  - `archive/governance/FAIL_FAST_RETRY_STANDARDS.md` — fail-fast and retry rules (#72)
- Wave 5 Knowledge Graph Pack (tasks #50–#60): 10 new KG governance/spec artifacts
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
