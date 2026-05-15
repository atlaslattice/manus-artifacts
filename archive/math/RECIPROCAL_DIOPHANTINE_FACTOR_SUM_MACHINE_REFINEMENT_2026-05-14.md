# Reciprocal Diophantine Factor-Sum Machine Refinement

```text
STATUS: MATHEMATICAL NOTE — CANDIDATE THEOREM REFINEMENT
DATE: 2026-05-14
SOURCE: Vesper refinement of reciprocal Diophantine primitive skeleton
CANON STATUS: not ratified
DEPLOYMENT STATUS: not applicable
PURPOSE: refine the primitive parametrization of 1/x + 1/y = k/z into a factorization-plus-coprime-sum machine.
```

## Starting Skeleton

For fixed `k in Z \ {0}`, primitive integer solutions to

```math
1/x + 1/y = k/z,
xyz \ne 0,
\gcd(x,y,z)=1
```

have the form

```math
(x,y,z)=(ga,gb,abc)
```

with

```math
\gcd(a,b)=1,
\qquad c(a+b)=kg,
\qquad \gcd(g,abc)=1.
```

## Vesper Compression

From

```math
\gcd(g,abc)=1
```

we have in particular

```math
\gcd(g,c)=1.
```

The equation

```math
c(a+b)=kg
```

therefore implies

```math
g \mid a+b.
```

Write

```math
a+b=gd.
```

Substituting gives

```math
cgd=kg.
```

Since `g \ne 0`, cancel `g`:

```math
cd=k.
```

## Refined Parametrization

Primitive solutions can therefore be written as

```math
x=ga,
\qquad y=gb,
\qquad z=abc,
```

where

```math
k=cd,
\qquad a+b=gd,
\qquad \gcd(a,b)=1,
\qquad \gcd(g,abc)=1.
```

Equivalently:

```text
factor k = c d using signed nonzero divisors
choose coprime a,b with a+b = g d
require g coprime to a b c
then (ga, gb, abc) is primitive
```

## Layer Separation

```text
GEOMETRY LAYER:
  x = ga
  y = gb
  z = abc

FACTOR LAYER:
  k = cd

SUM LAYER:
  a + b = gd

PRIMITIVE LAYER:
  gcd(a,b)=1
  gcd(g,abc)=1
```

## Small-k Examples

### k = 1

```math
cd=1.
```

So over integers:

```text
(c,d) = (1,1) or (-1,-1)
```

and hence

```math
a+b = \pm g.
```

### k = 2

```math
cd=2.
```

So over integers:

```text
(c,d) in {(1,2), (2,1), (-1,-2), (-2,-1)}
```

and hence

```text
a+b is one of 2g, g, -2g, -g
```

subject to the primitive filter

```math
\gcd(g,abc)=1.
```

## Punchline

```text
Primitive reciprocal solutions are controlled by factorizations of k plus coprime decompositions of gd.
```

The equation stops looking like a messy reciprocal Diophantine problem and becomes:

```text
factorization + coprime-sum machine
```

## Strongest Safe Claim

> Given the primitive skeleton `(x,y,z)=(ga,gb,abc)`, the condition `gcd(g,abc)=1` forces `g | (a+b)`, so the equation compresses to `k=cd` and `a+b=gd`. Thus primitive solutions are governed by signed factorizations of `k` together with coprime decompositions of `gd`, filtered by `gcd(g,abc)=1`.
