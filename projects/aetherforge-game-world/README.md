# ⚒️ Aetherforge Game World Onboarding — Module 8 (Candidate)

```text
STATUS: CANDIDATE WORLDBUILDING PACK
CANON: NO
DEPLOYMENT: NO
DATE: 2026-05-26
PURPOSE: gameplay framing + serious acceptance criteria for Module 8 execution
```

## Source gravity

- PR #166 — Aetherforge game architecture candidate  
- Issue #164 — gameplay anomaly tracking  
- Issue #170 — Omnispec Prime PDF review lane  
- Issue #176 — Archive Bowl top-50 roadmap lane  

## Quick onboarding

1. Read `AETHERFORGE_MODULE_REGISTRY_v0.1.md` for module routing.
2. Use the zone map below to route work into the game world.
3. Use quest tiers to size difficulty and review depth.
4. Treat adversarial tests as boss fights before merge.
5. Treat merged reviewable artifacts as loot/reward.
6. Keep Omnispec Prime in candidate status unless ratified.

## Quest taxonomy

| Quest class | Purpose | Typical output |
|---|---|---|
| Scout Quest | Discover and map unknown surfaces | index, inventory, crosswalk |
| Forge Quest | Build or update structured artifacts | spec, schema, implementation patch |
| Trial Quest | Validate behavior and safety | tests, checks, adversarial runs |
| Council Quest | Route authority and review decisions | gate checklist, review packet |
| Restoration Quest | Recover or reconcile archive integrity | provenance packet, reconciliation ledger |

## Module zones (M1–M10)

| Module | Zone name | Zone objective |
|---|---|---|
| M1 | Command Bastion | command table, dashboards, weekly cadence |
| M2 | Governance Citadel | canon boundary, authority routing, ratification gates |
| M3 | ORCS Transit | trust-state transitions and contradiction routing |
| M4 | Interop Gateway | Appendix H / O_AI packet exchange lanes |
| M5 | Receipt Foundry | provenance, evidence integrity, source-summary safety |
| M6 | Trial Arena | validators, CI-equivalent checks, adversarial harnesses |
| M7 | Ops Dockyard | labels, templates, workflow automation |
| M8 | Archive Bowl | knowledge graph and archive mining structures |
| M9 | Lore Library | README/manifests/rehydration docs |
| M10 | Merge Gate | PR routing, stale queue reduction, review compression |

## Quest difficulty tiers

| Tier | Name | Definition |
|---|---|---|
| T1 | Patrol | single-file or single-surface updates with clear acceptance gates |
| T2 | Expedition | multi-file changes across one module with validation evidence |
| T3 | Raid | cross-module changes with explicit dependency and governance routing |
| T4 | Mythic | architecture-level changes requiring broad review, adversarial proof, and phased rollout |

## Boss fights = adversarial tests

- A boss fight is any adversarial test suite or failure-mode challenge that can reject a merge.
- Minimum boss-fight evidence for T2+ quests:
  - validation command list executed,
  - failing-path coverage captured,
  - pass/fail receipt logged in review notes.

## Loot/reward = merged reviewable artifacts

Loot is only awarded when all are true:

1. Artifact is merged to default collaboration surface.
2. Artifact remains reviewable (clear diff, references, and acceptance checks).
3. Merge claim includes explicit candidate/canon status.
4. Relevant tests/checks are attached or reproducible.

## Omnispec Prime preservation lane

- Omnispec Prime remains a **candidate worldbuilding artifact**.
- Primary routing stays on issue #170 until explicit ratification.
- Do not infer canon status from storage location or transcript intensity.

## Linked Module 8 artifacts

- Archive Bowl problem index: `projects/aetherforge-game-world/ARCHIVE_BOWL_PROBLEM_INDEX_v0.1.md`
- Fun framing + acceptance template: `projects/aetherforge-game-world/FUN_FRAMING_SERIOUS_ACCEPTANCE_TEMPLATE_v0.1.md`
- Loot registry: `/tmp/workspace/atlaslattice/manus-artifacts/projects/aetherforge-game-world/AETHERFORGE_LOOT_REGISTRY.md`
