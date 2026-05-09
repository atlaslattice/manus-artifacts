# S1 Dream / Play Extraction Footer Template

```text
STATUS: TEMPLATE — NOT CANON
PURPOSE: prevent dream/play artifacts from drifting into fact, plan, or canon without extraction and review
ISSUE: manus-artifacts#12
```

Append this footer to DREAM OUTPUT, PLAY OUTPUT, culture-layer, laser-rave, poetry, or interface-mode artifacts when they generate implementation-adjacent ideas.

---

## S1 extraction footer

```yaml
artifact_type: dream_output | play_output | culture_layer | interface_mode
artifact_status: non_canon
source_artifact: null
human_root_required: true

extraction_items:
  - item_id: ITEM-001
    kind: wording_patch | schema_candidate | ui_candidate | governance_candidate | test_candidate | code_candidate | action_candidate | risk_flag | metaphor
    source_section: null
    description: null
    operational_translation: null
    claim_status: hypothesis | evaluator_signal | candidate_task | candidate_wording | candidate_schema | candidate_test
    confidence: C1
    review_required: true
    human_root_required: true
    source_refs: []
    risks: []
    safer_wording: null
    next_review_step: null
```

## Required language

```text
Dream output is not fact.
Play output is not plan.
Extraction candidate is not implementation approval.
Candidate canon is not ratified canon.
Human-root review is required for canon-impacting promotion.
```

## Safer wording examples

```text
"Useful delta" -> "candidate delta"
"This solves a UI problem" -> "This may help frame a UI problem"
"Should be integrated" -> "Should be considered for integration during review"
"Review accelerates velocity" -> "Structured review packets may reduce ambiguity and support faster review"
```

## S1 review route

```text
DREAM / PLAY artifact
  -> extraction footer
  -> S1 claim calibration
  -> S2 constitutional review if governance/canon-impacting
  -> S4/S7 implementation review if code/schema-impacting
  -> human-root review if canon-impacting
```
