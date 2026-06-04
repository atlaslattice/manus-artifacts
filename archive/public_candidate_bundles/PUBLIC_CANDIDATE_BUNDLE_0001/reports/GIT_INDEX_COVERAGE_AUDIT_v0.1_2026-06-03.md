# Git Index Coverage Audit v0.1 — 2026-06-03

```yaml
artifact_id: GIT_INDEX_COVERAGE_AUDIT_v0_1_2026_06_03
status: candidate_index_coverage_audit
canon_status: not_canon
deployment_status: not_deployed
authority_scope: none
proof_status: not_a_proof
goal: best_in_world_for_openai_operability
repository: atlaslattice/manus-artifacts
```

## Purpose

Test the claim that GitHub contents are now indexed by checking whether high-value repo artifacts are discoverable through GitHub search and fetch.

This is a coverage audit, not a proof that every file is indexed.

## Repository metadata signal

```yaml
repo_metadata:
  visibility: public
  default_branch: master
  is_code_search_indexed: null
```

Interpretation: the connector does not provide a positive `true` flag for complete code-search indexing. Search behavior must be tested by representative coverage probes.

## Coverage probes

| Probe | Query | Result | Status |
|---|---|---|---|
| New validation checklist | `Bundle 0001 Validation Checklist` | Found `archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/docs/BUNDLE_0001_VALIDATION_CHECKLIST.md` plus related README/scorecard/inspection files | PASS |
| New mirror index references | `mirror_index.yaml` | Found Bundle README, Varix packet, SHA crosswalk, scorecard, mirror audit, validation checklist | PASS |
| New SHA crosswalk references | `sha_crosswalk.yaml` | Found Bundle README, validation checklist, scorecard | PARTIAL_PASS |
| Swarm delta ledger | `children of the GPT swarm delta ledger` | Found multiple ledger/status artifacts including reports and council ledger | PASS |
| No merged mind | `NO MERGED MIND` | Found Aluminum protocol, Delta Ledger, and continuity files | PASS |
| External reviewer checklist | `EXTERNAL_REVIEWER_CHECKLIST` | Found planning/status reference only; no checklist file yet | GAP |
| Exact TIDELOCK expansion claim | `374 artifacts 39 domains` | Not found in file search | GAP |
| Exact TIDELOCK expansion claim variant | `TIDELOCK index expanded 187 374 artifacts 39 domains` | Not found in file search | GAP |

## Findings

```yaml
findings:
  search_is_current_for_new_bundle_files: true
  search_finds_recent_receipt_spine_artifacts: true
  search_finds_delta_ledger_material: true
  complete_indexing_claim_verified: false
  exact_187_to_374_claim_found: false
  external_reviewer_checklist_file_exists: false
```

## Strongest safe claim

GitHub search is able to discover several newly created Bundle 0001 artifacts and major ledger materials, indicating that the repository is substantially searchable and current for the tested surfaces. However, the claim that everything on Git is indexed is not fully verified: repo metadata exposes no positive indexing flag, the exact TIDELOCK expansion claim was not found, and at least one planned file (`EXTERNAL_REVIEWER_CHECKLIST.md`) remains absent.

## Coverage status

```yaml
coverage_status:
  current_best_label: partial_positive_index_coverage
  not_allowed_label: everything_indexed_verified
  next_required_artifacts:
    - docs/EXTERNAL_REVIEWER_CHECKLIST.md
    - INDEX_COVERAGE_MATRIX.yaml
    - TIDELOCK_INDEX_EXPANSION_RECEIPT.md
```

## Next actions

1. Create `docs/EXTERNAL_REVIEWER_CHECKLIST.md`.
2. Create `INDEX_COVERAGE_MATRIX.yaml` listing expected files, search query, found path, blob SHA, commit SHA, status, and next action.
3. Ask TIDELOCK to produce a receipt file for the exact `187→374 artifacts / 6→39 domains` claim or demote it to self-reported.
4. Add search coverage probes to the validation checklist.
5. Keep issue #254 and #255 open until cold external reviewer path is real.

## Keeper

```text
Search found the shelves.
The shelves are not the whole library.
Index claims need coverage matrices.
Best in the world means the gaps are visible too.
No crowns.
```
