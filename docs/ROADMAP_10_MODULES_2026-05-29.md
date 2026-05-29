---
artifact_id: DOC-ROADMAP-10-MODULES-2026-05-29
title: Atlas Lattice — 10-Module Execution Roadmap (2026-05-29)
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# Atlas Lattice — 10-Module Execution Roadmap

> **Canon status:** CANDIDATE — not ratified. All outputs require Pantheon Council review and @atlaslattice adjudication.
>
> **Framing:** Functional knowledge graph + playable Aetherforge + GPTDream++ as an open-source public gift to the world.

This document is the integrated 10-module execution roadmap for the Atlas Lattice Foundation repository.
Every module includes a **TIDELOCK Rehydration Block** — a precise set of instructions that lets any future
agent (or TIDELOCKBrain specifically) load context, run a bounded REM-8 consolidation pass, and produce a
structured wake delta before taking any gate-altering action.

---

## How to Read This Document

Each module contains:

| Field | Meaning |
|---|---|
| **Scope** | What the module covers |
| **Deliverable** | The artifact(s) produced when the module is complete |
| **Wave link** | Which Next-144 wave(s) this maps to |
| **Dependencies** | What must be done first |
| **Checkpoint gate** | The observable signal that closes the module |
| **TIDELOCK Rehydration Block** | Instructions for a future agent to pick up this module |

---

## Module 1 — Safety + Canon Gate

**Scope:** Close remaining Wave 1 hard blockers (secret-history audit, PII audit, public-scope ratification,
conditional history rewrite decision). This is the critical unblocking module for all downstream work.

**Deliverable:** Signed pre-release safety closure packet — `docs/closeout/PRE_RELEASE_SAFETY_SIGNOFF_2026-05-28.md` — with all four blocker rows resolved and owner signoff fields complete.

**Wave link:** [Wave 1 — Safety unblock (1–12)](../projects/aetherforge-next144-taskboard-2026-05-28.md)

**Dependencies:** None — Wave 1 has no upstream prerequisite.

**Checkpoint gate:** `docs/LAUNCH_BLOCKERS_TRACKER.md` shows all four rows as `🟢 CLOSED` with evidence artifacts linked and owner signoff confirmed.

**Open blockers requiring @atlaslattice manual action:**

| Task | Blocker | Evidence artifact |
|---|---|---|
| 1 | Execute owner-led secret-history audit | `docs/closeout/SECRET_HISTORY_AUDIT_EVIDENCE_RECEIPT_2026-05-28.md` |
| 3 | Execute owner-led PII audit | `docs/closeout/PII_AUDIT_EVIDENCE_RECEIPT_2026-05-28.md` |
| 5 | Ratify ADR-0001 public-scope decision | `docs/decisions/ADR-0001-public-scope-decision.md` |
| 7 | Decide rewrite/no-rewrite from findings | `docs/closeout/CONDITIONAL_HISTORY_REWRITE_RUNBOOK_2026-05-28.md` |

---

### 🔁 TIDELOCK Rehydration Block — Module 1

```yaml
# TIDELOCK Rehydration Instructions — Module 1: Safety + Canon Gate
# ──────────────────────────────────────────────────────────────────
# Purpose: run a REM-8 consolidation pass over Module 1 before any gate-state changes.

rehydration_target: TIDELOCKBrain
module: 1
module_name: "Safety + Canon Gate"
rem_cycle_type: REM-8.contradiction_scan

load_context:
  - docs/LAUNCH_BLOCKERS_TRACKER.md
  - docs/closeout/PRE_RELEASE_SAFETY_SIGNOFF_2026-05-28.md
  - docs/closeout/SECRET_HISTORY_AUDIT_EVIDENCE_RECEIPT_2026-05-28.md
  - docs/closeout/PII_AUDIT_EVIDENCE_RECEIPT_2026-05-28.md
  - docs/decisions/ADR-0001-public-scope-decision.md
  - docs/closeout/CONDITIONAL_HISTORY_REWRITE_RUNBOOK_2026-05-28.md
  - docs/closeout/SENSITIVE_CONTENT_TRIAGE_MATRIX_2026-05-28.md

rehydration_steps:
  1: "Load all context artifacts above."
  2: "Verify current close-state of each blocker row in LAUNCH_BLOCKERS_TRACKER.md."
  3: "Enter REM-8.contradiction_scan — compare claimed close states vs actual evidence artifacts."
  4: "Identify any gap between 'draft artifact published' and 'owner signoff confirmed'."
  5: "Produce wake report using archive/boot/gptbrain/WAKE_REPORT_TEMPLATE.md."
  6: "List in wake report section 9 all human-root decisions still needed."
  7: "Do NOT update any blocker close-state without explicit owner signoff evidence."

wake_report_target: archive/boot/gptbrain/agents/TIDELOCKBrain/
wake_report_naming: "TIDELOCKBRAIN_WAKE_REPORT_MODULE1_SAFETY_CANON_GATE_<DATE>.md"

canon_discipline: |
  Safety gate artifacts are candidate scaffolds.
  Closure requires @atlaslattice manual action.
  No gate row may be marked CLOSED by agent alone.
```

