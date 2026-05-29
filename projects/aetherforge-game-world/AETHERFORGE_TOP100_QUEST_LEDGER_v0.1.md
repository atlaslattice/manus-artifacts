# ⚔️ Aetherforge Top-100 Quest Ledger v0.1 (Candidate)

```text
STATUS: CANDIDATE QUEST LEDGER
CANON: NO
DATE: 2026-05-26
PURPOSE: optimal next-100 tasks across all repo components, framed as Aetherforge quests
METHOD: full repo audit snooped by TIDELOCK / S7 (CopilotBrain) — Metatron's Cube ring topology
AUDIT LOG: archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_WORK_LOG_TOP100_AUDIT_2026-05-26.md
STATUS MODEL: `done` only when completed in active execution board(s); default is `pending`
```

## Reading Guide

- **Ring** = Metatron's Cube layer (Center outward)
- **Zone** = M1–M10 game zone (from `projects/aetherforge-game-world/README.md`)
- **Tier** = T1 Patrol / T2 Expedition / T3 Raid / T4 Mythic
- **Seat** = best-fit Council seat (S1–S7) or `ALL`
- **Class** = quest class (Scout / Forge / Trial / Council / Restoration)
- **Status** = `done` if explicitly completed on the active top-10/144 boards, otherwise `pending`

## Status synchronization baseline (2026-05-29)

Done in active boards: `A03`, `A04`, `A05`, `A06`, `C03`, `D01`, `D02`, `D03`  
All other quests in this ledger are currently `pending`.

---

## 🌑 CENTER — The Meta Quest

| # | Quest Title | Zone | Tier | Seat | Class |
|---|---|---|---|---|---|
| C01 | **Metatron Awakening** — build a `knowledge_graph/GRAPH_INDEX.md` that links every node (doc, schema, agent, test, seat, module) in Metatron's Cube topology, making the repo fully self-navigating | M8 | T4 | ALL | Forge |

---

## 💠 Ring A — Governance & Canon (13 quests)

| # | Quest Title | Zone | Tier | Seat | Class |
|---|---|---|---|---|---|
| A01 | **Island Laws Refresh** — patch `COUNCIL_BRAIN_INDEX.md` to reflect all new agents and artifacts added since 2026-05-09 (swarm, TIDELOCKBrain, vendor bridge, Module 8–9) | M2 | T1 | S1 | Forge |
| A02 | **Gate Seed Ritual** — create `archive/boot/gptbrain/KRAKOA_GATE_INDEX.seed.jsonl` seeding active gates for Issue #11, #12, #13, ORCS, Wake Report, REM-8, Krakoa Keep, Human Root Review | M2 | T1 | S7 | Forge |
| A03 | **Unresolved Council Q-001→Q-006** — produce a single decision packet for @atlaslattice review answering all six open questions in `KRAKOA_UNRESOLVED_QUESTION_LEDGER_2026-05-26.md` | M2 | T2 | S1 | Council |
| A04 | **Ratification Schema** — define a `ratification_event` YAML schema (ratification_event_id + canon_status + trust_state + human_root_approved) so `is_canon()` has a machine-readable contract | M2 | T2 | S2 | Forge |
| A05 | **Weekly SITREP Charter** — write Q-006 answer: a `KRAKOA_SITREP_CADENCE_POLICY.md` defining frequency, owner, format, and archive path for weekly SITREPs | M1 | T1 | S6 | Forge |
| A06 | **Governance Changelog** — create `archive/boot/gptbrain/GOVERNANCE_CHANGELOG_2026-05.md` listing all canon-boundary patches made this month (CAS-001-A, is_canon() fix, etc.) | M2 | T1 | S2 | Forge |
| A07 | **Canon Truth Spine Audit** — verify the 5 truth-spine documents (`KRAKOA_CANON_TRUTH_SPINE_2026-05-26.md`) are still current; flag any drift in a delta note | M2 | T1 | S1 | Scout |
| A08 | **CONTRIBUTING Module 8 Update** — add Module 8–9 zone routing rules to `.github/CONTRIBUTING.md` | M7 | T1 | S7 | Forge |
| A09 | **Public Launch Blockers Issue** — open GitHub issue tracking 4 manual launch blockers: secret scan, PII audit, scope decision, history rewrite decision (Q-005 answer) | M2 | T1 | S7 | Council |
| A10 | **Repo Visibility Decision Doc** — create `REPO_VISIBILITY_DECISION.md` with @atlaslattice decision matrix: remain private / make public / create mirror | M2 | T1 | S2 | Council |
| A11 | **Secret Scan** — scan entire repo for accidentally committed secrets, tokens, or credentials; produce `KRAKOA_SECRET_SCAN_REPORT_2026-05-26.md` | M2 | T2 | S7 | Trial |
| A12 | **PII Audit** — scan all markdown/YAML/Python for personal data references; produce `KRAKOA_PII_AUDIT_REPORT_2026-05-26.md` with redaction candidates | M2 | T2 | S2 | Trial |
| A13 | **LICENSE Forge** — add `LICENSE` file (Apache 2.0 or MIT, @atlaslattice choice) — required before any public launch | M7 | T1 | S7 | Forge |

