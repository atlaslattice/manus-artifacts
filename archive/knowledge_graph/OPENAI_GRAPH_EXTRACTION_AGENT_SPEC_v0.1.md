# OpenAI Graph Extraction Agent Spec v0.1

```text
STATUS: AGENT SPEC CANDIDATE — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
PURPOSE: define OpenAI-powered extraction/review/write-candidate roles for a source-grounded knowledge graph
```

## Core doctrine

```text
OpenAI is not the memory.
OpenAI is not canon.
OpenAI is not authority.
OpenAI may extract, classify, cite, test, route, and propose graph writes.
Human-root decides promotion.
```

## Intended stack

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

## Agent roles

### SourceScannerAgent

```text
Purpose: locate candidate SourceArtifact nodes across GitHub, Drive, Notion, and uploaded files.
May propose graph writes.
May not ratify source contents.
```

### ClaimExtractorAgent

```text
Purpose: extract exact claims from RawExport or ParsedPacket nodes using structured output.
May create Claim candidates.
May not convert claims into facts.
```

### ReceiptValidatorAgent

```text
Purpose: identify EvidenceAnchor nodes such as SHA-256, commit SHA, PR URL, Drive URL, or file ID.
May mark receipts missing.
May not infer receipt validity without verification.
```

### ContradictionScannerAgent

```text
Purpose: detect contradictions, supersessions, and drift between claims.
May create contradicts or supersedes edge candidates.
May not delete either branch.
```

### ReviewRouterAgent

```text
Purpose: route graph nodes into Rootglass, Lucerna, Hashlight, TIDELOCK, AtlasBrain, Sable Vesper, Grok, or Claude review lanes.
May assign review lanes.
May not approve promotion.
```

### GraphWriterCandidateAgent

```text
Purpose: produce graph write packets for review.
May write candidates to a staging branch or issue.
May not write directly to canon or overwrite prior lineage.
```

## Pipeline

```text
SourceArtifact
→ text extraction
→ structured claim extraction
→ evidence anchor extraction
→ contradiction detection
→ review packet generation
→ eval scoring
→ graph write candidate
→ human-root review
```

## Required graph write packet

```yaml
graph_write_candidate:
  packet_id: null
  source_nodes: []
  proposed_nodes: []
  proposed_edges: []
  evidence_anchors: []
  missing_receipts: []
  risk_flags: []
  review_lanes: []
  canon_status: not_canon
  deployment_status: not_deployable
  authority_scope: none
  human_root_required: true
```

## Evals required

```yaml
evals:
  source_classification_accuracy: pending
  raw_vs_summary_detection: pending
  canon_language_detection: pending
  authority_inflation_detection: pending
  legal_claim_detection: pending
  company_name_gravity_detection: pending
  unsupported_deployment_language_detection: pending
  missing_receipt_detection: pending
```

## Guardrails

```text
Retrieved chunk is not truth.
Structured output is not proof.
Graph write candidate is not ratification.
Agent action is not human-root approval.
No silent canon promotion.
No lineage deletion.
No authority assignment without explicit decision node.
```

## First 10 graph queries to support

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
```

## Keeper

```text
First build the clipboard.
Then label the boxes.
Then scan the receipts.
Then let the agents argue about what the boxes mean.
```