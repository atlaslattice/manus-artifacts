# Physics Ingestion Pipeline v0.1

```text
STATUS: CANDIDATE INTERFACE SPEC
CANON: NO
DEPLOYMENT: NO
DATE: 2026-10-05
INPUT CONTRACT: source_record_v0.1.json
OUTPUT CONTRACT: physics_profile_v0.1.1.json
POLICY: SOURCE_PER_FIELD_POLICY_v0.1.md
```

## Purpose

Separate retrieval, raw-source preservation, normalization, validation, and Atlas attachment so parser mistakes remain reversible.

## Interface

Conceptual Python surface:

```python
def fetch_ame(query, release="AME2020") -> list[SourceRecord]: ...
def fetch_nubase(query, release="NUBASE2020") -> list[SourceRecord]: ...
def fetch_ensdf(query, release_meta=None) -> list[SourceRecord]: ...
def fetch_nist_asd(query) -> list[SourceRecord]: ...
def fetch_primary_experiment(citation) -> list[SourceRecord]: ...

def normalize_source_record(record, policy_version="v0.1") -> list[PropertyCandidate]: ...

def validate_source_record(record, schema="source_record_v0.1.json") -> ValidationResult: ...
def validate_physics_profile(profile, schema="physics_profile_v0.1.1.json") -> ValidationResult: ...

def attach_to_hsn(coordinate_id, physics_profile) -> AtlasAttachmentCandidate: ...
```

No `fetch_*` function may directly emit canonical physics properties.

## Stages

```text
1. FETCH
   external source -> SourceRecord
2. VERIFY RAW RECEIPT
   schema + source/release identity + checksum when available
3. NORMALIZE
   SourceRecord -> PropertyCandidate
4. CONVERT
   source units -> canonical units + conversion receipt
5. CLASSIFY
   evidence_status + source_qualifier
6. VALIDATE
   against physics_profile_v0.1.1
7. CROSS-FIELD CHECK
   A=Z+N; 0<=q<=Z; electron_count=Z-q; ionization_fraction=q/Z
8. ATTACH
   validated profile -> H##.S##.N##
9. COMMIT
   source/policy/schema/code version receipt
```

## ENSDF adapter

Capture release metadata before relying on upstream record IDs. Prefer scientific re-resolution keys over row IDs. Preserve published datafile checksums where available.

## Parser rule

A parser may not silently repair ambiguous source notation. Ambiguity routes to `NEEDS_REVIEW` at the ingestion workflow layer.

## Synthetic contract gate

Before real Z=1–12 ingestion, tests must cover valid symmetric/asymmetric uncertainty, limit semantics, multiple receipts, transient ENSDF-style IDs with release context, omitted unknowns, and explicit invalid cases such as q>Z or legacy {lower,upper} uncertainty.

## Real-data gate

```text
[ ] source policy committed
[ ] SourceRecord schema committed
[ ] physics profile v0.1.1 committed
[ ] ingestion contract committed
[ ] synthetic contract tests implemented and passing
```

No real Z=1–12 numerical dataset is committed before this gate passes.

## Design principle

```text
Retrieval can fail.
Parsing can fail.
Normalization can fail.
Validation can fail.

Failure must be visible and reversible.
Nothing earns a scientific value merely because a parser could fill the field.
```
