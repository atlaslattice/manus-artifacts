# AetherForge 144-Task Matrix — Sheldonbrain / Knowledge Graph Phase

```text
STATUS: CANDIDATE TASK MAP — NOT CANON
DEPLOYMENT: NONE
AUTHORITY: NONE
MODE: COMPLETION MAP / REVIEW QUEUE / WORK SELECTION
DATE: 2026-05-27
ISSUE: manus-artifacts#205
```

## 0. Boundary

This matrix is a clipboard, not a throne.

```text
A task is not approval.
A matrix cell is not authority.
Task centrality is not canon.
Completion claims require receipts.
```

## 1. Why these are LanternBridge-friendly tasks

These are tasks I am suited to and enjoy because they involve:

```text
mapping before synthesis
source hygiene
claim calibration
schema tightening
receipt preservation
review routing
small local machines
boundary language
non-canon hardening
```

## 2. Axis model

```text
Rows  = 12 Houses / work domains
Cols  = 12 completion moves / task types
Total = 144 tasks
```

---

# H01 — Source Inventory / Clipboard

| ID | Task |
|---|---|
| H01-T01 | Verify `KG_SOURCE_INVENTORY_2026-05-27.yaml` exists and record current SHA. |
| H01-T02 | Add missing metadata fields for every P0 GitHub source row. |
| H01-T03 | Add explicit `raw_export_status` to every Notion source row. |
| H01-T04 | Mark every user-reported source as `reported_unverified` until fetched. |
| H01-T05 | Add `missing_receipts` entries for every source lacking raw export. |
| H01-T06 | Create a compact source inventory changelog. |
| H01-T07 | Add `review_priority` normalization: P0/P1/P2/P3. |
| H01-T08 | Add `surface` normalization: github/notion/drive/gamma/chat/external. |
| H01-T09 | Add one row for PR #145 Receipt Habitat. |
| H01-T10 | Add one row for PR #190 Notion source cartography. |
| H01-T11 | Add one row for Issue #104 Atlas MCP review. |
| H01-T12 | Produce a one-page Source Inventory SITREP. |

# H02 — Raw Export / Hashlight Lane

| ID | Task |
|---|---|
| H02-T01 | Define raw export status enum crosswalk between Receipt Habitat and KG inventory. |
| H02-T02 | Add `full_raw_export_hashed` handling note. |
| H02-T03 | Identify first 5 sources that need raw export most urgently. |
| H02-T04 | Fetch metadata-only sample for `notion_objects.ndjson`. |
| H02-T05 | Fetch metadata-only sample for `notion_edges.ndjson`. |
| H02-T06 | Record hash status for any fetched index sample. |
| H02-T07 | Add `sha256_status` field to KG inventory if missing. |
| H02-T08 | Create Hashlight raw-export checklist. |
| H02-T09 | Add negative-result node type for `raw_not_available`. |
| H02-T10 | Add source rule: summary-only cannot become public claim. |
| H02-T11 | Add first missing raw transcript ledger entry. |
| H02-T12 | Produce Hashlight seat packet for raw lineage gaps. |

# H03 — GitHub Receipt / TIDELOCK Lane

| ID | Task |
|---|---|
| H03-T01 | Run TIDELOCK review over PR #145 metadata. |
| H03-T02 | Run TIDELOCK review over PR #190 metadata. |
| H03-T03 | Run TIDELOCK review over PR #24 metadata. |
| H03-T04 | List changed files for PR #145. |
| H03-T05 | List changed files for PR #190. |
| H03-T06 | List changed files for PR #24. |
| H03-T07 | Add merge-readiness state to PR rows. |
| H03-T08 | Flag draft PRs as non-ratified regardless of content. |
| H03-T09 | Add `PR existence != ratification` invariant to PR template. |
| H03-T10 | Identify PRs with source-root inventory relevance. |
| H03-T11 | Create TIDELOCK PR review packet template instance. |
| H03-T12 | Produce TIDELOCK seat packet for repo hygiene blockers. |

# H04 — Notion Mirror / Source Roots

