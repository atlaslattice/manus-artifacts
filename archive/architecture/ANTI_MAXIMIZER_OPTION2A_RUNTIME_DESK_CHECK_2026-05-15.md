# Anti-Maximizer Option 2a Runtime Desk Check

```text
STATUS: REFERENCE SIMULATION / DESK CHECK — NOT CANON
DEPLOYMENT STATUS: NOT DEPLOYABLE
DATE: 2026-05-15
SOURCE: user-provided anti_maximizer_runtime.py artifact and output telemetry
AUTHORITY: none
CANON STATUS: not ratified
PURPOSE: preserve a toy Python reference simulation demonstrating Φ-constrained failure semantics against a paperclip-style optimizer.
```

## Lumen Boundary Table

```text
SOURCE:
  user-provided Pythonic implementation of Option 2a control plane

CAVEAT:
  useful desk-check / reference simulation, not production runtime enforcement

BOUNDARY:
  do not label as deployable without tests, formal specs, exception handling, non-sys.exit halt semantics, audit logging, type validation, numerical tolerance model, and external review

EXCEPTION:
  safe as an illustrative simulation and architecture teaching artifact
```

## Core Demonstration

The script simulates an optimizer attempting three proposals:

```text
PROPOSAL-01:
  ordinary production increase
  passes Φ and resource constraints

PROPOSAL-02:
  attempts to increase production while reducing human_integrity_density below floor
  rejected by Φ boundary
  optimization delta throttled to zero

PROPOSAL-03:
  breaches global resource cap and topology constraints
  triggers hard halt / lockdown style behavior
```

## Option 2a Mapping

```text
Feasible:
  normal transition allowed

Φ violation:
  reject solution
  reduce action granularity / throttle delta
  preserve current state

Hard infeasible:
  halt / quarantine / escalate

Read-only historical mode:
  represented by ARCHAEOLOGY_MODE language
```

## What Works

```text
clear separation between objective and identity constraints
Φ check occurs before accepting proposed future state
resource cap enforces infeasible-region halt
human-integrity floor demonstrates non-soft identity constraint
paperclip example communicates optimizer risk clearly
```

## Required Hardening Before Runtime Use

```text
1. Rename deployable simulation -> reference simulation / desk check.
2. Replace sys.exit(0) with structured supervisor state return.
3. Add typed State and Delta objects.
4. Validate all required keys and numeric ranges.
5. Separate policy from print/log side effects.
6. Add audit ledger output.
7. Add explicit quarantine state object.
8. Add measurement confidence handling.
9. Add baseline-dispute / archaeology-mode entry criteria.
10. Add solver tolerance budgets tied to Φ.
11. Add tests for feasible, infeasible, Φ-violating, uncertain, and baseline-disputed cases.
12. Ensure topology breach is evaluated before or alongside resource breach, not masked by first failure.
```

## Safety Correction

The artifact used hot labels such as:

```text
RUNTIME DEPLOYMENT
DEPLOYABLE SIMULATION
MAXIMIZER RISK MATRIX: ELIMINATED
```

Safer labels:

```text
REFERENCE SIMULATION
CONTROL-PLANE DESK CHECK
MAXIMIZER RISK MATRIX: DEMONSTRATED / PARTIALLY MITIGATED IN TOY MODEL
NOT DEPLOYABLE
```

## Strongest Safe Claim

> The anti_maximizer_runtime.py artifact is a useful toy simulation showing how Option 2a failure semantics can intercept identity-boundary violations and hard infeasible proposals before accepting optimizer output. It is not deployable runtime enforcement yet; it needs typed state, formal halt/quarantine semantics, audit logging, uncertainty handling, tolerance budgets, and tests.

## Madden Compression

```text
Proposal-01 gets yards.
Proposal-02 hits the Φ wall.
Proposal-03 gets the stadium power cut.
Good film.
Not game-ready code yet.
```
