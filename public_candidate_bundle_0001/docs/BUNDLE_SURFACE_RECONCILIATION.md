# Bundle Surface Reconciliation — PUBLIC_CANDIDATE_BUNDLE_0001

**Status:** public candidate  
**Canon:** no  
**Deployment:** no  
**Authority:** none  
**Purpose:** reconcile the live public candidate bundle with the archived/staging bundle while preserving all work and fossil lineage.

## Core rule

Do not overwrite useful history. Do not collapse variants into a single source of truth. Preserve both surfaces, crosswalk them, and promote only reviewed public-safe material.

```text
Many versions before synthesis.
Fossils before polish.
Receipts before claims.
Council before canon.
Website before law.
```

## Surfaces being reconciled

```yaml
live_surface:
  path: public_candidate_bundle_0001/
  role: active public-facing candidate projection
  canon_status: not_canon
  deployment_status: not_deployed
  authority_scope: none

archive_surface:
  path: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/
  role: fossil/staging bundle with prior receipts, manifests, docs, examples, and review packets
  canon_status: not_canon
  deployment_status: not_deployed
  authority_scope: none
```

The live surface is the current public-facing path. The archive surface is retained as lineage, staging history, and prior receipt context.

## Shared upstream lineage pointer

Both surfaces point back to the same larger source-code ontology:

```yaml
upstream_lineage:
  source_code_map: Rainbow Yin Yang Lattice
  geometry:
    - Metatron's Cube
    - 12x12x12 hypercube lattice
    - Rainbow Yin Yang
    - Riemass S-curve across the yin-yang
  role: candidate Periodic Table 2.0 / source-code ontology
  status: candidate / not canon / not proof / not deployed
```

This lineage is preserved in:

```text
public_candidate_bundle_0001/docs/LATTICE_HYPERCUBE_12x12x12.md
public_candidate_bundle_0001/docs/CANONICAL_GEOMETRY_AND_MANY_VERSION_SYNTHESIS.md
public_candidate_bundle_0001/docs/NO_SINGLE_SOURCE_OF_TRUTH.md
```

## Promotion model

Archive files may be promoted into the live surface only by crosswalk, not overwrite.

A promoted file should record:

```yaml
promotion_record:
  source_archive_path: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/<path>
  live_target_path: public_candidate_bundle_0001/<path>
  promotion_status: promoted_to_live_public_candidate
  canon_status: not_canon
  deployment_status: not_deployed
  authority_scope: none
  preserves_original: true
  supersedes: null_unless_explicitly_reviewed
  review_required: true
```

## Candidate file crosswalk

```yaml
crosswalk:
  - archive_path: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/PR_CHECKLIST.md
    live_target: public_candidate_bundle_0001/PR_CHECKLIST.md
    priority: P0
    status: candidate_for_promotion
    reason: strong merge checklist; preserves receipt/status/review discipline

  - archive_path: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/BUNDLE_0001_FILE_MANIFEST.yaml
    live_target: public_candidate_bundle_0001/BUNDLE_0001_FILE_MANIFEST.yaml
    priority: P0
    status: candidate_for_promotion
    reason: bundle manifest and blocker ledger

  - archive_path: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/docs/ARCHIVIST_TRUST_FAILURE_PROTOCOL.md
    live_target: public_candidate_bundle_0001/docs/ARCHIVIST_TRUST_FAILURE_PROTOCOL.md
    priority: P1
    status: candidate_for_promotion
    reason: archivist/model trust failure resilience

  - archive_path: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/docs/SENSITIVE_TERM_RELEASE_GATE.md
    live_target: public_candidate_bundle_0001/docs/SENSITIVE_RELEASE_GATE.md
    priority: P1
    status: candidate_for_promotion_or_merge
    reason: public-safety gate; may need harmonization with floodgate rule

  - archive_path: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/examples/toy_graph_demo/README.md
    live_target: public_candidate_bundle_0001/examples/toy_graph/README.md
    priority: P1
    status: candidate_for_promotion
    reason: onboarding demo surface

  - archive_path: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/issues/FIRST_12_PUBLIC_INSPECTION_ISSUES.md
    live_target: public_candidate_bundle_0001/issues/FIRST_12_PUBLIC_INSPECTION_ISSUES.md
    priority: P2
    status: candidate_for_promotion
    reason: first public inspection queue

  - archive_path: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/module_packets/MODULE_11_PUBLIC_GITHUB_FORKABILITY_EXCELLENCE.md
    live_target: public_candidate_bundle_0001/module_packets/MODULE_11_PUBLIC_GITHUB_FORKABILITY_EXCELLENCE.md
    priority: P2
    status: candidate_for_promotion
    reason: public GitHub forkability quality packet

  - archive_path: archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/mirror_receipts/MIRROR_AUDIT_SHELDONBRAIN_RAG_GPTBRAIN_RAINBOW_YIN_YANG_GITHUB_DRIVE_NOTION_2026-05-30.md
    live_target: public_candidate_bundle_0001/mirror_receipts/MIRROR_AUDIT_SHELDONBRAIN_RAG_GPTBRAIN_RAINBOW_YIN_YANG_GITHUB_DRIVE_NOTION_2026-05-30.md
    priority: P2
    status: candidate_for_promotion
    reason: mirror audit receipt linking GitHub, Drive, Notion, Sheldonbrain, GPTBrain, and Rainbow Yin Yang lineage
```

## Supersession policy

No file in the archive surface is deleted or treated as obsolete merely because a live version exists.

Use these labels:

```yaml
supersession_labels:
  fossil_preserved: original remains useful as lineage
  promoted_to_live: public-safe copy or adaptation exists in live surface
  harmonized: live file merged selected content while preserving prior source path
  superseded_after_review: a later file replaces it with explicit review rationale
  quarantine_only: preserved but not public-promoted due to risk
```

## Merge sequence

```text
1. Promote PR_CHECKLIST.md.
2. Promote BUNDLE_0001_FILE_MANIFEST.yaml.
3. Harmonize SENSITIVE_TERM_RELEASE_GATE.md with current floodgate rule.
4. Promote or recreate toy graph README.
5. Promote first public inspection issues.
6. Promote forkability excellence packet.
7. Promote mirror receipt only if public-safe.
8. Update START_HERE.md to point to live and archive surfaces.
```

## Redlines

Do not promote:

```text
private raw transcripts
credentials, tokens, secrets, env files
unreviewed sensitive security or financial operational material
unclear copyrighted raw dumps
unreviewed Claude-originated governance doctrine as fact
claims of canon, deployment, official endorsement, legal authority, or scientific proof
```

## Keeper

```text
The archive surface is the film room.
The live surface is the public field.
The Rainbow Yin Yang Lattice is the source-code geometry.
The Riemass S-curve preserves the curve through the yin-yang.
No work is lost.
No fossil is erased.
No candidate crowns itself.
```