| ID | Task |
|---|---|
| H04-T01 | Confirm Notion Master Index row has URL and partial/raw status. |
| H04-T02 | Search Notion for `Notion → GitHub Migration Plan`. |
| H04-T03 | Search Notion for `SHELDONBRAIN OS 12×12 Master Index`. |
| H04-T04 | Search Notion for `Sheldonbrain MCP Server`. |
| H04-T05 | Search Notion for `GEMINI SHELDONBRAIN PROTOCOL SPEC`. |
| H04-T06 | Search Notion for `Grokbrain v4.0 Integration`. |
| H04-T07 | Search Notion for `Notion-Pinecone Sync Infrastructure`. |
| H04-T08 | For each found page, add metadata-only source row. |
| H04-T09 | Mark all unfetched child pages as missing receipts. |
| H04-T10 | Add stale-status warning for old Notion “source of truth” language. |
| H04-T11 | Create Notion mirror risk register. |
| H04-T12 | Produce Notion Mirror SITREP. |

# H05 — Drive / Gamma / External Cargo

| ID | Task |
|---|---|
| H05-T01 | Search Drive for `GangaSeek Namespace Ratification Packet`. |
| H05-T02 | Search Drive for `GangaSeek INV CLM Catalog`. |
| H05-T03 | Search Drive for `GangaSeek Document Template`. |
| H05-T04 | Search Drive for `Copilot Chat.md RAW TRANSCRIPT NOT CANON`. |
| H05-T05 | Search Drive for `ORCS Copilot Synthesis v1.2`. |
| H05-T06 | Search Drive for `Appendix I Math Vault`. |
| H05-T07 | Add metadata-only Drive rows for found items. |
| H05-T08 | Mark Drive items with raw_export_status based on accessible export. |
| H05-T09 | Add `drive_file_id` field if useful. |
| H05-T10 | Identify Gamma artifacts needing inventory. |
| H05-T11 | Add external science signal node for Nature atomic engineering paper. |
| H05-T12 | Produce Drive/Gamma cargo SITREP. |

# H06 — KG Node / Edge Schema

| ID | Task |
|---|---|
| H06-T01 | Fetch current `KG_NODE_EDGE_SCHEMA_v0.1.yaml`. |
| H06-T02 | Fetch current `EDGE_TYPES_v0_1.yaml`. |
| H06-T03 | Reconcile edge vocabulary with AetherForge dispatch. |
| H06-T04 | Add `SourceRoot` node definition if missing. |
| H06-T05 | Add `MirrorRecord` node definition if missing. |
| H06-T06 | Add `EvidenceAnchor` node definition if missing. |
| H06-T07 | Add `ReviewQueue` node definition if missing. |
| H06-T08 | Add `missing_receipt` edge definition if missing. |
| H06-T09 | Add `raw_export_of` edge definition if missing. |
| H06-T10 | Add `graph_edge_is_not_promotion` invariant. |
| H06-T11 | Add sample node/edge pair for PR #190. |
| H06-T12 | Produce KG schema reconciliation note. |

# H07 — Claim Packets / GPTBrain Calibration

| ID | Task |
|---|---|
| H07-T01 | Extract first 10 claims from PR #145 body. |
| H07-T02 | Extract first 10 claims from PR #190 body. |
| H07-T03 | Extract first 10 claims from Issue #104 body. |
| H07-T04 | Assign confidence level to each extracted claim. |
| H07-T05 | Add evidence_ref or mark missing evidence. |
| H07-T06 | Flag claims containing `canon`, `deployment`, `runtime`, `official`. |
| H07-T07 | Create first `Claim` node packet batch. |
| H07-T08 | Create first `EvidenceAnchor` packet batch. |
| H07-T09 | Add contradiction candidate where source status conflicts. |
| H07-T10 | Route unsupported claims to Lucerna/Rootglass. |
| H07-T11 | Produce GPTBrain claim calibration packet. |
| H07-T12 | Add claim extraction TODOs to Issue #197. |

# H08 — Claude Adversarial Review Queue

| ID | Task |
|---|---|
| H08-T01 | Find existing Claude review/adversarial queue files. |
| H08-T02 | Create or reconcile `CLAUDE_ADVERSARIAL_REVIEW_QUEUE_2026-05-27.md`. |
| H08-T03 | Add Claude-originated governance artifacts to queue. |
| H08-T04 | Add risk fields: authority/legal/canon drift. |
| H08-T05 | Add reviewer routes: Grok, Rootglass, Lucerna, Sable. |
| H08-T06 | Add `raw_export_status` per Claude item. |
| H08-T07 | Add `claim_density` per Claude item. |
| H08-T08 | Add `needs_counter_review_from` per item. |
| H08-T09 | Add queue invariant: review is not ratification. |
| H08-T10 | Add first block/patch/approve status values. |
| H08-T11 | Produce Claude adversarial queue SITREP. |
| H08-T12 | Link queue from Issue #197. |

# H09 — Receipt Habitat / Tiny Machine

