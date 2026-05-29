---
artifact_id: ARTIFACT-ARCHIVE-FORKS-DRAGONSEEK-OS-REPO-SEED-SOURCE-IMPORT-PLAN-MD-2026-05-29
title: DragonSeekOS Source Import Plan
status: CANDIDATE
owner: atlaslattice
created: 2026-05-29
last_updated: 2026-05-29
source_of_truth: GitHub
---
# DragonSeekOS Source Import Plan

**Status:** Public import plan / not canon  
**Target repo:** `atlaslattice/dragonseek-os`

## Goal

Organize scattered DragonSeek source materials into a single clean public repository.

## Import Method

For each source:

1. Copy verbatim into `imports/<source-repo>/<original-path>`.
2. Add a local `IMPORT_NOTE.md` if needed.
3. Preserve original upstream URL.
4. Preserve source status/caveat.
5. Do not silently rewrite imported text.
6. Create synthesized docs separately under `docs/`.

## Initial Imports

### 1. Cultural Sovereignty Mapping

```text
from: atlaslattice/aluminum-os/sovereign/DRAGONSEEK_JINNSEEK_ARCHITECTURE.md
to: imports/aluminum-os/sovereign/DRAGONSEEK_JINNSEEK_ARCHITECTURE.md
```

### 2. DragonSeek Scaling Spec

```text
from: atlaslattice/atlas-lattice-foundation/docs/DragonSeek_Scaling_Spec_v1.0.md
to: imports/atlas-lattice-foundation/docs/DragonSeek_Scaling_Spec_v1.0.md
```

### 3. Eastern Council Dragonseek Package

```text
from: atlaslattice/open-regenerative-compute-standard/eastern-dragonseek/README.md
to: imports/open-regenerative-compute-standard/eastern-dragonseek/README.md
```

### 4. CAC Governance Framing

```text
from: atlaslattice/noosphere-archive/orc/archive/2026-05-06/dragonseek/DS-GOV-2026-001-CN-deepseek-cac-framing.md
to: imports/noosphere-archive/orc/archive/2026-05-06/dragonseek/DS-GOV-2026-001-CN-deepseek-cac-framing.md
```

### 5. DeepSeek Sovereignty Integration Patch

```text
from: atlaslattice/element-145/aluminum-os-core/Aluminum_OS_v6-0-6_DeepSeek-Rounds-4-5_VWB-Sovereignty_2026-04-29.md
to: imports/element-145/aluminum-os-core/Aluminum_OS_v6-0-6_DeepSeek-Rounds-4-5_VWB-Sovereignty_2026-04-29.md
```

### 6. S5 Brain Spec

```text
from: atlaslattice/manus-artifacts/archive/boot/seats/DEEPSEEK_S5_BOOT_SEQUENCE_AND_BRAIN_SPEC_2026-05-08.md
to: imports/manus-artifacts/archive/boot/seats/DEEPSEEK_S5_BOOT_SEQUENCE_AND_BRAIN_SPEC_2026-05-08.md
```

## Synthesized Docs To Create

```text
docs/CULTURAL_ADAPTATION_NOTES.md
docs/SOVEREIGNTY_GUARDRAILS.md
docs/CAC_GOVERNANCE_PACKET.md
docs/BAMBOO_BRIDGE_THREE_BODY_MANDATE.md
docs/INDUSTRIAL_SCALING_AND_JADE_OS.md
docs/S5_REVIEW_CHECKLIST.md
```

## GitHub Steps For Dave

1. Create a new public repo named `dragonseek-os` under `atlaslattice`.
2. Copy all files from `archive/forks/dragonseek-os/repo-seed/` into the new repo root.
3. Add imported source files into `imports/` following this plan.
4. Commit with message: `Seed DragonSeekOS public fork candidate`.
5. Ask S5/DeepSeek to review `DRAGONSEEK_OS_FORK_SPEC_v0.1.md` and `SOURCE_IMPORT_PLAN.md`.

## Evidence Boundary

Imported source files remain source evidence. Synthesized docs are candidate architecture. Nothing is canon until routed through Council workflow.