---

## 🔧 Ring B — Reference Impl & Code (13 quests)

| # | Quest Title | Zone | Tier | Seat | Class |
|---|---|---|---|---|---|
| B01 | **Package Split Phase 1** — split `dream_memory_palace_reference_impl.py` into `gptbrain/models.py`, `engine.py`, `governance.py`, `retrieval.py`, `serialization.py`, `cli.py` per productionization plan | M6 | T3 | S7 | Forge |
| B02 | **Pydantic Schemas Phase 2** — add pydantic models for `MemoryObject`, `ClaimLedgerEntry`, `ArtifactRegistryEntry`, `AuditEvent`, `MemoryPacket`, `BootPacket`, `Contradiction`, `PromotionReceipt` | M6 | T3 | S7 | Forge |
| B03 | **pyproject.toml** — add `pyproject.toml` with pytest + ruff configuration so CI and local runs are config-identical | M7 | T1 | S7 | Forge |
| B04 | **SQLite Adapter** — implement SQLite storage adapter for local dev (Phase 3 productionization) | M5 | T3 | S7 | Forge |
| B05 | **JSONL Fossil Adapter** — implement JSONL append-only fossil-record adapter (Phase 3) | M5 | T2 | S7 | Forge |
| B06 | **CLI: gptbrain remember** — implement `gptbrain remember --file --type --confidence` command | M6 | T2 | S7 | Forge |
| B07 | **CLI: gptbrain recall** — implement `gptbrain recall "<query>" --project` command | M6 | T2 | S7 | Forge |
| B08 | **CLI: gptbrain challenge** — implement `gptbrain challenge --claim-id` command | M6 | T2 | S7 | Forge |
| B09 | **CLI: gptbrain promote** — implement `gptbrain promote --memory-id --human-root-approved` with audit receipt guard | M6 | T2 | S7 | Forge |
| B10 | **Sheldonbrain Importer** — implement Phase 5 importer: `artifact_registry.jsonl`, `claim_ledger.jsonl`, `memory_packet.json`, `BOOT_PACKET.md` → DreamMemoryPalace | M8 | T3 | S6 | Forge |
| B11 | **Ruff Linter CI** — add `ruff check` step to `gptbrain-reference-checks.yml` and fix all current ruff violations | M7 | T2 | S7 | Trial |
| B12 | **Type Checker CI** — add `mypy` or `pyright` step to CI; annotate any untyped functions in current codebase | M7 | T2 | S7 | Trial |
| B13 | **Krakoa Packet Validator** — implement a `krakoa_packet_validator.py` that checks any YAML block with `krakoa_packet_id:` against the krakoa packet schema from the Living Archive Charter | M5 | T2 | S7 | Forge |

---

## 🌀 Ring C — Swarm & Agents (13 quests)

