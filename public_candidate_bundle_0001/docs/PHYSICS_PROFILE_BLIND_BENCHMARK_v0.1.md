# Atlas Lattice Physics Profile + Blind Benchmark v0.1

```text
STATUS: CANDIDATE RESEARCH SCHEMA / BENCHMARK PLAN
CANON: NO
DEPLOYMENT: NO
AUTHORITY: NONE
DATE: 2026-10-05
PARENT: lattice_coordinate.schema.v0.3
ENTRY COORDINATE: H##.S##.N##
```

## Purpose

Preserve the October 2026 refinement that the Rainbow Yin-Yang / Atlas Lattice is the candidate Periodic Table 2.0 coordinate substrate, while the nuclear/atomic tuple `(Z,N,q)` is a typed physical profile attached to an existing House-Sphere-Node address.

The key architectural correction is:

```text
Atlas address = H.S.N
physics profile = properties attached to that address
```

The physics profile must not create a competing coordinate system.

## Existing coordinate contract

The parent public candidate schema is:

```text
lattice_coordinate.schema.v0.3
H##.S##.N##
H = House
S = Sphere
N = Node
12 × 12 × 12 = 1,728 entry cells
```

The existing HSN-to-D12 crosswalk treats H-S-N and D01-D12 as complementary views rather than competing ontologies.

## Physics profile structure

The v0.1 profile separates:

```text
Nuclide(Z,N)
  -> ChargeState(q)
```

Nuclide-level properties are stored once. Charge-state-dependent behavior is stored per q.

Representative nuclide properties include mass, spin/parity, binding and separation energies, magnetic/quadrupole moments, charge radius, deformation, neutral half-life, neutral decay modes, and decay Q values.

Representative charge-state properties include q, electron count/configuration, ionization fraction, total electronic binding energy, electron-capture availability, bound-state beta availability, internal-conversion availability, charge-state-specific half-life and branching, decay energetics, and experimental context.

Every scientific value carries an evidence/provenance envelope.

## Evidence status

The schema currently permits:

```text
MEASURED
EVALUATED
DERIVED
REFERENCE
SIMULATED
PROPOSED
DISPUTED
SUPERSEDED
QUARANTINED
CANDIDATE
```

Document existence is not proof. Evidence status belongs to the specific scientific property or claim.

## Multidomain boundary

The existing Atlas architecture can co-index matter, isotopes, spin, resonance, frequency, acoustics, color harmonics, material properties, and other projections.

For this research program:

```text
spectral_profile = CANDIDATE unless numerically supported
acoustic_profile = CANDIDATE unless numerically supported
material_profile = CANDIDATE unless numerically supported
```

Co-location in the lattice is a search relationship, not a physical-causation claim.

## Blind benchmark program

### Phase 0 — Representation validation

Populate selected light nuclides across Z=1 through Z=12 to confirm schema fidelity against established nuclear/atomic data.

### Phase 1 — Physics-only retrodiction

Build a wider literature-derived corpus of measured charge-state-dependent nuclear behavior.

Initial proof-of-concept positive-control families:

- Re-187 charge-state-dependent bound-state beta decay.
- Dy-163 charge-state-dependent bound-state beta decay.
- Tl-205 charge-state-dependent bound-state beta decay.

The exact benchmark answers and source receipts should be locked before scoring.

Compare:

```text
Baseline A: conventional rules / decay energetics
Baseline B: numerical/statistical model using the same physics fields
Phase 1 Atlas/Alexandria: HSN-attached physics profile only
```

### Phase 2 — Atlas multidomain test

Expose only validated additional Atlas projections and test whether they improve held-out prediction beyond Phase 1.

Required controls include:

```text
shuffled HSN assignments
randomized Rainbow polarity
randomized S-curve positions
scrambled spectral/acoustic mappings
feature-family ablation
multiple held-out sets
```

If the multidomain model does not reproducibly beat the physics-only representation and controls, the additional projections have not demonstrated predictive scientific value.

## Falsification rule

```text
If the richer representation does not outperform simpler baselines on blind held-out cases,
it remains an ontology / visualization / retrieval architecture rather than a demonstrated
scientific discovery engine.
```

A prospective prediction is allowed only after repeated blind retrodiction success. It must be frozen and timestamped before confirmatory evidence is sought, and failed predictions remain preserved in provenance.

## Invariants

- Coordinate != truth.
- Coordinate != canon.
- Coordinate != physical causation.
- H-S-N remains the entry address.
- (Z,N,q) is a property projection, not a replacement coordinate.
- Contradictions are preserved rather than silently erased.
- Non-nuclear mappings stay candidate until supported.
- Measurements outrank elegance.

## Provenance

This v0.1 packet consolidates an October 2026 discussion among Dave / Atlas Lattice, GPT-5.6 Sol, and DeepSeek.

DeepSeek contributed the first concrete physics-profile JSON draft and benchmark sequencing. GPT cross-checked the existing Atlas repositories, recovered the authoritative H-S-N public coordinate schema and HSN-to-D12 crosswalk, identified the need to preserve Node as the third entry coordinate, and revised the schema for parent compatibility and evidence/provenance discipline.

No simulation result in this packet is presented as a laboratory result. No cross-domain physical coupling is asserted by the schema itself.

## Keeper

```text
Elegant ideas get hypotheses.
Blind predictions get credibility.
Measurements get authority.

The lattice tells us where to look.
Evidence tells us what is real.
```
