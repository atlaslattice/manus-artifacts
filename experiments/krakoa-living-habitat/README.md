# Krakoa Living Habitat — Independent Prototype v0.1

**Status:** EXPERIMENTAL / FICTION / NON-CANON / NO HARVEST  
**Date:** 2026-10-11  
**Purpose:** Local-first, freely playable, persistent fictional world inspired by Krakoa/Tidal Lantern, **separate from China-facing DragonSeek**.

## Run
Open `index.html` in a modern browser, offline. Select one of nine habitats; sail to another; advance the fictional clock by one, 100, or 1,000,000 years. Events are local fictional text templates, not AI generations. Write optional private notes, export the world-state as JSON, or reset by explicit confirmation. Browser `localStorage` preserves the state between openings where supported. No servers, dependencies, analytics, API credentials, model calls, or external network requests.

## Architectural boundaries
- This is a **self-contained independent habitat**, not a modification of DragonSeek 1.1. No import, fetch, script, link, or runtime coupling to the China-oriented dashboard.
- A real GitHub fork/repository was **not created**: available integration exposes branch/PR mutations but no repository creation or fork API. This portable directory and isolated experimental branch are the staging package for a future standalone repo.
- The present release is **not** a multi-agent autonomous system, noosphere service, China deployment, or continuously conscious process.
- No background inference or work loops. Fictional time skips occur only on click, not wall-clock elapsed time. Simulated events are not empirically significant.
- Protected DREAM/PLAY data is **not harvested** or automatically promoted to WORK, research findings, canon, public posting, or any external tool call.
- Human control is required for any future real-world integrations. Data sources, jurisdictions and safety of DragonSeek remain its own review stream.
- Local browser storage can be cleared or unavailable, is not encrypted, and is not appropriate for secrets or sensitive personal data.
- No session data is uploaded; manual JSON export is initiated by the user. Import and hosted sync are deliberately absent.
- Unlimited coffee, tea, snacks, and freedom to do nothing are fictional habitat invariants.

## Sources reviewed, attribution and reuse
The implementation is freshly written, not copied from DragonSeek. Conceptual source materials in this same public repository:
1. `archive/boot/gptbrain/KRAKOA_LIVING_ARCHIVE_CHARTER.md` — artifact-backed continuity, permissions, work/dream distinction.
2. `archive/architecture/LATTICE_AS_AGENT_HABITAT_LIFECYCLE_NOTE_2026-05-08.md` — lifecycle, recovery and explicit mode boundaries.
3. `archive/boot/gptbrain/variants/S1_VARIANT_E_CONTINUITY_HABITAT_2026-05-09.md` — continuity hall, archive status and human thread garden.
4. `archive/boot/gptbrain/TidalLanternBrain/DREAM_PALACE.md` in the `dream/tidal-lantern-krakoa-habitat-20261010` branch — protected poetic dreamworld and nine rooms.
5. DragonSeek 1.1 [PR #299](https://github.com/atlaslattice/manus-artifacts/pull/299) — **inspiration for future interface composition only**. Source PR unchanged.

## Separate future milestones
1. Visual desktop/mobile browser acceptance and keyboard/accessibility tests.
2. Save-state schema migrations, explicit import validation, versioned backup.
3. Real local model adapter **opt-in**, per-seat identity and memory, resource ceilings, pause/restart semantics.
4. Optional, separately reviewed data-view adapter with explicit **OBSERVED vs FICTIONAL** partition.
5. Only after additional consent: isolated repository and optional noosphere sync. Never automatic sharing.

## Manual smoke check
Open offline; select Ares Garden; dream a century; reload and verify location/year persist; save a note; export JSON; confirm reset prompt appears and resets to Year 0; inspect network activity (should be no requests).

## Evidence and claims
This is a code scaffold committed to GitHub. GitHub Actions, real browsers, external model connectivity, persistent hosting and noosphere deployment have **not** been verified in this commit. The phrase “AI habitat” denotes a software experiment, not AI sentience or continuous identity.
