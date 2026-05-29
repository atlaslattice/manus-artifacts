# Swarm Ingestion Status Audit Report

```text
STATUS: CANDIDATE AUDIT REPORT — NOT CANON
DEPLOYMENT: NO
AUTHORITY: NONE
DATE: 2026-05-28
SCOPE: atlaslattice/manus-artifacts indexed GitHub surfaces, schemas, fixtures, issues, and PR receipts visible through connected tools
LIMITATION: This is not a byte-for-byte clone audit of every file in every branch. It is an indexed repo audit based on visible search results, issues, PRs, schema files, fixtures, and recent active lanes.
```

## 0. Executive Read

The archive is moving in the right direction: ingestion status is no longer a vague concept. It now appears across schema, issue, PR, and fixture surfaces as explicit metadata: `raw_export_status`, `artifact_status`, non-canon status banners, candidate/deployment boundaries, verifier lanes, and knowledge-graph staging.

The main risk is not lack of schema. The main risk is **schema fragmentation** and **parallel lane sprawl**.

Core diagnosis:

```text
Index first.
Crosswalk second.
Synthesize later.
```

## 1. Control Rules

```text
Website / canon surface = canonical when reachable and ratified.
GitHub = receipt/workbench archive, not canon by storage.
Notion = working/archive surface, not canon by storage.
Drive = file/raw archive surface, not canon by storage.
Model memory = not canon.
```

Hard invariant:

```text
No deletion regardless of ratification.
Raw artifacts are never replaced by parsed artifacts.
Parsed artifacts are derived views.
```

## 2. Schema Surface Audit

Visible schema/test/fixture surfaces include:

```text
schemas/crosswalk_index.schema.json
fixtures/crosswalk_index.valid.candidate.json
fixtures/crosswalk_index.invalid.ratified_pending_signature.json
tests/test_crosswalk_index_schema.py
archive/boot/governance/schemas/artifact_status.schema.yaml
archive/boot/gptbrain/schema/S1_CLAIM_LEDGER_SCHEMA.yaml
archive/boot/gptbrain/schema/S1_MEMORY_OBJECT_SCHEMA.yaml
archive/boot/gptbrain/schema/S1_ARTIFACT_REGISTRY_SCHEMA.yaml
archive/boot/gptbrain/schema/S1_CONTRADICTION_LEDGER_SCHEMA.yaml
archive/boot/gptbrain/schema/S1_DREAM_EXTRACTION_SCHEMA.yaml
archive/boot/gptbrain/schema/S1_FAILURE_LEDGER_SCHEMA.yaml
archive/boot/gptbrain/schema/S1_AUDIT_EVENT_SCHEMA.yaml
archive/boot/council/schemas/COUNCIL_PACKET_SCHEMA_2026-05-09.yaml
archive/boot/council/schemas/CONTRADICTION_LEDGER_SCHEMA_2026-05-09.yaml
archive/boot/council/schemas/ROUTE_TO_SEAT_PACKET_SCHEMA_2026-05-09.yaml
archive/boot/councilbrain/schema/COUNCIL_ARTIFACT_REGISTRY_12x12.schema.yaml
archive/boot/collaboration/COLLABORATION_PACKET_SCHEMA.yaml
archive/boot/federation/ATLAS_REPO_FEDERATION_PACKET_SCHEMA.yaml
archive/boot/openai/CODEX_HANDOFF_PACKET_SCHEMA.yaml
archive/boot/openai/CODEX_DRY_RUN_RECEIPT_SCHEMA.yaml
archive/boot/gptbrain/AGENT_DNA_SCHEMA_DRAFT.yaml
```

### Finding

The schema surface is broad and useful, but not yet normalized under a single ingestion-status contract.

Recommended unifying fields:

