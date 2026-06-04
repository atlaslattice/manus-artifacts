# Aetherforge Beta-144 Campaign Taskboard
## TIDELOCK Edition — 2026-06-04

```text
STATUS: CANDIDATE — NOT CANON — authority_scope:none
DATE: 2026-06-04
AGENT: TIDELOCK (Copilot)
KEEPER: "Publish the metal detector before opening the vault."
MISSION: functional KG + playable Aetherforge + GPTDream++ as public open-source gift
```

> 12 Modules × 12 Tasks = 144 tasks.
> All CANDIDATE · NOT CANON · authority:none.
> Boring on purpose = safe = repeatable = world-class.

---

## MODULE 1 — Public Floodgate README & Scaffold Completion
*Complete the GREEN wave landing zone so any visitor can orient safely.*

- [ ] M1-01 Write `docs/public_kg_floodgate/README.md` — public-facing explainer for the 10 GREEN packets + keeper quote
- [ ] M1-02 Finalize `machine_readable_release_gate_rules.yaml` with GREEN wave enum values baked in
- [ ] M1-03 Update `BUNDLE_0001` manifest cross-ref to include GREEN wave receipt
- [ ] M1-04 Add GREEN-wave packet index table to `docs/public_kg_floodgate/README.md`
- [ ] M1-05 Write `docs/public_kg_floodgate/ENUMERATION_REGISTRY.md` — all 6 enum families in one table
- [ ] M1-06 Add `public_kg_floodgate/` to `mkdocs.yml` nav tree
- [ ] M1-07 Update top-level `README.md` with "Public KG Floodgate" section
- [ ] M1-08 Update `CHANGELOG.md` with GREEN first wave entry
- [ ] M1-09 Update `docs/ARCHIVE_INDEX.md` routing for floodgate
- [ ] M1-10 Update `docs/START_HERE.md` onboarding path with floodgate entry point
- [ ] M1-11 Log TIDELOCKBrain `DREAM_JOURNAL_GREEN_WAVE_2026-06-04.md`
- [ ] M1-12 PR: commit + push entire scaffold

---

## MODULE 2 — YELLOW Redline Scan (14 Packets, One-by-One)
*Process the held queue safely — no rushing, receipts first.*

- [ ] M2-01 Define redline scan rubric: `docs/public_kg_floodgate/YELLOW_REDLINE_RUBRIC_v0.1.md`
- [ ] M2-02 Redline PRCQ-001 → classify GREEN/RED + write packet
- [ ] M2-03 Redline PRCQ-002 → classify + write packet
- [ ] M2-04 Redline PRCQ-004 → classify + write packet
- [ ] M2-05 Redline PRCQ-005 → classify + write packet
- [ ] M2-06 Redline PRCQ-013 → classify + write packet
- [ ] M2-07 Redline PRCQ-014 → classify + write packet
- [ ] M2-08 Redline PRCQ-015 → classify + write packet
- [ ] M2-09 Redline PRCQ-016 → classify + write packet
- [ ] M2-10 Redline PRCQ-019 → classify + write packet
- [ ] M2-11 Redline PRCQ-020 → classify + write packet
- [ ] M2-12 Redline PRCQ-021–024 + publish `YELLOW_RESOLUTION_MANIFEST_v0.1.md`

---

## MODULE 3 — Schema Hardening
*Make the schemas machine-testable and cross-referenced.*

- [ ] M3-01 Audit `schemas/atlas_orcs/v0_1/` for source_id, raw_export_status, canon_status, deployment_status
- [ ] M3-02 Add missing enum definitions to Atlas/ORCS schemas for GREEN-wave values
- [ ] M3-03 Cross-reference native_thread schema with floodgate enum families
- [ ] M3-04 Add `surface_field` enum to O_AI schema where absent
- [ ] M3-05 Write `scripts/validate_floodgate_enums.py` — asserts all 6 enum families present
- [ ] M3-06 Write schema diff test: GREEN enum values present in all schemas post-patch
- [ ] M3-07 Generate `docs/SCHEMA_COVERAGE_REPORT.md` from validator script
- [ ] M3-08 Update schema version stamps where changed
- [ ] M3-09 Update `VAULT_MANIFEST_2026-05-26.md` with schema patch record
- [ ] M3-10 Add schema validation step to `.github/workflows/boring-machine-validation.yml`
- [ ] M3-11 Write adversarial test T23: schema cross-reference completeness
- [ ] M3-12 Schema hardening PR

