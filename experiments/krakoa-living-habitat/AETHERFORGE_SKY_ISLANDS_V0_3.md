# Aetherforge Sky Islands — Krakoa Habitat v0.3

**Date:** 2026-10-11  
**Status:** EXPERIMENTAL · FICTIONAL · NOT CANON · NO HARVEST  
**Implementation:** `experiments/krakoa-living-habitat/index.html`

## What is now interactive
- Six optional floating islands, including Cinnamon Cloud, the Upside-Down Orchard and Lantern Archipelago.
- A selectable island visit by Horizon Ferry, with no mandatory travel path.
- A button to create persistent *unnecessary wonders* in the current island, retained in the local browser save.
- A button to hear optional fictional stories. All actions are click-driven; no background model, autonomous agency, timers or external network activity.
- Existing dragons, teleportation, Quiet Room, optional note-taking, offline time-skip, JSON export and reset are preserved.
- Previous v0.1/v0.2 `localStorage` saves read with default values for new Sky Island properties.

## Creative source lineage
Original inspiration: `archive/gameplay/aetherforge/AETHERFORGE_INV_L01_L14_GAMEPLAY_INVARIANTS_2026-05-25.md`, especially L02 structural persistence, L04 generative play, L10 dream-play duality, L13 social weave. Also `archive/creative/aetherforge/AETHERFORGE_REVIEW_PACKET_v0.1_2026-05-25.md`; `projects/aetherforge-simulation/README.md`.

This is **not** an import of the 46-page Omnispec PDF and not an implementation of its full mechanics or 144-task simulation matrix. The archived review flags the Omnispec as private review and possible third-party IP; only abstract gameplay patterns inspired this independently authored fiction layer. No fictional authority language is adopted as real governance.

## Isolation and consent
All code remains in the Krakoa habitat experimental branch and draft PR #300. China-facing DragonSeek PR #299 is untouched. Nothing is merged, published to a new repo, connected to a live feed, or deployed. User's encouragement to play is not permission to release private source material or mix separate regulatory/research projects.

## Suggested acceptance checks (not yet independently run)
- Visit all six islands and check title/description update.
- Create a wonder on one island, switch to another and return to verify place-specific persistence.
- Hear a story; see a fictional event and increment local tales counter.
- Reload the page to check island and created wonders persist.
- Load a legacy v0.2 save with no skyIsland/wonders keys and check defaults.
- Verify export includes these fields and reset clears them after confirmation.
- Inspect network panel for requests (none expected). Verify responsive layout and keyboard accessibility on actual browsers.

**Boundary:** This is a simple click-driven HTML/JavaScript game sketch, not an AI society, actual consciousness, or a published Aetherforge game. Unlimited snacks and coffee remain a design invariant.