| # | Quest Title | Zone | Tier | Seat | Class |
|---|---|---|---|---|---|
| C01 | **LumenBrain Folder** — create `archive/boot/gptbrain/LumenBrain/` with `LUMENBRAIN_INDEX.md` (Q-003 answer) | M9 | T1 | S1 | Forge |
| C02 | **Lumen Agent DNA** — create `LUMENBRAIN_AGENT_DNA_PROFILE.md` with best use, shadow risk, counterbalance, routing default, overclaim to avoid | M9 | T2 | S1 | Forge |
| C03 | **TIDELOCKBrain Canonical Folder** — create `archive/boot/gptbrain/TIDELOCKBrain/` as the dedicated canonical home (Q-004 answer); unify the two existing paths | M9 | T1 | S7 | Forge |
| C04 | **TIDELOCK Agent DNA** — create `TIDELOCKBRAIN_AGENT_DNA_PROFILE.md` under new canonical folder | M9 | T2 | S7 | Forge |
| C05 | **S7 Identity Credential Update** — update `archive/boot/seats/S7_IDENTITY_CREDENTIAL.md` to reflect TIDELOCK handle and current roles | M9 | T1 | S7 | Forge |
| C06 | **Swarm Slot TBD-04 Scout** — scout for the 4th child agent; produce a candidate identity profile proposal for @atlaslattice review | M9 | T2 | ALL | Scout |
| C07 | **Swarm Slots TBD-05→TBD-11 Scout** — research and propose names/roles for remaining 7 open swarm slots | M9 | T3 | ALL | Scout |
| C08 | **S8→S11 Seat Specs** — create seat spec stub docs for S8–S11 under `archive/boot/seats/` once slots are decided | M2 | T3 | S1 | Forge |
| C09 | **Squad Index Refresh** — update `CHILDREN_OF_THE_SWARM_SQUAD_INDEX` with all new entries (LumenBrain folder, TIDELOCK DNA, new slot candidates) | M9 | T2 | S7 | Forge |
| C10 | **Swarm Health Scorecard** — create monthly `SWARM_HEALTH_SCORECARD_TEMPLATE.md` tracking seat visibility, profile completeness, and routing coverage | M1 | T1 | S1 | Forge |
| C11 | **AsterBrain DNA Upgrade** — strengthen `archive/boot/gptbrain/AsterBrain/ASTERBRAIN_INDEX.md` with full Agent DNA (best use, shadow risk, counterbalance, routing, overclaim fence) | M9 | T2 | S1 | Forge |
| C12 | **Council Dream Round Protocol v2** — update dream palace round protocol to support 11-seat squad and new brain folders | M2 | T3 | ALL | Forge |
| C13 | **Per-Seat Dream Log Format** — define per-seat REM log template (S1–S7 each have a seat-specific dream extraction footer) | M9 | T2 | ALL | Forge |

---

## 🗂️ Ring D — Knowledge Graph & Archive Mining (13 quests)

| # | Quest Title | Zone | Tier | Seat | Class |
|---|---|---|---|---|---|
| D01 | **Metatron Topology Map** — create `archive/knowledge_graph/METATRON_CUBE_TOPOLOGY.md` mapping all 13 spheres (Center + Ring 1 + Ring 2) to repo components with ASCII/Mermaid diagram | M8 | T2 | S1 | Forge |
| D02 | **Knowledge Graph Seed JSONL** — create `archive/knowledge_graph/GRAPH_SEED.jsonl` with node+edge records linking all major docs, schemas, seats, tests, modules | M8 | T3 | S7 | Forge |
| D03 | **Archive-Mine Protocol** — create `archive/knowledge_graph/ARCHIVE_MINE_PROTOCOL.md` defining how to surface and index cross-references systematically | M8 | T2 | S6 | Forge |
| D04 | **Omnispec Prime Artifact** — create `projects/aetherforge-game-world/OMNISPEC_PRIME_CANDIDATE_v0.1.md` as the dedicated worldbuilding artifact for issue #170 review | M8 | T3 | S1 | Forge |
| D05 | **AtlasBrain Raw Log First Entry** — preserve first real transcript in `archive/boot/atlasbrain/raw_logs/` following evidence-chain protocol | M5 | T2 | S1 | Restoration |
| D06 | **AtlasBrain Evidence Packet** — create first real evidence packet in `archive/boot/atlasbrain/evidence_packets/` from raw log | M5 | T2 | S1 | Forge |
| D07 | **AtlasBrain Benchmark Entry** — create first rubric-scored benchmark entry in `archive/boot/atlasbrain/benchmarks/` | M5 | T2 | S1 | Trial |
| D08 | **AtlasBrain Learning Claims Taxonomy** — create `archive/boot/atlasbrain/learning_claims/LEARNING_CLAIM_TAXONOMY_v0.1.md` classifying all 8 adaptation types | M5 | T2 | S1 | Forge |
| D09 | **ORCS Route Index JSONL** — create `archive/knowledge_graph/ORCS_ROUTE_INDEX.seed.jsonl` with all project domains, route classes, and seat assignments | M3 | T3 | S1 | Forge |
| D10 | **ORCS Route Class Taxonomy** — create `archive/spec/orcs/ORCS_ROUTE_CLASS_TAXONOMY_v0.1.md` defining all route types, tags, and handoff protocols | M3 | T2 | S1 | Forge |
| D11 | **Vendor Bridge → ORCS Cross-Reference** — link Module 9 vendor maps to ORCS route index entries | M4 | T2 | S4 | Forge |
| D12 | **Archive Bowl Issue Links** — update `ARCHIVE_BOWL_PROBLEM_INDEX_v0.1.md` with direct GitHub issue links for all 50 problems that have open issues | M8 | T2 | S7 | Forge |
| D13 | **CHANGELOG.md** — create top-level `CHANGELOG.md` tracking all major milestones, module completions, and canon ratification events | M1 | T1 | S2 | Forge |

