# Deuteron Spin-Ergotropy Baseline v0.1

```text
STATUS: SIMULATION CANDIDATE
CANON: NO
DEPLOYMENT: NO
ENERGY_SOURCE_CLAIM: NO
FUSION: NOT MODELED
NUCLEAR_REACTION_ENGINEERING: NOT MODELED
DATE: 2026-10-06
```

## Purpose

This packet builds the conventional-physics control for the Stars 2.0 / deuteron spin-harvest hypothesis.

It does not assume room-temperature net energy exists.

Instead, it asks:

```text
How much extractable work does standard spin-1 Zeeman physics permit
for thermal, coherent, and inverted deuteron spin states?

How large would any additional nonstandard effect have to be
to overcome a declared process-energy ledger?
```

The goal is to isolate the genuinely novel claim from already-established modules.

## Baseline model

The deuteron is treated as a spin-1 system in a static magnetic field.

For positive gyromagnetic ratio and field magnitude B:

```text
m = +1 -> -ΔE
m =  0 ->  0
m = -1 -> +ΔE

ΔE = h * (gamma_d / 2π) * B
gamma_d / 2π ≈ 6.53569 MHz/T
```

The simulation computes **ergotropy**:

```text
W = Tr(rho H) - Tr(rho_passive H)
```

where the passive state is the lowest-energy population ordering compatible with the spectrum of rho.

Interpretation:

- a thermal equilibrium state is passive and has zero ergotropy;
- a coherent or inverted state can store extractable work;
- preparing that state requires work or another nonequilibrium resource;
- superposition is not an energy source by itself;
- any closed cycle must include preparation, reset, controls, separation, acoustics, electrochemistry, and losses.

## Reference states

The script evaluates:

```text
thermal
ground_m_plus_1
equal_coherent_superposition
fully_inverted_m_minus_1
```

The equal coherent state is:

```text
(|+1> + |0> + |-1>) / sqrt(3)
```

This is a reference state for quantum-thermodynamic accounting, not a claim that the state is easy or cheap to prepare.

## Energy ledger

The simulation exposes:

```text
parasitic_J_per_mol
recovery_efficiency
break_even_multiplier_on_recovered_work
```

The break-even multiplier is a sensitivity parameter only.

It answers:

```text
If standard spin-state work is insufficient,
how much larger would recovered work have to become
to equal the declared non-spin process cost?
```

A multiplier greater than one is not evidence for anomalous physics.

## Why this matters for Stars 2.0

The architecture now separates:

```text
ESTABLISHED / EXTERNAL
  H/D isotope separation
  sonoelectrochemistry
  acoustic levitation / droplet manipulation
  magnetic-resonance spin dynamics
  inductive/electromagnetic readout
  DISH microscale volumetric printing
  mesoscale deterministic atomic defect engineering

HYPOTHESIS
  a room-temperature deuteron spin cycle producing net positive energy
  after complete preparation/reset/process accounting
```

That means the simulation can hold the hypothesis to a conventional baseline rather than baking the answer in.

## DISH / Atomic Forge boundary

DISH is not atomic-scale positioning.

As reported in Nature (2026), DISH demonstrated roughly:
- ~19 micrometre overall printing resolution;
- ~12 micrometre finest independent positive feature;
- millimetre-scale objects in ~0.6 seconds.

That is around five orders of magnitude coarser than atomic dimensions.

The 2026 Nature atomic-engineering result instead used a steered electron beam with sub-20-picometre positioning accuracy to create more than 40,000 selected defects in CrSBr.

Therefore a grounded Atomic Forge stack should assign different jobs to different fields:

```text
DISH / volumetric photopolymerization
  -> chamber, scaffold, microfluidics, mesoscale geometry

acoustic fields
  -> droplet/particle containment, transport, streaming, organization

electrochemistry
  -> isotope-selective chemical pathways and redox

electromagnetic fields
  -> charged-particle and spin-state control

electron / optical probes
  -> atomic-scale manipulation or readout where independently supported
```

No one field is assumed to perform all scales of control.

## Relationship to existing Atlas work

Relevant antecedents include:

```text
atlas-lattice-foundation/provenance/STARS_OCEAN_002_2026-08-14.md

sheldonbrain-rag-api/docs/KGIS_GLOBAL_SANDBOX_TEST_PROGRAM_2026-08-11.md

atlas-lattice-foundation/docs/Holographic_Trashium_Acoustic_Spec_v1.0.md

atlas-lattice-foundation/spec_modules/18_volumetric_acoustic_printing_spec.md
```

The KGIS rule remains:

```text
GLOBAL SIMULATION FOR BREADTH.
LOCAL EXPERIMENTS FOR TRUTH.
```

## Current gate

Before adding any nonstandard Stars term:

```text
1. Run conventional baseline.
2. Verify thermal ergotropy = 0.
3. Verify coherent/inverted reference-state bounds.
4. Add declared process-energy ledger.
5. Compute break-even enhancement requirement.
6. Only then introduce one explicit hypothesis parameter at a time.
```

## Keeper

```text
Do not simulate the breakthrough into existence.
Make the hypothesis beat the baseline.
```
