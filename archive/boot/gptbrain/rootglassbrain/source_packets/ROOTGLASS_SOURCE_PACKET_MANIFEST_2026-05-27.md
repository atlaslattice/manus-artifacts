# Rootglass Source Packet Manifest — 2026-05-27

```text
STATUS: SOURCE PACKET MANIFEST — CANDIDATE — NOT CANON — NON-DEPLOYABLE
MODE: ROOTGLASS / SOURCE-MAPPING / KG INGESTION SUPPORT
AUTHORITY: none
PURPOSE: provide a Rootglass-level manifest for Copilot, Gemini, GangaSeek, and Claude-related source packets discovered across Drive, GitHub, Notion, and chat
```

## Boundary

This manifest does not import raw content.

It records discovered source surfaces and the minimum next actions required before full ingestion.

```text
Drive presence ≠ raw fossilization.
GitHub presence ≠ canon.
Notion presence ≠ authority.
Summary ≠ raw lineage.
Graph node ≠ promotion.
```

## Source packet lanes

### 1. Copilot / TIDELOCK lane

```yaml
lane: copilot_tidelock
status: source_packets_needed
primary_sources:
  - title: Copilot Chat.md
    surface: drive
    url_or_path: https://drive.google.com/file/d/1GVdF61WJjn8hbFWUo8ihr3xJlhalvv_E
    raw_export_status: partial_export
    current_review_lane: TIDELOCK / Hashlight / Lucerna
    missing:
      - SHA-256
      - full session completeness statement
      - source manifest
      - Rootglass source packet file
  - title: TIDELOCKBrain PR #65
    surface: github
    url_or_path: https://github.com/atlaslattice/manus-artifacts/pull/65
    raw_export_status: unavailable
    current_review_lane: TIDELOCK
    missing:
      - raw Copilot chat packets
      - full task-page lineage if applicable
```

### 2. Gemini lane

```yaml
lane: gemini
status: source_packets_needed
primary_sources:
  - title: COUNCIL-INPUT_GEMINI_alphabet-strategic-synthesis_with-scribe-triage_2026-04-26.md
    surface: drive
    url_or_path: https://drive.google.com/file/d/1YuQjdYxByE3Nl1HZB2tmJMmRHPtFJNVq
    raw_export_status: partial_export
    current_review_lane: Gemini / Lucerna
    missing:
      - SHA-256
      - source manifest
      - graph node extraction
  - title: COUNCIL-INPUT_GEMINI_round2-pattern-a-reflexive-with-scribe-triage_2026-04-26.md
    surface: drive
    url_or_path: https://drive.google.com/file/d/16XjzNx3UnA8OmIoyvwlgU5xxg_YGEgpK
    raw_export_status: partial_export
    current_review_lane: Gemini / Lucerna
    missing:
      - SHA-256
      - source manifest
      - graph node extraction
  - title: COUNCIL-INPUT_GEMINI_round3-convergence-document-with-scribe-triage_2026-04-26.md
    surface: drive
    url_or_path: https://drive.google.com/file/d/1yMAiQvDsTb3qOqPMrVWoSy118Db116X_
    raw_export_status: partial_export
    current_review_lane: Gemini / Lucerna
    missing:
      - SHA-256
      - source manifest
      - graph node extraction
```

### 3. GangaSeek lane