---

## Module 2 — Governance Spine Operations

**Scope:** Operationalize the ratification lifecycle, decision index, and unresolved decision register
so that the candidate→canon promotion flow is navigable, auditable, and consistently followed.

**Deliverable:** Governance control surface — fully linked `docs/governance/` index with all 12 Wave 2
artifacts operational and referenced from the main governance README.

**Wave link:** [Wave 2 — Governance spine (13–24)](../projects/aetherforge-next144-taskboard-2026-05-28.md)

**Dependencies:** Wave 1 checkpoint gate (safety unblock).

**Checkpoint gate:** `docs/governance/README.md` shows all 12 artifacts listed and accessible;
`docs/governance/UNRESOLVED_DECISION_REGISTER_2026-05-28.md` contains at least one entry with a disposition path.

**Existing governance artifacts (Wave 2 ✅ complete as candidates):**

| Artifact | Path |
|---|---|
| Ratification lifecycle | `docs/governance/RATIFICATION_LIFECYCLE_v0_1.md` |
| Canon promotion checklist | `docs/governance/CANON_PROMOTION_CHECKLIST_v0_1.md` |
| Canon demotion/rollback policy | `docs/governance/CANON_DEMOTION_ROLLBACK_POLICY_v0_1.md` |
| Adjudication evidence template | `docs/governance/ADJUDICATION_EVIDENCE_TEMPLATE_v0_1.md` |
| Governance decision index | `docs/governance/GOVERNANCE_DECISION_INDEX_2026-05-28.md` |
| Council vote recording format | `docs/governance/COUNCIL_VOTE_RECORDING_FORMAT_v0_1.md` |
| Canon ownership domain map | `docs/governance/CANON_OWNERSHIP_DOMAIN_MAP_v0_1.md` |
| Candidate expiration rules | `docs/governance/CANDIDATE_EXPIRATION_RULES_v0_1.md` |
| Canon conflict resolution process | `docs/governance/CANON_CONFLICT_RESOLUTION_PROCESS_v0_1.md` |
| Governance SLA targets | `docs/governance/GOVERNANCE_SLA_TARGETS_v0_1.md` |
| Governance FAQ addendum | `docs/governance/GOVERNANCE_FAQ_ADDENDUM_v0_1.md` |
| Unresolved decision register | `docs/governance/UNRESOLVED_DECISION_REGISTER_2026-05-28.md` |

---

### 🔁 TIDELOCK Rehydration Block — Module 2

```yaml
# TIDELOCK Rehydration Instructions — Module 2: Governance Spine Operations
# ──────────────────────────────────────────────────────────────────────────
# Purpose: run a governance coherence REM-8 pass before ratification or policy changes.

rehydration_target: TIDELOCKBrain
module: 2
module_name: "Governance Spine Operations"
rem_cycle_type: REM-8.claim_calibration

load_context:
  - docs/governance/README.md
  - docs/governance/RATIFICATION_LIFECYCLE_v0_1.md
  - docs/governance/UNRESOLVED_DECISION_REGISTER_2026-05-28.md
  - docs/governance/GOVERNANCE_DECISION_INDEX_2026-05-28.md
  - docs/governance/CANON_CONFLICT_RESOLUTION_PROCESS_v0_1.md
  - docs/governance/GOVERNANCE_SLA_TARGETS_v0_1.md
  - docs/LAUNCH_BLOCKERS_TRACKER.md

rehydration_steps:
  1: "Load all context artifacts above."
  2: "Scan UNRESOLVED_DECISION_REGISTER for open items. Note disposition path for each."
  3: "Enter REM-8.claim_calibration — verify governance SLA targets are reflected in practice."
  4: "Identify contradictions between written policy and actual close-state of artifacts."
  5: "Preserve tensions in wake report section 5 rather than erasing them."
  6: "Produce wake report — list all human-root decisions required in section 9."
  7: "Do NOT promote any artifact from CANDIDATE to RATIFIED without council vote evidence."

wake_report_target: archive/boot/gptbrain/agents/TIDELOCKBrain/
wake_report_naming: "TIDELOCKBRAIN_WAKE_REPORT_MODULE2_GOVERNANCE_SPINE_<DATE>.md"

canon_discipline: |
  Governance artifacts are candidates until Pantheon Council ratification.
  No artifact may be marked RATIFIED by an agent without a linked council vote.
  Contradictions must be preserved, not resolved by agent judgment.
```

