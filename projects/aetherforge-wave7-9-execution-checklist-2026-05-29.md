# Aetherforge Wave 7–9 — Execution Checklist
Status: Candidate
Date: 2026-05-29
Waves: 7–9 (Tasks 73–108)

Concrete execution checklist for the Next-144 board, focused on turning the lattice into a provenance-first, public-safe, world-class GitHub knowledge graph.

---

## Mission

Execute Waves 7–9 with strict governance boundaries, complete provenance coverage, deterministic operations, and a fork-and-synthesis intake path for missing components.

---

## Wave 7 — Canonical Governance Hardening (Tasks 73–84)

- [ ] Add/normalize candidate vs canon state fields across key indexes and registries.
- [ ] Require ratification metadata (`ratification_event_id`, `canon_status`, `trust_state`) for promotion routes.
- [ ] Add governance validation checks that fail on promotion packets missing adjudication evidence.
- [ ] Add decision-log linkage checks between candidate register and canon decision records.
- [ ] Define explicit website/publication gate criteria for canon-surface publishing.
- [ ] Publish governance runbook update for candidate→canon lifecycle controls.
- [ ] Add regression tests for canon-state transition invariants.
- [ ] Record Wave 7 receipts in Next-144 taskboard on completion.

### Wave 7 KPIs

- promotion_packets_with_complete_metadata ≥ 99%
- invalid_canon_transitions_blocked = 100%
- adjudication_link_coverage = 100%

---

## Wave 8 — Provenance-First KG Completeness (Tasks 85–96)

- [ ] Enforce required fields on all new/updated artifacts: H-S-N coordinate, source, license posture, evidence links, review state.
- [ ] Run orphan-node and dangling-lineage detection and create fix queue.
- [ ] Resolve high-priority lineage gaps and missing attribution records.
- [ ] Add quality gate thresholds for receipt coverage and attribution completeness.
- [ ] Add/refresh importer validations to reject malformed provenance packets.
- [ ] Add test fixtures for contradictory claims and unresolved evidence chains.
- [ ] Publish coverage scoreboard for provenance, receipts, and linkage health.
- [ ] Record Wave 8 receipts in Next-144 taskboard on completion.

### Wave 8 KPIs

- artifacts_with_full_provenance_fields ≥ 95%
- orphan_ratio ≤ 0.001
- attribution_completeness ≥ 98%

---

## Wave 9 — Operational Excellence + Fork-and-Synthesis (Tasks 97–108)

- [ ] Ensure deterministic graph/index build outputs and reproducible export receipts.
- [ ] Add fast query paths for claim→evidence→contradiction→review-status traversal.
- [ ] Publish operator-facing quality dashboard with build, quality-gate, and query health.
- [ ] Create fork-intake checklist: license, security, provenance, architecture fit, maintenance posture.
- [ ] Create synthesis register for accepted upstream components with source URL and commit lineage.
- [ ] Mark all imported modules as candidate until governance validation is complete.
- [ ] Add CI checks for third-party provenance/NOTICE completeness where applicable.
- [ ] Record Wave 9 receipts in Next-144 taskboard on completion.

### Wave 9 KPIs

- deterministic_build_pass_rate = 100%
- median_claim_trace_query_latency_ms ≤ 250
- fork_components_with_full_traceability = 100%
- imported_candidate_modules_validated_before_promotion = 100%

---

## Fork-and-Synthesis Guardrails (Required)

Any upstream fork or imported component must include:

- source repository URL
- source license and compatibility note
- pinned commit SHA
- rationale for inclusion
- adaptation notes
- security review receipt
- provenance/attribution receipt
- candidate-module marker until ratified

No forked/imported component is canon by default.

---

## Execution Cadence

For each task:

1. intake
2. normalize
3. link
4. validate
5. publish-candidate
6. adjudicate

---

## Links

- Campaign board: `projects/aetherforge-next144-taskboard-2026-05-28.md`
- Canon checklist: `docs/CANON_PROMOTION_CHECKLIST.md`
- Candidate register: `docs/canon-candidate-register.md`
- Quality gates workflow: `.github/workflows/lattice-kg-quality-gates.yml`
