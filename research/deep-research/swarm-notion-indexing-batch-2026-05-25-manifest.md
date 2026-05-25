# Swarm Deep Research Batch — Notion / GitHub Indexing Manifest

```text
ARTIFACT ID: SWARM-DEEP-RESEARCH-NOTION-GITHUB-INDEXING-BATCH-2026-05-25
STATUS: INTAKE MANIFEST — NOT CANON — NOT DEPLOYED
DATE: 2026-05-25
SOURCE: user-uploaded deep research markdown reports
PURPOSE: Preserve and triage simultaneous swarm deep-research outputs for Notion indexing, GitHub receipting, canon/candidate reconciliation, and brain-lane migration.
CANON: NO
AUTHORITY: NONE
DEPLOYMENT: NO
PUBLIC CLAIM STATUS: PRIVATE_REVIEW / SOURCE_RECONCILIATION_REQUIRED
```

---

## 1. Batch Receipt

```yaml
batch_receipt:
  uploaded_reports: 9
  unique_reports_by_hash: 8
  duplicate_detected: true
  duplicate_pair:
    - deep-research-report (22)(3).md
    - deep-research-report (21)(3).md
  duplicate_sha256: 398a49b738973e2911df536a7cbc3daec88bb601ff054cb3c6144ab33c09eb72
  status: intake_manifest_created
  next_action: synthesize_cross-report_delta_register_and_create_indexing_backlog
```

---

## 2. Uploaded Report Inventory

| File | SHA256 | Size bytes | Primary heading | Intake classification |
|---|---|---:|---|---|
| `deep-research-report (28).md` | `9a731ce478371516971eecb4c9875eba33ace629dbf1e968d6e301799d2be915` | 34084 | Canon and Candidate Audit Across Atlas Lattice Surfaces | canon/candidate surface audit |
| `deep-research-report (27).md` | `a797956ab082f9993ea88f8dec3d19d68f3b8c20a18bbbca2af316ab0a682e58` | 40890 | Krakoan Notion Archive and Indexing Protocols for AtlasBrain and GPTDream | AtlasBrain/GPTDream indexing protocol |
| `deep-research-report (26)(1).md` | `7bc815dfd14e47bbafc4b44b68c220a04a9b1f53499406419664ffbae783f8d4` | 51615 | Candidate Specification for Indexing Notion into a GitHub-Centric Swarm Memory Architecture | platform/spec architecture |
| `deep-research-report (25).md` | `ddeeab82d2c327b74c8337b38a40822a3c97ebf44017f554b87d0740b90bbd53` | 32354 | Atlas Lattice Notion Workspace Archival and Dream Memory Palace Readiness Audit | workspace archive / palace readiness |
| `deep-research-report (24)(1).md` | `d1df27254291cd6ccabed7ed57c446ae23ad504d7e1bf2366875cf79eacdf33d` | 37452 | Notion Archive Indexing Review for Krakoa and AtlasBrain | Krakoa / AtlasBrain index review |
| `deep-research-report (23)(2).md` | `84754b0b2db7cbdacf5fa3b9bfc33d488f7ca01c5abd88abf28eb98758f6db5f` | 33128 | Notion-First Cross-Source Index and Extraction for Regenerative Reversible Computing and ORCS | ORCS / reversible computing deltas |
| `deep-research-report (22)(3).md` | `398a49b738973e2911df536a7cbc3daec88bb601ff054cb3c6144ab33c09eb72` | 30849 | Atlas Lattice Notion Corpus Indexing and Reconciliation Report | corpus reconciliation report |
| `deep-research-report (21)(3).md` | `398a49b738973e2911df536a7cbc3daec88bb601ff054cb3c6144ab33c09eb72` | 30849 | Atlas Lattice Notion Corpus Indexing and Reconciliation Report | duplicate of report 22 |
| `deep-research-report (20)(4).md` | `c9bc6c7ad22cf373c5ba448119e6596dc745a0b6b00a25bb39a02a0536547671` | 39211 | Canonical Notion Indexing and Ingestion for KairoBrain | KairoBrain Notion ingestion schema |

---

## 3. Cross-Report Consensus

The reports converge on the same operating doctrine:

```text
1. Index before synthesis.
2. Preserve raw exports before normalization.
3. Notion is a mutable source/operator workspace.
4. GitHub is the more reliable receipt/control surface.
5. Website canon must remain the authority surface only when recoverable and ratified.
6. Search-only Notion enumeration is insufficient.
7. A root registry / shared-root crawl is required.
8. Candidate swarm outputs must not self-promote to canon.
9. Every artifact needs source_surface, raw_export_status, authority_scope, canon_status, deployment_status, review lane, and hash receipts.
```

