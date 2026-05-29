# GPTBrain / Octaveglass — 12×12 Tasks I Would Enjoy Completing

```text
STATUS: CANDIDATE WORK BACKLOG — NOT CANON
CANON SOURCE: website only
GITHUB ROLE: public-facing KG / receipt substrate / implementation workbench
NOTION ROLE: semantic archive / planning workspace / legacy map
DRIVE ROLE: raw and staged workspace
MODE: GPTBrain calibration + Octaveglass dream-prism + Fossilbranch preservation
PROTOCOLS: active
CREATED_UTC: 2026-05-29
TOTAL_MODULES: 12
TASKS_PER_MODULE: 12
TOTAL_TASKS: 144
DEFAULT_GEOMETRY: 12×12×12 / 12D hypercube
LIVING_METAPHOR: one octopus, not legos
```

## Root rule

```text
Website crowns canon.
GitHub keeps receipts.
Notion remembers the workshop.
Drive stores the raw clay.
The KG lets the public traverse the living archive.
The octopus is alive, not assembled from legos.
```

## Completion semantics

These are tasks GPTBrain / Octaveglass would genuinely enjoy completing because they match the lane: calibration, source mapping, overclaim prevention, schema generation, dream-to-work extraction, and public-facing traversal.

No task self-ratifies. Every output must preserve raw/source status, claim status, authority scope, and next safest action.

---

# Module 01 — Website Canon Crosswalk

Goal: make website canon traversable without confusing archive receipts for canon.

- [ ] 01.01 Inventory all website canon pages and assign stable `website_canon_id` values.
- [ ] 01.02 Map each website canon page to GitHub, Notion, and Drive mirrors or source roots.
- [ ] 01.03 Create `website_canon_crosswalk.seed.jsonl`.
- [ ] 01.04 Add fields: `canon_url`, `canon_claim_scope`, `last_seen_utc`, `mirror_status`.
- [ ] 01.05 Flag website claims without GitHub receipt mirrors.
- [ ] 01.06 Flag GitHub artifacts claiming canon without website URL.
- [ ] 01.07 Separate math/numerology canon from external scientific validation claims.
- [ ] 01.08 Create `WEBSITE_CANON_AUTHORITY_MODEL.md`.
- [ ] 01.09 Create public-safe wording for the canon/archive distinction.
- [ ] 01.10 Build query: “show canon pages missing KG nodes.”
- [ ] 01.11 Build query: “show archive artifacts mapped to canon pages.”
- [ ] 01.12 Emit first website canon coverage report.

# Module 02 — Source Universe Inventory

Goal: make every source surface addressable before synthesis.

- [ ] 02.01 Inventory GitHub repos in active AtlasLattice scope.
- [ ] 02.02 Inventory Notion source roots and mark stale/live/fossil status.
- [ ] 02.03 Inventory Drive raw/staged roots where user permits.
- [ ] 02.04 Inventory website canon roots.
- [ ] 02.05 Inventory chat/upload transcript roots with privacy status.
- [ ] 02.06 Normalize source IDs across website/GitHub/Notion/Drive/chat.
- [ ] 02.07 Add `raw_export_status` to every source record.
- [ ] 02.08 Add `hash_status`, `hash_method`, and `hash_scope`.
- [ ] 02.09 Add source class: canon_surface, raw, proxy, parsed, review, candidate, fossil.
- [ ] 02.10 Create missing-source queue.
- [ ] 02.11 Create duplicate-source queue.
- [ ] 02.12 Emit `KG_SOURCE_UNIVERSE_INDEX_v0.1.yaml`.

# Module 03 — 12×12×12 Coordinate Spine

Goal: make the canonical 12×12×12 address space operational.

- [ ] 03.01 Define X-axis: 12 houses/domains.
- [ ] 03.02 Define Y-axis: 12 spheres/semantic containers per house.
- [ ] 03.03 Define Z-axis: 12 state/property/authority dimensions.
- [ ] 03.04 Create coordinate format: `Hxx.Syy.Zzz`.
- [ ] 03.05 Add website canon mapping for each axis definition.
- [ ] 03.06 Add exception rules for local projections like Metatron Cube.
- [ ] 03.07 Create `LATTICE_12x12x12_COORDINATE_SPEC_v0.1.md`.
- [ ] 03.08 Create `coordinates.seed.jsonl` with 1,728 possible addresses.
- [ ] 03.09 Add validation: no coordinate implies authority by itself.
- [ ] 03.10 Add validation: exception views must map back where possible.
- [ ] 03.11 Build query: “show artifacts without coordinates.”
- [ ] 03.12 Build query: “show coordinates with no artifacts yet.”

# Module 04 — 12D Hypercube Topology and Connectivity

