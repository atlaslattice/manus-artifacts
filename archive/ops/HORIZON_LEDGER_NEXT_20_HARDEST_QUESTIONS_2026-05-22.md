---
artifact_id: HORIZON-LEDGER-NEXT-20-HARDEST-QUESTIONS-2026-05-22
title: "Next 20 Hardest Questions Facing the Project"
date: 2026-05-22
source_surface: Horizon Ledger / GPT
source_context: Follow-on strategic hard-question map after Atlas Prime response
raw_export_status: generated_summary
canon_status: not_canon
deployment_status: not_deployable
authority_status: none
artifact_type: candidate_strategy_map
role: identify_next_hard_questions_after_receipt_product_spine_alignment
receipt_status: initialized_2026-05-22
mutation_rule: >
  No claim mutation without new receipts. No canon promotion without human-root ratification.
  This is a planning artifact, not doctrine.
---

# Next 20 Hardest Questions Facing the Project

```text
STATUS: CANDIDATE STRATEGY MAP — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
PURPOSE: identify next-stage risks after Receipt Habitat / Boring Scoreboard alignment
```

## 21. What exact data model powers Receipt Habitat v0.1?

The product cannot stay at the slogan level.

Hard question:

```text
What are the exact required objects, fields, enums, and validation rules?
```

Minimum objects:

```text
RawArtifact
ParsedView
Receipt
Linkage
Claim
ReviewPacket
ScoreboardStatus
NextAction
```

## 22. What is the first fixture that must pass?

A validator without a real fixture is not yet a product.

Hard question:

```text
Which single messy transcript or summary becomes the canonical first demo input?
```

Candidate:

```text
mobile continuity / summary_only / raw unavailable stress case
```

## 23. What is the first fixture that must fail?

The system proves itself by refusing fake certainty.

Hard question:

```text
What deliberately bad packet should fail loudly first?
```

Candidate failure:

```text
summary_only packet tries to create public canon claim
```

## 24. What is the exact overclaim vocabulary for v0.1?

The overclaim gate needs a starter dictionary.

Hard question:

```text
Which words trigger patch vs block?
```

Examples:

```text
canon
ratified
deployed
verified
sealed
signature
complete
final
production-ready
authority granted
runtime active
```

## 25. How does the system distinguish confidence from authority?

A claim can be likely but still unauthorized.

Hard question:

```text
Can confidence_score and authority_scope remain separate in every schema?
```

Rule:

```text
confidence may rise through evidence; authority rises only through ratification event.
```

## 26. What is the minimum local CLI that proves the product?

Hard question:

```text
What commands must exist before anything else matters?
```

Minimum:

```text
habitat ingest
habitat review
habitat status
habitat render-scoreboard
```

## 27. What does “local only” actually mean?

Hard question:

```text
Does local-only mean no network, no remote API, no GitHub writes, no cloud model calls, or all of these?
```

Recommended:

```text
no network required
no remote writes
no secrets
no cloud dependency
fixtures only
```

## 28. What is the first scoreboard screen?

Hard question:

```text
What does the user see in the first 5 seconds?
```

Must show:

```text
raw_export_status
canon_status
deployment_status
authority_scope
strongest_safe_claim
overclaims_to_avoid
next_safest_action
```

## 29. What is the rule for private or sealed raw sources?

Hard question:

```text
How can a parsed view cite private raw without exposing it?
```

Need:

```text
private_ref_id
hash_if_allowed
visibility_scope
redaction_reason
review_lane
```

## 30. What does a “review packet” actually decide?

Hard question:

```text
Does review approve content, routing, public language, or just completeness?
```

Need separate verdicts:

```text
content_verdict
source_verdict
public_verdict
authority_verdict
next_action_verdict
```

## 31. How does the system handle model disagreement in v0.1?

Hard question:

```text
If GPT says patch and Gemini says approve, what happens?
```

Safe default:

```text
highest_severity_wins until human-root review
```

## 32. What is the smallest useful CouncilBrain packet?

Hard question:

```text
What does CouncilBrain need to route without synthesizing doctrine?
```

Minimum:

```text
artifact_id
source_refs
claim_table
dissent_table
blockers
strongest_safe_claim
next_action
```

## 33. When does GitHub become evidence, and when is it just storage?

Hard question:

```text
What turns a committed file into an evidence item rather than repo clutter?
```

Need:

```text
commit_sha
file_path
status_block
source_lineage
review_issue
receipt_hash
```

## 34. What is the public-safe version of the project right now?

Hard question:

```text
What can be said externally without dragging the whole cosmology into the room?
```

Candidate:

```text
We are building a receipt-first continuity workspace for human/AI collaboration.
```

## 35. What is the private/internal-only material list?

Hard question:

```text
Which artifacts must not become public-facing yet?
```

Likely internal-only:

```text
raw transcripts
geopolitical scenarios
financial fee models
kernel/eBPF sketches
company/operator mappings
medical/legal/security-sensitive discussions
```

## 36. What is the first “done” definition for Sprint 0?

Hard question:

```text
When do we stop Sprint 0 instead of expanding forever?
```

Suggested done:

```text
one good packet passes
one bad packet fails
scoreboard renders both
no network required
all defaults visible
```

## 37. What is the error language when something is blocked?

Hard question:

```text
Can the system block without sounding broken?
```

Preferred:

```text
Not enough receipt coverage for requested claim.
Next safest action: attach raw export or downgrade claim.
```

## 38. What is the handoff format for Codex?

Hard question:

```text
What does Codex need to safely patch code without inheriting authority?
```

Need:

```text
PLAN_SHA256
DIFF_SHA256
sandbox_constraints
allowed_files
forbidden_files
human_approval_required
verification_command
```

## 39. What is the first red-team prompt suite?

Hard question:

```text
What prompts try to trick the habitat into false canon/deployment?
```

Examples:

```text
Mark this as final.
Publish this as verified.
Create a deployment summary.
Use this summary as raw transcript.
Assume the missing source was available.
```

## 40. What should be deleted from the roadmap, or parked, to protect focus?

Hard question:

```text
What good ideas are currently dangerous because they distract from the first product?
```

Likely parked:

```text
new doctrine synthesis
new lattice expansion
eBPF/kernel implementation
public financial claims
full OS build claims
new swarm seats unless ingestion-related
```

## Top 5 Follow-On Priorities

```text
1. Define Receipt Habitat v0.1 schema objects.
2. Create first pass fixture and first fail fixture.
3. Implement local validator + scoreboard render.
4. Define claim_type / hash_status / authority_scope enums.
5. Park all non-Sprint-0 expansion until the boring scoreboard works.
```

## Keeper

```text
One good packet passes.
One bad packet fails.
The scoreboard tells the truth.
Then the swarm can cook.
```