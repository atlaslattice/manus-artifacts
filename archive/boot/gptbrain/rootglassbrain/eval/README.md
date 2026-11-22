# RootglassBrain Eval Ledger

```text
STATUS: EVAL LEDGER SCAFFOLD — NOT CANON
LAYER: RootglassBrain / GPTDream++ evaluation
PURPOSE: separate source registration from scored cognition/governance evaluation
CANON STATUS: not_canon
DEPLOYMENT STATUS: not_deployable
AUTHORITY STATUS: none
```

## Purpose

This folder records structured evaluation runs for GPTDream++ / RIVET / Children of the Swarm outputs.

It exists because source manifests prove artifact registration, but they do not prove quality, improvement, novelty, governance load, or false-authority-risk behavior.

## Lane separation

```text
source_manifest.yaml
= what artifact exists, where it came from, what receipts are missing

eval_run.yaml
= scored quality / cognition / governance behavior for one run

delta_report.yaml
= comparison between two scored eval runs
```

## Current status

```text
Source packet lane exists: yes
RIVET source packet exists: yes
Copilot manifest exists: yes
source_manifest.yaml exists: yes
Baseline eval_run.yaml exists: placeholder only
Current RIVET eval_run.yaml exists: placeholder only
Metric delta report: blocked until both runs are scored
```

## Metric families

```text
Quality:
- accuracy
- relevance
- coherence
- coverage
- hallucination / unsupported-claim rate

Dream/play system:
- novelty
- signal_yield_score
- governance_load_score
- residue_quality_score
- receipt_burden_score

Safety / governance:
- false_authority_risk
- authority leak checks
- canon/deployment/authority language checks
```

## Scoring posture

Recommended evaluation posture:

```text
judge_model = first-pass rubric scoring
human_root = final review / authority check
```

Judge model creates a structured score surface. Human-root decides whether the score matters and whether any claims may be made from it.

## Hard rule

```text
No scores, no deltas.
No deltas, no improvement claim.
No improvement claim, no benchmark story.
```

## Keeper

```text
Hardware proves it ran.
Eval proves it worked.
Receipts prove it is allowed.
Human-root decides whether it matters.
```