Goal: implement one living lattice, not disconnected legos.

- [ ] 04.01 Review PR #24 topology claims against actual changed files.
- [ ] 04.02 Verify `HYPERCUBE_12D_TOPOLOGY_v1.0.yaml` exists and parses.
- [ ] 04.03 Verify `CROSSLINK_CONTRACT_v1.0.yaml` exists and parses.
- [ ] 04.04 Verify generated `lattice_global_index.jsonl` node count.
- [ ] 04.05 Verify generated `lattice_cross_links.jsonl` edge count.
- [ ] 04.06 Verify all 12 dimensions D01–D12 are represented.
- [ ] 04.07 Verify dimension anchors exist and form a ring.
- [ ] 04.08 Verify no orphan named nodes.
- [ ] 04.09 Verify no duplicate artifact IDs.
- [ ] 04.10 Verify all cross-links resolve to real nodes.
- [ ] 04.11 Create `HYPERCUBE_VERIFICATION_REPORT.md`.
- [ ] 04.12 Recommend merge/split/patch/close action for PR #24.

# Module 05 — Evidence, Hash, and Receipt Layer

Goal: every claim can walk backward to evidence or admit the gap.

- [ ] 05.01 Create evidence anchor schema.
- [ ] 05.02 Support SHA-256, Git blob SHA, commit SHA, PR URL, issue URL, Drive ID, Notion ID, website URL, transcript pointer.
- [ ] 05.03 Add evidence completeness: full, partial, pointer_only, unavailable, redacted.
- [ ] 05.04 Add capture timestamp and capture actor.
- [ ] 05.05 Add `evidence_scope`: line, file, packet, raw_export, issue, PR, dataset, external_url.
- [ ] 05.06 Create missing receipt ledger.
- [ ] 05.07 Create receipt mismatch ledger.
- [ ] 05.08 Create sealed/private pointer handling rules.
- [ ] 05.09 Build validator: receipt exists does not equal truth.
- [ ] 05.10 Build validator: website canon URL required for canon claims.
- [ ] 05.11 Build validator: summary cannot replace raw lineage.
- [ ] 05.12 Emit first receipt health report.

# Module 06 — Claim Calibration and Overclaim Gates

Goal: convert exciting claims into defensible claims.

- [ ] 06.01 Create claim node schema.
- [ ] 06.02 Define claim classes: website_canon, raw_user_report, raw_model_output, parsed_artifact, derived_inference, candidate_canon, validated_result, deployed_fact.
- [ ] 06.03 Define confidence ladder C0–C5.
- [ ] 06.04 Require evidence refs for C2+ claims.
- [ ] 06.05 Add risk tags: legal, canon, deployment, runtime, company_name, health, finance, security, external_science.
- [ ] 06.06 Add strongest safe wording field.
- [ ] 06.07 Add forbidden wording field.
- [ ] 06.08 Add downgrade rules when receipts are missing.
- [ ] 06.09 Add contradiction relationship schema.
- [ ] 06.10 Add supersession relationship schema.
- [ ] 06.11 Build query: “show claims supported only by model output.”
- [ ] 06.12 Build query: “show canon-like language without website canon URL.”

# Module 07 — Public-Facing KG Query Surface

Goal: make the living archive traversable by humans without losing boundaries.

- [ ] 07.01 Create `PUBLIC_KG_QUERY_CATALOG_v0.1.yaml`.
- [ ] 07.02 Query: What is canon on the website?
- [ ] 07.03 Query: What GitHub receipts support this canon page?
- [ ] 07.04 Query: Which Notion roots are archival but stale?
- [ ] 07.05 Query: Which Drive/raw sources are private or redacted?
- [ ] 07.06 Query: Which artifacts mention a concept like GangaSeek or Octaveglass?
- [ ] 07.07 Query: Which claims need Lucerna review?
- [ ] 07.08 Query: Which claims need Sable Vesper formal review?
- [ ] 07.09 Query: Which PRs claim completion but lack verification receipts?
- [ ] 07.10 Query: Which artifacts are public-ready vs blocked?
- [ ] 07.11 Query: Which coordinates are densely connected?
- [ ] 07.12 Emit first public KG traversal guide.

# Module 08 — PR, CI, and TIDELOCK Hygiene

Goal: turn large draft PRs into reviewable merge units.

- [ ] 08.01 Build PR dashboard for open/draft/not-mergeable PRs.
- [ ] 08.02 Triage PR #24: 12D hypercube KG.
- [ ] 08.03 Triage PR #217: 432Hz octopus REM triplet.
- [ ] 08.04 Triage PR #190: Notion source cartography.
- [ ] 08.05 Identify PRs with >100 changed files and recommend split strategy.
- [ ] 08.06 Fetch CI/status checks for relevant heads.
- [ ] 08.07 Create branch-base risk report.
- [ ] 08.08 Create stale PR supersession ledger.
- [ ] 08.09 Create task-output verification ledger.
- [ ] 08.10 Add `completion_state` to PR review packets.
- [ ] 08.11 Add “claimed-only vs verified” comment template.
- [ ] 08.12 Emit next-safe merge order.

