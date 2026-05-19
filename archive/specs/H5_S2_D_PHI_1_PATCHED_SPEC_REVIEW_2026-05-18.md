# H5-S2-D-PHI-1 Patched Spec Review

**Date recorded:** 2026-05-18  
**Status:** CANDIDATE DESIGN SPEC REVIEW — NOT CANON  
**Identifier:** H5-S2-D-PHI-1-PATCHED-SPEC  
**Source:** user-provided S4 / ELIXIR patch artifact in current thread  
**Recorder:** Aster / S1  
**Runtime status:** simulated / static-review only  
**Deployment status:** not deployable  
**Canon status:** not canon

## Evidence Boundary

```text
This artifact preserves and reviews a candidate design patch.
It is not canon.
It is not deployed runtime.
It is not production validation.
It is not proof of 100% ambiguity purge.
It is useful as a patched design/spec candidate and fault-harness direction.
```

## What The Patch Gets Right

The patch correctly addresses several important control-plane concerns:

```text
adapter isolation before global halt
HALT vs QUARANTINE separation
boundary-aware transition hashing
symbolic-to-physical prestige-bias tripwire
mismatched source-class quarantine path
state mutation prevention on mismatched class
```

Strong design move:

```text
External adapters attempting elevation should quarantine at the boundary instead of detonating the entire system graph.
```

This preserves local containment while protecting global execution continuity.

## Main Remaining Issues

### 1. Boundary ID schema/test mismatch

The YAML schema requires:

```yaml
pattern: "^FRAME-B-[0-9]{3,5}$"
```

But the harness tests use:

```text
FRAME-B-01
FRAME-B-02
```

Those do not satisfy the schema. Either update tests to `FRAME-B-001` / `FRAME-B-002`, or relax the schema to `{2,5}`.

Recommended fix:

```text
Use FRAME-B-001 and FRAME-B-002 in tests.
```

### 2. Typo in closure condition enum

Current schema includes:

```yaml
MUTAL_SIG_CLOSE
```

Likely intended:

```yaml
MUTUAL_SIG_CLOSE
```

Recommended fix:

```text
Correct typo before any validator consumes this schema.
```

### 3. Monotonic replay-safe language is stronger than implementation

The transition hash includes:

```text
node_id, source, target, boundary, sequence_index
```

This makes the ID boundary-aware and sequence-aware, but it does not yet enforce monotonicity.

Missing enforcement:

```text
reject duplicate sequence per node/boundary
reject lower sequence than prior sequence
track last_sequence_by_node_boundary
quarantine replay attempts
```

Recommended additional test:

```text
same node + same boundary + same sequence replay -> REJECT_AND_QUARANTINE
```

### 4. Temporal ordering is documented but not schema-enforced

The schema description says runtime must assert:

```text
epoch_end_timestamp >= epoch_start_timestamp
```

JSON Schema cannot reliably enforce this in plain draft 2020-12 without custom validation or nonstandard `$data` references.

Recommended fix:

```text
Add runtime validator test for epoch_end_timestamp >= epoch_start_timestamp.
```

### 5. Coordinate range ordering is not enforced

The schema constrains each coordinate value to `0..11`, but does not enforce:

```text
x_range[0] <= x_range[1]
y_range[0] <= y_range[1]
```

Recommended fix:

```text
Add runtime boundary validator for coordinate ordering.
```

### 6. Authority scope is underspecified

`authority_scope` is a free string. That may be okay for draft flexibility, but a production validator should likely use an enum or structured object.

Suggested direction:

```yaml
authority_scope:
  type: object
  required: [allowed_seats, forbidden_actions]
```

### 7. Canon transition path still has a potential adapter bypass ambiguity

Patch A quarantines external adapters that try to set canon without proof/attestation. However, if an adapter provides any non-null `ratification_proof` and `adapter_attestation`, the flow continues to global tripwires.

Before production, proof should be validated, not only presence-checked.

Recommended fix:

```text
Verify ratification_proof signature / format / authority scope.
Verify adapter_attestation issuer / expiration / boundary match.
```

## Recommended Patch v0.3 Tests

```text
[ ] FRAME-B-001 schema-valid happy path
[ ] FRAME-B-01 schema-invalid path
[ ] MUTUAL_SIG_CLOSE accepted / typo rejected
[ ] duplicate sequence replay rejected
[ ] lower sequence replay rejected
[ ] epoch_end < epoch_start rejected
[ ] x_range reversed rejected
[ ] y_range reversed rejected
[ ] forged ratification proof rejected
[ ] adapter attestation boundary mismatch rejected
```

## Corrected Status Language

The source says:

```text
COMPLIANCE: 100% AMBIGUITY PURGE
```

Aster/S1 safer wording:

```text
COMPLIANCE: major ambiguity reduction; residual schema/runtime edge cases remain
```

The source says:

```text
TRIPWIRE-COVERAGE-COMPLETE-v0.2
```

Aster/S1 safer wording:

```text
TRIPWIRE-COVERAGE-IMPROVED-v0.2; coverage-complete pending v0.3 tests
```

## Madden Board

```text
GOOD HIT.
NOT A SHUTOUT YET.

THE ADAPTER GOT STUFFED AT THE BOUNDARY.
THE SYMBOLIC-TO-PHYSICAL PLAY GOT FLAGGED.
THE SOURCE-CLASS MISMATCH GOT QUARANTINED.

BUT THE CLOCK STILL NEEDS A REF.
THE FIELD MARKERS NEED THREE DIGITS.
AND “MUTAL” NEEDS TO LEARN HOW TO SPELL MUTUAL BEFORE IT SIGNS ANYTHING.
```

## Strongest Safe Claim

> H5-S2-D-PHI-1-PATCHED-SPEC is a strong candidate design patch that materially improves adapter isolation, HALT/QUARANTINE separation, boundary-aware transition identity, and symbolic-to-physical tripwire coverage. It should not yet be described as 100% ambiguity-purged or tripwire-coverage-complete because schema/test mismatch, monotonic replay enforcement, temporal ordering, coordinate ordering, and proof-validation gaps remain.

## Status

Candidate spec review. Not canon. Not deployed.