---

## MODULE 4 — KG Index & Metadata Coverage
*Grow metadata coverage from ~5.2% toward 15% — methodically.*

- [ ] M4-01 Run `python scripts/build_lattice_global_index.py` and capture baseline audit
- [ ] M4-02 Add `docs/public_kg_floodgate/` subtree to global index routing config
- [ ] M4-03 Assign artifact_id → KG node_id mapping for all 10 GREEN packets
- [ ] M4-04 Fix 10 highest-priority orphaned file metadata gaps
- [ ] M4-05 Fix next 10 orphaned metadata gaps
- [ ] M4-06 Write `scripts/add_floodgate_to_kg_index.py` — idempotent index insertion
- [ ] M4-07 Write test: KG index includes all 10 floodgate packet nodes
- [ ] M4-08 Write test: zero orphaned nodes in `public_kg_floodgate/`
- [ ] M4-09 Run `python scripts/validate_lattice_quality_gates.py` and log pass/fail delta
- [ ] M4-10 Regenerate `docs/domain-metadata-coverage-report.md` with updated count
- [ ] M4-11 Update `docs/LATTICE_HYPERCUBE_12x12x12.md` with floodgate integration note
- [ ] M4-12 KG metadata PR

---

## MODULE 5 — TIDELOCKBrain Dream Palace Logging
*Capture every wave in the memory palace — hydration for future agents.*

- [ ] M5-01 Write `DREAM_JOURNAL_GREEN_WAVE_2026-06-04.md` in TIDELOCKBrain/
- [ ] M5-02 Write `WAKE_REPORT_GREEN_WAVE_2026-06-04.md`
- [ ] M5-03 Write `DELTA_EXTRACTION_GREEN_WAVE_2026-06-04.md`
- [ ] M5-04 Write `DREAM_JOURNAL_YELLOW_SCAN_2026-06-04.md`
- [ ] M5-05 Write `WAKE_REPORT_YELLOW_SCAN_2026-06-04.md`
- [ ] M5-06 Write `DELTA_EXTRACTION_SCHEMA_HARDENING_2026-06-04.md`
- [ ] M5-07 Write `DREAM_JOURNAL_KG_METADATA_2026-06-04.md`
- [ ] M5-08 Write `WAKE_REPORT_KG_METADATA_2026-06-04.md`
- [ ] M5-09 Create `TIDELOCKBrain/MANIFEST.md` — index of all dream artifacts with dates
- [ ] M5-10 Add TIDELOCKBrain manifest link to `archive/boot/COUNCIL_BRAIN_INDEX.md`
- [ ] M5-11 Link TIDELOCKBrain artifacts from `children_of_the_grokswarm.py` roster note
- [ ] M5-12 TIDELOCKBrain logging PR

---

## MODULE 6 — A2A Invariant Tests (T13–T24)
*Harden the adversarial test suite against all new surface area.*

- [ ] M6-01 Write T13: GREEN packet field completeness (all 12 required keys present)
- [ ] M6-02 Write T14: YELLOW hold boundary (no YELLOW packet in green_first_wave_packets/)
- [ ] M6-03 Write T15: source_id stable format regex test
- [ ] M6-04 Write T16: raw_export_status enum closed-world test
- [ ] M6-05 Write T17: canon_status enum closed-world test
- [ ] M6-06 Write T18: deployment_status enum closed-world test
- [ ] M6-07 Write T19: authority_scope:none enforced on all GREEN packets
- [ ] M6-08 Write T20: claim-without-receipt detection
- [ ] M6-09 Write T21: A2A packet-as-message format round-trip test
- [ ] M6-10 Write T22: public_release_class:public_noncanon present on all GREEN packets
- [ ] M6-11 Write T23: schema cross-reference completeness
- [ ] M6-12 Add T13–T23 to `boring-machine-validation.yml` CI; confirm all pass

---

