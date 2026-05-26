# OpenAI Knowledge Graph Integration Architecture

```text
STATUS: ARCHITECTURE CANDIDATE — NOT CANON
DEPLOYMENT STATUS: NOT DEPLOYABLE
DATE: 2026-05-24
SOURCE: user-provided maximum OpenAI integration as knowledge graph proposal + Lumen preservation pass
AUTHORITY: none
CANON STATUS: not ratified
PURPOSE: define OpenAI as the graph-building, extraction, evaluation, and review orchestration layer rather than the sole memory store or canon authority.
```

## Core Doctrine

```text
Do not start with more agents.
Start with a graph substrate that separates:
raw source → parsed facts → claims → evidence → review → action.
```

## System Roles

```text
GitHub = durable artifact / receipt substrate
Drive = raw and semi-raw document archive
Notion = legacy knowledge / structured workspace archive
OpenAI = extraction, graph-building, review, evals, and agentic workflow layer
Human-root = authority gate
```

## Key Boundary

```text
The graph is not memory.
The graph is not canon.
The graph is not authority.
The graph is a receipt-indexed map of what exists, what it claims, what supports it, what contradicts it, and what still needs review.
```

## OpenAI Integration Role

Use OpenAI as:

```text
reasoning layer
extraction layer
evaluation layer
review packet generator
agent orchestration layer
structured-output producer
workflow assistant
```

Do not use OpenAI as:

```text
sole memory store
canon source
silent graph writer
lineage eraser
authority gate
replacement for raw sources
```

## Source-Grounded Knowledge Graph

The target is a source-grounded knowledge graph, not a model-memory graph.

Required separation:

```text
raw source artifacts stay raw
parsed packets cite raw sources
claims cite parsed packets and source anchors
evidence anchors remain explicit
review findings remain advisory until ratified
actions require human-root / approved workflow gates
```

## Node Types

```text
SourceArtifact
RawExport
ParsedPacket
Claim
EvidenceAnchor
ReviewFinding
Decision
Action
CanonCandidate
```

## Edge Types

```text
derived_from
cites
contradicts
supersedes
patches
requires_review
missing_receipt
raw_export_of
parsed_from
promoted_to
blocked_by
belongs_to_lane
source_mirrored_to
```

## Immediate Build Order

```text
1. KG_SOURCE_INVENTORY_2026-05-24.yaml
2. KG_NODE_EDGE_SCHEMA_v0.1.yaml
3. ROOTGLASS_SOURCE_PACKET_MANIFESTS
4. CLAUDE_ADVERSARIAL_REVIEW_QUEUE_2026-05-24.md
5. OPENAI_GRAPH_EXTRACTION_AGENT_SPEC_v0.1.md
```

## OpenAI Product Surface Mapping

```text
ChatGPT Projects / workspace GPTs:
  human cockpit for querying, summarizing, comparing, and producing SITREPs

OpenAI API / Agents SDK:
  extraction and workflow orchestration

MCP / connectors:
  source access and integration surfaces

File search / retrieval:
  document-grounded retrieval, not truth by itself

Structured output:
  graph node/edge packet generation

Evals:
  reliability tests for extractors and reviewers

Guardrails:
  canon / deployment / legal / runtime language blockers

Codex / coding agent:
  schema, validators, tests, and graph repo implementation candidates

Human-root:
  final promotion and authority gate
```

## Retrieval Boundary

```text
retrieved chunk ≠ fact
fact citation ≠ ratification
source presence ≠ canon
```

## Agent Boundary

```text
OpenAI agents may propose graph writes.
They may not silently ratify graph writes.
They may not promote canon.
They may not erase lineage.
```

## First 10 Queries

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

## Madden Board

```text
BOOM. Don’t send eleven agents into three warehouses with no clipboard.
First build the clipboard.
Then label the boxes.
Then scan the receipts.
Then let the agents argue about what the boxes mean.
```

## Strongest Safe Claim

> OpenAI should not be the memory or canon authority. OpenAI should be the graph-building engine: extract, classify, cite, test, route, and review. GitHub holds receipts, Drive holds raw cargo, Notion holds legacy structure, and human-root decides what graduates.
