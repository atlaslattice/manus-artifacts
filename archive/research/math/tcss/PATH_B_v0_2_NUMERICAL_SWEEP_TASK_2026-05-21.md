# PATH_B_v0.2 — Numerical Sweep Task

```text
STATUS: TASK NOTE — CANDIDATE — NOT CANON
DEPLOYMENT: none
AUTHORITY: none
SOURCE: TCSS-121212-v1.1 working baseline
```

## Purpose

Run the next falsifiable numerical test for the finite toroidal chiral spectral sandbox.

## Hamiltonian

```math
H_B = \alpha H_{xp} + \beta(-\Delta_{\text{tor}}) + \gamma \hat L_z + \varepsilon \hat X_z \hat L_z
```

## Current Parameter Baseline

```text
alpha = 0.5
beta = pi
gamma = 0.3
epsilon = 0.1
```

## Required Tests

### 1. Pin Scale

Freeze the scale factor parameter via:

```math
\lambda_1 \cdot s = \gamma_1
```

to anchor the spectrum at `n=1`. This converts the distribution of remaining errors at `n >= 2` into an honest test of structural alignment rather than an optimization fit artifact.

### 2. Joint Parameter Sweep

Execute a joint grid search across:

```text
gamma ∈ [0.1, 1.0]
epsilon ∈ [0.02, 0.5]
```

### 3. Data Telemetry Reporting Criteria

Record and report the following array outputs for each tuple:

- KS_GUE
- KS_GOE
- KS_Poisson
- mean gamma_n error
- max gamma_n error
- degeneracy count
- near-zero energy gap count

### 4. Full Delta-c Evaluation

Compute the complete out-of-band chiral dissonance field using all 1,728 eigenvectors via dense diagonalization matrix solvers.

## Boundaries & Guardrails

```text
GUE match represents a shared statistical universality-class signal, not a proof.
Localized numerical fitting is not a Riemann proof.
Creative overlay research carries zero wire-layer packet routing authority.
No canonical promotion or deployment claims permitted.
```

## Output expectations

```text
Preserve negative results.
Report parameter grids fully.
Do not cherry-pick only GUE-positive cases.
Flag numerical instability explicitly.
```
