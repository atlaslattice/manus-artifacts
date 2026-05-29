# Multi-Report Convergence Packet — Notion-First Indexing

**Date recorded:** 2026-05-25  
**Status:** CONVERGENCE / CONTROL NOTE — NOT CANON  
**Scope:** Notion, Drive, GitHub, Gamma, website canon, Atlas / Sheldonbrain / ORCS / GPTDream++ indexing and reconciliation  
**Recorder:** Aster / S1  
**Source:** user-supplied swarm convergence summary in current thread  
**Canon status:** not canon  
**Deployment status:** not deployable  
**Authority effect:** none

## Evidence Boundary

```text
This artifact records multi-report convergence and current operating posture.
It is not canon.
It is not a ratification ledger.
It does not claim corpus completeness.
It does not treat Notion, Drive, GitHub, Gamma, or website material as automatic authority.
It corrects stale connector-state claims and establishes the next indexing lane.
```

## Core Consensus

```text
Index first.
Export/hash second.
Crosswalk third.
Synthesize later.
Canon last.
```

The reports converge that the project should not summarize or merge the Notion corpus before indexing it.

Correct order:

```text
1. Identify source surfaces.
2. Export raw objects where possible.
3. Preserve hashes and raw/export status.
4. Classify authority/canon/deployment status.
5. Crosswalk Notion, Drive, GitHub, Gamma, and website canon.
6. Only then synthesize.
```

## Corrected Connector / Source State

Some research runs reported that live Notion access was unavailable. That was true for those runs, but it is now stale.

Current corrected state:

```text
NOTION: confirmed direct access
DRIVE: confirmed access
GITHUB: confirmed access
GAMMA: lower-priority adapter / mostly proxy or adjunct context for now
```

## Source Role Model

```text
Notion = mutable source / operator layer / historical Sheldonbrain OS corpus
Drive = proxy / export / research artifact / staging layer
GitHub = receipt / mirror / implementation / review layer
Website = intended canon publication surface
Council / Human-root = ratification layer
```

Keeper compression:

```text
Notion holds the living corpus.
GitHub holds receipts.
Drive holds proxies.
The website must expose canon.
Human-root decides what stands.
```

## Why Notion Is Priority

The Sheldonbrain OS Notion database is confirmed as the historical corpus surface. It exposes structured operating fields including:

```text
Sphere
Category
Source
Parse Complete
Council Needed
Execution Approved
Reviewed By Human
Council Output fields
Council Synthesis
Debate Status
Final Verdict
Confidence scores
Ingest Run ID
Original Filename
```

This means the index layer already exists in Notion. The next move is to extend, normalize, and crosswalk it instead of reinventing it.

## Website Canon Recoverability Gap

The reports agree on a canon-publication issue:

```text
The Atlas website is intended as canon,
but the canon surface is not yet robustly recoverable/fetchable enough for outside agents.
```

Needed canon recovery package:

```text
canon.md
canon.json
invariants.yaml
doctrines.yaml
artifacts.yaml
routes.yaml
SOURCE_OF_TRUTH.md
llms.txt
sitemap.xml
hash_manifest.sha256
```

Boundary:

```text
Website canon intent is not the same as portable canon receipts.
```

## GitHub Role

GitHub should act as:

```text
receipt surface
mirror surface
implementation surface
review surface
schema/manifest surface
issue/PR state surface
```

GitHub should not be treated as:

```text
automatic canon
authority source by storage alone
private raw vault if repository is public
```

## Drive Role

Drive should be treated as:

```text
staging layer
export layer
council-report repository
proxy artifact surface
large packet handoff surface
```

Known risk:

```text
Drive reports and exports can be high-value but are not substitutes for first-order Notion/API/GitHub receipts.
```

## Gamma Role

Gamma is useful but lower priority than Notion.

Current role:

```text
adjunct adapter / presentation / transformation surface
not primary corpus
not authority
not canon
```

## Phase Plan

### Phase 1 — Notion Corpus Source Registry

```text
P0 — Fetch Sheldonbrain OS data source schema and rows.
P0 — Build NOTION_WHITEPAPER_INDEX_v0.1 from page/database IDs.
P0 — Mark every artifact candidate_by_default.
P0 — Capture source_surface, raw_export_status, access_scope, canon_status, authority_scope, deployment_status.
P0 — Crosswalk to Drive exports and GitHub mirrors where available.
P0 — Create canon-gap list for website export needs.
```

### Phase 2 — Atlas Canon Recovery Package

```text
canon.md
canon.json
invariants.yaml
doctrines.yaml
artifacts.yaml
routes.yaml
SOURCE_OF_TRUTH.md
llms.txt
sitemap.xml
hash_manifest.sha256
```

### Phase 3 — Synthesis / Disposition

```text
preserve-as-is
revise/improve
synthesize/merge
archive/deprecate
escalate for human-root ratification
```

## Immediate Lane

```text
1. Query Sheldonbrain OS rows.
2. Export first 50–100 records into a candidate registry.
3. Identify white-paper clusters.
4. Crosswalk to Drive/GitHub.
5. Produce actionable NOTION_WHITEPAPER_INDEX_v0.1.
```

## Required Registry Fields

```yaml
artifact_id: null
title: null
source_surface: notion | drive | github | gamma | website | chat | upload
source_url_or_id: null
source_connector_status: direct | proxy | referenced_only | unavailable | unknown
raw_export_status: absent | pointer_only | partial | complete | unknown
raw_export_method: api_json | markdown | html | pdf | drive_file | github_file | none | unknown
content_hash: null
access_scope: private | shared | public | unknown
epistemic_label: raw | parsed | inferred | summarized | candidate | verified | disputed | mixed | unknown
canon_status: not_canon | candidate | ratified_unverified | ratified_verified | current_website_canon | unknown
authority_scope: none | advisory | review_only | implementation_candidate | human_ratified
deployment_status: not_deployed | implementation_candidate | deployed | unknown
review_lane: atlas | lucerna | hashlight | tidelock | rootglass | research_watchlist | council | unknown
related_notion_pages: []
related_drive_files: []
related_github_paths: []
related_github_issues_prs: []
related_gamma_objects: []
missing_receipts: []
next_action: index | export | hash | compare | ingest | review | quarantine | synthesize | ratification_candidate
```

## Guardrails

```text
Notion search is not exhaustive enumeration.
Notion page ≠ canon.
Drive export ≠ canon.
GitHub storage ≠ canon.
Website canon intent ≠ portable canon receipt.
Council review ≠ final canon.
Human-root ratification is the promotion gate.
Index shelves before synthesizing the library.
```

## Strongest Safe Claim

> The swarm reports converge that the current project should run a Notion-first, source-controlled indexing and reconciliation program. Notion is the priority historical corpus; Drive is the proxy/export layer; GitHub is the receipt/review/implementation layer; Gamma is adjunct; the website is the intended canon display but needs portable canon exports and hash manifests. The next correct move is to build `NOTION_WHITEPAPER_INDEX_v0.1` and a cross-source registry before synthesis or canon promotion.

## Status

Convergence/control note. Not canon.
