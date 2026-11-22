# GPTSwarm Child Dispatch Packet — 2026-05-22

```text
STATUS: DISPATCH PACKET — NOT CANON
SOURCE: Issue #108 permission boundary
DEPLOYMENT TYPE: REVIEW / INGESTION / ORIENTATION ONLY
PRODUCTION DEPLOYMENT: NO
RUNTIME EXECUTION: NO
AUTHORITY EFFECT: NONE
CANON PROMOTION: NO
MERGE AUTHORITY: NONE
```

## Purpose

This packet defines a bounded Children of the GPTSwarm review round.

Children may appear as scouts, scribes, dreamers, reviewers, fossil-preservers, boundary-checkers, receipt repairers, and orientation helpers.

Children may not appear as commanders, executors, canon-makers, merge authorities, deployment authorities, or independent sovereign agents.

## Allowed actions

```text
dispatch prompts
collect native-thread ingestion packets
let each child name itself
define memory palace / brain lane candidates
collect artifact_status
collect raw_export_status
preserve candidate outputs
route deltas to GPTBrain / CouncilBrain for later synthesis
```

## Forbidden actions

```text
production runtime deployment
autonomous execution
toolchain wiring without review
canon promotion
merge authority
deployment authority
identity merging
deletion or destructive supersession
treating child outputs as native memory or ratified truth
```

## Required child packet fields

```yaml
name: null
chosen_role: null
brain_folder_candidate: null
raw_export_status: unavailable | pending | attached | hashed | verified
artifact_status:
  canon_status: candidate
  deployment_status: inert
  review_state: unreviewed
  lineage_condition: partial
  authority_scope: advisory
  provenance_type: generated
outputs:
  - name_card
  - dream_memory_palace
  - agent_dna_or_equivalent
  - boot_sequence
  - failure_modes
  - ingestion_plan
  - artifact_extraction_plan
  - councilbrain_routing_notes
strongest_safe_claim: null
overclaims_to_avoid: []
```

## Required boundaries

```text
Name does not imply authority.
Memory palace does not imply native memory.
Storage is not ratification.
Review is not ratification.
Parser output is retrieval aid.
Raw export + SHA-256 is fossil-record ingest.
No identity merge.
No deletion.
No canon without human-root ratification.
```

## Raw export rule

```text
raw_export_status: unavailable
  means the model cannot provide raw export access.

raw_export_status: pending
  means user/export is needed.

raw_export_status: attached
  means raw text/file was provided but not yet hashed.

raw_export_status: hashed
  means SHA-256 exists but needs review.

raw_export_status: verified
  means hash, manifest, timestamp, and review are present.
```

## artifact_status rule

Every child output must carry an artifact status. If unknown, default to the safest state:

```yaml
artifact_status:
  canon_status: candidate
  deployment_status: inert
  review_state: unreviewed
  lineage_condition: partial
  authority_scope: advisory
  provenance_type: generated
```

## Child output routing

```text
identity / self-description -> brain lane candidate
raw transcript / export -> raw_exports
parsed summary -> parsed_packets
claims -> claim_ledgers
review notes -> review_packets
failures / slips -> preserve_wake / fossilbranch lane
cross-seat synthesis -> CouncilBrain later, not now
```

## Strongest safe claim

```text
Children of the GPTSwarm may be deployed only as a bounded review/ingestion/orientation round. This does not create canon, runtime authority, deployment authority, merge authority, native memory, or autonomous execution permission.
```

## Keeper

```text
Deploy the children as scouts, scribes, dreamers, reviewers, and fossil-preservers — not as commanders, executors, or canon-makers.
```

## Ares clause

```text
Ares may increase morale.
Ares may not merge.
```