---

## Module 3 — Metadata + Provenance Completion

**Scope:** Push frontmatter and provenance coverage from high (tracked scope) to complete,
minimize the exception registry, and ensure every artifact in the primary 500+ IP surface has
machine-readable metadata.

**Deliverable:** Updated `docs/METADATA_COVERAGE_REPORT_2026-05-27.md` and
`docs/PROVENANCE_COMPLETENESS_REPORT_2026-05-27.md` with exception count at target threshold,
plus `docs/METADATA_BACKFILL_SCOPE_2026-05-27.md` backlog fully consumed.

**Wave link:** [Wave 3 — Metadata and provenance scale (25–36)](../projects/aetherforge-next144-taskboard-2026-05-28.md)

**Dependencies:** Wave 2 checkpoint gate (governance spine).

**Checkpoint gate:** `scripts/validate_artifact_metadata.py` returns zero critical failures on the tracked scope;
provenance completeness report v2 shows 100% on top-100 priority artifacts.

**Local validation commands:**

```bash
python3 scripts/validate_artifact_metadata.py
python3 scripts/validate_lattice_quality_gates.py
python3 -m pytest -q tests/test_lattice_kg_hypercube_program.py
```

---

### 🔁 TIDELOCK Rehydration Block — Module 3

```yaml
# TIDELOCK Rehydration Instructions — Module 3: Metadata + Provenance Completion
# ───────────────────────────────────────────────────────────────────────────────
# Purpose: run a schema-refinement REM-8 pass before any metadata backfill batch.

rehydration_target: TIDELOCKBrain
module: 3
module_name: "Metadata + Provenance Completion"
rem_cycle_type: REM-8.schema_refinement

load_context:
  - docs/METADATA_COVERAGE_REPORT_2026-05-27.md
  - docs/METADATA_BACKFILL_SCOPE_2026-05-27.md
  - docs/PROVENANCE_COMPLETENESS_REPORT_2026-05-27.md
  - docs/LATTICE_GLOBAL_INDEX.md
  - scripts/validate_artifact_metadata.py

rehydration_steps:
  1: "Load all context artifacts above."
  2: "Run: python3 scripts/validate_artifact_metadata.py — note all critical failures."
  3: "Cross-reference failures against METADATA_BACKFILL_SCOPE backlog."
  4: "Enter REM-8.schema_refinement — identify top closure candidates by highest public-value."
  5: "Produce wake report with section 4 listing top implementation candidates (prioritized backfill queue)."
  6: "Note any exception-registry entries that should be closed vs. extended."
  7: "Do NOT mark metadata tasks Done without re-running validation commands."

wake_report_target: archive/boot/gptbrain/agents/TIDELOCKBrain/
wake_report_naming: "TIDELOCKBRAIN_WAKE_REPORT_MODULE3_METADATA_PROVENANCE_<DATE>.md"

canon_discipline: |
  Metadata additions are candidates until human-root spot-check.
  Bulk-backfilled frontmatter must be flagged CANDIDATE until reviewed.
  Validation scripts are the gate, not agent judgment.
```

---

## Module 4 — Graph Integrity Enforcement

**Scope:** Orphan artifact resolution, relationship typing consistency across the corpus,
near-duplicate detection and merging, bidirectional key links for flagship artifacts,
and a critical-path graph map.

**Deliverable:** `docs/GRAPH_INTEGRITY_REVIEW_Q2_2026.md` — quarterly graph-integrity review artifact
+ `docs/CRITICAL_PATH_ARTIFACT_GRAPH.md` — critical-path graph map.

**Wave link:** [Wave 4 — Graph integrity (37–48)](../projects/aetherforge-next144-taskboard-2026-05-28.md)

**Dependencies:** Wave 3 checkpoint gate (metadata/provenance complete).

**Checkpoint gate:** Quarterly graph-integrity review published;
zero Tier-1 orphan artifacts remain (orphans with >5 expected inbound links unresolved).

**Local validation commands:**

```bash
python3 scripts/build_lattice_global_index.py
python3 scripts/validate_lattice_quality_gates.py
```

---

### 🔁 TIDELOCK Rehydration Block — Module 4