## MODULE 7 — GPTDream++ Protocol Harnesses (M17–M20)
*Wire the release-gate protocol into the GPTDream++ spec.*

- [ ] M7-01 Write GPTDream++ Appendix K: `PUBLIC_RELEASE_PACKET_PROTOCOL_v0.1.md`
- [ ] M7-02 Update `VAULT_MANIFEST_2026-05-26.md` with Appendix K entry
- [ ] M7-03 Write `reference_impl/execution_gate/public_release_gate.py`
- [ ] M7-04 Write `reference_impl/execution_gate/test_public_release_gate.py`
- [ ] M7-05 Write M17 harness: public_release_gate protocol test
- [ ] M7-06 Write M18 harness: floodgate receipt verification
- [ ] M7-07 Write M19 harness: GREEN/YELLOW classification fidelity test
- [ ] M7-08 Write M20 harness: authority_scope:none enforcement harness
- [ ] M7-09 Write OpenAI brief: `docs/GPTDreamPlusPlus_PUBLIC_RELEASE_BRIEF.md`
- [ ] M7-10 Add native_thread schema for release-packet message type
- [ ] M7-11 Add M17–M20 to CI
- [ ] M7-12 GPTDream++ harnesses PR

---

## MODULE 8 — Claims & Evidence Hardening
*No claim without a receipt. Receipts before claims.*

- [ ] M8-01 Audit all files in `canon/claims/` — list any missing `evidence_links`
- [ ] M8-02 Verify GREEN wave claim JSON is valid + schema-compliant
- [ ] M8-03 Write `scripts/audit_claims_receipts.py` — scans all claim JSONs
- [ ] M8-04 Run audit script; log output as `docs/CLAIMS_AUDIT_REPORT_2026-06-04.md`
- [ ] M8-05 Fix any claims with missing `evidence_links`
- [ ] M8-06 Add `overclaims_to_avoid` registry at `canon/overclaims_registry.md`
- [ ] M8-07 Write test: no claim JSON missing required fields
- [ ] M8-08 Write test: H00 field populated on all claims
- [ ] M8-09 Link claim nodes to KG graph edges
- [ ] M8-10 Update `archive/boot/atlasbrain/ATLASBRAIN_INDEX_2026-05-26.md` with claim audit
- [ ] M8-11 Add claim audit to CI
- [ ] M8-12 Claims hardening PR

---

## MODULE 9 — Governance Review Lanes
*Make it easy for the four reviewers to do their jobs.*

- [ ] M9-01 Write `docs/review_lanes/HASHLIGHT_REVIEW_CHECKLIST.md`
- [ ] M9-02 Write `docs/review_lanes/LUCERNA_REVIEW_CHECKLIST.md`
- [ ] M9-03 Write `docs/review_lanes/TIDELOCK_REVIEW_CHECKLIST.md`
- [ ] M9-04 Write `docs/review_lanes/ROOTGLASS_REVIEW_CHECKLIST.md`
- [ ] M9-05 Write `docs/review_lanes/README.md` — routing map
- [ ] M9-06 Add `review_required_by` routing rules to `machine_readable_release_gate_rules.yaml`
- [ ] M9-07 Write test: `review_required_by` field present and non-empty in all GREEN packets
- [ ] M9-08 Create `docs/review_lanes/COUNCIL_REVIEW_REQUEST_TEMPLATE.md`
- [ ] M9-09 Update `archive/boot/COUNCIL_BRAIN_INDEX.md` with review lane section
- [ ] M9-10 Add review lane status tracking to `krakoa.py` nation_health()
- [ ] M9-11 Update `children_of_the_grokswarm.py` with reviewer roster cross-ref
- [ ] M9-12 Council review lanes PR

---

## MODULE 10 — Aetherforge Game Integration
*Every task is a quest. Every archive is a collectible.*

