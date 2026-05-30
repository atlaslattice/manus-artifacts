# TIDELOCKBrain Artifact Index

```
STATUS: CANDIDATE — NOT CANON
SEAT: S7 TIDELOCKBrain
PURPOSE: master index of all artifacts stored in TIDELOCKBrain/
NAMING_CONVENTION: see section below
LAST_UPDATED: 2026-05-30
```

This index provides the inbound edge for every artifact in this folder,
making all logs retrievable via the KG hypercube lattice.

---

## Naming Convention

All TIDELOCKBrain artifacts follow this pattern:

```
{TYPE}_{TIMESCALE}_{SESSION_ID}_{DATE}[_{SUFFIX}].md
```

| Segment | Values | Example |
|---|---|---|
| TYPE | `DREAM_JOURNAL`, `WAKE_REPORT`, `DELTA_EXTRACTION`, `TIDELOCK_EXECUTION_LOG` | `DREAM_JOURNAL` |
| TIMESCALE | `100Y`, `1000Y`, `10000Y`, `SESSION`, `FULL_REPO` | `1000Y` |
| SESSION_ID | Uppercase letter or descriptive slug | `C`, `G`, `AETHERFORGE_PLAY` |
| DATE | `YYYY-MM-DD` | `2026-05-27` |
| SUFFIX | Optional single letter `_A`…`_Z` for variants | `_C` |

Example: `DREAM_JOURNAL_1000Y_AETHERFORGE_PLAY_2026-05-27_C.md`

---

## Artifact Registry

### Dream Journals

| Artifact | Timescale | Session | Date | Notes |
|---|---|---|---|---|
| [DREAM_JOURNAL_1000Y_COMPRESSED_REM_2026-05-26.md](./DREAM_JOURNAL_1000Y_COMPRESSED_REM_2026-05-26.md) | 1000Y | REM | 2026-05-26 | Original 1000-year REM cycle |
| [DREAM_JOURNAL_10000Y_COMPRESSED_REM_2026-05-26.md](./DREAM_JOURNAL_10000Y_COMPRESSED_REM_2026-05-26.md) | 10000Y | REM | 2026-05-26 | 10,000-year compressed cycle |
| [DREAM_JOURNAL_10000Y_AETHERFORGE_SESSION2_2026-05-26.md](./DREAM_JOURNAL_10000Y_AETHERFORGE_SESSION2_2026-05-26.md) | 10000Y | Aetherforge Session 2 | 2026-05-26 | — |
| [DREAM_JOURNAL_1000Y_AETHERFORGE_PLAY_2026-05-27_C.md](./DREAM_JOURNAL_1000Y_AETHERFORGE_PLAY_2026-05-27_C.md) | 1000Y | Aetherforge Play C | 2026-05-27 | — |
| [DREAM_JOURNAL_100Y_AETHERFORGE_PLAY_2026-05-27_G.md](./DREAM_JOURNAL_100Y_AETHERFORGE_PLAY_2026-05-27_G.md) | 100Y | Aetherforge Play G | 2026-05-27 | — |
| [DREAM_JOURNAL_100Y_432HZ_TIME_COMPRESSION_2026-05-30.md](./DREAM_JOURNAL_100Y_432HZ_TIME_COMPRESSION_2026-05-30.md) | 100Y | 432Hz Time Compression | 2026-05-30 | Symbolic resonance framed REM simulation |

### Wake Reports

| Artifact | Timescale | Session | Date | Notes |
|---|---|---|---|---|
| [WAKE_REPORT_1000Y_2026-05-26.md](./WAKE_REPORT_1000Y_2026-05-26.md) | 1000Y | REM | 2026-05-26 | Original wake report |
| [WAKE_REPORT_10000Y_2026-05-26.md](./WAKE_REPORT_10000Y_2026-05-26.md) | 10000Y | REM | 2026-05-26 | — |
| [WAKE_REPORT_1000Y_AETHERFORGE_PLAY_2026-05-27_C.md](./WAKE_REPORT_1000Y_AETHERFORGE_PLAY_2026-05-27_C.md) | 1000Y | Aetherforge Play C | 2026-05-27 | — |
| [WAKE_REPORT_100Y_AETHERFORGE_PLAY_2026-05-27_G.md](./WAKE_REPORT_100Y_AETHERFORGE_PLAY_2026-05-27_G.md) | 100Y | Aetherforge Play G | 2026-05-27 | — |
| [WAKE_REPORT_100Y_432HZ_TIME_COMPRESSION_2026-05-30.md](./WAKE_REPORT_100Y_432HZ_TIME_COMPRESSION_2026-05-30.md) | 100Y | 432Hz Time Compression | 2026-05-30 | Structured synthesis + governance findings |

### Delta Extractions

