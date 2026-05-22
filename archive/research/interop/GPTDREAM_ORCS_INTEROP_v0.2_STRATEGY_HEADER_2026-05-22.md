# GPTDream++ / ORCS Interop v0.2 — Strategy Header

```text
STATUS: CANDIDATE STRATEGY HEADER — NOT CANON
DATE: 2026-05-22
DEPLOYMENT STATUS: NOT DEPLOYED
AUTHORITY: NONE
PURPOSE: Define the smallest testable packet that proves meaning survives handoff across heterogeneous AI systems.
```

## Core principle

```text
Do not design for universal interoperability first.
Design for one small test proving that meaning survives handoff.
```

## Vendor-lane framing

```text
Google / Gemini:
  high-bandwidth ingestion, multimodal context mapping, candidate reports

Microsoft / GitHub / Copilot:
  workflow integration, bounded execution, worktrees, diffs, PR review surfaces

OpenAI / GPT / Codex:
  reasoning, code generation, tool orchestration, evals, developer-first agent workflows

GPTDream++:
  packet-carried context, provenance, contradiction preservation, memory discipline

Human-root:
  review, approval, canon promotion, final sign-off
```

## v0.2 build target

```text
One harmless markdown file.
Three agents.
One packet format.
No external execution.
No authority transfer.
Full provenance.
Explicit failure cases.
```

## Minimal primitives

1. `AgentCard`
2. `ContextPacket`
3. `HandoffRecord`
4. `ValidationResult`
5. `ContradictionRecord`
6. `HumanReviewGate`

## Boundaries

```text
Recorded does not mean true.
Summarized does not mean verified.
Verified does not mean ratified.
Ratified does not mean deployed.
Tool access does not mean authority.
Gemini success does not prove Codex/OpenAI compatibility.
Copilot diffs do not imply merge approval.
OpenAI/Codex output does not imply production readiness.
```

## Next artifact

```text
archive/research/interop/schemas/GPTDREAM_PROTOCOL_PACKET_SCHEMA_v0.2.json
```

Scope limit:

```text
Define only the fields needed to run the fixture.
Do not generalize beyond what the test requires.
```

## Success criterion

Different systems can receive the same packet, preserve intended meaning, identify uncertainty, and produce a reviewable handoff without inventing authority or losing provenance.

## Keeper

```text
The goal is not to make agents sound aligned.
The goal is to make their handoffs inspectable, testable, and reviewable.
```
