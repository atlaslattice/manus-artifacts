# Reciprocal Diophantine Primitive Skeleton Theorem

```text
STATUS: MATHEMATICAL NOTE — CANDIDATE THEOREM
DATE: 2026-05-14
SOURCE: user-provided derivation / GPT review thread
CANON STATUS: not ratified
DEPLOYMENT STATUS: not applicable
PURPOSE: preserve the skeleton parametrization for primitive integer solutions of 1/x + 1/y = k/z.
```

## Problem

Fix `k in Z \ {0}` and solve

```math
1/x + 1/y = k/z,
xyz != 0,
gcd(x,y,z)=1.
```

Equivalently:

```math
z(x+y)=kxy.
```

## Skeleton Derivation

Write

```math
x = ga,
y = gb,
gcd(a,b)=1.
```

Then

```math
z(a+b)=kgab.
```

Since

```math
gcd(ab,a+b)=1,
```

we get

```math
ab | z.
```

Write

```math
z=abc.
```

Then the equation becomes

```math
c(a+b)=kg.
```

Therefore all solutions have the form

```math
(x,y,z)=(ga,gb,abc),
```

with

```math
gcd(a,b)=1,
quad c(a+b)=kg.
```

## Primitive Filter

Since

```math
gcd(x,y)=g,
z=abc,
```

we get

```math
gcd(x,y,z)=gcd(g,abc).
```

So primitiveness is exactly

```math
gcd(g,abc)=1.
```

## Theorem Statement

Up to swapping `x` and `y`, primitive integer solutions to

```math
1/x + 1/y = k/z,
xyz != 0,
gcd(x,y,z)=1
```

are exactly

```math
(x,y,z)=(ga,gb,abc)
```

for integers `a,b,c,g != 0` satisfying

```math
gcd(a,b)=1,
a+b != 0,
c(a+b)=kg,
gcd(g,abc)=1.
```

## Geometry / Arithmetic Split

```text
GEOMETRY:
  z(x+y)=kxy
  -> c(a+b)=kg

ARITHMETIC:
  gcd(a,b)=1
  gcd(g,abc)=1
```

## Useful Consequence for Fixed k

From the primitive condition `gcd(g,abc)=1`, in particular `gcd(g,c)=1`.

Since

```math
c(a+b)=kg,
```

and `gcd(c,g)=1`, it follows that

```math
c | k.
```

So for fixed `k`, the parameter `c` must be a nonzero divisor of `k`.

Writing

```math
m = k/c,
```

we have

```math
a+b = mg.
```

Thus a useful fixed-`k` search form is:

```text
choose c | k
set m = k/c
choose coprime a,b with a+b divisible by m
set g = (a+b)/m
require gcd(g,abc)=1
output (x,y,z)=(ga,gb,abc)
```

## Strongest Safe Claim

> The reciprocal Diophantine equation `1/x + 1/y = k/z` has a clean primitive skeleton: after extracting `g=gcd(x,y)`, the geometry forces `z=abc` and `c(a+b)=kg`, while primitiveness is exactly `gcd(g,abc)=1`.

## Next Natural Work

For small fixed values such as `k=2,3,4`, classify which primitive shapes survive the divisor condition `c | k` and the coprimality filter `gcd(g,abc)=1`.
