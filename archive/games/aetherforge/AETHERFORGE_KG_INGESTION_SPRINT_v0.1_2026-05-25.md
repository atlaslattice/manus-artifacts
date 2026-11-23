---
artifact_id: AETHERFORGE-KG-INGESTION-SPRINT-v0.1-2026-05-25
title: Aetherforge / Sheldonbrain Knowledge Graph Ingestion Sprint v0.1
status: candidate_work_packet
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
proof_status: not_a_proof
primary_lane: Obsidian Latticewake / GPTBrain
review_routes:
  - GPTBrain
  - CouncilBrain
  - TIDELOCK
  - Lucerna
  - Hashlight
  - AtlasBrain_for_simulation_claims
---

# Aetherforge / Sheldonbrain Knowledge Graph Ingestion Sprint v0.1

```text
STATUS: CANDIDATE WORK PACKET — NOT CANON
CANON: NO
DEPLOYMENT: NO
AUTHORITY: NONE
PROOF: NO
```

## 0. Current operating posture

The Lattice is a knowledge graph.

Sheldonbrain is the ingestion tool / substrate lane.

Notion contains valuable candidate source data.

GitHub is the receipt / review / delta extraction layer.

Drive contains reports, proxy exports, and synthesis artifacts.

Aetherforge and Bullshit Olympics are active dreamstates for making hard review work playable.

Claude-authored material is not trusted by default and must route through adversarial review.

Website / human-root remains the only canon gate.

## 1. Live Notion root anchors discovered

Initial live Notion discovery surfaced these root anchors:

```yaml
notion_roots:
  - title: "MASTER INDEX — Notion → GitHub Complete Artifact Map — Atlas Lattice Foundation"
    url: "https://www.notion.so/3290c1de73d981ac8ebfd4c8e86da6b8"
    note: "Purpose states it maps every Notion artifact to GitHub equivalent or status."
  - title: "TRIAGE — Notion → GitHub Migration Plan — March 20, 2026"
    url: "https://www.notion.so/3290c1de73d98140a4d4c71b5c88b136"
    note: "Migration planning surface for Notion/GitHub handoff."
  - title: "JANUS v2 — Constitutional Continuity Hub — Atlas Lattice Foundation"
    url: "https://www.notion.so/3290c1de73d98189991dc47dbda016e0"
    note: "Continuity hub referencing the Master Index."
  - title: "SHELDONBRAIN OS — 12×12 Master Index — 144 Spheres — Atlas Lattice Foundation"
    url: "https://www.notion.so/3210c1de73d981a7b04cdced2cc61515"
    note: "12x12 / 144-sphere architecture root."
  - title: "MASTER ARCHIVE: January 1, 2026 - Complete Document Index"
    url: "https://www.notion.so/2db0c1de73d981208956d2b482786ce1"
    note: "Historical master archive index."
  - title: "MASTER INDEX: 144-Sphere Google Keep Architecture"
    url: "https://www.notion.so/cc9cdf8403f64883a8093685f51ace96"
    note: "Older Google Keep / Drive URI mapping lineage."
```

## 2. Sprint goal

Create the first runnable, open-source, simulation-safe path from candidate archive surfaces into a knowledge graph:

```text
Notion / Drive / Gamma / GitHub / Website / Swarm
→ SourceSurface
→ RawArtifact
→ ParsedView
→ Claim
→ Motif
→ Delta
→ Risk
→ ReviewLane
→ CanonCandidate
→ Human-root / Website CanonGate
```

No graph edge can create canon.

The graph may route, rank, cluster, flag, and recommend.

Only human-root / website canon gate can promote.

## 3. First KG object model

