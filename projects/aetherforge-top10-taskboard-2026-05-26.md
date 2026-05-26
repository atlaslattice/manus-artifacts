# Aetherforge Top-10 Taskboard — 2026-05-26

## Run-all status

- [x] 1) Rehydrate/verify GPTBrain runtime check state (`reference_impl`)
- [x] 2) Run GPTBrain checks (`python -m pytest -q` and `bash run_checks.sh`)
- [x] 3) Audit docs integrity and repair the known broken Chinook artifact file
- [x] 4) Add repo hygiene workflow guardrails (workflow syntax + conflict markers)
- [x] 5) Add unresolved Swarm slot tracker artifact (TBD-08..TBD-11)
- [x] 6) Strengthen REM-8 wake flow with an execution checklist tied to WAKE_REPORT_TEMPLATE
- [x] 7) Add Tucker/Gemini adapter status note for current snapshot
- [x] 8) Validate Pinecone sync behavior and add sanity-check guidance
- [x] 9) Align project deployment-pack metadata across Free Bank / Chinook / Three-Tier
- [x] 10) Add CONTRIBUTING guidance for canon boundaries + local validation

## Verification receipts

- `archive/boot/gptbrain/reference_impl`: `python -m pytest -q` → pass
- `archive/boot/gptbrain/reference_impl`: `bash run_checks.sh` → pass
- `codebases/*/artifact_sync.py`: `python -m py_compile ...` → pass
- `projects/chinook-guardian/v1.0.md`: stale Notion export error payload replaced with valid markdown pack

## Notes

- In this repository snapshot, legacy paths referenced in some prior notes are absent (e.g., historical `.github` and `tucker_gemini` locations), so this run creates current-source-of-truth artifacts and guardrails directly in-repo.
