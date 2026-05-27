# Contributing to manus-artifacts

Thanks for contributing.

## Canon and authority boundary

- GitHub is the durable canonical substrate for this repository.
- Candidate canon is not ratified canon.
- No folder, spec, claim, or generated artifact self-ratifies.
- Human-root review is required for ratified canon and public claim promotion.

## First reads before changes

1. `archive/boot/gptbrain/KRAKOA_CANON_TRUTH_SPINE_2026-05-26.md`
2. `archive/boot/COUNCIL_BRAIN_INDEX.md`
3. `archive/boot/gptbrain/CURRENT_STATE.md`
4. `archive/boot/gptbrain/NEXT_ACTIONS.md`
5. `archive/boot/gptbrain/GPTBRAIN_INDEX_OF_INDEXES_2026-05-26.md`
6. `archive/boot/atlasbrain/README.md`
7. `archive/boot/atlasbrain/ATLASBRAIN_INDEX_2026-05-26.md`

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

## Aetherforge Module 8-9 routing

- Start with `AETHERFORGE_MODULE_REGISTRY_v0.1.md` and `projects/aetherforge-game-world/README.md` before routing Module 8 or Module 9 work.
- Route **M8 / Archive Bowl** work to knowledge-graph, archive-mining, and cross-reference artifacts. Keep every new index or graph edge source-linked and mark candidate/canon status explicitly.
- Route **M9 / Lore Library** work to documentation, manifests, boot cards, rehydration guidance, and agent-brain profile surfaces. Keep first-read paths current when routing changes.
- If a Module 8-9 change creates or moves a navigation surface, update the nearest README or index-of-indexes in the same patch.
- Do not treat Aetherforge game framing, quest titles, or storage location as ratification.

## Pull request expectations

- Keep changes surgical and repo-grounded.
- Update nearby docs when behavior or routing changes.
- Do not claim ratification unless explicitly approved.
