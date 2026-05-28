---
artifact_id: DOC-REDACTION-PROTOCOL-SAFE-PUBLICATION-EXCEPTIONS-2026-05-28
title: Redaction Protocol and Safe-Publication Exceptions
status: CANDIDATE
owner: atlaslattice
created: 2026-05-28
last_updated: 2026-05-28
source_of_truth: GitHub
---
# Redaction Protocol and Safe-Publication Exceptions

## Redaction protocol

1. Identify sensitive segment and classify via triage matrix.
2. Preserve an internal provenance pointer to original source context.
3. Replace sensitive text with a minimal redaction marker (`[REDACTED: reason]`).
4. Record decision rationale, owner, and date in the associated receipt.
5. Re-run metadata/link/quality checks after redaction edits.

## Safe-publication exception path

Use this path only when publication value is high but full publication is unsafe.

1. Publish a sanitized derivative artifact.
2. Add scope exception entry to blocker/readiness artifacts.
3. Link to adjudication evidence and owner ratification status.
4. Revisit exception at each readiness checkpoint until closed.
