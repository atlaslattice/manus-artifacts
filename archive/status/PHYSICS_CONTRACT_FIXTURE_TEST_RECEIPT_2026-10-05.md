# Physics Contract Fixture Test Receipt — 2026-10-05

```text
STATUS: LOCAL EXECUTION RECEIPT
CI: NO
GITHUB ACTIONS: NO
SCIENTIFIC DATA: NONE
DATE: 2026-10-05
```

## Inputs

Fetched from the default branch of `atlaslattice/manus-artifacts` immediately before execution:

```text
public_candidate_bundle_0001/schemas/physics_profile_v0.1.1.json
blob sha: 1f21bdd278ec6535186c5ce36dd7f62056937f15

public_candidate_bundle_0001/fixtures/physics_ingestion/CONTRACT_FIXTURES_v0.1.json
blob sha: a4e289518148280230b6c3f8659c1677646e974a

public_candidate_bundle_0001/tools/validate_physics_contract_fixtures.py
blob sha: fb587ad2b3c47e0330c1ca5463ed98541c5c0f07
```

## Execution scope

The fixture classifications were executed in the current ChatGPT Python environment using the committed v0.1.1 property-contract definitions and the exact committed fixture cases, together with the committed validator's policy checks.

This was not a GitHub Actions run and is not represented as CI.

## Results

```text
valid_symmetric_uncertainty
  expected: VALID
  actual:   VALID

valid_asymmetric_uncertainty
  expected: VALID
  actual:   VALID

invalid_legacy_lower_upper_shape
  expected: INVALID
  actual:   INVALID
  schema finding:
    {lower: 0.3, upper: 0.5} is not valid under the committed uncertainty schema
  policy finding:
    legacy/limit uncertainty shape is not allowed by v0.1.1

valid_upper_limit_semantics
  expected: VALID
  actual:   VALID

identity_field
  expected: VALID
  actual:   VALID
```

## Verdict

```text
PASS: 5 / 5 synthetic contract fixtures matched expected validity.
```

The test establishes contract behavior for these fixtures only.

It does not establish:
- scientific correctness of any nuclear datum,
- correctness of future parsers,
- correctness of cross-field constraints such as q <= Z,
- reproducibility under GitHub Actions,
- correctness of external-source adapters.

## Next execution gate

Before real Z=1–12 ingestion:

```text
[x] contract fixtures defined
[x] fixture expectations executed locally
[ ] committed validator executed from repository checkout / CI
[ ] SourceRecord fixture suite added and executed
[ ] one real source adapter implemented
[ ] one real nuclide passed end-to-end with receipts
```

## Rule

```text
A committed test is a test design.
A passing execution is a test result.
CI is a reproducibility layer beyond both.
```
