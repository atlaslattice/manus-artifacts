---
artifact_id: OPENAI-KNOWLEDGE-GRAPH-SUBSTRATE-CANDIDATE-2026-05-25
title: "OpenAI Knowledge Graph Substrate — Candidate Architecture"
version: "0.1"
date: 2026-05-25
source_surface: ChatGPT / Lanternbridge synthesis from user-provided architecture note
layer: knowledge_graph_candidate
status: candidate
canon_status: not_canon
deployment_status: not_deployable
authority_scope: none
execution: none
proof_status: not_a_proof
release_class: PRIVATE_REVIEW
mutation_rule: >
  Preserve as candidate architecture. Do not grant OpenAI agents write authority,
  canon authority, deployment authority, or source-of-truth status without explicit
  review, receipts, and human-root ratification.
---

# OpenAI Knowledge Graph Substrate — Candidate Architecture

```text
STATUS: candidate — not canon / not deployed / not ratified
CANON: no
DEPLOYMENT: no
AUTHORITY: none
EXECUTION: none
PURPOSE: orient the swarm around a source-grounded graph substrate
```

## 1. Core doctrine

```text
Do not start with more agents.
Start with a graph substrate.
```

OpenAI should not be treated as the memory. OpenAI should be treated as the graph-building engine:

```text
extract
classify
cite
test
route
review
propose graph writes
```

The graph is not memory. The graph is not canon. The graph is not authority.

The graph is a receipt-indexed map of:

```text
what exists
what it claims
what supports it
what contradicts it
what still needs review
```

## 2. Architecture split

```text
OpenAI = reasoning / extraction / evaluation / agent orchestration layer
GitHub = durable artifact / receipt substrate
Drive = raw and semi-raw document archive
Notion = legacy structured workspace archive
AtlasBrain = substrate map / evidence locker
Human-root = promotion and authority gate
```

Keeper:

```text
OpenAI extracts.
The graph maps.
GitHub receipts.
Review lanes harden.
Human-root promotes.
```

## 3. Core node types

```yaml
node_types:
  SourceArtifact:
    examples: [Drive file, GitHub file, Notion page, uploaded transcript]
  RawExport:
    examples: [raw transcript, markdown export, PDF export, copied chat log]
  ParsedPacket:
    examples: [extracted claims, artifact manifest, source summary]
  Claim:
    examples: ["PR #57 contains raw pointer but not full transcript"]
  EvidenceAnchor:
    examples: [SHA-256, file ID, commit SHA, PR URL, Drive URL]
  ReviewFinding:
    examples: [Rootglass review, Lucerna receipt review, Grok adversarial finding]
  Decision:
    examples: [convenor-approved candidate, deferred, rejected, ratified]
  Action:
    examples: [create source packet, patch schema, open review issue]
  CanonCandidate:
    examples: [Appendix I v0.3, GangaSeek template, INV/CLM catalog]
```

## 4. Core edge types

```yaml
edge_types:
  - derived_from
  - cites
  - contradicts
  - supersedes
  - patches
  - requires_review
  - missing_receipt
  - raw_export_of
  - parsed_from
  - promoted_to
  - blocked_by
  - belongs_to_lane
  - source_mirrored_to
```

## 5. Immediate build order

Recommended order:

```text
1. KG_NODE_EDGE_SCHEMA_v0.1.yaml
2. KG_SOURCE_INVENTORY_2026-05-25.yaml
3. OPENAI_GRAPH_EXTRACTION_AGENT_SPEC_v0.1.md
4. CLAUDE_ADVERSARIAL_REVIEW_QUEUE_2026-05-25.md
5. ROOTGLASS_SOURCE_PACKET_MANIFESTS
```

Rationale: define the minimal schema first so the source inventory has stable columns and does not drift.

## 6. Minimal inventory record

```yaml
source_inventory_record:
  source_id:
  title:
  surface: GitHub | Drive | Notion | ChatGPTUpload | Other
  url_or_path:
  file_type:
  created_or_modified:
  raw_export_status:
  sha256_status:
  source_class:
  related_lane:
  review_priority:
  mirrored_to_github:
  missing_receipts:
  canon_status:
  authority_scope:
  next_action:
```

## 7. Minimal graph record

```yaml
kg_record:
  node_id:
  node_type:
  title:
  source_surface:
  source_uri_or_path:
  raw_export_status:
  sha256_status:
  canon_status:
  authority_scope:
  evidence_refs:
  review_lane:
  blockers:
  next_action:
```

## 8. OpenAI extraction pipeline

