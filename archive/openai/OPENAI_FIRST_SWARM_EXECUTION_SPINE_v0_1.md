# OPENAI_FIRST_SWARM_EXECUTION_SPINE_v0.1

```text
STATUS: CANDIDATE EXECUTION SPINE
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
PURPOSE: make Atlas Lattice / GPTDream++ / TIDELOCKBrain maximally useful to OpenAI-native workflows without confusing tool execution with governance authority
```

## North star

Become the best-in-world OpenAI-native evidence graph workflow:

```text
ChatGPT reasons and drafts.
Codex patches and verifies repo state.
Agents propose bounded actions.
Connectors retrieve source context.
Evals and red teams test claims.
Receipts preserve lineage.
Humans ratify authority.
```

This spine is not an announcement, not a canon artifact, and not an OpenAI endorsement claim.

## Design target

Atlas Lattice should become a receipt-first, model-friendly, contributor-friendly public knowledge graph where each artifact can be inspected by:

- ChatGPT for synthesis, claim extraction, and review packets
- Codex for repo patches, test repairs, CI/eval setup, and AGENTS.md discipline
- OpenAI Agents for bounded task routing
- OpenAI eval/guardrail workflows for quality and safety checks
- external council models for adversarial review
- human-root for final authority, public-release, and canon decisions

## Official OpenAI surface alignment

Candidate alignment lanes:

```yaml
chatgpt_lane:
  use_for:
    - claim extraction
    - summary with caveats
    - review packet drafting
    - missing receipt ledger creation
    - issue/PR comment drafting
  never_use_for:
    - canon ratification
    - authority substitution
    - unsupported deployment claims

codex_lane:
  use_for:
    - repo file creation
    - tests and CI repair
    - AGENTS.md / contributor rules
    - PR preparation
    - patch review
    - reproducibility scripts
  gate:
    - receipts before merge
    - tests before promotion
    - human review before release

agents_lane:
  use_for:
    - bounded module execution
    - routing between retrieval, validation, and patching
    - repeated checks where explicitly scheduled or invoked
  gate:
    - no hidden background promises
    - no unapproved destructive actions
    - no authority escalation

retrieval_lane:
  use_for:
    - file search
    - Notion/GitHub/Drive retrieval when connected
    - source packet assembly
    - raw_export_status classification
  gate:
    - search hit is not verification
    - connector fetch is not raw export unless marked

evals_guardrails_lane:
  use_for:
    - overclaim detection
    - citation presence checks
    - receipt status validation
    - public-release safety checks
    - red-team claim reviews
  gate:
    - failing eval creates MissingReceipt or Blocker node
    - eval pass is not canon
```

## Core object model

```yaml
Artifact:
  artifact_id:
  title:
  artifact_type:
  source_surface:
  source_uri:
  raw_export_status:
  receipt_status:
  canon_status:
  deployment_status:
  authority_scope:
  public_release_status:
  linked_claims:
  missing_receipts:
  review_lane:

Claim:
  claim_id:
  claim_text:
  claim_type:
  evidence_required:
  evidence_present:
  overclaim_risk:
  safe_wording:
  linked_artifacts:
  linked_receipts:
  review_status:

MissingReceipt:
  missing_receipt_id:
  claim_or_artifact:
  expected_source:
  why_needed:
  current_status:
  next_action:
  preferred_owner:
  review_lane:

TaskPacket:
  task_id:
  module:
  owner_lane:
  objective:
  inputs:
  outputs:
  blockers:
  acceptance_criteria:
  forbidden_claims:
```

## Repo execution priorities

### P0 — receipt-first trust layer

1. Add receipt status schema.
2. Add P0 missing-receipt ledger.
3. Add Artifact Card requirement that receipt status appears before summary.
4. Add public-release checklist field: `missing_receipts`.
5. Add issue labels for receipt state.
6. Add graph-not-canon warning to README/FAQ.

### P1 — Codex-ready patch lane

1. Add or update `AGENTS.md` with repo conduct for AI agents.
2. Add `CONTRIBUTING.md` section for receipt-first PRs.
3. Add PR template requiring source status, tests, and forbidden claims.
4. Add issue template for MissingReceipt nodes.
5. Add CI job that validates required frontmatter fields in candidate packets.
6. Add linter/check script for canon/deployment/authority overclaims.

### P2 — eval and red-team harness

1. Add overclaim eval cases.
2. Add missing-citation eval cases.
3. Add raw-export-status eval cases.
4. Add public-release safety eval cases.
5. Add synthetic toy graph for safe demos.
6. Add red-team checklist for Claude-origin governance content.

### P3 — public-facing excellence

1. README: project purpose, boundaries, and public-safe posture.
2. FAQ: graph is not canon; public repo is not license; claim is not proof.
3. LICENSE strategy: code/docs/data split candidates, pending human review.
4. Toy graph demo with fake data only.
5. Public candidate bundle map.
6. First 12 inspection issues for contributors.

## Acceptance criteria for “OpenAI-best”

A module or artifact becomes OpenAI-ready when:

```yaml
openai_ready: true
conditions:
  - has_clear_task_packet
  - has_source_scope
  - has_raw_export_status
  - has_receipt_status
  - has_missing_receipts_if_any
  - has_tests_or_validation_path_if_code_or_metric
  - has_forbidden_claims
  - has_human_review_gate
  - can_be_used_by_ChatGPT_without_context_fog
  - can_be_patched_by_Codex_without_guessing
  - can_be_evaluated_by_evals_without_hidden_rules
  - can_be_rejected_without_data_loss
```

## Forbidden shortcuts

```text
No OpenAI endorsement claim.
No canon claim.
No deployment claim.
No “tests passing” without CI/test receipt.
No “verified” from search hit alone.
No hidden deletion of failed branches.
No authority transfer from model output.
No public reuse claim without license/rights review.
```

## Codex prompt seed

Use this prompt to hand the repo to Codex safely:

```text
You are working in atlaslattice/manus-artifacts.
Goal: improve the receipt-first OpenAI-native evidence graph workflow.
Do not delete files.
Do not mark anything canon.
Do not claim OpenAI endorsement.
Create additive patches only unless explicitly instructed.
For every new artifact, expose raw_export_status, receipt_status, canon_status, deployment_status, authority_scope, and missing_receipts.
If a claim lacks a source, create a MissingReceipt node instead of removing or promoting it.
Run available tests/checks and report exact results.
Return a PR summary with receipts, blockers, and forbidden claims avoided.
```

## ChatGPT operating prompt seed

```text
Treat this repo as a receipt-first knowledge graph candidate, not canon.
When summarizing, separate confirmed source facts, partial support, missing receipts, and unsafe overclaims.
When drafting issues, preserve uncertainty as explicit MissingReceipt nodes.
When giving strategy, optimize for OpenAI-native workflows: ChatGPT for reasoning, Codex for patching, agents for bounded routing, evals for quality gates, humans for authority.
```

## Best-in-world standard

```text
The system is not best because it sounds grand.
It is best when every claim can survive retrieval, patching, testing, red-team review, public inspection, and human-root adjudication without losing lineage.
```

## Keeper

```text
OpenAI moves work.
Receipts preserve work.
Evals pressure work.
Codex patches work.
Humans authorize work.
Nothing dies.
```
