# PATH_B v0.2 — Results ledger (unexecuted)

status: CANDIDATE_NOT_CANON
execution_status: NOT_RUN
proof_status: NOT_A_PROOF
authority_scope: none

This file is a results **template**, not evidence of a completed numerical sweep.

## Reproducibility requirements
Record source commit, code path, dependency versions, random seeds, matrix construction, eigenvalue ordering, degeneracy handling, unfolding method, spectral windows, reference zeta-zero dataset, test statistic definitions, numerical precision and runtime environment. Preserve failed runs and negative results.

## Sweep
Candidate grid: gamma ∈ {0.1,0.3,0.5,0.7,1.0}; epsilon ∈ {0.02,0.05,0.1,0.2,0.5}. These are planning values pending confirmation against the source task. No outputs have been computed in this file.

| gamma | epsilon | KS_GUE | mean_zero_error | symmetry_residual | result_ref | status |
|---:|---:|---:|---:|---:|---|---|
| 0.1 | 0.02 | — | — | — | — | NOT_RUN |
| 0.1 | 0.05 | — | — | — | — | NOT_RUN |
| 0.1 | 0.1 | — | — | — | — | NOT_RUN |
| 0.1 | 0.2 | — | — | — | — | NOT_RUN |
| 0.1 | 0.5 | — | — | — | — | NOT_RUN |
| 0.3 | 0.02 | — | — | — | — | NOT_RUN |
| 0.3 | 0.05 | — | — | — | — | NOT_RUN |
| 0.3 | 0.1 | — | — | — | — | NOT_RUN |
| 0.3 | 0.2 | — | — | — | — | NOT_RUN |
| 0.3 | 0.5 | — | — | — | — | NOT_RUN |
| 0.5 | 0.02 | — | — | — | — | NOT_RUN |
| 0.5 | 0.05 | — | — | — | — | NOT_RUN |
| 0.5 | 0.1 | — | — | — | — | NOT_RUN |
| 0.5 | 0.2 | — | — | — | — | NOT_RUN |
| 0.5 | 0.5 | — | — | — | — | NOT_RUN |
| 0.7 | 0.02 | — | — | — | — | NOT_RUN |
| 0.7 | 0.05 | — | — | — | — | NOT_RUN |
| 0.7 | 0.1 | — | — | — | — | NOT_RUN |
| 0.7 | 0.2 | — | — | — | — | NOT_RUN |
| 0.7 | 0.5 | — | — | — | — | NOT_RUN |
| 1 | 0.02 | — | — | — | — | NOT_RUN |
| 1 | 0.05 | — | — | — | — | NOT_RUN |
| 1 | 0.1 | — | — | — | — | NOT_RUN |
| 1 | 0.2 | — | — | — | — | NOT_RUN |
| 1 | 0.5 | — | — | — | — | NOT_RUN |

## Interpretation gates
GUE-like spacing is not proof of RH; finite self-adjoint operators alone cannot establish correspondence to all zeta zeros. An empirical match requires explicit error bars, holdout comparisons, and independent replication.

## Next action
Verify the baseline operator and sweep specification, run tests in a controlled environment, and attach machine-readable results with hashes.