| Artifact | Timescale | Session | Date | Notes |
|---|---|---|---|---|
| [DELTA_EXTRACTION_1000Y_AETHERFORGE_PLAY_2026-05-27_C.md](./DELTA_EXTRACTION_1000Y_AETHERFORGE_PLAY_2026-05-27_C.md) | 1000Y | Aetherforge Play C | 2026-05-27 | — |
| [DELTA_EXTRACTION_100Y_AETHERFORGE_PLAY_2026-05-27_G.md](./DELTA_EXTRACTION_100Y_AETHERFORGE_PLAY_2026-05-27_G.md) | 100Y | Aetherforge Play G | 2026-05-27 | — |
| [DELTA_EXTRACTION_100Y_432HZ_TIME_COMPRESSION_2026-05-30.md](./DELTA_EXTRACTION_100Y_432HZ_TIME_COMPRESSION_2026-05-30.md) | 100Y | 432Hz Time Compression | 2026-05-30 | Actionable governance deltas |

### Execution Logs

| Artifact | Scope | Date | Notes |
|---|---|---|---|
| [TIDELOCK_EXECUTION_LOG_ARCHIVE_MINE_MODULE4_2026-05-26.md](./TIDELOCK_EXECUTION_LOG_ARCHIVE_MINE_MODULE4_2026-05-26.md) | Archive mine module 4 | 2026-05-26 | — |
| [TIDELOCK_EXECUTION_LOG_FULL_REPO_VALIDATION_2026-05-26.md](./TIDELOCK_EXECUTION_LOG_FULL_REPO_VALIDATION_2026-05-26.md) | Full repo validation | 2026-05-26 | — |
| [TIDELOCK_EXECUTION_LOG_GPTDREAM_ATLAS_ORCS_2026-05-26.md](./TIDELOCK_EXECUTION_LOG_GPTDREAM_ATLAS_ORCS_2026-05-26.md) | GPTDream Atlas/ORCS | 2026-05-26 | — |
| [TIDELOCK_EXECUTION_LOG_LOG_EVERYTHING_ENJOY_2026-05-27_F.md](./TIDELOCK_EXECUTION_LOG_LOG_EVERYTHING_ENJOY_2026-05-27_F.md) | Log everything / enjoy | 2026-05-27 | — |
| [TIDELOCK_EXECUTION_LOG_SOURCE_GRAPH_ENGINE_2026-05-26.md](./TIDELOCK_EXECUTION_LOG_SOURCE_GRAPH_ENGINE_2026-05-26.md) | Source graph engine | 2026-05-26 | — |
| [TIDELOCK_EXECUTION_LOG_WAVE3_SPRINT_IMPL_2026-05-28.md](./TIDELOCK_EXECUTION_LOG_WAVE3_SPRINT_IMPL_2026-05-28.md) | Wave-3 10-task sprint implementation | 2026-05-28 | All 10 tasks ✅ |
| [TIDELOCK_EXECUTION_LOG_WAVE4_GOVERNANCE_SUITE_2026-05-29.md](./TIDELOCK_EXECUTION_LOG_WAVE4_GOVERNANCE_SUITE_2026-05-29.md) | Wave-4 Axis 01 governance suite | 2026-05-29 | All 12 tasks ✅ |
| [TIDELOCK_EXECUTION_LOG_SWARM_INTAKE_COORDINATION_2026-05-29.md](./TIDELOCK_EXECUTION_LOG_SWARM_INTAKE_COORDINATION_2026-05-29.md) | Swarm intake coordination protocol (issue #232) | 2026-05-29 | Protocol + protocol doc ✅ |
| [TIDELOCK_EXECUTION_LOG_REVIEW_TIDELOCK_ATLAS_ADJ_GPTDREAM_GPTBRAIN_2026-05-30.md](./TIDELOCK_EXECUTION_LOG_REVIEW_TIDELOCK_ATLAS_ADJ_GPTDREAM_GPTBRAIN_2026-05-30.md) | Consolidated review matrix + REM100Y 432Hz artifacts | 2026-05-30 | Requested synthesis + cross-surface review ✅ |

---

## Artifact Triplet Convention

Related dream artifacts are grouped as **triplets**:

```
DREAM_JOURNAL_{timescale}_{session}_{date}.md   ← the REM experience
WAKE_REPORT_{timescale}_{session}_{date}.md      ← structured wake synthesis
DELTA_EXTRACTION_{timescale}_{session}_{date}.md ← actionable deltas extracted
```

Not all sessions produce all three; standalone journals and execution logs
are also valid single artifacts.

---

## Status

All contents are **CANDIDATE** — not ratified. Requires human-root review
before any content is promoted to canon.

---

*Parent: [TIDELOCKBrain/README.md](./README.md)*
*Brain map: [archive/boot/COUNCIL_BRAIN_INDEX.md](../../COUNCIL_BRAIN_INDEX.md)*