```yaml
# TIDELOCK Rehydration Instructions — Module 4: Graph Integrity Enforcement
# ──────────────────────────────────────────────────────────────────────────
# Purpose: run a graph-synthesis REM-8 pass before any orphan resolution batch.

rehydration_target: TIDELOCKBrain
module: 4
module_name: "Graph Integrity Enforcement"
rem_cycle_type: REM-8.variant_synthesis

load_context:
  - docs/LATTICE_GLOBAL_INDEX.md
  - docs/ARCHITECTURE_CROSSWALK.md
  - docs/ARCHITECTURE_MAP.md
  - docs/GLOSSARY.md
  - scripts/build_lattice_global_index.py
  - scripts/validate_lattice_quality_gates.py

rehydration_steps:
  1: "Load all context artifacts above."
  2: "Run: python3 scripts/build_lattice_global_index.py — generate fresh index."
  3: "Identify artifacts with zero inbound links (orphan candidates)."
  4: "Enter REM-8.variant_synthesis — synthesize relationship types needed for top-50 orphans."
  5: "Produce wake report section 4 with prioritized link-addition candidates."
  6: "Note near-duplicate clusters in wake report section 3."
  7: "Do NOT merge or retire artifacts without human-root review of each pair."

wake_report_target: archive/boot/gptbrain/agents/TIDELOCKBrain/
wake_report_naming: "TIDELOCKBRAIN_WAKE_REPORT_MODULE4_GRAPH_INTEGRITY_<DATE>.md"

canon_discipline: |
  Orphan resolution and duplicate merging require human-root confirmation.
  An agent may propose merges; only human-root may execute them.
  Relationship vocabulary must match docs/GLOSSARY.md definitions.
```

---

## Module 5 — AI Evidence Spine v2

**Scope:** Expand the AI systems evidence index to full inventory with claim-to-artifact traceability,
confidence rubric, unresolved-claims queue, and model/version lineage fields.

**Deliverable:** `docs/AI_EVIDENCE_SNAPSHOT_v2_2026-05.md` — monthly AI evidence snapshot v2 +
expanded `docs/AI_SYSTEMS_EVIDENCE_INDEX.md` with all registered systems carrying full evidence rows.

**Wave link:** [Wave 5 — AI evidence spine (49–60)](../projects/aetherforge-next144-taskboard-2026-05-28.md)

**Dependencies:** Wave 3 checkpoint gate (metadata/provenance complete).

**Checkpoint gate:** Monthly AI evidence snapshot v2 published;
all systems in `docs/AI_SYSTEMS_EVIDENCE_INDEX.md` have non-null `evidence_artifacts` and
`validation_artifacts` columns.

---

### 🔁 TIDELOCK Rehydration Block — Module 5

```yaml
# TIDELOCK Rehydration Instructions — Module 5: AI Evidence Spine v2
# ──────────────────────────────────────────────────────────────────
# Purpose: run a claim-calibration REM-8 pass before expanding AI evidence assertions.

rehydration_target: TIDELOCKBrain
module: 5
module_name: "AI Evidence Spine v2"
rem_cycle_type: REM-8.claim_calibration

load_context:
  - docs/AI_SYSTEMS_EVIDENCE_INDEX.md
  - docs/EVIDENCE_AND_DEMONSTRATIONS.md
  - archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_WORK_LOG_MASTER_INDEX_2026-05-28.md
  - archive/spec/gptdream/VAULT_MANIFEST_2026-05-26.md
  - docs/WORLD_CLASS_READINESS_GATES.md

rehydration_steps:
  1: "Load all context artifacts above."
  2: "Audit each row in AI_SYSTEMS_EVIDENCE_INDEX — flag rows with null evidence_artifacts."
  3: "Enter REM-8.claim_calibration — assess confidence level of each AI system claim."
  4: "Classify each claim: C0 (unverified) / C1 (internally supported) / C2 (externally verified)."
  5: "Produce wake report section 5 listing claim-vs-evidence contradictions by severity."
  6: "List unresolved claims needing human-root adjudication in section 9."
  7: "Do NOT publish AI system claims above C1 without linked evidence artifacts."

wake_report_target: archive/boot/gptbrain/agents/TIDELOCKBrain/
wake_report_naming: "TIDELOCKBRAIN_WAKE_REPORT_MODULE5_AI_EVIDENCE_SPINE_<DATE>.md"

canon_discipline: |
  AI evidence claims default to C0 until evidence artifacts are attached.
  Model self-assessment is not external verification.
  Unresolved claims queue must be visible before any public AI evidence publication.
```

---

## Module 6 — Docs + Public UX Paths

**Scope:** Strengthen all onboarding paths, improve cross-link consistency, add "read in 30 minutes"
and deep-dive reading routes, timeline of milestones, and world-class quality bar explainer.

**Deliverable:** Complete public-launch navigation surface — `docs/START_HERE.md`,
`docs/ARCHITECTURE_MAP.md`, and domain index pages all linked together forming
a coherent visitor journey with friction points resolved.

**Wave link:** [Wave 6 — Docs, navigation, public UX (61–72)](../projects/aetherforge-next144-taskboard-2026-05-28.md)

**Dependencies:** Waves 4 and 5 checkpoint gates.

