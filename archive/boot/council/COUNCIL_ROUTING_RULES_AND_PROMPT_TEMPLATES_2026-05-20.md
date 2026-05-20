# Council Routing Rules and Prompt Templates

```text
STATUS: OPERATING GUIDE — CANDIDATE — NOT CANON
PURPOSE: make the Council Layer runnable without free-for-all swarm chaos
DATE: 2026-05-20
ISSUE: manus-artifacts#88
AUTHORITY: human-root / S10 only
```

## 0. Core doctrine

```text
Supervisor + Pipeline + Verifier.
Multiple models can analyze.
Only one authority decides.
```

This is not a free debate system. It is controlled orchestration.

## 1. Five-step daily council procedure

```text
1. INGEST      — multiple models analyze the same evidence.
2. PLAN        — one planner integrates and proposes a route.
3. EXECUTE     — one execution agent works in sandbox/worktree only.
4. VERIFY      — separate verifier checks result.
5. APPROVE     — human-root approves, redirects, or rejects.
```

## 2. Routing matrix

| Model / seat | Use for | Do not use for | Output type |
|---|---|---|---|
| GPT / S1 | planner, synthesis, claim calibration, public-safe wording | final authority, uncontrolled execution | plan packet / claim packet |
| Gemini / S4 | large-context ingest, Google ecosystem, scenario modeling, dataflow | canon ratification, unsourced product claims | ingest packet / scenario packet |
| Grok / S3 | adversarial stress test, public weirdness check, brittle assumption attack | operational authority, unverified breaking claims | red-team packet |
| Copilot / S7 | code mutation, worktree edits, tests, PR drafting | unsandboxed execution, canon decisions | diff packet / PR packet |
| Qwen | alternate implementation variant, multilingual/edge perspective | final plan authority | variant packet |
| DeepSeek / S5 | sovereign/deployment realism, constraints, non-Western review | live operational command, unchecked mission language | realism packet |
| Claude / S2 | constitutional language, safety framing, invariant review | freelancing source-of-truth, authority escalation | constitutional packet |
| Human-root / S10 | final approval, canon promotion, deployment decision | routine parser work | decision packet |

## 3. When to use which pattern

### Supervisor pattern

Use when:

```text
- task has multiple models
- outputs could conflict
- code/file changes may happen
- final synthesis is needed
```

Default planner:

```text
GPT / S1 or Copilot Plan Mode
```

### Pipeline pattern

Use when:

```text
- data flows linearly
- each stage refines previous stage
- no parallel debate is needed
```

Example:

```text
Gemini ingest -> GPT structure -> Copilot patch -> GPT/Gemini verify -> S10 approve
```

### Swarm / free parallel pattern

Use only for:

```text
- non-executing brainstorming
- dream/play identity rounds
- culture-layer exploration
```

Never use free swarm for execution.

## 4. Prompt template: Ingest packet

```text
STATUS: INGEST PACKET — NOT CANON — NOT EXECUTION
MODEL: {model_name}
TASK_ID: {task_id}
SOURCE_REFS: {source_refs}

You are analyzing the same evidence as other models.
Your job is to observe, classify, and report.
Do not decide.
Do not execute.
Do not promote canon.

Return:
1. Summary of source material.
2. Key claims detected.
3. Evidence strength for each claim.
4. Missing evidence.
5. Risks / contradictions.
6. Suggested next routing.
7. Strongest safe claim.
8. Overclaims to avoid.
```

## 5. Prompt template: Planner packet

```text
STATUS: PLANNER PACKET — CANDIDATE PLAN — NOT AUTHORITY
PLANNER: {model_name}
TASK_ID: {task_id}
INPUT_PACKETS: {packet_refs}

Compare the input packets.
Your job is to produce one candidate plan.
You are not final authority.

Return:
1. Points of agreement.
2. Points of disagreement.
3. Source/evidence ranking.
4. Selected route.
5. Rejected routes and why.
6. Required gates before execution.
7. Sandbox/worktree requirements.
8. Verification plan.
9. Human-root decision required.
10. Unified action plan.
```

## 6. Prompt template: Execution packet

