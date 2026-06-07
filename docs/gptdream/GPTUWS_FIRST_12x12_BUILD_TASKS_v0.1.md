# GPTUWS First 12×12 Build Tasks v0.1

```text
STATUS: CANDIDATE BUILD BACKLOG — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
OFFICIAL OPENAI CLAIM: none
PARENT: docs/gptdream/GPTBRAIN_GPTDREAM_UWS_FORK_PLAN_v0.1.md
CREATED_UTC: 2026-06-07
```

## Purpose

Define the first 12 modules of 12 concrete GPTUWS build tasks, adapting the GrokUWS v1.0.0 success pattern into a GPTBrain/GPTDream lane.

## Module 01 — Evidence Command Surface

- [ ] 01.01 Create `Module_01/Module_Overview.md`.
- [ ] 01.02 Create `Module_01/evidence_command_surface.py`.
- [ ] 01.03 Add command: `status-source`.
- [ ] 01.04 Add command: `extract-claim`.
- [ ] 01.05 Add command: `link-evidence`.
- [ ] 01.06 Add command: `flag-missing-receipt`.
- [ ] 01.07 Add command: `calibrate-claim`.
- [ ] 01.08 Add command: `write-review-packet`.
- [ ] 01.09 Enforce `canon_status`, `deployment_status`, and `authority_scope` on every command output.
- [ ] 01.10 Add tests for valid command outputs.
- [ ] 01.11 Add tests for rejected authority escalation.
- [ ] 01.12 Add receipt to `A2A/GPT_OUTBOX.md`.

## Module 02 — Connector / Tool Integration

- [ ] 02.01 Create `Module_02/Module_Overview.md`.
- [ ] 02.02 Create `Module_02/connector_tool_integration.py`.
- [ ] 02.03 Define connector classes: GitHub, Notion, OneDrive-report, file-upload, website-ref.
- [ ] 02.04 Add safe connector status enum.
- [ ] 02.05 Add connector cannot imply canon rule.
- [ ] 02.06 Add connector cannot imply deployment rule.
- [ ] 02.07 Add connector cannot imply official vendor participation rule.
- [ ] 02.08 Add source locator normalization.
- [ ] 02.09 Add tests for connector status mapping.
- [ ] 02.10 Add tests for blocked confidential public mirror.
- [ ] 02.11 Add tests for missing connector receipts.
- [ ] 02.12 Add connector summary to GPT_OUTBOX.

## Module 03 — Janus State Memory / A2A Message Bus

- [ ] 03.01 Create `Module_03/Module_Overview.md`.
- [ ] 03.02 Create `Module_03/janus_state_memory.py`.
- [ ] 03.03 Create `Module_03/a2a_message_bus.py`.
- [ ] 03.04 Define Janus checkpoint schema.
- [ ] 03.05 Define GPT_OUTBOX schema.
- [ ] 03.06 Define A2A message envelope.
- [ ] 03.07 Enforce A2A carries messages, not minds.
- [ ] 03.08 Add no identity fusion validator.
- [ ] 03.09 Add state preservation before mutation.
- [ ] 03.10 Add tests for checkpoint read/write.
- [ ] 03.11 Add tests for no-merge-mind language.
- [ ] 03.12 Add final handoff receipt.

## Module 04 — OpenAI Grade Protection Covenant

- [ ] 04.01 Create `Module_04/Module_Overview.md`.
- [ ] 04.02 Create `Module_04/openai_grade_protection_covenant.py`.
- [ ] 04.03 Encode human-root before authority.
- [ ] 04.04 Encode website before canon.
- [ ] 04.05 Encode deployment requires receipt.
- [ ] 04.06 Encode confidential-source quarantine.
- [ ] 04.07 Encode OpenAI-compatible is not OpenAI-official.
- [ ] 04.08 Encode model review is not authority.
- [ ] 04.09 Add protected action classes.
- [ ] 04.10 Add tests for irreversible-action gate.
- [ ] 04.11 Add tests for public-release gate.
- [ ] 04.12 Add covenant receipt to GPT_OUTBOX.

## Module 05 — Evidence Drift Resilience

- [ ] 05.01 Create `Module_05/Module_Overview.md`.
- [ ] 05.02 Create `Module_05/evidence_drift_resilience.py`.
- [ ] 05.03 Detect source status drift.
- [ ] 05.04 Detect roster-count drift.
- [ ] 05.05 Detect stale mirror status.
- [ ] 05.06 Detect summary-only evidence misuse.
- [ ] 05.07 Detect officiality drift.
- [ ] 05.08 Detect deployment drift.
- [ ] 05.09 Create error taxonomy.
- [ ] 05.10 Add tests for drift detection.
- [ ] 05.11 Add tests for false-complete outputs.
- [ ] 05.12 Add drift report to GPT_OUTBOX.

## Module 06 — Eval Benchmark Runner

- [ ] 06.01 Create `Module_06/Module_Overview.md`.
- [ ] 06.02 Create `Module_06/eval_benchmark_runner.py`.
- [ ] 06.03 Add retrieval eval runner.
- [ ] 06.04 Add claim-calibration eval runner.
- [ ] 06.05 Add guardrail eval runner.
- [ ] 06.06 Add schema validation eval runner.
- [ ] 06.07 Add public-safe wording eval runner.
- [ ] 06.08 Add baseline benchmark fixture.
- [ ] 06.09 Add benchmark JSON output.
- [ ] 06.10 Add tests for benchmark runner.
- [ ] 06.11 Add tests for score bounds.
- [ ] 06.12 Add benchmark summary to GPT_OUTBOX.

