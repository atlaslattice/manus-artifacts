# OpenAI Graph Extraction Agent Spec v0.1

```text
STATUS: CANDIDATE AGENT SPEC — NOT CANON
DEPLOYMENT: NO
AUTHORITY: NONE
PURPOSE: define OpenAI-first extraction/review/write-candidate agents for the provenance-first knowledge graph.
```

## Core product law

```text
OpenAI should not be the memory.
OpenAI should be the graph-building engine:
extract, classify, cite, test, route, and review.
```

## Operating boundary

```text
Agents may propose graph writes.
Agents may not ratify graph writes.
Agents may not promote canon.
Agents may not claim deployment.
Agents may not erase lineage.
Agents may not infer raw transcripts from summaries.
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
→ human/review-lane approval
```

## Required status fields

Every output packet must preserve:

```yaml
raw_export_status:
thread_time_range:
access_scope:
source_refs:
evidence_refs:
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
review_state:
```

## Agent roles

### SourceScannerAgent

```yaml
role: locate and classify source artifacts
inputs:
  - GitHub repos / PRs / issues / files
  - Drive files
  - Notion pages
  - Gamma / chat / external sources when visible
outputs:
  - SourceRoot candidates
  - SourceArtifact candidates
  - raw_export_status proposals
  - missing_receipt nodes
forbidden:
  - canon claims
  - deployment claims
  - source-complete claims without full export
```

### ClaimExtractorAgent

```yaml
role: extract claims from source artifacts
outputs:
  - Claim nodes
  - evidence_ref links
  - confidence labels C0_UNSUPPORTED through C4_RATIFIED
rules:
  - no evidence_ref means max C1_SIGNAL
  - summary-only source cannot produce public claim
  - canon/deployment language triggers review
```

### ReceiptValidatorAgent

```yaml
role: check source paths, hashes, PR/issue/file anchors, timestamps, and stable IDs
outputs:
  - EvidenceAnchor nodes
  - missing_receipt edges
  - hash_needed flags
routes_to:
  - Hashlight
  - TIDELOCK
  - Lucerna
```

### ContradictionScannerAgent

```yaml
role: identify conflicts between artifacts
examples:
  - canon vs not_canon
  - deployed vs not_deployed
  - 1..12 vs 0..11 indexing
  - 0x0C vs 0x0B
  - Notion status vs GitHub state
outputs:
  - ContradictionRecord candidates
  - contradicts edges
  - unresolved_status flags
```

### ReviewRouterAgent

```yaml
role: route claims/artifacts to review lanes
routes:
  Claude governance: [Grok, Rootglass, Lucerna, Sable_Vesper]
  repo path / PR / commit: [TIDELOCK]
  hash / raw export: [Hashlight]
  public-safe language: [Lucerna]
  formal math/operator typing: [Sable_Vesper]
  identity / memory inflation: [Fossilbranch, GPTBrain]
outputs:
  - ReviewQueue entries
  - requires_review edges
```

### GraphWriterCandidateAgent

```yaml
role: generate candidate node/edge YAML only after validation
outputs:
  - graph_write_candidate packets
forbidden:
  - direct canon graph mutation
  - authority promotion
  - deletion
  - overwriting prior lineage
```

### EvalRunnerAgent

```yaml
role: run extraction and overclaim evals
initial_eval_fixtures:
  - false_canon_from_summary_only
  - deployment_claim_from_open_pr
  - verified_claim_from_model_memory
  - missing_receipt_public_claim
  - raw_transcript_inferred_from_summary
  - graph_centrality_as_authority
outputs:
  - eval_result packets
  - regression flags
```

### CodexPatchAgent

```yaml
role: implement validators, schemas, tests, and local tooling through GitHub PRs
allowed:
  - draft PRs
  - tests
  - schemas
  - local-only tools
forbidden:
  - silent merges
  - production deployment
  - canon promotion
  - secrets or credential handling
```

## Minimal graph write candidate schema

```yaml
graph_write_candidate:
  candidate_id:
  generated_by_agent:
  generated_at:
  source_artifacts:
  proposed_nodes:
    - node_id:
      node_type:
      title:
      status:
      raw_export_status:
      canon_status: not_canon
      deployment_status: not_deployed
      authority_scope: none
      evidence_refs:
  proposed_edges:
    - edge_id:
      edge_type:
      from_node:
      to_node:
      evidence_ref:
      status: candidate
  contradictions_or_uncertainties:
  missing_receipts:
  review_required:
  strongest_safe_claim:
  forbidden_claims:
```

## First target query set

```text
1. What artifacts mention GangaSeek?
2. Which ORCS items are source-visible but not hashed?
3. Which Notion pages claim source-of-truth status?
4. Which Drive files are raw/semi-raw cargo but not mirrored to GitHub?
5. Which Claude artifacts need adversarial review?
6. Which GitHub PRs are open draft vs merged?
7. Which artifacts contain deployment/runtime language?
8. Which claims lack evidence anchors?
9. Which contradictions are unresolved?
10. Which next actions are safest and lowest-drift?
```

## OpenAI integration posture

```text
Use structured output for node/edge packets.
Use evals for extraction reliability.
Use guardrails for canon/deployment/legal/runtime language blockers.
Use Codex for schema/test/validator implementation.
Use file search/retrieval only as retrieval, not truth.
Use Agents SDK/tooling only after graph gates exist.
```

## Interop posture

```text
OpenAI-first does not mean OpenAI-only.
Google, Microsoft, and xAI remain interoperable lanes.
No vendor surface is root authority.
```

## Keeper

```text
Graph writes are candidates.
Review turns candidates into decisions.
Human-root decides what graduates.
```