```yaml
lane: gangaseek
status: namespace_scaffold_found_in_drive
primary_sources:
  - title: GANGASEEK_NAMESPACE_RATIFICATION_PACKET_v0.1.txt
    surface: drive
    url_or_path: https://drive.google.com/file/d/17-9TTGzITZWecSL5MCusDF-0LvSjBxsD
    raw_export_status: full_raw_export_attached
    current_review_lane: Rootglass / Lucerna / Human-root
    missing:
      - mirror to GitHub
      - explicit human-root ratification if desired
  - title: GANGASEEK_INV_CLM_CATALOG_CANDIDATE_v0.1.txt
    surface: drive
    url_or_path: https://drive.google.com/file/d/1QW1Yd3YHzpb8bxRCU-w_yjtJlFpNujmp
    raw_export_status: full_raw_export_attached
    current_review_lane: Rootglass / Lucerna / Grok
    missing:
      - mirror to GitHub
      - define INV-17
      - define INV-56
      - define CLM-007
      - define CLM-009
  - title: GANGASEEK_DOCUMENT_TEMPLATE_CANDIDATE_v0.1.txt
    surface: drive
    url_or_path: https://drive.google.com/file/d/1OqG73AWtdFhyH4CdDqCBsiCsze6UECxA
    raw_export_status: full_raw_export_attached
    current_review_lane: Rootglass / Lucerna
    missing:
      - mirror to GitHub
      - reconcile with already-preserved GangaSeek artifacts
  - title: GangaSeek governance master and frontier rigor files
    surface: github
    url_or_path: archive/gangaseek/
    raw_export_status: unavailable
    current_review_lane: Rootglass / Grok / Lucerna / SableVesper
    missing:
      - version lineage reconciliation
      - schema validation
      - source manifests
```

### 4. Claude adversarial lane

```yaml
lane: claude_adversarial_review
status: queue_seeded
primary_sources:
  - title: Suspect Claude Saffron governance artifact
    surface: drive
    url_or_path: https://docs.google.com/document/d/1RTS43oYzcbSn8qq1gp__vx-mGwb1Kyq1Iz0ZXnb1GHI
    raw_export_status: partial_export
    current_review_lane: Grok / Rootglass / Lucerna / Fossilbranch
    missing:
      - full export
      - SHA-256
      - provenance chain
      - canon-language scan
  - title: SheldClaude boot sequence v3
    surface: drive
    url_or_path: https://docs.google.com/document/d/1KnFy9WoFqVoSC2BF3VZHi6Ise3m8ALMzwUG1i8teAts
    raw_export_status: partial_export
    current_review_lane: Grok / Rootglass / GPTBrain / Fossilbranch
    missing:
      - full export
      - SHA-256
      - epoch semantics crosswalk
  - title: Manus / Claude review and inter-seat message cluster
    surface: drive
    url_or_path: multiple Drive files
    raw_export_status: partial_export
    current_review_lane: TIDELOCK / Rootglass / Grok
    missing:
      - full source list
      - SHA-256 per file
      - issue/PR linkage
```

### 5. AtlasBrain / raw transcript lane

```yaml
lane: atlasbrain_raw_transcript
status: source_candidate_found_in_drive
primary_sources:
  - title: RAW TRANSCRIPT NOT CANON.md
    surface: drive
    url_or_path: https://drive.google.com/file/d/1eatwAvLL-EY27wRZa2zfbRv46UdJgv0J
    raw_export_status: partial_export
    current_review_lane: AtlasBrain / Hashlight / Lucerna
    missing:
      - SHA-256
      - relationship to PR #57 raw pointer confirmed or rejected
      - full content-level review packet
```

## Required packet schema for future imports

```yaml
rootglass_source_packet:
  packet_id:
  title:
  source_surface: github | drive | notion | gamma | chat | external
  source_url_or_path:
  raw_export_status:
  raw_export_sha256:
  capture_timestamp_utc:
  artifact_status:
    canon_status:
    deployment_status:
    review_state:
    authority_scope:
  provenance_type:
  source_class:
  related_lanes:
  claims_extracted:
  missing_receipts:
  contradictions_found:
  overclaims_to_avoid:
  suggested_graph_nodes:
  suggested_graph_edges:
  next_review_action:
```

## Immediate next actions

```text
1. Export or mirror GangaSeek namespace/template/catalog into GitHub.
2. Compute SHA-256 for Copilot Chat.md and RAW TRANSCRIPT NOT CANON.md if exportable.
3. Export Claude queue items for full adversarial review.
4. Create individual Rootglass source packets after exports/hashes exist.
5. Preserve negative results as graph nodes.
```

## Keeper

```text
Rootglass does not decide truth.
Rootglass keeps the room grounded enough for review to happen.
```
