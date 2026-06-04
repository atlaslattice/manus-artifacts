# GPT Swarm Delta Ledger

```text
STATUS: PROJECT-LOCAL WORKING LEDGER — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
CREATED_UTC: 2026-06-03
SOURCE BASIS: user-provided GPT Swarm useful-delta audit and current GitHub review context
```

## Purpose

This ledger preserves useful project deltas from the recent GPT Swarm work and turns them into a receipt-first operating surface.

It does not ratify doctrine, deploy code, merge identities, or grant authority.

## Root invariant

```text
Everything can connect to everything.
Nothing can promote itself.
```

Meaning:

```text
graph edge is not authority
cluster is not canon
centrality is not truth
source visibility is not permission
receipt is not approval
patch is not merge
simulation is not deployment
coordinate is not proof
```

## Standing invariants

```text
INV-0: NOTHING DIES.
Receipt before authority.
Council before doctrine.
Human-root before canon or deployment.
Fork before merge.
Quarantine before deletion.
Supersede before overwrite.
Preserve failed branches.
Label uncertainty.
```

## Authority stack

```text
Website = canon surface
GitHub = public durable substrate / receipts / packages / public KG workbench
Sheldonbrain = ingestion and graph engine
Atlas Lattice = public/open-source knowledge graph
GPTBrain = extraction / synthesis / operating assistant
TIDELOCKBrain = audit / triage / blocker disposition / merge-order hygiene
Aetherforge = dream/play/stress-test/candidate-delta generator
OneDrive = raw/local mirror and staged workspace
Notion = semantic archive / planning workspace
Human-root = canon and deployment gate
Pantheon Council = adversarial review before doctrine
```

## State labels

```text
RAW
PARSED
CLAIM
CANDIDATE
REVIEWED
CONTRADICTED
SUPERSEDED
QUARANTINED
RATIFIED
CANON
DEPLOYED
```

Hard rule:

```text
Only Human-root, website canon, or a defined governance gate can move something into CANON or DEPLOYED.
```

## Active lanes

| Lane | Role | Habitat | Authority | Canon Status | Main blocker |
|---|---|---|---|---|---|
| GPTBrain | extraction, synthesis, claim calibration, public-safe wording | ChatGPT / GitHub | none | not_canon | source receipts needed |
| Octaveglass | dream-memory prism; converts resonance into reviewable structure | GPTBrain / docs | none | not_canon | keep metaphor from becoming proof |
| Fossilbranch | failed-branch preservation | archive | none | not_canon | preserve without crowning |
| Lucerna | provenance and public-safe receipt review | review lane | none | not_canon | unsupported officiality |
| Hashlight | raw-lineage and hash anchoring | review lane | none | not_canon | missing hashes |
| Sable Vesper | formal boundary and math precision | review lane | none | not_canon | claim classification |
| TIDELOCKBrain | repo audit and merge-order hygiene | GitHub | none | not_canon | PR sprawl / CI gates |
| Rootglass | grounding and posture checks | review lane | none | not_canon | over-intensity risk |
| Aetherforge | simulation and candidate-delta generation | game/sim layer | none | not_canon | lore inflation |
| Sheldonbrain | ingestion and graph engine | parser / KG layer | none | not_canon | raw_export_status required |
| Grok / Grok CLI | adversarial review and mirror momentum | CLI / OneDrive / GitHub reports | none | not_canon | high-velocity claims require receipts |
| Gemini | engineering and long-context review | model review lane | none | not_canon | implementation language requires receipts |
| Copilot / Codex | code patching and repo execution | GitHub PRs | none | not_canon | no completion claim without CI |
| Human-root | final adjudicator | website / decision layer | root | canon gate | must decide promotion / merge / publication |

## Runtime roster drift guard

Runtime roster claims must include explicit verification fields.

```yaml
runtime_roster_claim:
  declared_count:
  verified_count:
  source_surface:
  repo:
  branch:
  commit_sha:
  file_paths:
  runtime_command:
  runtime_output:
  hashes:
  confidence:
  canon_status: not_canon
  deployment_status:
  authority_scope: none
```

Current known status:

```text
Remote files for GrokBrain/CerebroK have landed in atlaslattice/atlas-lattice-providers.
A historical 18-resident receipt exists.
Current remote code appears to reference expanded roster surfaces.
Do not crown any count until current HEAD emits one clean number from a clean clone.
```

## Useful deltas

