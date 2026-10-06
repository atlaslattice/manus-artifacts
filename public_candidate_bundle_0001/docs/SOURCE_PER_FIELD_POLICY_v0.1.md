# Source-Per-Field Policy v0.1

```text
STATUS: CANDIDATE DATA POLICY — REVIEWED FOR PRE-INGESTION USE
CANON: NO
DEPLOYMENT: NO
AUTHORITY: NONE
DATE: 2026-10-05
PARENTS:
  lattice_coordinate.schema.v0.3
  physics_profile_v0.1.1.json
  source_record_v0.1.json
COMPANION:
  PHYSICS_PROFILE_BLIND_BENCHMARK_v0.1.md
```

## Purpose

Define source authority by field, raw-source preservation, conflict handling, uncertainty semantics, unit normalization, missing-data behavior, and evidence classification before any real nuclear-data corpus is committed.

Core rule:

```text
Unknown stays unknown.
Raw stays recoverable.
Evidence status describes evidence type, not a universal rank.
```

## Source-per-field policy

| Field family | Preferred source | Secondary / cross-check | Ingestion rule |
|---|---|---|---|
| Atomic mass, mass excess | AME2020 | later authoritative AME edition when explicitly versioned | ingest AME evaluated value as EVALUATED |
| Binding energy/A, AME-published beta energy | AME2020 mass table | independent calculation | AME table value = EVALUATED; our recomputation = DERIVED |
| S1n, S1p, S2n, S2p, AME reaction Q values | AME2020 reaction tables | ENSDF/current evaluation when relevant | preserve published evaluated value and any separately derived check |
| Ground-state / adopted Jπ and level structure | current ENSDF adopted evaluation | NUBASE2020 fixed snapshot | retain evaluation identity/date; conflicts are field-level |
| Ground/isomer half-life and decay modes | current ENSDF adopted evaluation + NUBASE2020 fixed snapshot | DDEP/IAEA dedicated evaluation where available | do not mechanically subordinate current evaluation to older snapshot |
| Dedicated high-precision decay recommendation | DDEP/IAEA when a dedicated evaluation exists | ENSDF/NUBASE | retain all receipts and record preferred display rationale |
| Electron configuration / ionization data | NIST ASD | primary atomic literature when required | preserve NIST evaluator/theory/interpolation qualifier |
| Charge-state-specific nuclear behavior | primary peer-reviewed experiment | evaluated/database summary as cross-reference | MEASURED requires primary experimental receipt |
| Discovery/interface layer | NuDat/NNDC interfaces | underlying ENSDF datasets | interface is not independent evidence |

## AME precedence

AME2020 publishes more than masses. Where AME itself publishes an evaluated quantity, ingest that value as `EVALUATED`.

If Atlas independently computes the same physical quantity from AME inputs, store that result as a separate `DERIVED` claim with `derived_from` and SourceRecord references.

Never overwrite the evaluated value with the derived check merely because the formulas agree.

## ENSDF release identity

The ENSDF API may expose database record IDs that are not durable across full regenerations.

For ENSDF API captures, record:

```text
API/schema version
dataGeneratedAt / release generation identity
scientific lookup key (nuclide/dataset context)
dataset/evaluation identity where available
source datafile identity/checksum where available
retrieval request
retrieval timestamp
```

A transient API ID is a lookup convenience, not a permanent scientific accession.

## Evidence status semantics

| Status | Meaning |
|---|---|
| IDENTITY | defining identity field, not an experimental measurement (e.g. nuclide Z/A identity) |
| MEASURED | direct experimental result with primary receipt |
| EVALUATED | evaluator-adopted/recommended value synthesizing available evidence |
| DERIVED | Atlas-computed from sourced inputs |
| REFERENCE | cross-reference/pointer, not itself a measurement |
| SIMULATED | explicit model/calculation output |
| PROPOSED | explicit hypothesis/prediction not yet tested |
| DISPUTED | unresolved conflicting sourced claims |
| SUPERSEDED | historical claim replaced by later adopted evaluation |
| QUARANTINED | provenance/integrity problem |
| CANDIDATE | unvalidated Atlas projection or mapping |

`MEASURED` does not automatically outrank `EVALUATED`. A new measurement enters as a new measured claim. An evaluated/adopted value changes when an appropriate evaluator updates it.

## Identity fields

For the first ingestion profile:

