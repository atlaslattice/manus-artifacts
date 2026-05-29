# Receipt Requirements — Aetherforge GPTDream++ (2026-05-27)

```text
STATUS: CANDIDATE — NOT CANON
AUTHORITY: none
DEPLOYMENT: not deployable
```

---

## Principle

```text
Directory or it didn't happen.
Schema or it will drift.
Receipt or it isn't evidence.
```

---

## Minimum viable receipt (MVR)

Every artifact entering the graph must carry a receipt YAML block at the bottom.

```yaml
artifact_receipt:
  artifact_id: <unique-slug>            # required
  artifact_type: <type>                 # task_board | dream_log | work_log | schema | ...
  source: <source>                      # drive | notion | github | manual
  source_date: YYYY-MM-DD              # required
  created_by: <agent or human>          # required
  canon_status: candidate               # required; never self-promote
  work_phase: YES | NO                  # 8/8/8 tag
  play_phase: YES | NO                  # 8/8/8 tag
  rem_phase: YES | NO                   # 8/8/8 tag
  claude_contamination: clean | review_required | flagged
  atlas_orcs_audit_state: AUDIT_REQUIRED | AUDIT_PASSED | AUDIT_FAILED
  human_root_review_required: true | false
```

---

## Extended receipt (for high-value artifacts)

```yaml
extended_receipt:
  artifact_id: <unique-slug>
  parent_sources:
    - source_id: <id>
      source_type: <type>
      hash: <sha256 if available>
  delta_extraction_ids: []              # list of extracted delta IDs if applicable
  adversarial_review_status: pending | passed | flagged
  promotion_gate_cleared: false         # true only after atlas_orcs_audit_state = AUDIT_PASSED
  ratification_event_id: null           # filled on full council ratification only
  notes: ""
```

---

## Receipt format rules

1. Receipt block must appear at the **bottom** of the artifact.
2. `canon_status` must be `candidate` unless a `ratification_event_id` is present.
3. `work_phase`, `play_phase`, and `rem_phase` must all be declared — this feeds the
   8/8/8 cadence tracker.
4. `claude_contamination` must be `clean` or explicitly reviewed before `atlas_orcs_audit_state`
   can be set to `AUDIT_PASSED`.
5. No receipt = artifact is ineligible for KG node promotion.

---

## Receipt non-escalation rule

```text
A receipt is evidence of provenance.
A receipt is not a canon declaration.
A receipt is not a deployment authorization.
Filling in a receipt does not grant authority to the artifact.
Authority comes only from:
  - full council ratification
  - adjudication by @atlaslattice
```

---

## Sample receipt (work log)

```yaml
artifact_receipt:
  artifact_id: TIDELOCKBRAIN-WORKLOG-2026-05-27-G
  artifact_type: work_log
  source: github
  source_date: 2026-05-27
  created_by: TIDELOCKBrain / S7
  canon_status: candidate
  work_phase: YES
  play_phase: NO
  rem_phase: NO
  claude_contamination: clean
  atlas_orcs_audit_state: AUDIT_REQUIRED
  human_root_review_required: true
```
