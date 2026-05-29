---
artifact_id: ARTIFACT-ARCHIVE-ARCHITECTURE-SHELDONBRAIN-MISSING-PARSER-MODULE-DISCOVERY-2026-05-08-MD-2026-05-29
title: Sheldonbrain Missing Parser Module Discovery
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# Sheldonbrain Missing Parser Module Discovery

**Date:** 2026-05-08  
**Status:** Public architecture / integration note  
**Related repo:** https://github.com/atlaslattice/sheldonbrain-rag-api  
**Key path:** `grokbrain_parser/GDRIVE_QUICKSTART.md`

## Discovery

The user identified a missing module called **Sheldonbrain**: a parsing tool intended to parse raw chat logs and categorize artifacts. The tool was not being used in the current public evidence archive workflow.

A GitHub search found a public repository:

`atlaslattice/sheldonbrain-rag-api`

This repo appears to contain the relevant infrastructure under `grokbrain_parser`.

## Confirmed Capabilities From Repository

The `grokbrain_parser/GDRIVE_QUICKSTART.md` file describes Grokbrain v4.0 support for automatic ingestion from Google Drive folders containing Grok chat exports.

Documented workflow:

```text
Google Drive Folder
  → download to ./exports/
  → parse Grok JSON
  → classify 144 Spheres
  → upload to xAI Collections
```

Supported formats include:

- Grok nested JSON exports
- simple chat JSON from OpenAI, Gemini, DeepSeek
- text transcripts using `Human:` / `Assistant:` patterns

The pipeline reportedly creates artifacts, categorizes items, detects projects, populates 144-sphere classifications, stores results in Qdrant, and supports xAI Collections upload.

## Why This Matters

The current manual archive workflow has been creating:

- raw-log pointers
- integrity hashes
- high-signal assessments
- benchmark hypotheses
- scorecards
- candidate-canon notes

Sheldonbrain/Grokbrain appears designed to automate a major part of that work:

- raw chat ingestion
- artifact extraction
- project detection
- ontology classification
- timeline generation
- retrieval database creation
- xAI/Grok knowledge-base upload

## Strategic Implication

The project already has a parser/classifier module that should be wired into the public GitHub evidence archive pipeline.

Instead of manually extracting every raw transcript, the next pipeline should be:

```text
raw chat export / pasted transcript
  → Sheldonbrain parser
  → artifact JSON / JSONL index
  → 144-sphere classification
  → project timeline
  → raw-log pointer + hash
  → GitHub archive commit
  → benchmark scorecard queue
  → candidate canon only after review
```

## Guardrails

- Sheldonbrain extraction output is not canon.
- Parser classifications may be wrong and require review.
- 144-sphere tags are retrieval aids until validated.
- Sensitive/private content must be redacted or separated before public GitHub commit.
- OAuth credentials and tokens must never be committed.

## Immediate Integration Target

Create a `sheldonbrain-import` workflow for the `manus-artifacts` repo that accepts:

1. raw `.txt` transcript
2. exported `.json` chat log
3. source model label
4. date
5. privacy/public flag
6. benchmark family
7. optional sphere tags

Outputs:

1. raw-log pointer with SHA-256
2. extracted artifact index JSONL
3. event timeline JSONL
4. candidate benchmark cases
5. candidate invariant/meta-invariant entries
6. public assessment draft

## Recommended Next Step

Inspect the full `sheldonbrain-rag-api` repo, then either:

1. import the parser into `manus-artifacts/tools/sheldonbrain-import/`, or
2. link the two repos and use `sheldonbrain-rag-api` as the parser backend.

## Core Principle

> The manual archive process proved the method. Sheldonbrain should now industrialize it.

## Status

Public integration note only. Not canon unless routed through Council workflow.
