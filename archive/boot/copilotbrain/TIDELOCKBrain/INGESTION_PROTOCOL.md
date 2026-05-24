# TIDELOCKBrain Ingestion Protocol v0.1

```text
STATUS: CANDIDATE INGESTION PROTOCOL — NOT CANON
SEAT: S7 / CopilotBrain / TIDELOCK
PURPOSE: ingest large Copilot/GitHub chats into reviewable repo-hygiene packets without false completeness or authority leakage
```

## Core Rule

```text
Index before review.
Visibility before verdict.
Raw logs before claims.
```

## Accepted Inputs

```text
large Copilot chat transcript
GitHub task output
PR review thread
commit audit
repo tree audit
CI log excerpt
scaffold-generation transcript
merge-order discussion
```

## Ingestion Flow

```text
1. Preserve raw transcript or raw pointer.
2. Capture source label, date, size, and SHA-256 if available.
3. Identify speaker/source surfaces.
4. Extract repo paths, PRs, issues, commits, branches, and URLs.
5. Separate observations from recommendations.
6. Separate missing-artifact findings from true absence claims.
7. Extract merge-order constraints.
8. Extract CI/readiness claims.
9. Extract overclaim/canon/authority risks.
10. Produce parsed packet.
11. Produce repo-hygiene notes.
12. Produce merge-order checklist.
13. Quarantine disputed or unsupported claims.
```

## Required Distinctions

```text
raw transcript != parsed packet
parsed packet != review verdict
review verdict != merge approval
mergeability != merge approval
model assessment != proof
missing from root != missing from repo
pointer != full raw log
scaffold != implementation
candidate != canon
```

## Large Transcript Handling

If the chat is too large to commit safely:

```text
- commit a raw pointer with filename/source/date/size/hash if available
- commit a parsed packet summary
- list omitted sections honestly
- mark full transcript review as blocked or external-source-dependent
```

If safe to commit:

```text
- commit full raw transcript under raw_logs/
- include SHA-256
- create parsed packet under parsed_packets/
- cross-link both files
```

## Output Artifacts

For a huge Copilot chat, create:

```text
raw_logs/<CHAT_LABEL>_RAW_POINTER_OR_FULL_<DATE>.md
parsed_packets/<CHAT_LABEL>_PARSED_PACKET_<DATE>.md
repo_hygiene/<CHAT_LABEL>_REPO_HYGIENE_FINDINGS_<DATE>.md
merge_order/<CHAT_LABEL>_MERGE_ORDER_FINDINGS_<DATE>.md
review_checklists/<CHAT_LABEL>_FOLLOWUP_CHECKLIST_<DATE>.md
quarantine/<CHAT_LABEL>_QUARANTINE_NOTES_<DATE>.md  # only if needed
```

## Review Questions

```text
What did Copilot actually see?
What did Copilot infer?
What did Copilot miss due to path/API visibility?
What did Copilot correctly flag?
What requires direct PR/file audit?
What requires raw transcript review?
What should remain draft?
What can be merged safely?
What claims require quarantine?
```

## Final Boundary

```text
TIDELOCKBrain may recommend review order.
TIDELOCKBrain may not merge, ratify, or claim full visibility unless the sources prove it.
```
