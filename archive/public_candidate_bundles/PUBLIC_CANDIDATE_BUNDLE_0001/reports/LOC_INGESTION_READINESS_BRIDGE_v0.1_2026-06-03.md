# LOC Ingestion Readiness Bridge v0.1 — 2026-06-03

```yaml
artifact_id: LOC_INGESTION_READINESS_BRIDGE_v0_1_2026_06_03
status: candidate_readiness_bridge
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
proof_status: not_a_proof
goal: best_in_world_for_openai_operability
institutional_target: Library_of_Congress_compatible_ingestion_discipline
```

## Purpose

Prepare PUBLIC_CANDIDATE_BUNDLE_0001 for a future institutional-archive ingestion pathway inspired by Library of Congress preservation and metadata practices.

This does **not** claim Library of Congress partnership, acceptance, endorsement, ingest eligibility, or submission readiness.

It defines a readiness bridge: how to make the bundle cleaner, more preservable, more interoperable, and easier for a public institution or external librarian to evaluate.

## Why LOC-style ingestion is plausible later

Bundle 0001 is already developing the primitives institutions care about:

```yaml
existing_primitives:
  - source paths
  - mirror index
  - SHA / fixity crosswalk
  - validation checklist
  - public/non-public/release boundary doctrine
  - missing receipt reporting
  - overclaim reporting
  - provenance and review lanes
  - external reviewer path
  - candidate/not-canon status discipline
```

LOC-style readiness means strengthening these into boring, exportable, standards-aware packages.

## LOC-facing concepts to align with

```yaml
loc_alignment_targets:
  recommended_formats:
    local_mapping: record preferred/acceptable file format status where possible
    bundle_need: add format class, MIME type, extension, and preservation preference fields
  sustainability_factors:
    local_mapping: disclosure, adoption, transparency, self-documentation, dependencies, patents, technical protection
    bundle_need: add sustainability review fields per file or artifact class
  metadata_standards:
    local_mapping: MODS / Dublin Core / BIBFRAME-adjacent crosswalks as future export targets
    bundle_need: create minimal Dublin Core and MODS candidate crosswalks for each artifact
  structured_api_interop:
    local_mapping: JSON/YAML machine-readable bundle records
    bundle_need: make mirror_index.yaml and sha_crosswalk.yaml stable enough for machine ingestion
  fixity_and_provenance:
    local_mapping: SHA hashes, chain of custody, source lineage, version history
    bundle_need: add export hash, source system, timestamp, and transformation lineage fields
```

## Candidate metadata crosswalk

```yaml
artifact_to_dublin_core_candidate:
  title: artifact_title
  creator: creator_or_source_actor
  contributor: model_or_reviewer_lanes
  date: created_or_recorded_date
  description: strongest_safe_claim
  format: file_format_or_mime_type
  identifier: path_or_url_or_artifact_id
  language: language
  publisher: repository_or_archive_surface
  relation: source_inputs / derived_from / supersedes
  rights: rights_status / license_status
  source: source_surface / source_url_or_path
  subject: tags / sphere / module / claim type
  type: artifact_type

artifact_to_mods_candidate:
  titleInfo: artifact_title
  name: creator_or_contributor
  typeOfResource: artifact_type
  genre: module_packet / receipt / schema / report / checklist
  originInfo: created_date / publisher_surface
  language: language
  physicalDescription: format / extent / digital_origin
  abstract: strongest_safe_claim
  note: boundary_notes / overclaims_to_avoid
  subject: tags / modules / concepts
  identifier: artifact_id / path / URL / SHA
  location: repository_path / mirror_path
  accessCondition: rights_status / privacy_status / license_status
  relatedItem: source_inputs / superseded_by / derived_from
```

## Required LOC-readiness fields

```yaml
loc_readiness_fields:
  identity:
    - artifact_id
    - title
    - artifact_type
    - version
    - date_created
    - date_recorded
  location:
    - repository
    - path
    - branch_or_ref
    - public_url
    - mirror_url
  fixity:
    - blob_sha
    - commit_sha
    - sha256_export_hash
    - hash_algorithm
    - hash_created_at
  provenance:
    - source_surface
    - source_url_or_path
    - source_actor
    - model_or_tool_actor
    - transformation_history
    - derived_from
    - supersedes
  rights_and_access:
    - privacy_status
    - rights_status
    - license_status
    - third_party_material_status
    - sensitive_terms_status
    - public_release_class
  preservation:
    - file_format
    - mime_type
    - encoding
    - preferred_or_acceptable_format_status
    - disclosure_status
    - transparency_status
    - external_dependencies
    - technical_protection_status
  review:
    - canon_status
    - deployment_status
    - authority_scope
    - proof_status
    - reviewer_lanes
    - missing_receipts
    - overclaims_to_avoid
    - strongest_safe_claim
    - next_safest_action
```

## Package structure target

```text
PUBLIC_CANDIDATE_BUNDLE_0001/
  README.md
  BUNDLE_0001_FILE_MANIFEST.yaml
  metadata/
    bundle_dc.json
    bundle_mods_candidate.xml
    artifact_metadata_records.yaml
    loc_readiness_matrix.yaml
  mirror_receipts/
    mirror_index.yaml
    sha_crosswalk.yaml
    export_hash_manifest.yaml
  docs/
    BUNDLE_0001_VALIDATION_CHECKLIST.md
    EXTERNAL_REVIEWER_CHECKLIST.md
    LOC_INGESTION_READINESS_BRIDGE_v0.1_2026-06-03.md
  reports/
    GIT_INDEX_COVERAGE_AUDIT_v0.1_2026-06-03.md
    INDEX_COVERAGE_MATRIX.yaml
  examples/
    toy_graph_demo/
```

## First 12 LOC-readiness tasks

1. Create `metadata/loc_readiness_matrix.yaml`.
2. Create `metadata/artifact_metadata_records.yaml` for top 12 Bundle 0001 files.
3. Add Dublin Core candidate fields for each top artifact.
4. Add MODS candidate fields for each top artifact.
5. Add file format / MIME type / encoding fields.
6. Add privacy / rights / license status fields.
7. Add fixity rows: blob SHA, commit SHA, export SHA-256 where available.
8. Add source/provenance rows: source surface, source path, derived-from links.
9. Add preservation factors: disclosure, transparency, self-documentation, external dependencies.
10. Add release gate: not public-release-ready until rights/privacy/license complete.
11. Add external reviewer rubric aligned to preservation metadata, not hype language.
12. Create issue for `LOC_READINESS_MATRIX_v0.1` and keep it candidate-only.

## Forbidden claims

```yaml
forbidden_claims:
  - Library_of_Congress_partner
  - LOC_ingestion_approved
  - LOC_submission_ready
  - institutional_archive_ready
  - preservation_complete
  - rights_cleared_without_review
  - metadata_standard_compliant_without_validation
```

## Strongest safe claim

PUBLIC_CANDIDATE_BUNDLE_0001 now has enough receipt, mirror, validation, and external-review structure to begin a candidate LOC-style ingestion readiness pathway. It is not LOC-approved, not submission-ready, not rights-cleared, not preservation-complete, not canon, and not deployed.

## Keeper

```text
LOC is the mountain.
Bundle 0001 is learning to pack like a climber.
Metadata is oxygen.
Fixity is rope.
Rights review is weather.
No summit claims from base camp.
```