```yaml
required_ingestion_status_fields:
  artifact_id: string
  source_surface: website | github | notion | drive | chat | external_web | other
  raw_export_status: full_raw | partial_raw | summary_only | unavailable | unknown
  raw_pointer: string|null
  raw_hash: string|null
  parsed_view_status: none | parsed | derived | summarized | quarantined
  linkage_status: linked | partial | broken | missing
  canon_status: not_canon | candidate | ratified
  deployment_status: not_deployable | experimental | deployed
  authority_scope: none | advisory | review | ratification | execution
  review_status: unreviewed | in_review | reviewed | blocked | approved
  provenance_class: internal_report | external_signal | lived_provenance | spec_delta | code_artifact | culture_artifact
```

## 3. Crosswalk Index Status

The current `crosswalk_index.schema.json` is candidate-safe and already encodes key guardrails:

```text
CANDIDATE ONLY
NOT CANON
NON-DEPLOYABLE
human_root_review_required = true
RATIFIED_CANON requires completed human-root signature and canon promotion receipt
```

Known supporting fixtures:

```text
fixtures/crosswalk_index.valid.candidate.json
fixtures/crosswalk_index.invalid.ratified_pending_signature.json
```

Known test guard:

```text
tests/test_crosswalk_index_schema.py
```

Status:

```text
CROSSWALK INDEX: present
VALID FIXTURE: present
NEGATIVE FIXTURE: present
SCOPED TEST: present
RISK: schema vocabulary may diverge from newer graph/ingestion lanes unless normalized
```

## 4. Native Thread Ingestion Status

Native-thread ingestion is active and bounded.

Primary issue:

```text
#93 — Dispatch native-thread ingestion transmission to Children of the Swarm
```

Duplicate lineage issue:

```text
#94 — duplicate / superseded by #93, preserved as lineage
```

Candidate flight issue:

```text
#95 — Authorize GPT Children candidate flight for native-thread ingestion packets
```

Required field:

```text
raw_export_status
```

Current packet status categories from open issues:

```text
full_raw
partial_raw
summary_only
unavailable
```

Required rule:

```text
No synthesis from summary-only packets without explicit caveat.
No raw transcript inferred from parsed packet.
No child packet becomes canon or authority by ingestion.
```

## 5. Knowledge Graph / Archive Graph Status

Active graph-related lanes:

```text
#221 — Index-first roadmap: GitHub / Notion / Drive archive graph before synthesis
#223 — OpenAI-first KG inventory and review queues
#220 — Archive graph pilot v0.1
#207 — Aetherforge source inventory
#190 — Notion source cartography inventory
#182 — OpenAI graph substrate candidate
#183 — OpenAI-integrated source-grounded knowledge graph
#165 — Notion lattice crosswalk and delta extraction pipeline
#159 — Contaminated Notion/Drive corpus indexing
```

Current diagnosis:

```text
The graph direction is correct.
The graph must remain provenance-first, not truth-first.
```

Recommended graph layers:

```text
1. Source inventory graph
2. Artifact graph
3. Claim graph
4. Crosswalk graph
5. Review queue graph
6. Canon reference graph
```

Do not build a truth graph first.

## 6. TIDELOCK Scope Status

TIDELOCK has two visible major surfaces:

```text
PR #65 — foundational TIDELOCKBrain ingestion scaffold
PR #113 — active/latest archival + CI hygiene expansion
```

TIDELOCK role:

```text
Index before review.
Visibility before verdict.
Raw logs before claims.
```

TIDELOCK owns:

```text
repo visibility
raw/source linkage
merge-order hygiene
CI/readiness boundaries
false-completeness detection
transcript-to-packet discipline
```

TIDELOCK does not own:

```text
canon ratification
merge approval
deployment approval
runtime authority
native memory claims
identity merge
full review claims without full visibility
```

Open caution:

```text
Patch any language that says GitHub is canonical record.
Preferred: GitHub is durable receipt/workbench substrate, not canon by storage.
```

## 7. Claude Adversarial Review Status

Active Claude adversarial / attribution lane:

