# Deuteron Spin-Ergotropy Baseline — Local Test Receipt

```text
DATE: 2026-10-06
STATUS: LOCAL EXECUTION RECEIPT
CI: NO
SCIENTIFIC_VALIDATION: NO
ENERGY_SOURCE_CLAIM: NO
```

## Test

The candidate Python baseline was executed locally with:

```text
B = 1 T
T = 300 K
parasitic = 1 J/mol
recovery efficiency = 1.0
```

## Conventional outputs

```text
deuteron Larmor frequency:
  6.53569 MHz

adjacent Zeeman spacing:
  4.33059404186535e-27 J per deuteron

dimensionless spacing ΔE/kT:
  1.0455454987389626e-6
```

Reference-state ergotropy:

```text
thermal:
  0 J/mol

ground m=+1:
  0 J/mol

equal coherent superposition:
  0.002607944689453048 J/mol

fully inverted m=-1:
  0.0052158893789060945 J/mol
```

With an illustrative declared non-spin cost of 1 J/mol:

```text
equal coherent state:
  conventional net = -0.997392055310547 J/mol
  break-even multiplier on recovered work ≈ 383.44

fully inverted state:
  conventional net = -0.994784110621094 J/mol
  break-even multiplier on recovered work ≈ 191.72
```

## Interpretation

This does not estimate a real Stars apparatus.

The 1 J/mol process cost is intentionally illustrative.

The important validation targets are:

```text
thermal equilibrium ergotropy = 0
coherent reference state has finite stored work
inverted reference state has the largest simple Zeeman-state ergotropy
all non-equilibrium state preparation/reset costs remain outside this first baseline
```

## Consequence

At ordinary room-temperature Zeeman scales, conventional deuteron spin-state work is small.

Any net-positive Stars 2.0 claim must therefore identify and measure a nonequilibrium resource or nonstandard effect large enough to survive a complete energy ledger.

That requirement is a falsification gate, not an assumption that such an effect exists.

## Next simulation step

```text
Add a process-ledger layer with separately sourced:
- isotope separation cost
- acoustic/ultrasonic cost
- electrochemical cost
- polarization/preparation cost
- readout/recovery efficiency
- reset cost

Then compute the break-even enhancement requirement without inserting a positive anomaly by hand.
```