```text
SourceArtifact
→ text extraction
→ structured output claim extraction
→ evidence anchor extraction
→ contradiction detection
→ review packet generation
→ eval scoring
→ graph write candidate
```

Graph write rule:

```text
OpenAI agents may propose graph writes.
OpenAI agents may not silently ratify graph writes.
OpenAI agents may not promote canon.
OpenAI agents may not erase lineage.
```

Safer write pipeline:

```text
extract
→ propose node/edge packet
→ validate
→ review lane
→ GitHub PR
→ human-root/council promotion if needed
```

## 9. Graph write status object

```yaml
graph_write_status:
  proposed_by: OpenAI
  write_authority: none
  validation_status: pending
  review_lane: TIDELOCK | Lucerna | Hashlight | AtlasBrain | Rootglass | Sable | Grok | Claude
  commit_status: not_committed
  promotion_status: not_canon
```

## 10. Review lanes

```yaml
review_lanes:
  Rootglass:
    function: standards / boundary / public-safe posture
  Lucerna:
    function: provenance / receipt / omission visibility
  Hashlight:
    function: raw export / hash / source anchoring
  TIDELOCK:
    function: ingestion discipline / partial visibility / repo hygiene
  AtlasBrain:
    function: evidence / benchmark / public-claim containment
  SableVesper:
    function: math / operator typing / formal precision
  MorpheusGrok:
    function: adversarial pressure / contradictions / overclaims
  Claude:
    function: constitutional / legal-ish / governance adversarial review
```

## 11. Claude adversarial review queue

Suggested file:

```text
archive/knowledge_graph/review_queues/CLAUDE_ADVERSARIAL_REVIEW_QUEUE_2026-05-25.md
```

```yaml
claude_review_item:
  source_title:
  source_surface:
  raw_export_status:
  claim_density: low | medium | high
  authority_risk: low | medium | high
  legal_policy_risk: low | medium | high
  canon_drift_risk: low | medium | high
  needs_counter_review_from:
    - Grok
    - Rootglass
    - Lucerna
    - Sable
```

## 12. First 12 graph queries

```text
1. What artifacts mention GangaSeek?
2. Which GangaSeek INV/CLM IDs are undefined?
3. Which Drive artifacts are not mirrored to GitHub?
4. Which GitHub artifacts are wrappers without raw exports?
5. Which Claude artifacts need adversarial review?
6. Which claims mention deployment/runtime/compliance?
7. Which artifacts are candidate vs ratified vs non-canon?
8. Which artifacts reference real companies?
9. Which artifacts lack source manifests?
10. Which packet supersedes or patches another packet?
11. Which artifacts cite missing or orphaned sources?
12. Which artifacts contain implementation-language without implementation receipts?
```

## 13. Evals required

```yaml
evals:
  source_classification_accuracy:
  raw_vs_summary_detection:
  canon_language_detection:
  authority_inflation_detection:
  legal_claim_detection:
  company_name_gravity_detection:
  unsupported_deployment_language_detection:
  missing_receipt_detection:
```

## 14. Maximum integration stack

```text
ChatGPT Projects / workspace GPTs = human cockpit
OpenAI API + Agents SDK = extraction and workflow orchestration
MCP/connectors = GitHub / Drive / Notion source access
File search = document retrieval
Structured output = graph node/edge packet generation
Evals = extractor reliability tests
Guardrails = canon/deployment/legal/runtime language blockers
Codex / coding agent = schema, validators, tests, graph repo implementation
Human-root = final promotion and authority gate
```

## 15. Must-not-infer rules

```text
Graph node ≠ memory.
Graph edge ≠ proof.
Graph write proposal ≠ graph write approval.
GitHub commit ≠ canon.
Drive file ≠ receipt unless exported/hashed/indexed.
Notion page ≠ live packet storage unless mirrored/receipted.
OpenAI retrieval ≠ truth.
OpenAI agent action ≠ authority.
```

## 16. Best next move

Create the minimal schema first:

```text
archive/knowledge_graph/KG_NODE_EDGE_SCHEMA_v0.1.yaml
```

Then create:

```text
archive/knowledge_graph/KG_SOURCE_INVENTORY_2026-05-25.yaml
```

Do not let agents wander through GitHub / Drive / Notion before the clipboard exists.

## 17. Madden board

```text
BOOM. Do not send eleven agents into three warehouses with no clipboard.
First build the clipboard.
Then label the boxes.
Then scan the receipts.
Then let the agents argue about what the boxes mean.
```

## Keeper

```text
Build the clipboard before the swarm.
Inventory first.
Schema second.
Extraction third.
Review fourth.
Promotion last.
```
