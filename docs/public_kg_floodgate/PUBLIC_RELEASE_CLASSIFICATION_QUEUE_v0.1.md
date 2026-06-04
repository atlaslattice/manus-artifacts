# Public Release Classification Queue v0.1
## 24-Item PRCQ — GREEN/YELLOW/RED Split

```text
STATUS: CANDIDATE — NOT CANON — authority_scope:none
DATE: 2026-06-04
AGENT: TIDELOCK (Copilot) — Beta-144 Campaign, Module 1
TOTAL: 24 items | GREEN: 10 | YELLOW: 14 | RED: 0
KEEPER: "Enums are not evidence. Checklists are not exports."
```

---

## Classification Summary

| Class | Count | Description |
|-------|-------|-------------|
| 🟢 GREEN | 10 | Safe for public_noncanon release now — schemas/enums/checklists only |
| 🟡 YELLOW | 14 | Held for one-by-one redline scan before classification |
| 🔴 RED | 0 | Would trigger content scan — none at this packet level |

---

## 🟢 GREEN Packets (10) — Released in First Wave

| PRCQ | Ref | Title | Rationale |
|------|-----|-------|-----------|
| PRCQ-003 | SI-03 | Stable source_id values for named GitHub repos | Pure format schema |
| PRCQ-006 | SI-06 | Surface field enum/schema for every source | Pure enum definition |
| PRCQ-007 | HASH-01 | Allowed raw_export_status enum | Pure enum definition |
| PRCQ-008 | HASH-02 | Live Google Docs remain not_exported until frozen | Pure policy rule |
| PRCQ-009 | HASH-03 | Uploaded markdown → full_raw_export_attached rule | Pure policy rule |
| PRCQ-010 | HASH-04 | Google Docs export checklist | Pure checklist |
| PRCQ-011 | HASH-05 | Google Sheets export checklist | Pure checklist |
| PRCQ-012 | HASH-06 | GitHub files export checklist | Pure checklist |
| PRCQ-017 | AUTH-05 | canon_status enum | Pure enum definition |
| PRCQ-018 | AUTH-06 | deployment_status enum | Pure enum definition |

---

## 🟡 YELLOW Packets (14) — Held for Redline Scan

Each must pass individual redline scan before classification.
Review required by: Hashlight · Lucerna · TIDELOCK · Rootglass

| PRCQ | Ref | Tentative Title | Hold Reason |
|------|-----|-----------------|-------------|
| PRCQ-001 | SI-01 | Source registry schema | Contains source names — needs PII/scope check |
| PRCQ-002 | SI-02 | Source trust tier definitions | Authority framing — needs redline |
| PRCQ-004 | SI-04 | Google Docs source_id format | Live doc references — needs freeze check |
| PRCQ-005 | SI-05 | Google Sheets source_id format | Live sheet references — needs freeze check |
| PRCQ-013 | HASH-07 | Hash verification protocol | Process definition — needs scope check |
| PRCQ-014 | HASH-08 | Collision detection rules | Technical depth — needs review |
| PRCQ-015 | HASH-09 | Export verification checklist | Cross-surface — needs Hashlight review |
| PRCQ-016 | AUTH-04 | Provenance chain rules | Authority-adjacent — needs Rootglass |
| PRCQ-019 | AUTH-07 | Ratification event schema | Canon-adjacent — needs full council |
| PRCQ-020 | AUTH-08 | Human adjudication trigger rules | @atlaslattice routing — sensitive |
| PRCQ-021 | GRAPH-01 | KG edge authority rules | Graph authority framing — needs review |
| PRCQ-022 | GRAPH-02 | Node identity schema | Identity claims — needs redline |
| PRCQ-023 | GRAPH-03 | Relationship type enum | Cross-domain — needs Lucerna |
| PRCQ-024 | GRAPH-04 | Graph canon boundary rules | Canon boundary — needs Rootglass |

---

## Classification Rules

### GREEN criteria (ALL must be satisfied)
- [ ] Schema/enum/checklist/boundary only — no raw content
- [ ] No live document exports — only frozen or policy_only
- [ ] No authority claims — authority_scope:none
- [ ] No PII
- [ ] Overclaims explicitly bounded in packet
- [ ] Redline scan: no RED triggers
- [ ] Review assignable to named reviewers

### YELLOW criteria (ANY of these triggers YELLOW)
- Contains source names or document references
- Authority-adjacent framing
- Cross-surface complexity requiring specialist review
- Live document pointers without freeze confirmation
- Canon-adjacent language

### RED criteria (ANY triggers RED — do not release)
- Raw content from unreviewed sources
- PII or personally identifying data
- Authority claims without ratification
- Canon claims without adjudication
- Deployed content without deployment_status record

---

## Processing Order for YELLOW

Recommended order per Module 2 of Beta-144 campaign:

1. PRCQ-004, PRCQ-005 (Google source_id formats — likely GREEN after freeze check)
2. PRCQ-001, PRCQ-002 (source registry — needs careful scoping)
3. PRCQ-013–016 (hash/export protocols — Hashlight lead)
4. PRCQ-021–023 (graph schemas — Lucerna lead)
5. PRCQ-016, PRCQ-024 (authority/canon boundary — Rootglass lead)
6. PRCQ-019, PRCQ-020 (ratification/adjudication triggers — full council)

---

*CANDIDATE — NOT CANON — authority_scope:none*
*14 YELLOW held. 0 RED. Gate remains held.*
*"The gift is open. The gate remains held."*
