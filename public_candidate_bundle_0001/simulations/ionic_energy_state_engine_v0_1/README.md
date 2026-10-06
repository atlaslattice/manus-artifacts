# Ionic Energy State Engine v0.1 — Alexandrian Candidate Screen

```text
STATUS: PUBLIC CANDIDATE / SIMULATION SCAFFOLD
CANON: NO
DEPLOYMENT: NO
ENERGY_SOURCE_CLAIM: NO
DATE: 2026-10-06
PURPOSE: Compare ionic energy pathways under one thermodynamic + resource + ecology ledger.
```

## Why this exists

The research target is broader than deuterium.

The useful object is an **ionic transformation pathway**:

```text
working medium
+ initial state
+ external gradient / nonequilibrium resource
+ conversion mechanism
+ final state
+ reset / recycle path
+ ecological and infrastructure ledger
```

Deuterium remains interesting because natural water contains a huge total inventory of deuterium and existing water/desalination infrastructure can potentially host isotope-separation steps. That makes D-bearing water a potentially attractive **working medium / feedstock**.

It does **not** make deuterium an energy source by abundance alone.

Core distinction:

```text
RESOURCE != ENERGY SOURCE
WORKING MEDIUM != FUEL
ABUNDANCE != EFFICIENCY
```

The energy must come from a measured gradient or nonequilibrium state such as salinity, humidity, redox chemistry, electric potential, pressure/flow, temperature, mechanically supplied acoustic work, externally prepared charge state, externally prepared spin polarization, or another explicitly identified source.

## Thermodynamic core

For an ionic species i, the idealized electrochemical potential is:

```text
mu_tilde_i = mu_i^0 + R*T*ln(a_i) + z_i*F*phi
```

For a transition from state 1 to state 2:

```text
Delta_mu_i = R*T*ln(a2/a1) + z_i*F*(phi2-phi1)
```

For a spontaneous downhill transition, the decrease in free energy defines an ideal reversible-work ceiling. Real systems must debit pumping, pretreatment, separation, membrane resistance, concentration polarization, fouling, electrode overpotential, acoustic power, field generation, ionization/state preparation, readout, reset, thermal management, maintenance, material replacement, and discharge treatment.

## Two independent scoreboards

### A. Physics / energy ledger

No candidate receives performance credit without a defined state transition and energy ledger.

### B. Alexandrian resource / ecology screen

The screening layer asks about abundance, circularity, access to a replenished gradient, extraction burden, local ecological consequences, infrastructure compatibility, and technology maturity.

The screening score is a **policy/research-priority heuristic**, not a law of physics and not a substitute for life-cycle assessment. UNKNOWN values reduce score coverage instead of being silently filled.

## Why deuterium remains interesting

The current Stars-Ocean provenance record places the natural-water deuterium inventory at roughly 30–35 g D-equivalent per cubic metre of seawater.

For comparison, seawater lithium is roughly 0.17 g/m^3.

That makes D-bearing water interesting on feed-volume economics even though isotope separation is fundamentally different from ordinary ion recovery and may still be energetically expensive.

## Initial research question

Do not ask:

```text
Which ion contains the most energy?
```

Ask:

```text
Which repeatable ionic state transition has:
1. a real external free-energy source,
2. low preparation/reset cost,
3. high recoverable work,
4. abundant or circular working medium,
5. low ecological burden,
6. infrastructure compatibility,
7. a falsifiable laboratory path?
```

This is a Pareto problem, not a single-winner periodic table.

## Atomic Forge / DISH integration

DISH and acoustic manufacturing belong primarily to the device-architecture layer:

```text
DISH / volumetric printing
  -> microchannels
  -> membrane supports
  -> electrode geometry
  -> acoustic cavities
  -> droplet chambers
  -> gradient manifolds
  -> sensor / optical paths

acoustic fields
  -> streaming
  -> boundary-layer control
  -> particle / droplet manipulation
  -> interface modulation

electrochemistry / membranes
  -> selective ion transport
  -> redox
  -> concentration gradients

EM fields
  -> charged-particle / spin-state control where applicable
```

DISH is not assumed to position individual ions or atoms.

## Gate before promotion

A candidate may move from resource screen to energy benchmark only when it has a defined initial state, final state, external energy source/gradient, sourced state variables, declared system boundary, preparation/reset costs, ecological boundary, and falsification criterion.

## Keeper

```text
Do not hunt for the ion with the biggest number.
Hunt for the cheapest circular path between two useful states.
```