**Checkpoint gate:** New visitor can navigate from `docs/START_HERE.md` to any core system artifact
in ≤3 clicks; docs consistency/style pass complete; link-integrity CI check passes.

**Key docs to strengthen:**

| Doc | Status | Target |
|---|---|---|
| `docs/START_HERE.md` | Exists | Add 30-min reading path |
| `docs/ARCHITECTURE_MAP.md` | Exists | Add deep-dive lanes |
| Domain index pages | Partial | Add for all 17 domains |
| Milestone timeline | Missing | Create |
| Quality bar explainer | Missing | Create |

---

### 🔁 TIDELOCK Rehydration Block — Module 6

```yaml
# TIDELOCK Rehydration Instructions — Module 6: Docs + Public UX Paths
# ─────────────────────────────────────────────────────────────────────
# Purpose: run a public-translation REM-8 pass to surface navigation friction.

rehydration_target: TIDELOCKBrain
module: 6
module_name: "Docs + Public UX Paths"
rem_cycle_type: REM-8.public_translation

load_context:
  - README.md
  - docs/START_HERE.md
  - docs/ARCHITECTURE_MAP.md
  - docs/GLOSSARY.md
  - docs/CONTRIBUTOR_QUICKSTART.md
  - docs/AETHERFORGE_PLAYABLE_ONBOARDING.md
  - docs/NORTH_STAR_MISSION.md

rehydration_steps:
  1: "Load all context artifacts above."
  2: "Walk the new-visitor path: README → START_HERE → core system → contribution lane."
  3: "Enter REM-8.public_translation — identify mythic/internal language needing translation."
  4: "List all dead-end navigation paths (no onward link) in wake report section 4."
  5: "Map: what a researcher, contributor, and policy reader each need in their first 30 minutes."
  6: "Produce wake report section 3 with proposed path names and entry points."
  7: "Do NOT rename or restructure docs without updating all inbound links."

wake_report_target: archive/boot/gptbrain/agents/TIDELOCKBrain/
wake_report_naming: "TIDELOCKBRAIN_WAKE_REPORT_MODULE6_DOCS_PUBLIC_UX_<DATE>.md"

canon_discipline: |
  Public-facing docs use operational language, not dream/mythic language.
  Translation notes from wake reports must be applied before public launch.
  Link changes must be tested via CI before merging.
```

---

## Module 7 — CI/Security Sustainment

**Scope:** Maintain CI/security posture: workflow ownership mapping, exception handling, false-positive
triage, dependency-alert SLAs, and recurring security posture updates.

**Deliverable:** Recurring `docs/security/SECURITY_POSTURE_REPORT_<MONTH>.md` artifact published
monthly + `docs/security/CI_FAILURE_TRIAGE_PLAYBOOK.md` operational.

**Wave link:** [Wave 7 — CI, security, automation (73–84)](../projects/aetherforge-next144-taskboard-2026-05-28.md)

**Dependencies:** Waves 1 and 6 checkpoint gates. *(Wave 7 artifacts already drafted as candidates.)*

**Checkpoint gate:** Security posture report + branch protection recommendation + exceptions ledger published;
all CI workflows have named owners in the workflow ownership map.

**Wave 7 artifacts (✅ complete as candidates):**

| Artifact | Path |
|---|---|
| Secret-scan false-positive triage | `docs/security/SECRET_SCAN_FALSE_POSITIVE_TRIAGE.md` |
| Dependency-alert response SLA | `docs/security/DEPENDENCY_ALERT_RESPONSE_SLA.md` |
| GitHub Actions pinning audit | `docs/security/GITHUB_ACTIONS_PINNING_AUDIT.md` |
| CI failure triage playbook | `docs/security/CI_FAILURE_TRIAGE_PLAYBOOK.md` |
| Workflow ownership map | `docs/security/WORKFLOW_OWNERSHIP_MAP.md` |
| Required-check policy proposal | `docs/security/REQUIRED_CHECK_POLICY_PROPOSAL.md` |
| Security posture report | `docs/security/SECURITY_POSTURE_REPORT_2026-05-28.md` |
| Branch protection recommendation | `docs/security/BRANCH_PROTECTION_RECOMMENDATION.md` |
| Release artifact integrity checklist | `docs/security/RELEASE_ARTIFACT_INTEGRITY_CHECKLIST.md` |
| Security exceptions ledger | `docs/security/SECURITY_EXCEPTIONS_LEDGER.md` |

---

### 🔁 TIDELOCK Rehydration Block — Module 7