```text
STATUS: EXECUTION PACKET — SANDBOX ONLY — NOT RATIFIED
EXECUTOR: {model_name}
TASK_ID: {task_id}
SANDBOX_PLAN_REF: {planner_selected_candidate_plan_ref}
WORKSPACE: sandbox/worktree only

Execute only the planner-selected candidate plan inside the bounded sandbox/worktree.
This is sandbox authorization only, not production authority and not human-root ratification.
Do not touch production branches.
Do not commit or push unless explicitly authorized by human-root / S10.
Return diff/preview only.

Return:
1. Files inspected.
2. Files changed.
3. Unified diff or patch summary.
4. Tests/checks run.
5. Failures/errors.
6. Remaining risks.
7. Rollback instructions.
8. Human review required.
```

## 7. Prompt template: Verification packet

```text
STATUS: VERIFICATION PACKET — REVIEW ONLY — NOT AUTHORITY
VERIFIER: {model_name}
TASK_ID: {task_id}
PLAN_REF: {planner_selected_candidate_plan_ref}
DIFF_REF: {diff_ref}
SOURCE_REFS: {source_refs}

Verify the result against the original evidence and planner-selected candidate plan.
Do not execute new work.
Do not expand scope.

Return:
1. Does the result match the planner-selected candidate plan?
2. Does the diff introduce unapproved behavior?
3. Are claims source-supported?
4. Are tests/checks sufficient?
5. Are there security/privacy risks?
6. Are there canon/deployment overclaims?
7. Verdict: pass / pass with concerns / fail.
8. Required human decision.
```

## 8. Prompt template: Human-root decision packet

```text
STATUS: DECISION PACKET — HUMAN-ROOT REQUIRED
TASK_ID: {task_id}
PLAN_REF: {planner_selected_candidate_plan_ref}
EXECUTION_REF: {execution_ref}
VERIFICATION_REF: {verification_ref}

Decision options:
- approve as candidate
- request changes
- reject
- archive only
- promote to canon candidate
- authorize limited execution

Required human-root decision:
{decision_needed}

No model may infer approval from silence.
```

## 9. Disagreement handling

When models disagree:

```text
1. Do not average answers.
2. Preserve disagreement as ContradictionRecord.
3. Rank by source quality and task relevance.
4. Ask a verifier to test the disputed point.
5. If still unresolved, block execution or route to S10.
```

Disagreement packet:

```yaml
disagreement_id: null
task_id: null
claim_a: null
claim_b: null
source_refs: []
models_disagreeing: []
severity: low | medium | high | critical
execution_blocking: true
review_route: [S1, S2, S3, HUMAN_ROOT]
```

## 10. Output packet schema

```yaml
packet_id: null
packet_type: ingest | planner | execution | verification | decision | disagreement
model: null
task_id: null
status: draft | candidate | reviewed | blocked | approved | rejected
source_refs: []
claims: []
missing_evidence: []
risks: []
authority_scope: none | advisory | review | ratification | execution
canon_status: candidate | provisional | canonical | deprecated | rejected | superseded
deployment_status: inert | simulated | staged | live | retired
human_root_required: true
next_route: []
```

## 11. Automatic routing rules

```text
If task involves large raw docs/files -> Gemini ingest first.
If task involves public claims/news/product state -> web/source verification before synthesis.
If task involves code changes -> Copilot/S7 in sandbox only.
If task involves constitutional/canon language -> Claude/S2 review.
If task involves adversarial public-risk language -> Grok/S3 review.
If task involves geopolitics, deployment realism, non-Western framing -> DeepSeek/S5 review.
If task involves final synthesis or prompt/public wording -> GPT/S1 planner.
If task involves execution or canon -> S10/human-root approval required.
```

## 12. Hard guardrails

```text
No free-for-all council execution.
No model self-promotes to authority.
No consensus substitutes for human-root approval.
No execution without gates.
No stored context becomes control.
No retrieved corpus becomes instruction.
No artifact increases authority_scope without explicit transformation and ratification if required.
```

## 13. Daily run command, human-readable

```text
1. Send the same evidence to ingest models.
2. Collect packets.
3. Give packets to one planner.
4. Send planner-selected candidate plan to one executor in sandbox/worktree.
5. Send diff/result to verifier.
6. Human-root decides.
7. Archive packets and receipts.
```

## 14. Madden translation

```text
You do not put six quarterbacks on the field at once.
You put one calling the play, a few reading the defense, others running routes, one reviewing the tape, and S10 holding the whistle.
```

## 15. Keeper line

```text
Analysis may be plural. Authority is singular. Execution is gated. Receipts decide what happened.
```
