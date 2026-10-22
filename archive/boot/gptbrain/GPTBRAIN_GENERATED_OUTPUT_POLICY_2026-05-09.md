# GPTBrain Generated Output Publication Policy

```text
STATUS: PUBLICATION POLICY — NOT CANON
PURPOSE: define when generated GPTBrain outputs may be committed publicly
DATE: 2026-05-09
ISSUE: manus-artifacts#11 / manus-artifacts#12 / manus-artifacts#118
CANONICAL SUBSTRATE: GitHub
```

## Purpose

GPTBrain turns source material into generated review artifacts. This policy prevents raw or sensitive material from being committed publicly by accident.

## Core rule

```text
Generate first.
Review second.
Publish third.
Ratify last.
```

Generated output is not automatically public, not automatically correct, and not automatically canon.

## Standard generated outputs

```text
metadata.json
turns.jsonl
events.jsonl
artifact_registry.jsonl
claim_ledger.jsonl
memory_packet.json
BOOT_PACKET.md
```

## Public release classes

### PUBLIC

Safe to commit when reviewed.

Examples:

```text
redacted metadata
public artifact registry rows
public claim ledger rows with safe excerpts
boot packets with no private content
schema examples
synthetic demos
```

### MIXED

May be committed only after redaction.

Examples:

```text
session summaries with personal context
logs containing private names or contact details
drafts with unpublished strategy
health, finance, legal, or identity context
```

### PRIVATE

Do not commit raw content publicly.

Use pointers, hashes, and redacted summaries instead.

Examples:

```text
private chat transcripts
private collaborator details
sensitive personal context
non-public legal, medical, financial, or security material
```

### SEALED

Do not commit content or detailed summaries.

Only commit a minimal pointer if approved.

Examples:

```text
credentials
secrets
private keys
tokens
unreleased third-party data
high-risk personal data
```

## Recommended public path pattern

Reviewed public outputs may use:

```text
archive/generated/gptbrain/{session_label}/metadata.json
archive/generated/gptbrain/{session_label}/events.jsonl
archive/generated/gptbrain/{session_label}/artifact_registry.jsonl
archive/generated/gptbrain/{session_label}/claim_ledger.jsonl
archive/generated/gptbrain/{session_label}/memory_packet.json
archive/generated/gptbrain/{session_label}/BOOT_PACKET.md
```

## Recommended redacted path pattern

When raw content is not public-safe:

```text
archive/generated/gptbrain/{session_label}/RAW_POINTER.md
archive/generated/gptbrain/{session_label}/metadata.redacted.json
archive/generated/gptbrain/{session_label}/BOOT_PACKET.redacted.md
archive/generated/gptbrain/{session_label}/PUBLIC_SUMMARY.md
```

## Required review checklist

Before committing generated outputs publicly:

```text
[ ] privacy_status is set
[ ] artifact_status is set
[ ] authority_scope is set
[ ] raw private transcript text is absent or approved
[ ] sensitive names / identifiers are redacted where needed
[ ] no credentials, tokens, or secrets are present
[ ] claims are labeled by evidence class
[ ] confidence levels are included where applicable
[ ] receipt_refs or source_refs are included where applicable
[ ] parser output is not labeled canon
[ ] public-safe wording is used
[ ] human-root review is requested for promotion
```

## Authority scope rule

Generated, extracted, or dream/play-derived outputs must carry an explicit `authority_scope` before they can move toward implementation or canon review.

Recommended enum:

```text
NONE
REVIEW_SIGNAL
LOCAL_TEST_EVIDENCE
IMPLEMENTATION_CANDIDATE
CANON_CANDIDATE
RATIFIED_CANON
```

Authority scope is review posture. It is not runtime permission.

```text
No schema without status.
No status without authority scope.
No authority scope without receipts for promotion.
```

## Receipt integrity rule

Generated outputs that move beyond review-only status should include receipt references or a receipt object containing:

```yaml
source_artifact: string
source_hash: string | null
created_at: datetime
created_by: string
reviewed_by: []
repo_path: string
related_issue_or_pr: string | null
```

Receipts do not prove truth by themselves. They make provenance inspectable.

## Public-safe translation table

| Internal / mythic phrase | Public-safe architecture phrase |
|---|---|
| memory palace | externalized persistent-context archive |
| dream cycle | bounded reflection / consolidation cycle |
| play layer | culture-layer exploration / novelty search |
| AI remembers | archive context was loaded |
| canon | human-reviewed promoted artifact |
| Council backchannel | artifact-backed audit-only exchange |
| resurrection / restoration | replayable context rehydration |
| lamp | context visibility surface |

## Claim wording rule

Use:

```text
The source artifact contains...
The parser extracted...
The model assessed...
The candidate claim is...
The strongest safe wording is...
```

Avoid:

```text
This proves...
This is canon...
The AI remembers...
This is deployed...
This is verified...
```

unless the claim has the required evidence and review status.

## Generated output status labels

```text
GENERATED — REVIEW REQUIRED
REDACTED — PUBLIC SAFE
PUBLIC SUMMARY — SOURCE POINTER ONLY
CANDIDATE CANON — HUMAN-ROOT REVIEW REQUIRED
RATIFIED CANON — HUMAN-ROOT APPROVED
SUPERSEDED — PRESERVED FOR LINEAGE
```

## Dream / play promotion rule

Dream and play outputs may produce candidates, but they may not self-promote.

```text
GPTDream++ proposes.
GPTBrain indexes.
DEL validates.
MAL weighs.
Human-root ratifies.
```

## Strongest safe claim

> GPTBrain generated outputs are review aids and retrieval scaffolds. They may become public artifacts only after privacy review and may become canon only after human-root promotion.