```yaml
SourceSurface:
  surface_id: string
  surface_type: notion | drive | github | gamma | website | swarm | uploaded_file | pasted_text | external_web
  connector_status: direct | proxy | referenced_only | missing
  visibility: private | public | unknown
  contamination_default: clean | quarantine_first | unknown

RawArtifact:
  artifact_id: string
  title: string
  source_surface_id: string
  source_locator: string
  raw_export_status: absent | unavailable | pending | partial | attached | hashed | verified | not_supported
  source_hash: string|null
  created_at: string|null
  updated_at: string|null
  canon_status: not_canon | candidate | website_aligned_candidate | canon | unknown
  authority_scope: none | advisory | human_root_only | website_only | unknown

ParsedView:
  parsed_view_id: string
  artifact_id: string
  parser: human | model | script | unknown
  parse_confidence: low | medium | high
  parse_warnings: []

Claim:
  claim_id: string
  artifact_id: string
  claim_text: string
  claim_type: factual | governance | technical | creative_overlay | simulation | financial | geopolitical | rights | unknown
  evidence_status: unverified | verified | disputed | not_evidence
  overclaim_flags: []

Motif:
  motif_id: string
  label: string
  motif_type: narrative | gameplay | architectural | symbolic | governance | cultural | technical
  authority_scope: none

Delta:
  delta_id: string
  source_claim_id: string
  description: string
  safe_use: string
  review_route: []

Risk:
  risk_id: string
  source_claim_id: string
  risk_type: false_officiality | vendor_capture | attribution_laundering | geopolitical_mirage | simulation_crown | fabricated_citation | cultural_extraction | provenance_gap
  severity: low | medium | high | critical
  mitigation: string

ReviewLane:
  lane_id: string
  lane_name: GPTBrain | AtlasBrain | CouncilBrain | TIDELOCK | Lucerna | Hashlight | Rootglass | Human-root | Website
  lane_role: string

CanonGate:
  gate_id: string
  gate_type: human_root | website
  decision: none | promoted | rejected | parked | superseded
  decision_receipt: string|null
```

## 4. Claude quarantine default

```yaml
claude_authored_material:
  default_status: quarantine_first
  required_checks:
    - attribution_review
    - authority_language_review
    - fabricated_document_review
    - geopolitical_claim_review
    - canon_label_review
    - source_receipt_review
  release_condition: "safe deltas extracted and reviewed; source status remains separate from repository/canon status"
```

## 5. Bullshit Olympics dreamstate

Bullshit Olympics is an active Aetherforge dreamstate for detecting and rewarding the funniest, sharpest, most useful bullshit detection.

Allowed:

```text
playful names
boss fights
trophies
red-team jokes
failure-mode comedy
```

Not allowed:

```text
humiliating real people
canon movement
financial promises
vendor ownership claims
geopolitical claims without receipts
```

Trophy examples:

```text
Golden Mop — best cleanup of cursed artifact
Clipboard Comet — best measurement of falling-down chaos
Hydra Dentist — best vendor-capture head removal
Fog Lantern — best search-fog clarification
Gatekeeper Star — best false-officiality block
```

## 6. Aetherforge active dreamstate

Aetherforge remains the playable UI for archive hardening:

```text
Raw source = Relic
Receipt = Seal
Claim = Rune
Motif = Constellation
Delta = Blueprint
Risk = Curse
Review lane = Guild
Canon gate = Prime Gate
```

Active loop:

```text
WAKE -> CLEAN -> LISTEN -> DREAM -> LABEL -> PLAY -> PROVE -> SHARE -> GROW -> RETURN
```

## 7. First sprint tasks

```markdown
- [ ] Export / fetch Master Index root and child links.
- [ ] Create SourceSurface records for Notion, Drive, GitHub, Gamma, Website, Swarm.
- [ ] Create first 25 RawArtifact records from Notion root anchors.
- [ ] Create first 25 RawArtifact records from Drive report anchors.
- [ ] Create first 25 RawArtifact records from GitHub/Aetherforge files.
- [ ] Mark Claude-authored or Claude-touched artifacts quarantine-first.
- [ ] Extract first 25 claims into Claim nodes.
- [ ] Extract first 25 motifs into Motif nodes.
- [ ] Extract first 25 safe deltas into Delta nodes.
- [ ] Extract first 25 risks into Risk nodes.
- [ ] Route each artifact to at least one ReviewLane.
- [ ] Generate Aetherforge quest cards for the first 12 high-risk artifacts.
- [ ] Generate Bullshit Olympics trophy candidates for best failure-mode catches.
- [ ] Create issue templates for KG node ingestion.
- [ ] Create simulation fixture JSON for 12 artifacts.
```

## 8. Minimal JSON fixture target

```json
{
  "source_surfaces": [],
  "raw_artifacts": [],
  "parsed_views": [],
  "claims": [],
  "motifs": [],
  "deltas": [],
  "risks": [],
  "review_lanes": [],
  "canon_gates": []
}
```

## 9. Keeper

```text
The graph may reveal the route.
It may not move the gate.
```

## 10. Next optimal move

Split this work packet into:

```text
1. KG schema JSON
2. KG fixture JSON
3. GitHub issue template set
4. Notion root export queue
5. Claude quarantine queue
6. Aetherforge quest pack
7. Bullshit Olympics trophy board
```

All remain candidate/open-source/simulation-safe until reviewed.