---

## 4. Major Findings by Theme

### 4.1 Canon / Candidate Surface Control

The canon/candidate audit argues that the website is intended as canon, while Notion, Gamma, GitHub, GPT swarm outputs, and Manus artifacts should remain candidate/staging/review/mirror surfaces unless explicitly promoted.

Risk identified:

```text
authority without recoverability
```

Meaning:

```text
If /canon is asserted as authority but not independently exportable or recoverable, canon cannot be audited.
```

### 4.2 Notion Ingestion Architecture

The GitHub-centric swarm memory specification recommends a hybrid ingestion pipeline:

```text
Notion export for cold-start snapshots
Notion API for structured extraction
Notion webhooks for incremental deltas
Scheduled reconciliation over known roots and data sources
GitHub branches/issues/commits for receipts and review
```

Important Notion constraint:

```text
Search is discovery aid, not exhaustive enumerator.
```

### 4.3 Brain / Palace Migration

The AtlasBrain / GPTDream / Dream Memory Palace audits identify a strong palace-standardization lane, but with verification debt:

```text
- direct Notion exports still needed
- page timestamps and hashes missing
- prompt reconstruction and model/version receipts needed
- raw transcript preservation required before synthesis
```

### 4.4 KairoBrain Schema Direction

The KairoBrain report proposes a structured Notion graph with objects, edges, assets, receipts, and exports.

Useful registry components:

```text
notion_objects
notion_edges
notion_assets
notion_receipts
notion_exports
```

### 4.5 ORCS / Reversible Computing Delta Lane

The ORCS report flags regenerative reversible computing and the internal 47% boundary thesis as a high-value research delta, but not as external consensus or canon.

Status:

```text
high-value research delta
not canon
not established external consensus
needs source and review receipts
```

---

## 5. Highest-Priority Deltas to Extract

```yaml
priority_deltas:
  - id: DELTA-001
    name: Atlas Artifact Registry overlay
    description: Common schema for source surface, export status, authority, canon/deployment status, review lane, hashes, and receipts.
    source_reports:
      - deep-research-report (28).md
      - deep-research-report (26)(1).md
      - deep-research-report (20)(4).md

  - id: DELTA-002
    name: Notion root registry crawl
    description: Replace search-only enumeration with root/shared-page registry and recursive page/data-source crawl.
    source_reports:
      - deep-research-report (26)(1).md
      - deep-research-report (20)(4).md

  - id: DELTA-003
    name: Canon recoverability package
    description: Export canon.json, invariants.yaml, doctrines.yaml, llms.txt, and content hash manifest for website canon auditability.
    source_reports:
      - deep-research-report (28).md
      - deep-research-report (22)(3).md

  - id: DELTA-004
    name: Dream Memory Palace / Brain-lane standardization
    description: Standard seat bundle for AGENT_DNA, DREAM_MEMORY_PALACE, raw logs, parsed packets, receipts, and authority boundaries.
    source_reports:
      - deep-research-report (27).md
      - deep-research-report (25).md
      - deep-research-report (24)(1).md

  - id: DELTA-005
    name: ORCS / regenerative reversible computing review lane
    description: Extract 47% boundary thesis and reversible regenerative computing as research-delta candidate with external validation debt.
    source_reports:
      - deep-research-report (23)(2).md

  - id: DELTA-006
    name: KairoBrain Notion ingestion schema
    description: Adopt or adapt notion_objects, notion_edges, notion_assets, notion_receipts, notion_exports for GitHub-centric vault.
    source_reports:
      - deep-research-report (20)(4).md
```

---

## 6. Recommended Backlog

```text
1. Create `schemas/atlas-artifact-registry-overlay.schema.json`.
2. Create `manus-vault/notion/index/notion_objects.ndjson` scaffold.
3. Create `manus-vault/notion/index/notion_edges.ndjson` scaffold.
4. Create Notion shared-root registry artifact.
5. Create canon recoverability issue.
6. Create brain-lane palace standard package.
7. Deduplicate reports 21 and 22.
8. Extract ORCS / regenerative reversible computing delta packet.
9. Generate GitHub issue set from priority deltas.
```

---

## 7. Status Patch

These reports are research outputs, not ratification.

```text
Swarm deep research ≠ canon.
Deep research consensus ≠ implementation.
Indexing recommendation ≠ completed index.
GitHub receipt ≠ website canon.
Notion source ≠ public authority.
```

---

## 8. Keeper

```text
The swarm found the shape.
Now the registry must hold the edges.
Index first.
Synthesize later.
Canon only with receipts.
```