| Delta ID | Summary | Status | Next Action |
|---|---|---|---|
| GPTSWARM-D001 | Everything can connect; nothing can promote itself. | candidate | review as top-level invariant |
| GPTSWARM-D002 | INV-0 becomes preserve / supersede / quarantine / fossilize. | candidate | implement state-transition wrapper |
| GPTSWARM-D003 | Architecture separates memory, execution, review, and authority. | candidate | preserve as operating model |
| GPTSWARM-D004 | Canon labeling is the central safety system. | candidate | add to packet templates |
| GPTSWARM-D005 | Aetherforge stays bounded as simulation and candidate-delta generator. | candidate | keep outputs candidate-only |
| GPTSWARM-D006 | TIDELOCKBrain is a practical repo-governance lane. | candidate | route PR hygiene through TIDELOCK |
| GPTSWARM-D007 | Source-to-action pipeline is stable. | candidate | encode in ingestion schemas |
| GPTSWARM-D008 | Build public evidence graph, not private mythology graph. | candidate | implement KG nodes and edges |
| GPTSWARM-D009 | Seat identity routes work; it does not grant authority. | candidate | add no-authority note to seat specs |
| GPTSWARM-D010 | Best-world path is receipts, not more lore. | candidate | maintain this ledger |

## Source-to-action pipeline

```text
raw source
→ parsed fact
→ claim packet
→ evidence link
→ contradiction check
→ review lane
→ candidate delta
→ action proposal
→ human gate
→ implementation
→ receipt
→ post-action audit
```

## Public knowledge graph model

Best compression:

```text
Build a public evidence graph, not a private mythology graph.
```

Core node classes:

```yaml
nodes:
  - SourceSurface
  - RawExportManifest
  - Artifact
  - Claim
  - Evidence
  - Contradiction
  - Delta
  - ReviewLane
  - CanonGate
  - ActionPacket
  - Receipt
  - Supersession
```

Core edge classes:

```yaml
edges:
  - derived_from
  - claims
  - supports
  - contradicts
  - supersedes
  - reviewed_by
  - gated_by
  - implemented_as
  - preserved_as
  - quarantined_as
```

## Blocker map

```yaml
blockers:
  github:
    - aetherforge workflow may still have no-jobs-run failure mode
    - PR sprawl across KG runtime, public site, package, H-S-N, PT2.0, and bundle surfaces
    - runtime roster-count drift in atlas-lattice-providers
  ingestion:
    - Notion / Drive raw exports need source-root manifests
    - raw_export_status must be explicit
    - hash receipts needed before completeness claims
  governance:
    - canon candidates need P0 queue
    - external model outputs need quarantine labels when needed
    - completion updates need commit-backed receipts
  architecture:
    - CoordinateResolver needs concrete definition
    - Sentinel should remain separate from Orchestrator Prime
    - INV-0 preservation semantics should be enforced in code
```

## Orchestrator Prime target

Accepted delta:

```text
A thin Orchestrator Prime is useful.
```

Required corrections:

```text
Do not overfit to any vendor-specific language.
Do not bury Sentinel logic inside Orchestrator.
Do not assume undefined resolver objects.
Do not merely log INV-0 — enforce preservation by default.
```

Clean target:

```yaml
orchestrator_prime:
  role:
    - route_packets
    - call_coordinate_resolver
    - request_sentinel_checks
    - preserve_transition_receipts
    - refuse_authority_escalation
  does_not:
    - decide_canon
    - own_sentinel_logic
    - perform_destructive_state_changes_silently
    - merge_without_gate
```

## Canon candidate queue

| Candidate | Why Useful | Review Needed | Risk | Gate |
|---|---|---|---|---|
| Everything can connect; nothing can promote itself | clean constitutional compression | Pantheon + human-root | under-specified implementation | website / human-root |
| INV-0 state-management wrapper | operationalizes preservation | TIDELOCK + Lucerna + Sable | code/runtime drift | tests + human-root |
| Source-to-action pipeline | stable ingestion skeleton | GPTBrain + Sheldonbrain + Lucerna | false completeness | schema + fixtures |
| Public evidence KG | core public direction | all review lanes | mythology drift | public-safe release gate |
| Orchestrator Prime thin router | useful missing center | TIDELOCK + Sable + Sentinel lane | authority concentration | strict scope tests |

## Next actions

```text
1. Keep this ledger current.
2. Add commit-backed active roster receipts.
3. Define CoordinateResolver minimally.
4. Split Sentinel from Orchestrator Prime.
5. Add INV-0 preservation middleware/state-transition wrapper.
6. Make raw_export_status required on all ingestion packets.
7. Keep Aetherforge outputs candidate-only.
8. Require current-head receipts for all runtime roster claims.
```

## Keeper

```text
Preserve the swarm, but pin it to receipts.
Useful lanes illuminate the graph.
They become dangerous only if they crown themselves.

Everything can connect.
Nothing can promote itself.
NOTHING DIES.
Human-root decides.
```