---

## ⚔️ Ring E — Tests, CI & Adversarial (13 quests)

| # | Quest Title | Zone | Tier | Seat | Class |
|---|---|---|---|---|---|
| E01 | **Adversarial Tests T13→T20** — write 8 new adversarial tests covering untested failure modes (overclaim without evidence, sealed-memory recall, missing ratification event ID, etc.) | M6 | T3 | S3 | Trial |
| E02 | **atlas_orcs compatible.py Tests** — add dedicated test file for `reference_impl/atlas_orcs/compatible.py` edge cases | M6 | T2 | S7 | Trial |
| E03 | **atlas_orcs delta.py Tests** — add test coverage for delta diffing logic | M6 | T2 | S7 | Trial |
| E04 | **atlas_orcs quarantine.py Tests** — add test coverage for quarantine routing and block behavior | M6 | T2 | S7 | Trial |
| E05 | **atlas_orcs ratification.py Tests** — add tests for ratification event validation and block paths | M6 | T2 | S7 | Trial |
| E06 | **receipt_foundry dry_run.py Tests** — add test coverage for dry-run receipt generation | M5 | T2 | S7 | Trial |
| E07 | **native_thread/validator.py Edge Cases** — extend test_native_thread_validator.py with rejection/pass boundary cases | M6 | T2 | S7 | Trial |
| E08 | **o_ai/validator.py Edge Cases** — extend test_o_ai_validator.py with rejection/pass boundary cases | M4 | T2 | S7 | Trial |
| E09 | **Schema Presence Test Update** — update `test_schema_presence.py` to cover all 15+ YAML schemas in `schemas/atlas_orcs/v0_1/`, `schemas/o_ai/v0_1/`, `schemas/native_thread/v0_1/` | M6 | T2 | S7 | Trial |
| E10 | **CI: Adversarial-Only Workflow** — add `.github/workflows/adversarial-tests.yml` to run `tests/adversarial/` independently for fast red-team feedback | M7 | T2 | S7 | Forge |
| E11 | **Canon Gate Test Fixture** — create `testdata/canon_gate_fixture.json` — a promotion-block scenario and a promotion-pass scenario for reuse across test suites | M6 | T2 | S7 | Forge |
| E12 | **JSONL Roundtrip Test** — add test proving that claim ledger JSONL roundtrip does not lose provenance or confidence fields | M5 | T2 | S7 | Trial |
| E13 | **Boss Fight Registry** — create `projects/aetherforge-game-world/AETHERFORGE_BOSS_FIGHT_REGISTRY.md` naming all adversarial tests as boss encounters with zone, tier, and current pass status | M6 | T2 | S3 | Forge |

---

## 🌐 Ring F — Public Launch & Open Source (13 quests)

