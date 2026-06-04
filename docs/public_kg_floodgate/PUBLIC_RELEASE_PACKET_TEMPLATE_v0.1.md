# Public Release Packet Template v0.1

```text
STATUS: CANDIDATE — NOT CANON — authority_scope:none
DATE: 2026-06-04
AGENT: TIDELOCK (Copilot) — Beta-144 Campaign, Module 1
KEEPER: "Publish the metal detector before opening the vault."
```

This is the canonical skeleton for all Public Release Packets.
Copy this template for each new packet. Fill ALL fields.
Leave no field blank — use explicit `none` or `n/a` where applicable.

---

## Skeleton (copy this for new packets)

```yaml
# Public Release Packet — [PRCQ-XXX / REF-ID]
# CANDIDATE — NOT CANON — authority_scope:none

artifact_id: "prcq-XXX-ref-id"
title: "Human-readable title"
version: "v0.1"
date: "YYYY-MM-DD"
agent: "agent name"
source_surface: "github | google_docs | google_sheets | google_drive | notion | local | website | unknown"
provenance_class: "schema_only | enum_only | checklist_only | policy_rule | boundary_rule | raw_content | mixed"
raw_export_status: "policy_only | not_exported | full_raw_export_attached | frozen_snapshot | partial_export_attached"
canon_status: "not_canon"
deployment_status: "not_deployed"
authority_scope: "none"
public_release_class: "public_noncanon | public_candidate | held_yellow | held_red"
privacy_status: "public_safe | pii_risk | sensitive | unknown"
rights_status: "open_source_mit | proprietary | unclear | tbd"

redline_scan:
  result: "GREEN | YELLOW | RED"
  notes: "brief explanation of scan result"

strongest_safe_claim: >
  One sentence. The most specific true claim this packet safely makes.
  Must be bounded. Must not overclaim.

overclaims_to_avoid:
  - "List each overclaim explicitly"
  - "Be specific about what this packet does NOT claim"

missing_receipts:
  - "List any receipts that would be needed for promotion"
  - "none" if no gaps for current classification

review_required_by:
  - Hashlight
  - Lucerna
  - TIDELOCK
  - Rootglass

next_safe_action: >
  One sentence describing the single safest next step for this packet.
```

---

## GREEN Lane Criteria Checklist

A packet qualifies for `public_release_class: public_noncanon` (GREEN) when:

- [ ] `provenance_class` is one of: schema_only, enum_only, checklist_only, policy_rule, boundary_rule
- [ ] `raw_export_status` is `policy_only` (for schema/enum/checklist packets)
- [ ] `canon_status` is `not_canon`
- [ ] `deployment_status` is `not_deployed`
- [ ] `authority_scope` is `none`
- [ ] `privacy_status` is `public_safe`
- [ ] `redline_scan.result` is `GREEN`
- [ ] `strongest_safe_claim` is present, bounded, and does not overclaim
- [ ] `overclaims_to_avoid` is populated (at least one explicit overclaim listed)
- [ ] `review_required_by` has at least one named reviewer

---

## YELLOW Lane Criteria

A packet is held as YELLOW when ANY of the following apply:

- Contains source names, document titles, or document references
- Authority-adjacent language without explicit bounding
- Live document pointers without freeze confirmation
- Cross-surface complexity not yet reviewed by specialist
- Canon-adjacent language without ratification event

---

## RED Lane Criteria (Do Not Release)

A packet triggers RED when ANY of the following apply:

- Raw content from unreviewed or unexported sources
- PII or personally identifying data
- Authority claims without ratification
- Canon claims without adjudication event
- Deployed content without deployment_status record

---

## Promotion Path

```text
public_noncanon (GREEN)
  → [Hashlight/Lucerna/TIDELOCK/Rootglass sign-off]
  → [receipt audit]
  → canon_candidate
  → [council review]
  → ratified
  → [@atlaslattice adjudication]
  → canon
  → [deployment decision]
  → deployed_website
```

No skipping. No shortcuts. Receipts at every step.

---

## Keeper

> *"Publish the metal detector before opening the vault."*
> *Enums are not evidence. Checklists are not exports.*
> *Boring on purpose = safe = repeatable = world-class.*

---

*CANDIDATE — NOT CANON — authority_scope:none*