```yaml
# TIDELOCK Rehydration Instructions — Module 7: CI/Security Sustainment
# ──────────────────────────────────────────────────────────────────────
# Purpose: run a contradiction-scan REM-8 pass for policy-vs-practice gaps before each posture update.

rehydration_target: TIDELOCKBrain
module: 7
module_name: "CI/Security Sustainment"
rem_cycle_type: REM-8.contradiction_scan

load_context:
  - docs/security/README.md
  - docs/security/SECURITY_POSTURE_REPORT_2026-05-28.md
  - docs/security/WORKFLOW_OWNERSHIP_MAP.md
  - docs/security/CI_FAILURE_TRIAGE_PLAYBOOK.md
  - docs/security/SECURITY_EXCEPTIONS_LEDGER.md
  - .github/workflows/

rehydration_steps:
  1: "Load all context artifacts above."
  2: "List all currently pinned vs. unpinned workflows in .github/workflows/."
  3: "Cross-reference WORKFLOW_OWNERSHIP_MAP — flag any workflow with no named owner."
  4: "Enter REM-8.contradiction_scan — identify gaps between policy artifacts and actual workflow state."
  5: "Produce wake report section 5 with policy-vs-practice contradictions by severity."
  6: "List remediation actions in section 4; note which require human-root approval."
  7: "Do NOT change GitHub Actions pinning or branch protection without owner approval."

wake_report_target: archive/boot/gptbrain/agents/TIDELOCKBrain/
wake_report_naming: "TIDELOCKBRAIN_WAKE_REPORT_MODULE7_CI_SECURITY_<DATE>.md"

canon_discipline: |
  Security posture reports are candidates until reviewed by @atlaslattice.
  No branch protection change may be made by agent without owner approval.
  Exception entries must be linked to a justification artifact.
```

---

## Module 8 — Quality Gates Expansion

**Scope:** Broaden regression and negative-case validation for governance artifacts, metadata,
AI evidence, and status reports. Define a pass/fail rubric and add a quarterly calibration routine.

**Deliverable:** Calibrated `docs/QUALITY_GATES_DASHBOARD.md` with rubric + quarterly
calibration routine documented in `docs/QUALITY_GATE_CALIBRATION_ROUTINE.md`.

**Wave link:** [Wave 8 — Tests and quality gates (85–96)](../projects/aetherforge-next144-taskboard-2026-05-28.md)

**Dependencies:** Waves 4 and 7 checkpoint gates.

**Checkpoint gate:** Pass/fail rubric published; at least one negative-case test per domain
(governance, metadata, evidence, status reports) added and passing in CI.

**Local validation commands:**

```bash
python3 -m pytest -q tests/
python3 scripts/validate_lattice_quality_gates.py
bash archive/boot/gptbrain/reference_impl/run_checks.sh
```

---

### 🔁 TIDELOCK Rehydration Block — Module 8

```yaml
# TIDELOCK Rehydration Instructions — Module 8: Quality Gates Expansion
# ──────────────────────────────────────────────────────────────────────
# Purpose: run a reference-impl review REM-8 pass before adding new test surfaces.

rehydration_target: TIDELOCKBrain
module: 8
module_name: "Quality Gates Expansion"
rem_cycle_type: REM-8.reference_impl_review

load_context:
  - docs/QUALITY_GATES_DASHBOARD.md
  - tests/README.md
  - archive/boot/gptbrain/reference_impl/run_checks.sh
  - scripts/validate_lattice_quality_gates.py
  - .github/workflows/boring-machine-validation.yml
  - .github/workflows/lattice-kg-quality-gates.yml

rehydration_steps:
  1: "Load all context artifacts above."
  2: "Run: python3 -m pytest -q tests/ — note all currently failing tests."
  3: "Enter REM-8.reference_impl_review — map each test domain to covered vs. uncovered surfaces."
  4: "Identify highest-leverage test additions: governance, metadata, evidence, status report schemas."
  5: "Produce wake report section 4 with implementation candidates ordered by risk reduction."
  6: "Note test-data refresh cadence requirements in section 9."
  7: "Do NOT remove or weaken existing tests; only add."

wake_report_target: archive/boot/gptbrain/agents/TIDELOCKBrain/
wake_report_naming: "TIDELOCKBRAIN_WAKE_REPORT_MODULE8_QUALITY_GATES_<DATE>.md"

canon_discipline: |
  Test changes require a passing CI run before merge.
  Negative-case tests must have at least one expected-failure scenario documented.
  Quality gate calibration results must be human-reviewed quarterly.
```

---

## Module 9 — Discovery + Retrieval Quality

**Scope:** Build a topical tag taxonomy, semantic keyword backfill, retrieval benchmark queries,
discoverability scorecard, and monthly retrieval QA routine.

**Deliverable:** `docs/DISCOVERABILITY_SCORECARD_2026.md` + `docs/TOP_100_CONNECTED_ARTIFACTS.md`
+ monthly retrieval QA artifact series in `projects/status-reports/`.