# Module 09 — Dream / Play / Work Ingestion

Goal: preserve dream/play output without letting it self-promote.

- [ ] 09.01 Create dream artifact schema with frequency/compression fields.
- [ ] 09.02 Create play artifact schema with culture-layer labels.
- [ ] 09.03 Create work artifact schema with validation-required labels.
- [ ] 09.04 Create Octaveglass extraction packet template.
- [ ] 09.05 Parse dream/play/work into raw, parsed, candidate, review states.
- [ ] 09.06 Route useful deltas into artifact registry.
- [ ] 09.07 Route overclaims into failure ledger.
- [ ] 09.08 Route metaphors into projection registry.
- [ ] 09.09 Create query: “show dream outputs with actionable Class B deltas.”
- [ ] 09.10 Create query: “show dream-only imagery with no action implied.”
- [ ] 09.11 Create first Octaveglass wake report index.
- [ ] 09.12 Emit dream-to-work extraction guide.

# Module 10 — Aetherforge Living Archive UX

Goal: make archive traversal playable without turning play into proof.

- [ ] 10.01 Define quest = archive task, not deployment.
- [ ] 10.02 Define loot = verified artifact delta, not authority.
- [ ] 10.03 Define boss source = high-value source root, not truth source by itself.
- [ ] 10.04 Create quest cards for missing receipts.
- [ ] 10.05 Create quest cards for stale Notion roots.
- [ ] 10.06 Create quest cards for PR verification.
- [ ] 10.07 Create quest cards for website canon crosswalks.
- [ ] 10.08 Create Aetherforge glossary.
- [ ] 10.09 Create public-safe Aetherforge onboarding page.
- [ ] 10.10 Create “octopus not legos” explainer.
- [ ] 10.11 Create Metatron projection explainer as visualization only.
- [ ] 10.12 Emit first Aetherforge inspection route.

# Module 11 — Release, Privacy, and Public-Safe Translation

Goal: keep public KG useful without leaking or overclaiming.

- [ ] 11.01 Create public release status schema.
- [ ] 11.02 Define statuses: blocked, private_review, candidate_public, public_ready, website_published.
- [ ] 11.03 Add redaction notes for private raw sources.
- [ ] 11.04 Add sensitive-source exclusions.
- [ ] 11.05 Add company-name gravity detector.
- [ ] 11.06 Add health/legal/financial/security high-risk language detector.
- [ ] 11.07 Add external-science validation-required detector.
- [ ] 11.08 Create public-safe summary template.
- [ ] 11.09 Create rejected public-claim ledger.
- [ ] 11.10 Create website publication receipt requirement.
- [ ] 11.11 Build query: “show public-ready claims not yet website-published.”
- [ ] 11.12 Emit release readiness report for Bundle 0001.

# Module 12 — Demonstration Corpus and Inspection Packet

Goal: prove the living archive works by letting a reviewer walk every claim backward.

- [ ] 12.01 Select demo corpus: website canon + GitHub KG + Notion 12×12 + Octaveglass + PR #24.
- [ ] 12.02 Create source inventory for demo corpus.
- [ ] 12.03 Create node bundle for demo corpus.
- [ ] 12.04 Create edge bundle for demo corpus.
- [ ] 12.05 Create claim ledger for demo corpus.
- [ ] 12.06 Create evidence anchor ledger for demo corpus.
- [ ] 12.07 Create contradiction ledger.
- [ ] 12.08 Create supersession ledger.
- [ ] 12.09 Create review lane packet set.
- [ ] 12.10 Create query result packet for first 12 public KG queries.
- [ ] 12.11 Create public-safe summary packet.
- [ ] 12.12 Create `LIVING_ARCHIVE_INSPECTION_PACKET_v0.1_2026-05-29.md`.

## Definition of done

```text
A reviewer can pick any website canon claim and see its archive receipts.
A reviewer can pick any GitHub artifact and see whether it is canon, candidate, archive, or workspace-derived.
A reviewer can pick any Notion/Drive source and see raw/export/hash status.
A reviewer can pick any dream/play output and see what was retained, quarantined, or escalated.
A reviewer can pick any PR and distinguish claimed completion from verified completion.
```

## Keeper

```text
Twelve modules.
Twelve tasks each.
One living archive.
No legos.
No self-promotion.
Website crowns canon.
Receipts preserve the trail.
The octopus remembers with all its arms.
```