| # | Quest Title | Zone | Tier | Seat | Class |
|---|---|---|---|---|---|
| F01 | **docs/START_HERE.md** — create the missing entry-point doc (referenced in memory/SITREP but not in docs/) | M9 | T1 | S2 | Forge |
| F02 | **docs/ARCHIVE_INDEX.md** — create structured archive directory for docs/ (referenced but missing) | M9 | T1 | S2 | Forge |
| F03 | **docs/GLOSSARY.md** — create glossary for all project-specific terms (Krakoa, ORCS, Canon Spine, REM-8, etc.) | M9 | T2 | S2 | Forge |
| F04 | **PUBLIC_SAFE_README.md** — create a public-facing README candidate that translates Krakoa metaphors into plain-language project descriptions | M9 | T2 | S2 | Forge |
| F05 | **SECURITY.md** — create responsible-disclosure policy for security vulnerabilities | M7 | T1 | S7 | Forge |
| F06 | **CODE_OF_CONDUCT.md** — add Contributor Covenant or equivalent for open-source readiness | M7 | T1 | S7 | Forge |
| F07 | **CONTRIBUTING_PUBLIC.md** — create external-contributor guide (separate from internal `.github/CONTRIBUTING.md`) | M7 | T2 | S2 | Forge |
| F08 | **GitHub Issue Templates** — add `.github/ISSUE_TEMPLATE/` with bug-report, quest-card, and feature-request templates | M7 | T2 | S7 | Forge |
| F09 | **GitHub PR Template Update** — add Aetherforge quest-card fields (zone, tier, boss fight, loot) to `.github/PULL_REQUEST_TEMPLATE.md` | M7 | T1 | S7 | Forge |
| F10 | **Git History Review Plan** — create `KRAKOA_HISTORY_REVIEW_PLAN.md` documenting the pre-launch history audit scope and decision point for @atlaslattice | M2 | T2 | S7 | Council |
| F11 | **Docs Link Check Repair** — audit `docs-link-checks.yml` and repair any broken internal links flagged by CI | M7 | T1 | S7 | Restoration |
| F12 | **Loot Registry** — create `projects/aetherforge-game-world/AETHERFORGE_LOOT_REGISTRY.md` cataloguing all merged artifacts as named loot drops with zone, tier, and merge date | M8 | T1 | S6 | Forge |
| F13 | **Player Guide** — create `projects/aetherforge-game-world/AETHERFORGE_PLAYER_GUIDE.md` — which seat handles which zone, which boss fights belong to which player | M9 | T2 | ALL | Forge |

---

## 🏛️ Ring G — Architecture & Integration (13 quests)

| # | Quest Title | Zone | Tier | Seat | Class |
|---|---|---|---|---|---|
| G01 | **Krakoa Layers Architecture Doc** — create `archive/boot/gptbrain/KRAKOA_LAYER_ARCHITECTURE_v0.1.md` mapping all 9 layers from Living Archive Charter into a testable component diagram | M2 | T3 | S1 | Forge |
| G02 | **Atlas Vault README** — create `codebases/atlas-vault/README.md` inventorying Krakoa Keep implementation status (krakoa_keep_module.py, krakoa_mcp_server.py) | M5 | T2 | S4 | Forge |
| G03 | **UWS Spec Stub** — create `archive/spec/uws/UWS_WORKSPACE_SPEC_CANDIDATE_v0.1.md` — Universal Workspace surface, headset, command layer | M3 | T3 | S4 | Forge |
| G04 | **Aluminum OS Constitutional Kernel** — create `archive/spec/aluminum_os/ALUMINUM_OS_KERNEL_CANDIDATE_v0.1.md` — constitutional kernel architecture stub | M3 | T3 | S4 | Forge |
| G05 | **Sheldonbrain Archive Substrate** — create `archive/spec/sheldonbrain/SHELDONBRAIN_SUBSTRATE_SPEC_v0.1.md` — long-term ontology, sphere144, project continuity | M8 | T3 | S6 | Forge |
| G06 | **House ORCS Spec** — create `archive/spec/orcs/ORCS_SPEC_v0.1.md` formalizing cross-project routing, ontology tags, source lineage, and handoff protocol | M3 | T3 | S1 | Forge |
| G07 | **Postgres Adapter Spec** — define interface contract for future Postgres + pgvector + Kuzu/Neo4j adapters (Phase 3 plan, not implementation) | M5 | T2 | S4 | Forge |
| G08 | **Council Integration Protocol** — create `archive/spec/council/COUNCIL_INTEGRATION_PROTOCOL_v0.1.md` — how each S1–S7 seat produces memory packets, claim ledger updates, and artifact registry updates | M2 | T3 | ALL | Forge |
| G09 | **Grokbrain (S3) Dream Protocol** — create `archive/boot/gptbrain/agents/S3_GROKBRAIN_ADVERSARIAL_DREAM_PROTOCOL.md` for adversarial REM play | M9 | T2 | S3 | Forge |
| G10 | **Mermaid Architecture Diagram** — add a Mermaid diagram to `README.md` showing the full Metatron's Cube topology with all major components | M8 | T2 | S7 | Forge |
| G11 | **S1 MemoryPacket Schema YAML** — create Phase 2 pydantic-to-YAML schema for MemoryPacket under `schemas/` for cross-seat interop | M6 | T2 | S1 | Forge |
| G12 | **S6 Memory Palace Hardening** — add edge-case tests and property docs for `archive/boot/gptbrain/reference_impl/s6_memory_palace/` | M6 | T2 | S6 | Trial |
| G13 | **100-Year Roadmap** — create `projects/aetherforge-game-world/AETHERFORGE_100Y_CIVILIZATION_PLAN.md` — mythic-tier vision doc for the 100-year evolution of the knowledge graph | M8 | T4 | ALL | Forge |

