# Contributing to manus-artifacts

Thanks for contributing.

## Canon and authority boundary

- GitHub is the durable canonical substrate for this repository.
- Candidate canon is not ratified canon.
- No folder, spec, claim, or generated artifact self-ratifies.
- Human-root review is required for ratified canon and public claim promotion.

## First reads before changes

1. `archive/boot/COUNCIL_BRAIN_INDEX.md`
2. `archive/boot/gptbrain/CURRENT_STATE.md`
3. `archive/boot/gptbrain/NEXT_ACTIONS.md`
4. `archive/boot/gptbrain/GPTBRAIN_INDEX_OF_INDEXES_2026-05-26.md`
5. `archive/boot/atlasbrain/README.md`
6. `archive/boot/atlasbrain/ATLASBRAIN_INDEX_2026-05-26.md`

## High-signal local checks

Run from:

`/home/runner/work/manus-artifacts/manus-artifacts/archive/boot/gptbrain/reference_impl`

```bash
python -m pytest -q
bash run_checks.sh
```

## Evidence discipline

- Preserve sources first (raw logs), then score claims.
- Evaluator reactions are signals, not proof.
- Contradictions should be linked/routed, not silently erased.
- Quarantine preserves disputed artifacts without authority leakage.

## Pull request expectations

- Keep changes surgical and repo-grounded.
- Update nearby docs when behavior or routing changes.
- Do not claim ratification unless explicitly approved.