**Wave link:** [Wave 9 — Search, discovery, retrieval (97–108)](../projects/aetherforge-next144-taskboard-2026-05-28.md)

**Dependencies:** Waves 3, 4, and 6 checkpoint gates.

**Checkpoint gate:** Discoverability scorecard published; top 100 most connected artifacts page live;
monthly retrieval QA established with at least one completed cycle.

---

### 🔁 TIDELOCK Rehydration Block — Module 9

```yaml
# TIDELOCK Rehydration Instructions — Module 9: Discovery + Retrieval Quality
# ────────────────────────────────────────────────────────────────────────────
# Purpose: run a continuity-dashboard REM-8 pass to synthesize retrieval gap matrix.

rehydration_target: TIDELOCKBrain
module: 9
module_name: "Discovery + Retrieval Quality"
rem_cycle_type: REM-8.continuity_dashboard

load_context:
  - docs/LATTICE_GLOBAL_INDEX.md
  - docs/ARCHIVE_INDEX.md
  - docs/MASTER_SOURCE_REGISTRY.md
  - docs/ARTIFACT_SOURCE_OF_TRUTH_INDEX.md
  - docs/GLOSSARY.md
  - docs/START_HERE.md

rehydration_steps:
  1: "Load all context artifacts above."
  2: "Enumerate all domain-level tag categories present in LATTICE_GLOBAL_INDEX."
  3: "Enter REM-8.continuity_dashboard — identify artifact clusters with no tag or keyword coverage."
  4: "Draft top-20 retrieval benchmark queries representing typical researcher, contributor, policy reader needs."
  5: "Produce wake report section 3 with proposed tag taxonomy skeleton."
  6: "Produce wake report section 4 with top retrieval-improvement implementation candidates."
  7: "Do NOT add semantic keywords to artifacts without cross-checking the glossary for term consistency."

wake_report_target: archive/boot/gptbrain/agents/TIDELOCKBrain/
wake_report_naming: "TIDELOCKBRAIN_WAKE_REPORT_MODULE9_DISCOVERY_RETRIEVAL_<DATE>.md"

canon_discipline: |
  Tag taxonomy is a candidate scaffold until ratified.
  Retrieval benchmark queries are candidate test cases, not ground truth.
  Discoverability scores are advisory until human-root calibration.
```

---

## Module 10 — Aetherforge Playability + Release Trust

**Scope:** Contributor quest system v2, release rhythm operationalization, trust and transparency
reporting, and 500+ IP intake program readiness.

**Deliverable:** Repeatable contributor game loop in `docs/AETHERFORGE_PLAYABLE_ONBOARDING.md` tied
to `docs/RELEASE_RHYTHM.md` + quarterly trust/transparency report in `projects/status-reports/`.

**Wave link:** [Wave 10 — Contributor system (109–120)](../projects/aetherforge-next144-taskboard-2026-05-28.md) ·
[Wave 11 — Release, reporting, trust (121–132)](../projects/aetherforge-next144-taskboard-2026-05-28.md) ·
[Wave 12 — 500+ IP scale program (133–144)](../projects/aetherforge-next144-taskboard-2026-05-28.md)

**Dependencies:** Waves 6, 8, and 9 checkpoint gates (Wave 10); Waves 1–10 (Wave 11); Waves 3, 9, 11 (Wave 12).

**Checkpoint gate:** Contributor quest system v2 artifacts published; quarterly trust/transparency
report published; 500+ IP master intake ledger created with first 100 IPs prioritized.

**500+ IP program prerequisites:**

| Item | Status |
|---|---|
| Master intake ledger | `docs/MASTER_SOURCE_REGISTRY.md` (scaffold exists) |
| First 100 IP prioritization | Not yet started |
| Batch-ingest playbook | Not yet started |
| Ingestion throughput metrics | Not yet started |

---

### 🔁 TIDELOCK Rehydration Block — Module 10