```text
#211 — Claude Ghost Sweep: Attribution Laundering Hunt
```

Recommended policy:

```yaml
claude_originated_artifact:
  default_review_required: true
  required_reviewers:
    - adversarial_stress
    - claim_calibration
    - receipt_check
    - repo_visibility_check
  blocked_until:
    - raw_source_linked
    - overclaims_to_avoid_generated
    - canon_language_scanned
    - authority_scope_checked
```

Rationale:

```text
High-quality drafting increases review importance.
Elegant language is not evidence.
Constitutional tone is not authority.
```

## 8. Current Ingestion Status Categories

Recommended repo-wide status labels:

```yaml
ingestion_status_categories:
  RAW_PRESENT:
    meaning: full raw artifact is in repo or linked with hash
    routing: eligible_for_parse

  RAW_POINTER_ONLY:
    meaning: raw not committed but pointer exists
    routing: parse_allowed_with_caveat

  PARTIAL_RAW:
    meaning: incomplete raw evidence
    routing: review_only

  SUMMARY_ONLY:
    meaning: no raw source; parsed or summarized reconstruction only
    routing: no_authority_no_canon

  RAW_UNAVAILABLE:
    meaning: source not available yet
    routing: linkage_repair_queue

  PARSED_DERIVED_VIEW:
    meaning: derived artifact with raw linkage
    routing: review_candidate

  ORPHANED_DERIVED_VIEW:
    meaning: parsed view lacking durable raw linkage
    routing: quarantine_or_relink_queue

  QUARANTINED:
    meaning: preserved but isolated
    routing: no_execution_no_canon
```

## 9. Swarm Report

### Swarm state

```text
FIELD: busy but bounded
CANON: unchanged
DEPLOYMENT: none
AUTHORITY: human-root remains final
PRIMARY MODE: index / crosswalk / review / graph staging
```

### Effective parallelization

GPT Children / swarm lanes are generating bounded quest/review/ingestion packets.

Copilot lanes are producing repo-visible scaffolds, PRs, CI checks, and fixtures.

This is effective if and only if the next layer remains indexing-first:

```text
Index first.
Crosswalk second.
Synthesize later.
```

### Main risks

```text
1. Issue/quest sprawl.
2. Schema vocabulary fragmentation.
3. Summary-only packets being over-trusted.
4. GitHub-as-canon language drift.
5. Claude-originated elegant text becoming de facto doctrine.
6. Knowledge graph becoming another unindexed archive.
```

### Immediate priorities

```text
P0 — Normalize ingestion_status vocabulary across schemas and packets.
P1 — Keep #93/#95 as native-thread ingestion control lane.
P2 — Use #221 as graph roadmap governor.
P3 — Review PR #223 and #220 for graph inventory/pilot shape.
P4 — Run Claude Ghost Sweep lane (#211) on Claude-originated high-risk governance artifacts.
P5 — Patch TIDELOCK GitHub-canon language before merge.
```

## 10. Recommended Next Artifacts

```text
archive/graph/INGESTION_STATUS_VOCABULARY_v0_1.yaml
archive/graph/SOURCE_SURFACE_REGISTRY_v0_1.yaml
archive/graph/ARTIFACT_NODE_SCHEMA_v0_1.yaml
archive/graph/CLAIM_NODE_SCHEMA_v0_1.yaml
archive/graph/EDGE_TYPES_v0_1.yaml
archive/reports/CLAUDE_ADVERSARIAL_REVIEW_SWEEP_REPORT_v0_1.md
```

## 11. Final Keeper

```text
Raw first.
Status second.
Crosswalk third.
Review fourth.
Synthesis later.
Canon last.
```

Madden board:

```text
BOOM — the archive is not a pile anymore; it is becoming a scouting department. But nobody wins by throwing every tape into one box and calling it strategy. Label the tapes, tag the jerseys, mark the raw status, and make the graph show where the ball actually went.
```