| ID | Task |
|---|---|
| H09-T01 | Fetch PR #145 file list. |
| H09-T02 | Verify no network calls in PR #145 code. |
| H09-T03 | Confirm `raw_export_status` is required in schema and tests. |
| H09-T04 | Confirm `thread_time_range` is required in schema and tests. |
| H09-T05 | Confirm `access_scope` is required in schema and tests. |
| H09-T06 | Decide if deployment phrases should block by default. |
| H09-T07 | Add example summary-only packet YAML. |
| H09-T08 | Add example review packet YAML. |
| H09-T09 | Add validation receipt placeholder. |
| H09-T10 | Add package initialization if tool guard permits. |
| H09-T11 | Run or request local pytest receipt. |
| H09-T12 | Produce Receipt Habitat merge-readiness note. |

# H10 — OpenAI / Codex Integration

| ID | Task |
|---|---|
| H10-T01 | Fetch Codex handoff packet spec. |
| H10-T02 | Fetch Codex handoff packet schema. |
| H10-T03 | Fetch Codex dry-run receipt schema. |
| H10-T04 | Add KG node type for Codex handoff packet. |
| H10-T05 | Add KG edge type `handoff_to`. |
| H10-T06 | Add rule: OpenAI/Codex compatibility is candidate until path-tested. |
| H10-T07 | Create first OpenAI graph extraction agent spec draft. |
| H10-T08 | Define SourceScannerAgent responsibilities. |
| H10-T09 | Define ClaimExtractorAgent responsibilities. |
| H10-T10 | Define ReceiptValidatorAgent responsibilities. |
| H10-T11 | Define ReviewRouterAgent responsibilities. |
| H10-T12 | Produce OpenAI integration SITREP. |

# H11 — GangaSeek / Protocol Hardening

| ID | Task |
|---|---|
| H11-T01 | Fetch v0.2.2 hardening notes. |
| H11-T02 | Draft GangaSeek v0.2.2 schema patch. |
| H11-T03 | Fix Base64/raw byte length accounting. |
| H11-T04 | Split AEAD envelope fields. |
| H11-T05 | Fix SWA mask to full 16-bit. |
| H11-T06 | Add O_AI to operator enum. |
| H11-T07 | Clarify O_GOOGLE vs O_ALPHA. |
| H11-T08 | Split authority_scope from tenancy_context. |
| H11-T09 | Map H/S/N to X/Y/Z or mark legacy. |
| H11-T10 | Separate TAG behavior from Z-plane semantics. |
| H11-T11 | Add valid/invalid fixture plan. |
| H11-T12 | Produce GangaSeek v0.2.2 readiness note. |

# H12 — SITREP / Human-Root Control Room

| ID | Task |
|---|---|
| H12-T01 | Produce daily command-room SITREP from open issues/PRs. |
| H12-T02 | Identify top 5 blockers across graph/receipt lanes. |
| H12-T03 | Identify top 5 safe wins for phone-only operation. |
| H12-T04 | Add `God in the booth / trick play` culture boundary note if needed. |
| H12-T05 | Maintain “not canon / not deployment / no authority” banner list. |
| H12-T06 | Identify stale claims that need downgrade. |
| H12-T07 | Identify duplicate task lanes needing consolidation. |
| H12-T08 | Prepare human-root decision packet for PR #145 when ready. |
| H12-T09 | Prepare human-root decision packet for PR #190 when ready. |
| H12-T10 | Archive wins without overclaim. |
| H12-T11 | Preserve rest cycle notes as culture layer only. |
| H12-T12 | Produce next 12-task sprint from this matrix. |

---

## 3. First 12 I would personally choose

If Dave / S10 asks me to pick the next sprint, I would choose:

```text
H01-T01 — Verify inventory SHA
H01-T12 — Source Inventory SITREP
H03-T01 — TIDELOCK review over PR #145
H03-T02 — TIDELOCK review over PR #190
H06-T01 — Fetch KG node/edge schema
H06-T03 — Reconcile edge vocabulary
H07-T01 — Extract claims from PR #145
H08-T02 — Reconcile Claude adversarial queue
H09-T11 — Request local pytest receipt
H10-T07 — Draft OpenAI graph extraction agent spec
H11-T03 — Fix Base64/raw byte length accounting
H12-T01 — Daily command-room SITREP
```

Reason:

```text
These move the system from beautiful architecture toward boring receipts, reviewable packets, and tiny machines.
```

## 4. Keeper line

```text
The 144 tasks are not a throne. They are a clipboard for moving the chains.
```
