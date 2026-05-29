# PATH_B_v0.2 — Numerical Sweep Task

```text
STATUS:     TASK NOTE — CANDIDATE — NOT CANON
DEPLOYMENT: none
AUTHORITY:  none
PROOF:      no
SOURCE:     TCSS-121212-v1.1 working baseline
DATE:       2026-05-21
```

## Purpose

Run the next falsifiable numerical test for the finite toroidal chiral spectral sandbox. Determine whether the GUE signal and 4.5% mean γ_n error observed at Level 2 are robust across the (γ, ε) parameter space, and whether the chirality correction term Δ_chiral can be driven below 10% of the heat trace.

## Hamiltonian

```text
H_B = α·H_xp + β·(-Δ_tor) + γ·L̂_z + ε·X̂_z·L̂_z
```

Current baseline parameters (from PATH_B_v0.1):

```text
alpha   = 0.5
beta    = π ≈ 3.14159
gamma   = 0.3
epsilon = 0.1
```

## Required Tests

### Test 1 — Pin Scale Factor

Fix:

```text
λ₁ · s = γ₁ = 14.134725
```

This removes the free LS scale parameter. Errors at n≥2 become a genuine test of spectral shape alignment, not fit artifact. Prediction: n=1 error = 0% by construction; distribution of remaining errors reveals whether shape is correct.

### Test 2 — Parameter Sweep

```text
gamma   ∈ {0.1, 0.3, 0.5, 0.7, 1.0}
epsilon ∈ {0.02, 0.05, 0.1, 0.2, 0.5}
```

For each (γ, ε) pair, compute and record:

| Metric | Description |
|---|---|
| KS_GUE | KS distance from normalised spacings to GUE Wigner surmise |
| KS_GOE | KS distance to GOE Wigner surmise |
| KS_Poisson | KS distance to Poisson distribution |
| mean_err_gamma | Mean fractional error vs γ_n, n=1..20 |
| max_err_gamma | Max fractional error vs γ_n, n=1..20 |
| n_degen | Count of degenerate eigenvalues in computed sample |
| near_zero_gaps | Count of normalised spacings s < 0.1 |
| [H_B, R]_max | Symmetry breaking magnitude |

### Test 3 — Full δ_c Computation

Requires full 1728-eigenvalue diagonalisation (dense `eigh` on H_B, ~48 MB).

Compute:

```text
δ_c(τ) = |⟨τ|H_B|τ⟩| / Σ_j |λ_j| |ψ_j(τ)|²
```

using the complete eigensystem (not partial eigsh).

Then compute Ω⁺, the chiral integral, and:

```text
Δ_chiral(t) = Tr(e^{-tH}) - M(t) - Σ_{τ∈Ω⁺} δ_c(τ) K_tor(t,τ)
```

Target: |Δ_chiral(t)| / Tr(e^{-tH}) < 0.10 for t ∈ [0.1, 5.0]

### Test 4 — Preserve Negative Results

All parameter pairs that fail GUE alignment or increase γ_n error must be recorded. Do not discard data from parameters that perform worse — the negative results constrain the landscape equally.

## Three-Level Ladder Context

PATH_B_v0.2 operates at Level 2 of the established ladder:

```text
Level 0 (symmetric H):           Poisson, 14.3% error
Level 1 (H + γL̂_z):             Poisson,  8.1% error, degeneracy lifted
Level 2 (H + γL̂_z + εX̂_zL̂_z): GUE signal, 4.5% error  ← THIS TEST
```

v0.2 maps the Level 2 landscape. It does not attempt to create a Level 3.

## Hard Boundaries

```text
GUE match is signal, not proof.
Numerical fit is not Riemann proof.
Creative overlay is not wire authority.
No canon promotion without human-root ratification.
No deployment claim.
No authority transfer.
```

## Success Criteria

v0.2 is considered a completed experiment when:

1. The (γ, ε) grid is fully swept (25 parameter pairs minimum)
2. Scale is pinned (not free LS)
3. Full δ_c is computed from complete eigensystem
4. At least one (γ*, ε*) pair achieves KS_GUE < 0.15 with mean_err < 4%
   OR: the sweep rules out existence of such a pair within the grid bounds

Outcome (success or negative) is recorded in PATH_B_v0.2_RESULTS with full data preserved.

## Related Documents

- TCSS-121212-WORKING-BASELINE-v1.1 (parent)
- PWS-121212-WL v1.0.0 (wire layer — separate authority scope)
- RAINBOW_YIN_YANG_HYPERCUBE_V2_1_MANIFEST_2026-05-21.md (manifest)