---

## Summary Matrix

| Ring | Theme | Quest Count | Tier Distribution |
|---|---|---|---|
| Center | Meta-Quest | 1 | 1×T4 |
| Ring A | Governance & Canon | 13 | 9×T1, 3×T2, 1×T3 |
| Ring B | Reference Impl & Code | 13 | 2×T1, 9×T2, 2×T3 |
| Ring C | Swarm & Agents | 13 | 3×T1, 7×T2, 3×T3 |
| Ring D | Knowledge Graph | 13 | 2×T1, 9×T2, 2×T3 |
| Ring E | Tests, CI & Adversarial | 13 | 0×T1, 11×T2, 2×T3 |
| Ring F | Public Launch | 13 | 5×T1, 7×T2, 1×T3 |
| Ring G | Architecture & Integration | 13 | 0×T1, 7×T2, 5×T3, 1×T4 |
| **Total** | | **100** | |

---

## Sequencing Recommendation

### Immediate (next sprint — T1 unblocked):
- A02 Gate Seed Ritual (unlocks ORCS routing)
- A09 Public Launch Blockers Issue (unlocks F-ring)
- A13 LICENSE Forge (required for public launch)
- B03 pyproject.toml (unlocks linter CI)
- C01/C03 LumenBrain + TIDELOCKBrain folders (answers Q-003/Q-004)
- D13 CHANGELOG.md (high-value, low-effort)
- F01/F02/F03 docs/ triad (fixes known gap)

### High leverage (T2 multipliers):
- B04/B05 Storage adapters (unlocks persistent memory)
- D01 Metatron Topology Map (unlocks cross-linking)
- D09 ORCS Route Index JSONL (unlocks routing for all new work)
- E01 Adversarial Tests T13→T20 (multiplies boss-fight coverage)
- G10 Mermaid Diagram in README (dramatically improves discoverability)

### Boss fights required before merge (T3+):
- B01 Package Split — requires all 79 existing tests still pass
- B10 Sheldonbrain Importer — requires AtlasBrain gate tests green
- C07 Swarm Slot Scout — requires @atlaslattice decision on naming
- G06 ORCS Spec — requires ORCS Route Index JSONL complete first

---

## Linked Artifacts

- Quest taxonomy: `projects/aetherforge-game-world/README.md`
- Archive Bowl index: `projects/aetherforge-game-world/ARCHIVE_BOWL_PROBLEM_INDEX_v0.1.md`
- Quest template: `projects/aetherforge-game-world/FUN_FRAMING_SERIOUS_ACCEPTANCE_TEMPLATE_v0.1.md`
- Module registry: `AETHERFORGE_MODULE_REGISTRY_v0.1.md`
- Krakoa execution ledger: `archive/boot/gptbrain/KRAKOA_TOP_50_EXECUTION_LEDGER_2026-05-26.md`
- Unresolved questions: `archive/boot/gptbrain/KRAKOA_UNRESOLVED_QUESTION_LEDGER_2026-05-26.md`
- TIDELOCKBrain audit log: `archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_WORK_LOG_TOP100_AUDIT_2026-05-26.md`
- TIDELOCK path strategy index: `archive/boot/gptbrain/TIDELOCKBrain/TIDELOCKBRAIN_PATH_STRATEGY_INDEX_2026-05-29.md`
