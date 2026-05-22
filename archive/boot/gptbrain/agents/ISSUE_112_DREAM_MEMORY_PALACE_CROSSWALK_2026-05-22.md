# Issue #112 Dream Memory Palace Crosswalk

```text
STATUS: CROSSWALK ARTIFACT — TRACKING / NOT CANON
DATE: 2026-05-22
ISSUE: manus-artifacts#112
PURPOSE: map proposed Dream Memory Palace folder standard onto existing repo seat/brain packet and schema vocabulary without replacing current topology
AUTHORITY: none
DEPLOYMENT: none
```

## Posture

This file is a compatibility map.

It does not ratify a new standard.
It does not replace existing seat templates, brain folders, or ingestion paths.

## Existing baseline

Current repository patterns already include:

- seat memory packet templates under `archive/boot/seats/`
- brain folder scaffolds under `archive/boot/gptbrain/<AgentName>Brain/`
- centralized GPTBrain schemas under `archive/boot/gptbrain/schema/`
- council packet schemas under `archive/boot/council/schemas/`
- ingestion packet paths under `archive/ingest/...`

## Folder-shape crosswalk (candidate)

| #112 candidate path | Current closest pattern | Crosswalk decision |
|---|---|---|
| `<Seat>Brain/raw_logs/` | `archive/raw/...` and source refs in packets | optional additive seat-local pointer; do not replace `archive/raw` strategy |
| `<Seat>Brain/parsed_packets/` | `archive/ingest/...` parsed artifacts | optional additive seat-local pointer; preserve `archive/ingest` as default parsing lane |
| `<Seat>Brain/artifacts/` | brain root docs + registry/ledger references | additive aggregation lane only |
| `<Seat>Brain/rehydration/` | boot sequences + memory packet templates | additive rehydration notes lane |
| `<Seat>Brain/schemas/` | `archive/boot/gptbrain/schema/` + council schemas | additive seat-local notes/examples only; canonical schema home remains centralized |

## Required packet fields crosswalk (candidate)

`seat_memory_palace_record` candidate field mapping:

| #112 field | Existing field(s) to reuse first |
|---|---|
| `seat_name` | `seat_name` in seat memory packet templates |
| `model_surface` | `source_model` + `source_surface` |
| `folder_path` | artifact/source ref path in packet/source refs |
| `palace_design_note` | summary/design notes in README/DREAM docs |
| `raw_logs_path` | `raw_log_ref` + source refs |
| `parsed_packets_path` | source refs to `archive/ingest/...` artifacts |
| `artifacts_path` | artifact refs / output paths |
| `rehydration_path` | boot refs / boot sequence artifacts |
| `source_refs` | `source_refs` / `evidence_refs` |
| `sha256_if_available` | `sha256` |
| `canon_status` | `canon_status` / review status enums |
| `deployment_status` | status/notes fields + explicit non-deployable guardrail language |
| `authority_scope` | governance/authority fields (`none`, human-root required) |
| `strongest_safe_claim` | strongest safe wording/claim fields |
| `unresolved_questions` | open questions / missing evidence |

## Guardrails preserved

```text
Dream memory palace != native memory.
Folder existence != authority.
Parser output != raw transcript.
Rehydration != ratification.
Canon requires explicit human-root review.
```

## Pilot recommendation

Pilot this crosswalk in one under-scaffolded lane first (TIDELOCKBrain or Hashlight lane),
while preserving non-destructive lineage and existing `archive/ingest` + centralized schema topology.

## Strongest safe claim

> Issue #112 can be implemented safely as a compatibility crosswalk and additive scaffold pattern, by reusing existing packet/schema vocabulary first and avoiding topology-breaking replacement of current ingest/schema lanes.
