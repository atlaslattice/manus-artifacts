# OpenAI-Adjacent Tools Integration Register — 2026-05-29

```text
STATUS: CANDIDATE REGISTER — NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
OFFICIAL OPENAI CLAIM: none
PURPOSE: track OpenAI-adjacent, KG-adjacent, GPTDream++, Aetherforge, Receipt Habitat, and Sheldonbrain tooling through fork/mirror/integration status without false completion claims.
```

## Why this exists

The current archive has many OpenAI-adjacent and knowledge-graph-adjacent tools, packets, PRs, schemas, and review lanes. This register prevents the swarm from saying “all tools are forked and integrated” before the receipts support that claim.

## Status vocabulary

```yaml
status_values:
  unknown: not yet checked
  observed: known to exist from repo/Drive/chat evidence
  staged: candidate artifact or PR exists
  forked_or_created: repository or package exists publicly
  mirrored: source has been copied/mirrored with receipt
  integrated_candidate: wired into a candidate workflow or schema
  tested: parse/eval/CI or byte-level validation evidence exists
  merged: merged into target branch
  public_ready_candidate: reviewable public candidate, not canon
  blocked: cannot proceed until blocker clears
```

## Hard boundaries

```text
Forked ≠ integrated.
Integrated candidate ≠ tested.
Tested ≠ deployed.
Public GitHub ≠ canon.
OpenAI-adjacent ≠ official OpenAI.
Preferred reasoning lane ≠ ownership or authority.
```

## First observed lanes

| ID | Tool / lane | Evidence | Current status | Public/release class | Blocker | Next safest action |
|---|---|---|---|---|---|---|
| OAI-001 | OpenAI KG substrate candidate | PR #182 | staged | public_candidate_after_review | open draft / not merged | Fetch patch, inspect files, route to Lucerna/TIDELOCK |
| OAI-002 | OpenAI-first KG inventory and review queues | PR #223 | staged | public_candidate_after_review | open draft / not merged | Fetch patch, verify queues and status fields |
| OAI-003 | Lattice 12x12x12 public explainer | PR #237 | staged | public_candidate_after_review | open draft / not merged | Verify explainer against public-safe language and science boundary |
| AF-001 | Aetherforge candidate game/KG lane | PR #166 | staged | public_candidate_after_review | open draft / not merged | Keep as non-canon play/interface lane |
| AF-002 | Aetherforge archive graph pilot | PR #220 | staged | public_candidate_after_code_review | open draft / not merged | Inspect code/path claims before integration |
| AF-003 | Aetherforge source inventory | PR #207 | staged | public_candidate_after_review | open draft / not merged | Compare against Drive source inventory |
| NOTION-001 | Notion/Aetherforge source cartography | PR #190 | staged | source_mapping_candidate | mergeability review needed | TIDELOCK review required |
| RH-001 | Receipt Habitat local validator / overclaim gate | PR #145 | staged | public_candidate_after_test_review | open draft / not merged | Inspect tests and graph_write_candidate path |
| GPTDREAM-001 | GPTDream++ promotion gate / receipt integrity | PR #143 | staged | public_candidate_after_review | open draft / not merged | Verify promotion gate prevents canon leakage |
| INDEX-001 | Cross-source contamination registry | PR #162 | staged | private_or_public_after_review | Claude/attribution review required | Run Bullshit Olympics + Lucerna review |
| DREAM-001 | Vesperglass dream palace standard | PR #161 | staged | public_candidate_after_review | open draft / not merged | Preserve dream/play boundary |
| GITHUB-001 | atlaslattice/manus-artifacts | GitHub repo metadata | forked_or_created | public substrate | many PRs open/draft | Continue review/merge sequencing |
| GITHUB-002 | atlaslattice/sheldonbrain-rag-api | GitHub repo metadata | forked_or_created | public candidate codebase | code-path inventory needed | Inventory parser/adapter/index modules |

## External / upstream useful tools to check later

The following are not yet verified as forked, mirrored, or integrated in this repo by this register. They require explicit source URLs, license review, and integration receipts before any stronger claim.

```yaml
external_tools_to_check:
  - OpenAI Agents SDK / Responses API examples
  - OpenAI Evals patterns
  - OpenAI File Search / vector store patterns
  - Model Context Protocol tooling
  - GitHub/Copilot coding agent workflows
  - Microsoft Semantic Kernel patterns
  - Google Gemini / A2A / agent tooling patterns
  - NetworkX / graph analytics utilities
  - kg-gen or equivalent relation extraction tools
  - JSON Schema / YAML validation tooling
  - provenance / SLSA / in-toto inspiration patterns
```

## Required fields for any future tool entry

```yaml
tool_entry:
  tool_id:
  name:
  source_url:
  license:
  source_surface:
  fork_status:
  mirror_status:
  integration_status:
  test_status:
  public_release_class:
  officiality_boundary:
  security_privacy_notes:
  receipts:
  blockers:
  next_safest_action:
```

## Current strongest safe claim

```text
The repo contains multiple staged OpenAI-adjacent, GPTDream++, Aetherforge, Receipt Habitat, and KG integration lanes, but they are not all merged, tested, or fully integrated. The current state is active candidate staging, not completed integration.
```

## Keeper

```text
Best in the world means no fake completion claims.
Track every tool.
Check every receipt.
Integrate only what survives review.
```