```text
Z and A: IDENTITY when they define the nuclide
N: IDENTITY or DERIVED from A-Z, with method recorded
q: IDENTITY when defining a charge state; MEASURED only when the experiment's determination of q is itself the asserted observable
```

Do not call mass number A an atomic-mass measurement.

## Raw-source preservation

External source material enters first as `SourceRecord`.

```text
External source
  -> immutable SourceRecord
  -> parser/normalizer
  -> normalized physics property
  -> schema validation
  -> HSN attachment
```

Raw fields belong to SourceRecord rather than being silently collapsed into the normalized property.

A normalized property cites one or more `source_record_refs`.

## Uncertainty contract

The committed v0.1/v0.1.1 property representation is:

```json
"uncertainty": 2.0
```

for symmetric uncertainty, or:

```json
"uncertainty": {
  "minus": 1.8,
  "plus": 2.0
}
```

for asymmetric uncertainty.

Do not emit `{symmetric: ...}` or `{lower: ..., upper: ...}` into this schema.

Limits and ranges are not uncertainty. v0.1.1 adds `value_relation`: EXACT, APPROXIMATE, UPPER_LIMIT, LOWER_LIMIT, RANGE.

Raw/source-native uncertainty syntax is retained in SourceRecord.

## Unit normalization

| Quantity | Canonical normalized unit |
|---|---|
| atomic_mass | u |
| mass_excess | MeV |
| binding/separation energies | MeV |
| decay/reaction Q values | MeV |
| half-life | s |
| magnetic moment | μ_N |
| quadrupole moment | barn |
| charge radius | fm |
| cross section (future) | barn |

The original unit remains in SourceRecord.

Every nontrivial conversion should have a reproducible conversion receipt containing source unit, target unit, conversion factor/constants, and software/policy version.

## Source qualifiers

Source-native qualifiers are separate from `evidence_status`.

Examples: estimated, interpolated, extrapolated, semi-empirical, theoretical, recommended, upper limit, approximate.

Preserve the raw qualifier in SourceRecord and normalized semantic qualifier in `source_qualifier`.

## Missing data

| Situation | Representation |
|---|---|
| no measurement and no prediction | omit property |
| explicit model calculation | SIMULATED |
| explicit published hypothesis | PROPOSED |
| measured/evaluated disagreement | preserve claims; use DISPUTED when unresolved |
| obsolete adopted value | SUPERSEDED, never deleted |

Forbidden: `value: null, evidence_status: PROPOSED` when the real meaning is merely “unknown”.

A neutral-state value never auto-propagates to another q.

## Charge-state-specific rules

1. Neutral-state evaluated behavior may use ENSDF/NUBASE/DDEP as appropriate.
2. Highly charged / bare-ion nuclear behavior requires primary-experiment evidence for `MEASURED`.
3. Intermediate q states are omitted when unknown; do not interpolate nuclear behavior.
4. Bookkeeping such as `electron_count = Z-q` and `ionization_fraction = q/Z` may be DERIVED.
5. Availability flags such as electron capture, internal conversion, or bound-state beta must cite explicit rules/energetics and be DERIVED or sourced; they are not magic labels.

## Conflict handling

- Resolve at field/claim level, not record level.
- Preserve all source receipts.
- Newer does not automatically mean better.
- New measurements do not silently overwrite adopted evaluations.
- When a later evaluation supersedes an earlier evaluation, retain the older value as `SUPERSEDED`.
- Display preference must carry rationale and remain reversible.

## Synthetic fixtures

Synthetic fixtures are encouraged before live ingestion. They must use `record_kind: SYNTHETIC_FIXTURE` and are prohibited from serving as scientific evidence.

Fixture tests should cover symmetric/asymmetric uncertainty, limits, missing omission, multiple receipts, disagreements, transient ENSDF-style IDs plus release identity, and conversion receipts.

## Baseline integrity

Baseline A receives the strongest reasonable conventional atomic/nuclear physics representation available.

Atlas is not allowed to win by weakening the comparator.

## Reproducibility invariant

Every committed normalized scientific property must be reproducible from:

```text
SourceRecord(s)
+ policy version
+ normalization/conversion code version
+ schema version
```

## Keeper

```text
Elegant ideas get hypotheses.
Blind predictions get credibility.
Measurements get authority.

Unknown stays unknown.
Raw stays recoverable.
The baseline gets to win.
```
