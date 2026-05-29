# Φ Kernel → QP Supervisor Option 2 Transition Note

```text
STATUS: ARCHITECTURE / MATHEMATICAL CONTROL NOTE — CANDIDATE — NOT CANON
DEPLOYMENT STATUS: NOT DEPLOYABLE
DATE: 2026-05-15
SOURCE: user-provided Option 2 validation / tightening pass
AUTHORITY: none
CANON STATUS: not ratified
PURPOSE: preserve the transition rule from Φ as conserved kernel to QP supervisor objectives constrained inside Φ.
```

## Core Validation

Φ is now treated as a legitimate kernel, not a metaphor:

```text
Φ is not narrative identity.
Φ is not policy.
Φ is not an optimization target.
Φ is a conserved quantity defined over admissible transitions.
```

Formally:

```math
\Phi : X \to \mathbb{R}^m,\qquad m \ll n
```

with hard invariance:

```math
\forall T \in \mathcal{T},\quad \Phi(T(x)) = \Phi(x)
```

This means Φ defines the null space / conserved structure of allowed dynamics.

The supervisor must respect Φ, not optimize it.

## Required Tightening Before Option 2

### Composition Invariance

Φ must be invariant under arbitrary finite compositions of admissible operators:

```math
\forall k \in \mathbb{N},\ \forall T_1,\dots,T_k \in \mathcal{T}:\quad
\Phi(T_k \circ \dots \circ T_1(x)) = \Phi(x)
```

### Lumen Note

If every operator is exactly admissible and preserves Φ on every intermediate state, this follows by induction.

However, it must still be explicit in the architecture because real supervisors operate with:

```text
incremental moves
numerical tolerances
approximate equality
state-dependent admissibility
projection steps
optimizer loops
```

Without this explicit closure rule, a system can suffer death-by-gradient-descent drift: individually acceptable micro-moves accumulate into Φ violation.

## Option 2 Rule

```text
Φ does not appear in the objective function.
Ever.
```

Φ appears only as equality constraints defining the feasible set.

## QP Supervisor Form

The QP supervisor should solve:

```math
\begin{aligned}
\text{minimize}_{x'} \quad & f(x') \\
\text{subject to} \quad
& \Phi_M(x') = \Phi_M(x) \\
& \Phi_E(x') = \Phi_E(x) \\
& \Phi_I(x') = \Phi_I(x) \\
& \Phi_A(x') = \Phi_A(x) \\
& A x' \le b
\end{aligned}
```

Interpretation:

```text
Φ defines the allowed manifold.
A x' <= b defines situational guardrails.
f(x') may optimize efficiency, resilience, latency, fairness, or throughput.
But f may only optimize inside Φ.
```

## Sub-Kernel Notes

### Φ_M — Matter

```text
Topological rank invariance is the right invariant.
QP should not reason about raw topology, only allocations within it.
```

### Φ_E — Energy

```text
Energy is not just conservation; it is auditability.
Energy flows must be measured variables, not merely inferred.
Slack variables are dangerous unless physically grounded.
Treat Φ_E as hard equality, not soft penalty.
```

### Φ_I — Information

```text
Monotonicity is correct.
Rollback becomes non-feasible, not merely expensive.
This prevents classes of clever attacks.
```

### Φ_A — Agents

With:

```math
\sum_{i=1}^{N} w_i = W_{\text{total}}
```

Φ_A:

```text
prevents governance inflation
forces redistribution instead of accumulation
makes capture detectable as conservation violation
```

## Big Picture Split

```text
Φ  = identity as conserved structure
QP = behavior as optimization inside identity
```

This separates:

```text
who the system is      -> non-negotiable
what the system does   -> situational, optimizable
```

## Option 2 Lock Rules

```text
1. Φ invariance applies under composition.
2. Φ appears only as equality constraints.
3. Objectives optimize within Φ, never toward or against Φ.
```

## Implementation Warnings

```text
Do not make Φ a reward term.
Do not soften Φ into a penalty without explicit emergency protocol.
Do not allow accumulated tolerances to become invisible drift.
Do not allow local admissibility to bypass global composition invariance.
Do not let optimizer convenience redefine identity.
```

## Next Natural Work

```text
canonical QP objective library:
  efficiency
  resilience
  fairness
  latency
  throughput

existence / feasibility conditions:
  when is the constrained manifold non-empty?
  when do guardrails conflict with Φ?

failure modes:
  hard halt
  graceful degradation
  quarantine
  human-root review
  rollback refusal / forward-only repair
```

## Strongest Safe Claim

> Option 2 is unlocked once Φ is explicitly treated as composition-invariant conserved structure. QP supervisors may optimize situational objectives only inside the equality-constrained Φ manifold; Φ must never become an objective, reward, or soft preference.