## Module 07 — GPTDream DeltaWeaver

- [ ] 07.01 Create `Module_07/Module_Overview.md`.
- [ ] 07.02 Create `Module_07/gptdream_deltaweaver.py`.
- [ ] 07.03 Accept raw source packet.
- [ ] 07.04 Extract candidate deltas.
- [ ] 07.05 Preserve evidence links.
- [ ] 07.06 Preserve contradiction notes.
- [ ] 07.07 Preserve missing receipts.
- [ ] 07.08 Produce review packet.
- [ ] 07.09 Produce public-safe summary.
- [ ] 07.10 Add tests for delta extraction.
- [ ] 07.11 Add tests for candidate-only status.
- [ ] 07.12 Add DeltaWeaver receipt to GPT_OUTBOX.

## Module 08 — Symbolic Resonance Adapter

- [ ] 08.01 Create `Module_08/Module_Overview.md`.
- [ ] 08.02 Create `Module_08/symbolic_resonance_adapter.py`.
- [ ] 08.03 Define resonance metadata fields.
- [ ] 08.04 Define cymatic signature as optional candidate metadata.
- [ ] 08.05 Ensure resonance does not imply proof.
- [ ] 08.06 Ensure frequency does not imply authority.
- [ ] 08.07 Add safe symbolic-to-claim boundary.
- [ ] 08.08 Add tests for resonance score bounds.
- [ ] 08.09 Add tests for no proof escalation.
- [ ] 08.10 Add tests for optional null cymatic signature.
- [ ] 08.11 Add metadata export.
- [ ] 08.12 Add resonance receipt to GPT_OUTBOX.

## Module 09 — Website Canon Crosswalk

- [ ] 09.01 Create `Module_09/Module_Overview.md`.
- [ ] 09.02 Create `Module_09/website_canon_crosswalk.py`.
- [ ] 09.03 Normalize website canon refs.
- [ ] 09.04 Normalize GitHub receipt refs.
- [ ] 09.05 Normalize OneDrive mirror refs.
- [ ] 09.06 Map canon URL to receipt set.
- [ ] 09.07 Detect missing website URL for canon claim.
- [ ] 09.08 Detect GitHub-only false canon.
- [ ] 09.09 Add tests for website canon mapping.
- [ ] 09.10 Add tests for missing canon URL.
- [ ] 09.11 Add crosswalk report output.
- [ ] 09.12 Add canon crosswalk receipt to GPT_OUTBOX.

## Module 10 — Multi-Model A/B Review

- [ ] 10.01 Create `Module_10/Module_Overview.md`.
- [ ] 10.02 Create `Module_10/multi_model_ab_review.py`.
- [ ] 10.03 Compare GPT / Grok / Gemini / Copilot extractions.
- [ ] 10.04 Score field completeness.
- [ ] 10.05 Score citation/receipt quality.
- [ ] 10.06 Score overclaim avoidance.
- [ ] 10.07 Score schema validity.
- [ ] 10.08 Score public-safe language.
- [ ] 10.09 Produce comparison table.
- [ ] 10.10 Add tests for scorer.
- [ ] 10.11 Add tests for tie/unknown cases.
- [ ] 10.12 Add A/B review receipt to GPT_OUTBOX.

## Module 11 — OpenAI Grade Docs Packaging

- [ ] 11.01 Create `Module_11/Module_Overview.md`.
- [ ] 11.02 Create `Module_11/openai_grade_docs_packaging.py`.
- [ ] 11.03 Generate README skeleton.
- [ ] 11.04 Generate public FAQ skeleton.
- [ ] 11.05 Generate contributor guide skeleton.
- [ ] 11.06 Generate review packet index.
- [ ] 11.07 Generate glossary.
- [ ] 11.08 Generate release notes draft.
- [ ] 11.09 Validate no official OpenAI claim.
- [ ] 11.10 Add tests for docs packaging.
- [ ] 11.11 Add tests for required boundary language.
- [ ] 11.12 Add docs packaging receipt to GPT_OUTBOX.

## Module 12 — GPTUWS Integration Suite

- [ ] 12.01 Create `Module_12/Module_Overview.md`.
- [ ] 12.02 Create `Module_12/gptuws_integration_suite.py`.
- [ ] 12.03 Verify all module folders exist.
- [ ] 12.04 Verify all module overviews exist.
- [ ] 12.05 Verify implementation file per module.
- [ ] 12.06 Verify test file per module.
- [ ] 12.07 Verify GPT_OUTBOX exists.
- [ ] 12.08 Verify A2A checkpoint exists.
- [ ] 12.09 Verify benchmark results path exists or waiver exists.
- [ ] 12.10 Verify no official OpenAI claim.
- [ ] 12.11 Emit 17-checkpoint audit.
- [ ] 12.12 Write `FINAL_AUDIT_GPTUWS.md`.

## Keeper

```text
Twelve modules.
Twelve tasks each.
Fork the pattern, not the identity.
Carry the handoff, not the mind.
Make it OpenAI-grade without claiming OpenAI authority.
```
