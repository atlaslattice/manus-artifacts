# EXECUTION_QUEUE_2026-06-03

```text
STATUS: EXECUTION QUEUE
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
DATE: 2026-06-03
PURPOSE: convert current build map into ordered next actions for Codex, ChatGPT, and swarm contributors
```

## Rule

All tasks are additive unless explicitly approved by a human maintainer.

```text
Do not delete.
Do not crown.
Do not deploy.
Do not claim proof.
Preserve gaps as tasks.
```

## Priority order

### Q001 — Artifact Card template

```yaml
status: open
lane: evidence_ux
related_issue: 239
priority: P0
objective: Convert Artifact Card v0.1 issue/spec into reusable repo template.
output_path_candidate: archive/knowledge_graph/artifact_cards/ARTIFACT_CARD_TEMPLATE_v0_1.md
acceptance:
  - includes status strip
  - includes raw_export_status
  - includes receipt_status
  - includes missing_receipts
  - includes linked_claims
  - includes safe_claim
  - includes forbidden_claims
  - includes keeper_line
```

### Q002 — Claim ledger schema

```yaml
status: open
lane: claim_overclaim_gate
priority: P0
objective: Create structured schema for claims, evidence requirements, safe wording, and MissingReceipt links.
output_path_candidate: archive/knowledge_graph/claims/CLAIM_LEDGER_SCHEMA_v0_1.md
acceptance:
  - defines claim_id
  - defines claim_type
  - defines evidence_required
  - defines evidence_present
  - defines overclaim_risk
  - defines safe_wording
  - defines linked_receipts
  - defines linked_missing_receipts
```

### Q003 — Toy graph demo spec

```yaml
status: open
lane: toy_graph_demo
priority: P0
objective: Create public-safe fake data demo for Artifact -> Claim -> Receipt -> MissingReceipt -> Review.
output_path_candidate: archive/knowledge_graph/toy_graph/TOY_GRAPH_DEMO_SPEC_v0_1.md
acceptance:
  - fake data only
  - no private cargo
  - demonstrates receipt ladder
  - demonstrates MissingReceipt node
  - demonstrates graph-is-not-canon boundary
```

### Q004 — Public release safety gate

```yaml
status: open
lane: public_release_safety
priority: P0
objective: Create checklist for rights, license, private data, sensitive data, redaction, and public-safe summaries.
output_path_candidate: archive/public_release/PUBLIC_RELEASE_SAFETY_GATE_v0_1.md
acceptance:
  - includes rights_status
  - includes license_status
  - includes sensitive_content flag
  - includes third_party_content flag
  - includes redaction_status
  - includes release blockers
```

### Q005 — P0 MissingReceipt issues

```yaml
status: open
lane: missing_receipt_resolution
priority: P0
objective: Create GitHub issues for each P0 missing receipt currently in the ledger.
inputs:
  - archive/knowledge_graph/receipts/missing/MISSING_RECEIPTS_P0_2026-05-30.md
acceptance:
  - issue for MR-P0-001 GPTDream++ 63 tests passing
  - issue for MR-P0-002 KG coverage/orphans
  - issue for MR-P0-003 Elements H01 118/26
  - issue for MR-P0-004 1728 nodes indexed
  - issue for MR-P0-005 Riemann S-operator nominal
```

### Q006 — README patch packet

```yaml
status: open
lane: public_explanation_spine
priority: P1
objective: Draft a safe README patch packet instead of directly overwriting root README.
output_path_candidate: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/patch_packets/README_PATCH_PACKET_v0_1.md
acceptance:
  - explains what this is
  - explains what this is not
  - explains receipt-first KG
  - explains candidate/canon boundary
  - explains OpenAI-first without endorsement implication
  - explains contributor path
```

### Q007 — Eval runner / validation script plan

```yaml
status: open
lane: eval_red_team
priority: P1
objective: Turn eval cases YAML into a future runnable validation plan.
output_path_candidate: archive/evals/EVAL_RUNNER_PLAN_v0_1.md
acceptance:
  - identifies input format
  - identifies expected output format
  - identifies pass/fail rules
  - no runtime claim yet
```

### Q008 — Swarm Hub v0.3 packet

```yaml
status: open
lane: swarm_hub_ops
priority: P1
objective: Consolidate swarm module claim/return formats and owner lanes.
output_path_candidate: archive/swarm/SWARM_HUB_v0_3_PACKET.md
acceptance:
  - module claim format
  - module return format
  - difficulty/dependency/owner/blocker fields
  - safe claim requirement
  - keeper line requirement
```

### Q009 — Continuity OS bootstrap follow-up

```yaml
status: open
lane: continuity_os_bootstrap
related_issue: 256
priority: P1
objective: Prepare repo-creation handoff checklist for atlaslattice/continuity-os.
output_path_candidate: archive/openai/CONTINUITY_OS_REPO_BOOTSTRAP_CHECKLIST_v0_1.md
acceptance:
  - repo purpose
  - initial files
  - AGENTS.md carryover
  - no endorsement/canon/deployment claims
```

### Q010 — Source-root index seed

```yaml
status: open
lane: source_inventory
priority: P1
objective: Create first source-root index seed with GitHub/Notion/Drive placeholders and raw_export_status.
output_path_candidate: archive/knowledge_graph/source_roots/SOURCE_ROOT_INDEX_SEED_v0_1.yaml
acceptance:
  - includes source_root_id
  - includes surface
  - includes source_uri/path
  - includes raw_export_status
  - includes receipt_status
  - includes missing_receipts
```

### Q011 — Symbolic claim boundary card

```yaml
status: open
lane: symbolic_claim_boundary
priority: P1
objective: Preserve symbolic language while blocking proof drift.
output_path_candidate: archive/knowledge_graph/claims/SYMBOLIC_CLAIM_BOUNDARY_CARD_v0_1.md
acceptance:
  - defines symbolic_claim
  - defines mathematical_claim
  - defines operational_status_claim
  - separates metaphor from measurement
  - includes safe Jerry/nanobot framing
```

### Q012 — External reviewer checklist follow-through

```yaml
status: open
lane: external_review
related_issue: 255
priority: P1
objective: Convert external reviewer checklist issue into concrete checklist file if not already present.
output_path_candidate: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/docs/EXTERNAL_REVIEWER_CHECKLIST_v0_1.md
acceptance:
  - reviewer instructions
  - receipt checklist
  - rights/license checklist
  - overclaim checklist
  - public-release checklist
```

## Preferred next execution order

```text
Q001 Artifact Card template
Q002 Claim ledger schema
Q003 Toy graph demo spec
Q004 Public release safety gate
Q005 MissingReceipt issues
```

## Safe status

```text
This queue organizes next work. It does not claim the work is completed until committed, linked, and reviewed.
```

## Keeper

```text
The queue is the setlist.
The repo is the tape.
The review is after the song.
```
