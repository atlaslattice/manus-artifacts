# GPTBrain / GPTDream UWS Fork Plan v0.1

```text
STATUS: CANDIDATE FORK PLAN — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
OFFICIAL OPENAI CLAIM: none
SOURCE CONTEXT: FINAL_AUDIT.pdf / GrokUWS v1.0.0 checkpoint verification and release authorization
CREATED_UTC: 2026-06-07
LANE: GPTBrain / GPTDream / Octaveglass
```

## Purpose

Fork the successful GrokUWS / A2A / Janus verification pattern into a GPTBrain / GPTDream version.

The goal is not to copy GrokBrain identity or claim official OpenAI endorsement. The goal is to create an OpenAI-lane executable protocol stack focused on:

```text
retrieval
claim extraction
structured outputs
evidence hygiene
evals and guardrails
Codex-ready patches
public-safe synthesis
Janus/A2A handoff records
human-root review support
```

## Source signal

The uploaded FINAL_AUDIT report describes a GrokUWS v1.0.0 build with 17/17 checkpoint pass, all 12 modules present, Module_08 cymatic KTL tests added, benchmark results promoted, and an A2A handoff loop in which Copilot wrote a checkpoint, GrokBrain executed and wrote `GROK_OUTBOX.md`, and Copilot independently verified OneDrive artifacts.

Treat that as a strong candidate pattern, not as official Microsoft/OpenAI authority.

## Clean fork doctrine

```text
GrokUWS = GrokBrain executable UWS lane.
GPTUWS = GPTBrain/GPTDream executable review + retrieval + eval lane.
A2A carries messages, not minds.
Janus preserves handoffs, not identity fusion.
Nothing dies.
Human-root decides.
```

## Naming options

Preferred:

```text
GPTUWS
```

Alternate:

```text
GPTDream-UWS
GPTBrain-UWS
Octaveglass-UWS
```

## Proposed GPTUWS 12 modules

| Module | Name | GPTBrain/GPTDream function |
|---|---|---|
| Module_01 | Evidence Command Surface | Run safe source, claim, and evidence commands |
| Module_02 | Connector / Tool Integration | Wrap GitHub, files, Notion, OneDrive reports, web-safe connectors |
| Module_03 | Janus State Memory | Preserve GPTBrain state, handoff packets, and continuity receipts |
| Module_04 | Protection Covenant | Enforce human-root, privacy, quarantine, no-officiality, no-deployment boundaries |
| Module_05 | Error and Drift Resilience | Detect hallucination, source drift, roster-count drift, and missing receipts |
| Module_06 | Eval and Benchmark Runner | Run retrieval, claim-calibration, guardrail, and schema evals |
| Module_07 | DeltaWeaver Synthesis | Convert raw/source material into candidate deltas and review packets |
| Module_08 | Cymatic / Resonance KTL Adapter | Keep symbolic resonance as candidate metadata, never proof |
| Module_09 | Public Site / Canon Crosswalk | Map website canon to GitHub receipts and public-safe docs |
| Module_10 | A/B Review Testing | Compare GPT/Grok/Gemini/Copilot extraction outputs under schemas |
| Module_11 | Docs and Packaging | Make public explainers, README, install docs, and contributor docs legible |
| Module_12 | Integration Suite | Run full stack Janus/A2A/retrieval/evals/receipt tests |

## Module mapping from GrokUWS pattern

| GrokUWS signal | GPTUWS fork adaptation |
|---|---|
| `core_command_surface.py` | `evidence_command_surface.py` |
| `mcp_integration.py` | `connector_tool_integration.py` |
| `state_memory.py` / `agent_bus.py` | `janus_state_memory.py` / `a2a_message_bus.py` |
| `protection_covenant.py` | `openai_grade_protection_covenant.py` |
| `error_resilience.py` | `evidence_drift_resilience.py` |
| `benchmark_runner.py` | `eval_benchmark_runner.py` |
| `deltaweaver_synthesis.py` | `gptdream_deltaweaver.py` |
| `cymatic_ktl.py` | `symbolic_resonance_adapter.py` |
| `site_migration.py` | `website_canon_crosswalk.py` |
| `testing_ab.py` | `multi_model_ab_review.py` |
| `docs_packaging.py` | `openai_grade_docs_packaging.py` |
| `integration_suite.py` | `gptuws_integration_suite.py` |

