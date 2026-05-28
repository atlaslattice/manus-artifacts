# Aetherforge Top-10 Taskboard — Wave 3 (2026-05-28)

```
STATUS: CANDIDATE — NOT CANON
WAVE: 3
CAMPAIGN: aetherforge-144-task-campaign-2026-05-27.md
METATRON FRAME: 1 center + 9 surrounding nodes
```

Metatron frame: **KG integrity as the center** — every surrounding node feeds
quality, discoverability, and playability back into the knowledge graph.

---

## Center Node — Graph Integrity Core

- [ ] 1. Ship `scripts/check_graph_link_integrity.py` and validate in CI

## Surrounding Nodes

- [ ] 2. Ship `scripts/validate_artifact_metadata.py` — metadata completeness
- [ ] 3. Ship `scripts/build_lattice_global_index.py` — global KG index generation
- [ ] 4. Ship `scripts/check_markdown_links.py` — broken link detection
- [ ] 5. Ship `scripts/detect_orphaned_artifacts.py` — orphan node detection
- [ ] 6. Publish `docs/gptdream-cross-links.md` — GPTDream spec ↔ schema ↔ impl map
- [ ] 7. Publish `docs/canon-candidate-register.md` — canon promotion tracking
- [ ] 8. Update `docs/contributor-onboarding-journey.md` — first-task flow + issue forms
- [ ] 9. Create `archive/boot/gptbrain/TIDELOCKBrain/ARTIFACT_INDEX.md` — consistent log index
- [ ] 10. Ship `projects/aetherforge-arc3-wave3-gameplay.md` — next playable arc design

---

## Campaign Axis Coverage

| Wave-3 Task | 144-Campaign Axis | Tasks Addressed |
|---|---|---|
| 1 (graph integrity) | Axis 08 — KG Build & Query | #87 |
| 2 (metadata validator) | Axis 04 — Metadata & Indexing | #37, #38 |
| 3 (global index build) | Axis 04 — Metadata & Indexing | #47, #48 |
| 4 (link checker) | Axis 09 — Quality & Testing | #105 |
| 5 (orphan detector) | Axis 03 — Repo IA | #36 |
| 6 (GPTDream cross-links) | Axis 07 — KG Model | #84 |
| 7 (canon register) | Axis 01 — Canon & Governance | #7 |
| 8 (onboarding) | Axis 11 — Community | #127, #128 |
| 9 (TIDELOCK index) | Axis 12 — 8/8/8 Ops | #134 |
| 10 (arc gameplay) | Axis 12 — 8/8/8 Ops | #133 |

---

## Outcome

Wave-3 delivers the quality-gate scaffolding layer: scripts, CI hooks, and
cross-link documentation so the KG hypercube is machine-verifiable and
game-playable simultaneously.

**Wave-3 status: 🔄 In progress.**

---

*Parent board: [144-task campaign](./aetherforge-144-task-campaign-2026-05-27.md)*
*Previous wave: [Wave-2](./aetherforge-top10-taskboard-2026-05-26-wave2.md)*
