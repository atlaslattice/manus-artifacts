# Public KG Floodgate — README

```text
STATUS: CANDIDATE — NOT CANON — authority_scope:none
DATE: 2026-06-04
AGENT: TIDELOCK (Copilot) — Beta-144 Campaign, Module 1
KEEPER: "Publish the metal detector before opening the vault."
STRATEGY: boring on purpose = safe = repeatable = world-class
```

> **All artifacts in this directory are CANDIDATE, NOT CANON, authority_scope:none.**
> No claim here constitutes evidence. No enum constitutes an export.
> Receipts before promotion. Human adjudication before canonization.

---

## What is the Public KG Floodgate?

The **Public KG Floodgate** is a controlled release scaffold for the Atlas Lattice
knowledge graph. It defines the criteria, classification queue, and release packets
that determine what is safe to share publicly — and in what form — before the full
knowledge graph is opened.

The core keeper:

> *"Publish the metal detector before opening the vault."*

We publish the **detection machinery** (enums, schemas, checklists, boundary rules)
first. This creates a receipts-before-claims foundation that makes the eventual
vault opening safe, auditable, and world-class.

---

## GREEN First Wave — 10 Safe Packets

The GREEN First Wave contains 10 packets classified as **public_noncanon** —
the safest possible release class. These are enums, schemas, checklists, and
boundary rules only. No raw content. No live documents. No authority claims.

| # | Packet ID | Title | Surface | Release Class |
|---|-----------|-------|---------|---------------|
| 1 | PRCQ-003 | Stable source_id values for named GitHub repos | GitHub | public_noncanon |
| 2 | PRCQ-006 | Surface field enum/schema for every source | All | public_noncanon |
| 3 | PRCQ-007 | Allowed raw_export_status enum | All | public_noncanon |
| 4 | PRCQ-008 | Live Google Docs remain not_exported until frozen | Google Docs | public_noncanon |
| 5 | PRCQ-009 | Uploaded markdown → full_raw_export_attached rule | GitHub | public_noncanon |
| 6 | PRCQ-010 | Google Docs export checklist | Google Docs | public_noncanon |
| 7 | PRCQ-011 | Google Sheets export checklist | Google Sheets | public_noncanon |
| 8 | PRCQ-012 | GitHub files export checklist | GitHub | public_noncanon |
| 9 | PRCQ-017 | canon_status enum | All | public_noncanon |
| 10 | PRCQ-018 | deployment_status enum | All | public_noncanon |

Individual packet files: [`green_first_wave_packets/`](./green_first_wave_packets/)

---

## YELLOW Wave — 14 Held Packets

14 packets are held for one-by-one redline scan before classification.
They will not be released until each passes individual review by:
**Hashlight · Lucerna · TIDELOCK · Rootglass**

See: [`PUBLIC_RELEASE_CLASSIFICATION_QUEUE_v0.1.md`](./PUBLIC_RELEASE_CLASSIFICATION_QUEUE_v0.1.md)

---

## Key Documents in This Directory

| File | Purpose |
|------|---------|
| `README.md` (this file) | Public orientation |
| `GREEN_FIRST_WAVE_RELEASE_MANIFEST_v0.1.md` | Full manifest + strategy + 10 GREEN selections |
| `PUBLIC_RELEASE_CLASSIFICATION_QUEUE_v0.1.md` | 24-item PRCQ queue with GREEN/YELLOW split |
| `PUBLIC_RELEASE_PACKET_TEMPLATE_v0.1.md` | Canonical template skeleton for all release packets |
| `ENUMERATION_REGISTRY.md` | All 6 enum families in one machine-readable table |
| `green_first_wave_packets/` | 10 individual release packet YAML files |

---

## Invariants

- Every artifact here is `canon_status: not_canon`
- Every artifact here is `deployment_status: not_deployed`
- Every artifact here is `authority_scope: none`
- Every artifact here is `public_release_class: public_noncanon`
- No claim without a receipt
- Enums are not evidence
- Checklists are not exports
- Human ratification required before any promotion

---

## Review Required By

All GREEN packets require sign-off from:
- **Hashlight** — raw/hash gap review
- **Lucerna** — canon drift check
- **TIDELOCK** — path strategy alignment
- **Rootglass** — canon boundary enforcement

No packet may be promoted without full council review and @atlaslattice adjudication.

---

*CANDIDATE — NOT CANON — authority_scope:none*
*"Publish the metal detector before opening the vault."*
*Grok Leads. Lattice Routes. KRAKOA PLAYS FOOTBALL. HUZZAH!*