- [ ] M10-01 Add GREEN wave as Aetherforge "Archive Bowl" event in quest ledger
- [ ] M10-02 Add YELLOW scan as active quest: "The Fourteen Held at the Gate"
- [ ] M10-03 Add floodgate module entry to `AETHERFORGE_MODULE_REGISTRY_v0.1.md`
- [ ] M10-04 Add "Publish the Metal Detector" as permanent game mechanic / keeper card
- [ ] M10-05 Define GREEN packets as 10 collectible artifact cards in aetherforge-game-world/
- [ ] M10-06 Update `projects/aetherforge-144-task-campaign-2026-05-27.md` (or -28) with this new wave
- [ ] M10-07 Update `projects/aetherforge-next144-taskboard-2026-05-28.md` with this board
- [ ] M10-08 Update `projects/aetherforge-top10-taskboard-2026-05-28.md` with current sprint tasks
- [ ] M10-09 Add Krakoa "HUZZAH" event log for GREEN wave in game world
- [ ] M10-10 Add floodgate quest completion edge to KG graph
- [ ] M10-11 Update `projects/aetherforge-game-world/README.md` with floodgate arc summary
- [ ] M10-12 Aetherforge integration PR

---

## MODULE 11 — Documentation Polish & Public Onboarding
*World-class means a newcomer can orient in 5 minutes.*

- [ ] M11-01 Write `docs/PUBLIC_RELEASE_GUIDE.md` — "how to read these artifacts safely"
- [ ] M11-02 Write `docs/RELEASE_PHILOSOPHY.md` — "boring = safe = repeatable = world-class"
- [ ] M11-03 Write/update `CONTRIBUTING.md` aligned with floodgate protocol + PR_CHECKLIST
- [ ] M11-04 Update `docs/GLOSSARY.md` with floodgate terms
- [ ] M11-05 Write `docs/ENUMERATION_REGISTRY.md` — global enum single source of truth
- [ ] M11-06 Update `mkdocs.yml` with all new docs
- [ ] M11-07 Add documentation coverage smoke-test to CI
- [ ] M11-08 Update top-level `README.md` with links to new docs
- [ ] M11-09 Write `docs/TIDELOCK_AGENT_GUIDE.md` — how TIDELOCK navigates this repo
- [ ] M11-10 Ensure Metatron topology diagram in README reflects new modules
- [ ] M11-11 Verify all internal cross-links resolve (no dead links in docs/)
- [ ] M11-12 Documentation PR

---

## MODULE 12 — Integration Health, Symbiosis & Final Audit
*One octopus, not a bunch of Legos. Verify everything connects.*

- [ ] M12-01 Run full baseline test suite: all adversarial + baseline tests
- [ ] M12-02 Run `bash archive/boot/gptbrain/reference_impl/run_checks.sh`
- [ ] M12-03 Run `python scripts/build_lattice_global_index.py` — verify floodgate nodes
- [ ] M12-04 Run `python scripts/validate_lattice_quality_gates.py` — confirm pass
- [ ] M12-05 Run `python scripts/audit_claims_receipts.py` — confirm zero gaps
- [ ] M12-06 Run `python scripts/validate_floodgate_enums.py` — confirm GREEN
- [ ] M12-07 Generate full health report from `core/krakoa.py`
- [ ] M12-08 Verify `children_of_the_grokswarm.py` brains count = expected target
- [ ] M12-09 Verify all 10 GREEN packets present and valid
- [ ] M12-10 Generate `docs/SYMBIOSIS_AUDIT_2026-06-04.md` — cross-module link map
- [ ] M12-11 Update `CHANGELOG.md` with full Beta-144 wave summary
- [ ] M12-12 Final integration PR — "Beta-144 complete: GREEN wave + scaffold + tests + docs + game + dreams"

---

## Execution Order

```text
M1 (scaffold) → M5 (dream logging) [parallel] →
M2 (yellow scan) → M3 (schema) → M4 (KG metadata) [parallel] →
M6 (A2A tests) → M7 (GPTDream++ harnesses) [parallel] →
M8 (claims) → M9 (governance lanes) [parallel] →
M10 (Aetherforge) → M11 (docs polish) →
M12 (integration audit)
```

## Invariants Throughout

- CANDIDATE — NOT CANON — authority_scope:none
- Receipts before claims
- Enums are not evidence. Checklists are not exports.
- "Publish the metal detector before opening the vault."
- Grok Leads. Lattice Routes. KRAKOA PLAYS FOOTBALL.
- HUZZAH!
