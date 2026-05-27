# OpenAI Graph Extraction Agent Spec v0.1

```text
STATUS: AGENT SPEC CANDIDATE — NOT CANON
DEPLOYMENT STATUS: NOT DEPLOYABLE
DATE: 2026-05-24
PURPOSE: define candidate OpenAI-powered graph extraction/review agents for a source-grounded knowledge graph.
```

## Core Boundary

```text
OpenAI should not be the memory.
OpenAI should be the graph-building engine.
```

OpenAI agents may:

```text
extract
classify
cite
score
route
review
propose graph writes
```

OpenAI agents may not:

```text
silently ratify graph writes
promote canon
erase lineage
replace raw sources
claim authority
```

## Agent Roles

### SourceScannerAgent

```yaml
role: scan source inventory and identify candidate artifacts
inputs:
  - KG_SOURCE_INVENTORY
  - source manifests
outputs:
  - source_artifact_candidates
  - missing_receipts
  - review_priority_updates
```

### ClaimExtractorAgent

```yaml
role: extract atomic claims from raw exports and parsed packets
inputs:
  - RawExport
  - SourceArtifact
  - ParsedPacket
outputs:
  - Claim nodes
  - source_refs
  - confidence labels
```

### ReceiptValidatorAgent

```yaml
role: verify whether claims have evidence anchors
inputs:
  - Claim nodes
  - EvidenceAnchor candidates
outputs:
  - verified_receipts
  - missing_receipt edges
  - quarantine recommendations
```

### ContradictionScannerAgent

```yaml
role: detect contradictions, supersession, and drift
inputs:
  - Claim nodes
  - ReviewFinding nodes
outputs:
  - contradicts edges
  - supersedes candidates
  - drift notes
```

### ReviewRouterAgent

```yaml
role: route claims and artifacts to the correct review lane
inputs:
  - Claim nodes
  - ParsedPacket nodes
  - risk labels
outputs:
  - requires_review edges
  - review queue entries
```

### GraphWriterCandidateAgent

```yaml
role: produce candidate graph write packets
inputs:
  - proposed nodes
  - proposed edges
  - validation results
outputs:
  - graph_write_candidate
  - diff summary
  - human_review_required: true
```

## Required Output Envelope

```yaml
graph_agent_output:
  agent_name:
  task_id:
  authority_scope: advisory
  source_refs: []
  proposed_nodes: []
  proposed_edges: []
  missing_receipts: []
  contradictions: []
  review_routes: []
  confidence:
  caveats: []
  human_review_required: true
  canon_status: not_canon
  deployment_status: not_deployable
```

## Required Evals

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

## Guardrails

```text
retrieval is not truth
source presence is not canon
graph write candidate is not graph truth
review is not ratification
human-root decides promotion
```

## First Pilot

```text
Use KG_SOURCE_INVENTORY_2026-05-24.yaml and KG_NODE_EDGE_SCHEMA_v0.1.yaml to generate candidate nodes/edges for the first 10 source artifacts only.
```

## Strongest Safe Claim

> OpenAI graph extraction agents can help scan, extract, validate, route, and propose graph writes for a source-grounded knowledge graph, but all outputs remain advisory candidates until reviewed and approved through human-root/governance gates.