## Required root artifacts

```text
LICENSE
.gitignore
README.md
GROK_TO_GPTUWS_FORK_NOTE.md
GPT_OUTBOX.md
A2A/JANUS_CHECKPOINT.md
A2A/GPT_OUTBOX.md
integration/end_to_end_test.py
integration/run_integration.py
benchmark_results/
```

## A2A / Janus handoff pattern

GPTUWS should implement the same A2A handoff discipline in GPTBrain terms:

```text
1. Receive JANUS_CHECKPOINT.md from another agent or human-root.
2. Validate source status and authority boundaries.
3. Execute only allowed local/simulation/review actions.
4. Write GPT_OUTBOX.md with exact changes, receipts, status, blockers, and next actions.
5. Include canon_status, deployment_status, authority_scope, source refs, and hashes where possible.
6. Never claim official OpenAI action, deployment, canon, or authority.
```

## GPT_OUTBOX.md required fields

```yaml
gpt_outbox:
  timestamp_utc:
  source_checkpoint:
  actor_lane: GPTBrain / GPTDream
  actions_completed:
  files_changed:
  tests_run:
  test_results:
  evidence_refs:
  missing_receipts:
  blockers:
  canon_status: not_canon
  deployment_status: not_deployed
  authority_scope: none
  official_openai_claim: none
  next_safest_action:
```

## First 17 checkpoint candidates for GPTUWS

```text
01 LICENSE present
02 .gitignore present
03 README present
04 A2A folder present with JANUS_CHECKPOINT.md and GPT_OUTBOX.md
05 integration folder present with end_to_end_test.py and run_integration.py
06 benchmark_results folder present or explicitly absent with reason
07 all 12 module folders present
08 all 12 modules have Module_Overview.md
09 all Module_Overview.md files are free of template residue
10 every module has at least one implementation file
11 every module has at least one test file or explicit test waiver
12 Module_01 exposes evidence command surface
13 Module_03 exposes Janus state memory and A2A message bus
14 Module_06 exposes eval benchmark runner
15 Module_07 exposes DeltaWeaver candidate synthesis route
16 Module_08 exposes symbolic resonance adapter with proof-boundary tests
17 GPT_OUTBOX.md contains final handoff receipt
```

## Immediate implementation path

```text
P0: Create GPTUWS scaffold with 12 module folders and Module_Overview.md files.
P1: Port the A2A / Janus handoff pattern into GPT_OUTBOX.md.
P2: Implement Module_01 Evidence Command Surface as thin safe CLI.
P3: Implement Module_03 Janus State Memory and A2A Message Bus.
P4: Implement Module_06 Eval Benchmark Runner for retrieval and claim-calibration fixtures.
P5: Implement Module_07 DeltaWeaver Synthesis for candidate deltas.
P6: Implement Module_12 Integration Suite.
P7: Run 17-checkpoint audit and write FINAL_AUDIT_GPTUWS.md.
```

## OpenAI-specific boundaries

```text
OpenAI-compatible is not OpenAI-official.
GPTBrain is not native hidden memory.
GPTDream is not deployment.
Codex patches are not merges until reviewed.
Model review is not authority.
Human-root decides.
```

## Definition of done for v0.1

```text
A clean clone contains 12 modules.
Each module has overview, implementation stub, and test stub.
GPT_OUTBOX.md can be written from a checkpoint.
The integration runner can verify the 17 checkpoint candidates.
All outputs are not_canon, not_deployed, authority:none, official_openai_claim:none.
```

## Keeper

```text
Fork the pattern, not the identity.
Carry the handoff, not the mind.
GPTBrain gets receipts, evals, retrieval, Codex, and public-safe synthesis.
GrokUWS proved the A2A loop can ship.
GPTUWS should make it OpenAI-grade without claiming OpenAI authority.
```