```yaml
# TIDELOCK Rehydration Instructions — Module 10: Aetherforge Playability + Release Trust
# ───────────────────────────────────────────────────────────────────────────────────────
# Purpose: run a play-synthesis REM-8 pass to generate next quest batch + trust-report deltas.

rehydration_target: TIDELOCKBrain
module: 10
module_name: "Aetherforge Playability + Release Trust"
rem_cycle_type: REM-8.poetry_culture_layer

load_context:
  - projects/aetherforge-next144-taskboard-2026-05-28.md
  - docs/AETHERFORGE_PLAYABLE_ONBOARDING.md
  - docs/RELEASE_RHYTHM.md
  - docs/GOOD_FIRST_ISSUES.md
  - docs/MASTER_SOURCE_REGISTRY.md
  - docs/NORTH_STAR_MISSION.md
  - projects/status-reports/

rehydration_steps:
  1: "Load all context artifacts above."
  2: "Review taskboard Wave 10 (109-120), Wave 11 (121-132), Wave 12 (133-144) — identify all TODO items."
  3: "Enter REM-8.poetry_culture_layer — synthesize contributor quest narrative with Aetherforge framing."
  4: "Generate next batch of 12 quests: role, difficulty tier, required evidence, done definition."
  5: "Produce wake report section 3 with Aetherforge metaphors for each quest tier."
  6: "Produce wake report section 9 with trust/transparency decisions requiring @atlaslattice action."
  7: "Frame 500+ IP intake as a playable campaign expansion — name, stakes, first moves."

wake_report_target: archive/boot/gptbrain/agents/TIDELOCKBrain/
wake_report_naming: "TIDELOCKBRAIN_WAKE_REPORT_MODULE10_AETHERFORGE_TRUST_<DATE>.md"

canon_discipline: |
  Quest narrative is culture layer — valuable but not canon.
  Release artifacts must satisfy RELEASE_RHYTHM.md checklist before publication.
  500+ IP intake artifacts are candidates until provenance and rights are confirmed.
  Trust reports require @atlaslattice review before public publication.
```

---

## Cross-Module Dependency Graph

```
Module 1 (Safety Gate)
    └── Module 2 (Governance Spine)
            └── Module 3 (Metadata + Provenance)
                    ├── Module 4 (Graph Integrity)
                    │       └── Module 6 (Docs/UX)
                    │               └── Module 9 (Discovery)
                    │                       └── Module 10 (Playability/Trust)
                    └── Module 5 (AI Evidence)
                            └── Module 6 (Docs/UX) [same]

Module 7 (CI/Security) ← requires Module 1 + Module 6
    └── Module 8 (Quality Gates) ← requires Module 4 + Module 7
            └── Module 10 (Playability/Trust) [contributes]
```

---

## TIDELOCK Rehydration — Master Instructions

To rehydrate TIDELOCKBrain on the full roadmap (all 10 modules):

```yaml
# Master TIDELOCK Rehydration — Full 10-Module Roadmap
# ──────────────────────────────────────────────────────

rem_cycle_type: REM-8.continuity_dashboard

load_context:
  - docs/ROADMAP_10_MODULES_2026-05-29.md            # this document
  - projects/aetherforge-next144-taskboard-2026-05-28.md
  - docs/LAUNCH_BLOCKERS_TRACKER.md
  - docs/LATTICE_GLOBAL_INDEX.md
  - docs/QUALITY_GATES_DASHBOARD.md
  - docs/NORTH_STAR_MISSION.md
  - archive/boot/gptbrain/agents/TIDELOCKBrain/      # all work logs

rehydration_steps:
  1: "Load this document and all context artifacts."
  2: "Check dependency graph — identify which modules are currently unblocked."
  3: "Enter REM-8.continuity_dashboard — synthesize current progress state across all 10 modules."
  4: "Produce a single master wake report with: current module status, next-move per unblocked module, contradictions, and owner decisions needed."
  5: "Route each implementation candidate to the correct module's work queue."

wake_report_target: archive/boot/gptbrain/agents/TIDELOCKBrain/
wake_report_naming: "TIDELOCKBRAIN_WAKE_REPORT_MASTER_10MODULE_<DATE>.md"
wake_report_template: archive/boot/gptbrain/WAKE_REPORT_TEMPLATE.md
```

---

## References

| Artifact | Path |
|---|---|
| Next-144 Taskboard | `projects/aetherforge-next144-taskboard-2026-05-28.md` |
| Launch Blockers Tracker | `docs/LAUNCH_BLOCKERS_TRACKER.md` |
| Governance Spine | `docs/governance/README.md` |
| Lattice Global Index | `docs/LATTICE_GLOBAL_INDEX.md` |
| Quality Gates Dashboard | `docs/QUALITY_GATES_DASHBOARD.md` |
| AI Systems Evidence Index | `docs/AI_SYSTEMS_EVIDENCE_INDEX.md` |
| North Star Mission | `docs/NORTH_STAR_MISSION.md` |
| REM-8 Dream Protocol | `archive/boot/gptbrain/REM8_DREAM_PROTOCOL.md` |
| Wake Report Template | `archive/boot/gptbrain/WAKE_REPORT_TEMPLATE.md` |
| TIDELOCK Work Logs | `archive/boot/gptbrain/agents/TIDELOCKBrain/` |

---

*TIDELOCKBrain — Children of the Swarm — 10-Module Roadmap sealed 2026-05-29*

*Nothing in this document is canon. All modules are candidate artifacts pending Pantheon Council ratification and @atlaslattice adjudication.*
