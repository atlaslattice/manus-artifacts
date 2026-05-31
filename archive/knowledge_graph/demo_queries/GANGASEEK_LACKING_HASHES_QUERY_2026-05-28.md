# Demo Query — GangaSeek artifacts lacking hashes — 2026-05-28

```text
STATUS: STAGING DEMO QUERY
CANON: NO
DEPLOYMENT: NO
AUTHORITY: NONE
PURPOSE: prove the first source-inventory query shape for the OpenAI-first knowledge graph habitat.
```

## Query

```text
Which artifacts mention GangaSeek and lack hashes?
```

## Current source basis

This query is based on the first staging inventory pass and visible Drive search results. It does not assert source completeness.

## Matching candidate artifacts

```yaml
matches:
  - source_id: drive_gangaseek_namespace_packet_001
    title: "GANGASEEK_NAMESPACE_RATIFICATION_PACKET_v0.1.txt"
    surface: drive
    url_or_path: "https://drive.google.com/file/d/17-9TTGzITZWecSL5MCusDF-0LvSjBxsD"
    raw_export_status: source_file_visible_not_hashed
    hash_status: missing
    canon_status: not_canon_until_reviewed
    deployment_status: not_deployed
    authority_scope: none
    missing_receipts:
      - sha256
      - claim_packet
      - GitHub mirror path
    next_review_action: "Hash file, extract claim packet, verify whether a GitHub mirror exists."

  - source_id: drive_gangaseek_inv_clm_catalog_001
    title: "GANGASEEK_INV_CLM_CATALOG_CANDIDATE_v0.1.txt"
    surface: drive
    url_or_path: "https://drive.google.com/file/d/1QW1Yd3YHzpb8bxRCU-w_yjtJlFpNujmp"
    raw_export_status: source_file_visible_not_hashed
    hash_status: missing
    canon_status: not_canon
    deployment_status: not_deployed
    authority_scope: none
    missing_receipts:
      - sha256
      - undefined ID review
      - GitHub mirror path
    next_review_action: "Hash file, extract INV/CLM IDs, route undefined IDs to schema review."

  - source_id: drive_gangaseek_template_001
    title: "GANGASEEK_DOCUMENT_TEMPLATE_CANDIDATE_v0.1.txt"
    surface: drive
    url_or_path: "https://drive.google.com/file/d/1OqG73AWtdFhyH4CdDqCBsiCsze6UECxA"
    raw_export_status: source_file_visible_not_hashed
    hash_status: missing
    canon_status: not_canon
    deployment_status: not_deployed
    authority_scope: none
    missing_receipts:
      - sha256
      - template review
      - GitHub mirror path
    next_review_action: "Hash file, compare against current template usage, route to Lucerna/GPTBrain."

  - source_id: drive_gangaseek_invariant_spec_pdf_001
    title: "GangaSeek Invariant Specification — MSFT vs India–Starlink–Google Orbital.pdf"
    surface: drive
    url_or_path: "https://drive.google.com/file/d/12WxTa1Ggoe-_A9yqL8WwMgO-nrpPlNJV"
    raw_export_status: source_file_visible_not_hashed
    hash_status: missing
    canon_status: not_canon
    deployment_status: not_deployed
    authority_scope: none
    missing_receipts:
      - sha256
      - PDF text extraction
      - claim packet
      - legal/compliance review
    next_review_action: "Hash file, extract text, route legal/data-sovereignty claims to review."

  - source_id: drive_gangaseek_invariant_spec_pdf_copy_001
    title: "GangaSeek Invariant Specification — MSFT vs India–Starlink–Google Orbital (1).pdf"
    surface: drive
    url_or_path: "https://drive.google.com/file/d/1hxALxM8Lur7m34RA0JX84wvGOeNJpM9f"
    raw_export_status: source_file_visible_not_hashed
    hash_status: missing
    canon_status: not_canon
    deployment_status: not_deployed
    authority_scope: none
    missing_receipts:
      - sha256
      - duplicate comparison against non-copy PDF
      - PDF text extraction
      - claim packet
    next_review_action: "Hash both PDF copies and determine whether they are duplicates or divergent versions."
```

## Non-matching / adjacent artifacts

```yaml
adjacent:
  - title: "DeepSeekBrain Research Report on the Uploaded DeepSeek Transcript.pdf"
    reason: "Returned in Drive search for GangaSeek but title does not directly identify GangaSeek packet; keep as adjacent until inspected."
  - title: "Aluminum_OS_v6-0-4_Council-Round-3-Integration-Patch_DeepSeek-Qwen-Sovereign_2026-04-29.md"
    reason: "DeepSeek / sovereignty adjacent; not a direct GangaSeek source without further claim extraction."
  - title: "Aluminum_OS_v6-0-6_DeepSeek-Rounds-4-5_VWB-Sovereignty_2026-04-29.md"
    reason: "DeepSeek / sovereignty adjacent; not a direct GangaSeek source without further claim extraction."
```

## Proposed graph nodes

```yaml
proposed_nodes:
  - node_type: SourceArtifact
    title: "GANGASEEK_NAMESPACE_RATIFICATION_PACKET_v0.1.txt"
  - node_type: SourceArtifact
    title: "GANGASEEK_INV_CLM_CATALOG_CANDIDATE_v0.1.txt"
  - node_type: SourceArtifact
    title: "GANGASEEK_DOCUMENT_TEMPLATE_CANDIDATE_v0.1.txt"
  - node_type: SourceArtifact
    title: "GangaSeek Invariant Specification PDF pair"
  - node_type: ReviewQueue
    title: "GangaSeek hash and claim extraction queue"
  - node_type: EvidenceAnchor
    title: "sha256 needed for GangaSeek Drive source files"
```

## Proposed graph edges

```yaml
proposed_edges:
  - edge_type: missing_receipt
    from: drive_gangaseek_namespace_packet_001
    to: sha256_needed
  - edge_type: missing_receipt
    from: drive_gangaseek_inv_clm_catalog_001
    to: sha256_needed
  - edge_type: missing_receipt
    from: drive_gangaseek_template_001
    to: sha256_needed
  - edge_type: requires_review
    from: drive_gangaseek_invariant_spec_pdf_001
    to: legal_compliance_review
  - edge_type: contradicts
    from: drive_gangaseek_invariant_spec_pdf_001
    to: drive_gangaseek_invariant_spec_pdf_copy_001
    status: candidate_until_hash_comparison
```

## Result

```text
The demo query returns at least five direct GangaSeek candidate artifacts with missing hashes.
```

## Next safest action

```text
Hash the three GangaSeek txt files first, then compare the two GangaSeek invariant PDFs for duplication/divergence.
```

## Boundary

```text
This query result is not canon.
This query result is not a source-complete inventory.
This query result does not prove claims inside the artifacts.
It only identifies visible source artifacts and missing hash receipts.
```
