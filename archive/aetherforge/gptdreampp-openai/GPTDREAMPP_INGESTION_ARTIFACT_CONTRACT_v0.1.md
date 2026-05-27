# GPTDream++ Ingestion Artifact Contract v0.1

```text
STATUS: CONTRACT — CANDIDATE — NOT CANON
DEPLOYMENT: NONE
AUTHORITY: NONE
```

## Required fields

- `artifact_id`
- `artifact_path`
- `source_pointer`
- `source_system` (`github` | `drive` | `notion` | `other`)
- `lineage_parent_ids`
- `provenance_receipt_path`
- `content_hash_sha256`
- `hash_status` (`present` | `missing` | `mismatch`)
- `claim_class` (`raw` | `parsed` | `claim` | `review` | `decision` | `action`)
- `review_state` (`unreviewed` | `in_review` | `challenged` | `adjudicated`)
- `promotion_eligibility` (`blocked` | `candidate` | `ratified`)
- `contamination_flags` (array; include `claude_touched` when applicable)
- `contradiction_links` (array of artifact IDs)
- `tests_required`
- `tests_run`
- `blockers`
- `next_safest_action`

## Admission rules

1. Missing `source_pointer` or `content_hash_sha256` blocks admission.
2. `claim` artifacts cannot move to `candidate` without linked `review` artifact.
3. `promotion_eligibility=ratified` is invalid without explicit ratification/adjudication receipt.
4. Claude-touched governance artifacts must carry contamination flag and adversarial review before promotion.

## Review lanes

- OpenAI execution lane: extraction/orchestration support only.
- Bullshit Olympics lane: overclaim, false-authority, and canon-drift challenge pass.
- Human governance lane: final adjudication for any promotion.
