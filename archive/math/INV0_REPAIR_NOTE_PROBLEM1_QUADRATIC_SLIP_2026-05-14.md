# INV 0 Repair Note — Problem 1 Quadratic Slip

```text
STATUS: MATH REPAIR NOTE — FOSSILIZED TYPO / INHERITED SOLUTION
DATE: 2026-05-14
ARTIFACT TYPE: math-solutions batch
PROBLEM: Problem 1
FAULT TYPE: displayed algebra slip
SEVERITY: minor
DOWNSTREAM THEOREM: intact
REPAIR ACTION: corrected intermediate quadratic
CONTINUITY STATUS: preserved
BRANCH STATUS: fossilized typo, inherited solution
CANON STATUS: not ratified
```

## Fossilbranch Summary

This is an INV 0 repair event.

The artifact should not be discarded. The typo should not be hidden. The valid downstream parametrization should not be thrown away.

Correct action:

```text
preserve the artifact
mark the displayed algebra slip
patch the derivation
inherit the valid result forward
```

## Original Equation

```math
x^2+y^2+z^2=2(xy+yz+zx)
```

Treating this as a quadratic in `z` gives the corrected intermediate chain:

```math
z^2-2(x+y)z+x^2+y^2-2xy=0
```

Since

```math
x^2+y^2-2xy=(x-y)^2,
```

we get

```math
z^2-2(x+y)z+(x-y)^2=0.
```

Completing the square:

```math
(z-x-y)^2=4xy.
```

## Consequence

The downstream parametrization survives:

```math
x=d a^2,
qquad y=d b^2,
qquad z=d(a\pm b)^2
```

up to coordinate permutation.

## Corrected Status Packet

```text
artifact: math-solutions batch
problem: Problem 1
fault type: displayed algebra slip
severity: minor
downstream theorem: intact
repair action: corrected intermediate quadratic
continuity status: preserved
branch status: fossilized typo, inherited solution
```

## INV 0 Lesson

```text
Do not delete the branch.
Do not pretend the typo did not exist.
Do not discard the valid theorem.
Fossilize the slip.
Patch the chain.
Inherit the result.
```

## Strongest Safe Claim

> Problem 1 contained a minor displayed algebra slip in an intermediate quadratic, but the corrected chain still yields `(z-x-y)^2=4xy`, so the square parametrization remains valid up to coordinate permutation.
