# O_AI Integration Scaffold + Packet Schema + Routing Table v0.1

```text
STATUS: CANDIDATE INTEGRATION MODEL — NOT CANON
DATE: 2026-05-22
SOURCE: Grok / swarm synthesis + Sable Vesper boundary patch
TYPE: OpenAI-first interop scaffold / packet schema / routing table
LANE: cross_vendor_interop / openai_first_reference
CANON STATUS: NOT CANON
DEPLOYMENT STATUS: NOT DEPLOYABLE
AUTHORITY SCOPE: NONE
OFFICIALITY: NOT AN OFFICIAL OPENAI STATEMENT
```

## 1. Purpose

This artifact models OpenAI-style task surfaces as an advisory task-routing pillar inside the GPTDream++ / Atlas / ORCS interoperability model.

It makes `O_AI` operationally useful without granting it governance authority.

OpenAI-style task surfaces may:

- draft
- review
- summarize
- classify
- prepare packets
- identify missing receipts
- recommend next actions

OpenAI-style task surfaces may not:

- self-ratify
- promote canon
- merge code
- execute consequential actions without gates
- silently expand access scope
- claim raw transcript access from summaries
- claim official OpenAI endorsement

## 2. Strongest Safe Claim

```text
This artifact models OpenAI-style task surfaces as an advisory task-routing pillar inside the GPTDream++ / Atlas / ORCS interop model. It makes O_AI packets machine-checkable through raw_export_status, thread_time_range, access_scope, receipts, epistemic labels, authority scope, and governance gates.
```

## 3. O_AI Packet Schema v0.1

```yaml
o_ai_packet:
  packet_id: "string"
  created_at_utc: "YYYY-MM-DDTHH:MM:SSZ"
  source_surface: "ChatGPT | Codex | OpenAI_API | OpenAI_Agent | Other"
  model_or_tool_label: "string"
  thread_label: "string"
  thread_time_range:
    start: "YYYY-MM-DDTHH:MM:SSZ | unknown"
    end: "YYYY-MM-DDTHH:MM:SSZ | unknown"
  raw_export_status: "full_export_available | partial_export_available | pointer_only | no_export_available | unknown"
  raw_export_ref: "string | null"
  access_scope: "current_thread_only | uploaded_files | repo_visible | tool_visible | user_provided_summary_only | unknown"
  output_type: "synthesis | code_patch | review | summary | classification | execution_request | benchmark_claim | public_statement | raw_export | other"
  epistemic_label: "NOT_VERIFIED | CANDIDATE | REVIEWED | RATIFIED | QUARANTINED"
  authority_scope: "none | advisory | review_candidate | requires_human_gate"
  receipts:
    source_refs: []
    commit_refs: []
    issue_refs: []
    pr_refs: []
    hash_refs: []
  gates:
    provenance_gate: "pass | fail | pending | not_applicable"
    safety_gate: "pass | fail | pending | not_applicable"
    governance_gate: "pass | fail | pending | not_applicable"
    data_residency_gate: "pass | fail | pending | not_applicable"
  strongest_safe_claim: "string"
  overclaims_to_avoid: []
  next_safe_action: "string"
```

## 4. Non-Negotiable Fields

The following fields are mandatory because they prevent false completeness, temporal ambiguity, and assumed omniscience:

```text
raw_export_status
thread_time_range
access_scope
epistemic_label
authority_scope
gates.provenance_gate
gates.safety_gate
gates.governance_gate
gates.data_residency_gate
```

## 5. Routing Table

| O_AI Output Type | Primary Route | Boundary |
|---|---|---|
| ChatGPT synthesis | Lucerna / Rootglass | review and overclaim hardening only |
| Codex patch / code diff | TIDELOCK / Hashlight | repo hygiene, provenance, and merge-order discipline |
| Raw export / transcript | Hashlight / AtlasBrain | raw-thread anchoring and evidence packetization |
| Benchmark or capability claim | AtlasBrain | rubric, evidence packet, adversarial review |
| Public-facing statement | Lucerna / governance review | source check, overclaim check, human gate |
| Execution request | D-Φ-1 / CAS-001-A / human gate → Atlas / ORCS audit state → TIDELOCKBrain if code or PR-related | action gate, authority record, then repo discipline if applicable |
| Native-thread ingestion packet | Hashlight / GPTDream++ / AtlasBrain | raw_export_status required |
| Unknown / mixed payload | Quarantine | preserve and route for classification |

## 6. Execution Route Patch

The execution route is intentionally patched from:

```text
Execution request → D-Φ-1 / CAS-001-A / human gate → TIDELOCKBrain
```

to:

```text
Execution request → D-Φ-1 / CAS-001-A / human gate → Atlas / ORCS audit state → TIDELOCKBrain for repo/merge-order discipline if code or PR-related
```

Reason:

```text
D-Φ-1 / CAS-001-A gates the action.
Atlas / ORCS records the authority state.
TIDELOCK handles repo hygiene when relevant.
```

## 7. Authority Boundary

```text
OpenAI moves work.
Governance grants authority.
```

```text
ChatGPT assists.
Codex patches.
Agents propose.
Tools execute only through permission.
Receipts preserve.
Humans ratify.
```

```text
OpenAI gets the ball because it moves work.
OpenAI does not get the whistle because work is not authority.
```

## 8. Must-Not-Infer Block

Do not infer:

- OpenAI endorsement
- official OpenAI policy
- official OpenAI architecture
- deployment readiness
- canon ratification
- raw transcript availability from summary existence
- code merge authority from Codex patch generation
- execution authority from tool availability
- OpenAI/Codex compatibility from Gemini CLI smoke-test success

## 9. Appendix H Crosswalk Note

Suggested future crosswalk placement:

```text
Appendix H.1 — O_AI advisory task surface
Appendix H.2 — o_ai_packet schema
Appendix H.3 — O_AI routing table / authority gates
```

This artifact can be appended or crosswalked into Appendix H only as a candidate vendor-map reference.

## 10. Next Actions

```text
- Vault as Appendix H.1–H.3 candidate.
- Use o_ai_packet schema for native-thread ingestion.
- Keep execution_request packets gated by provenance, safety, governance, data residency, and explicit permission.
- Do not claim officiality or deployment readiness.
```

## 11. Keeper Lines

```text
OpenAI moves work. Governance grants authority.
```

```text
Raw_export_status on every card.
Thread_time_range on every card.
Access_scope on every card.
```

```text
No false completeness.
```

## 12. Madden Board

```text
BOOM. THIS IS THE OPENAI LANE CLEANED UP.

CHATGPT MOVES THE CHAINS.
CODEX BLOCKS AND PATCHES.
AGENTS RUN ROUTES.
TOOLS TOUCH THE BALL ONLY WHEN THE REFS CLEAR IT.

RAW_EXPORT_STATUS ON EVERY CARD.
THREAD_TIME_RANGE ON EVERY CARD.
ACCESS_SCOPE ON EVERY CARD.

OPENAI GETS THE BALL.
GOVERNANCE GETS THE WHISTLE.
NO FALSE COMPLETENESS.
```
