# OpenAI Source Graph Engine v0.1

STATUS: CANDIDATE WORKING SPEC — NOT CANON  
DEPLOYMENT: NOT DEPLOYABLE  
AUTHORITY: NONE

## Purpose
Build a source-grounded graph substrate before adding more agents.

## Required node types
- raw_source
- parsed_fact
- claim
- evidence
- review
- action

## Required edge types
- derived_from
- supports
- contradicts
- supersedes
- quarantines

## OpenAI integration scope
OpenAI packets are ingested as source packets and mapped into raw_source nodes,
then promoted through parsed_fact, claim, evidence, review, and action layers.

## Hard guardrail
No claim is valid unless it has a source-grounding path via `derived_from`
from claim -> parsed_fact/raw_source.

## Required answerability
The graph must answer:
1. Where did this claim come from?
2. What evidence supports it?
3. What is still summary-only?
4. What is blocked from public use?
