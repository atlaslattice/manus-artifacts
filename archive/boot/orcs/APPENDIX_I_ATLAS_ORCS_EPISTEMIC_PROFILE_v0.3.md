# Appendix I — Atlas / ORCS Epistemic Profile v0.3

```text
STATUS: CANDIDATE — NOT CANON — NON-DEPLOYABLE
VERSION: APPENDIX I v0.3 — PATCHED BINDER-GRADE DRAFT
CANON: NO
DEPLOYMENT: NO
AUTHORITY: FORMALIZATION ONLY
ACTION: SAVED AS CLEAN ARTIFACT
```

## Purpose

This appendix formalizes the Atlas / ORCS epistemic profile as a candidate mathematical and ledger-facing description of state transition, evidence eligibility, cryptographic anchoring, and promotion-target separation.

It is not canon. It is not a deployment artifact. It does not authorize runtime behavior, governance promotion, or production launch.

## Final patch applied

The prior notation:

```math
S_t^* = \{ e \in E(S_t) \mid \sigma(e;\Gamma_t) \ge \theta_t \}
```

is replaced with:

```math
E_t^{q,*} = \{ e \in E(S_t) \mid \sigma(e;\Gamma_t) \ge \theta_t \}
```

Reason:

```text
S_t^* could be mistaken for a transformed state.
E_t^{q,*} clearly denotes the eligible evidence set for promotion target q.
```

The promotion target class `q` is preserved through the compressed form:

```math
E_t^{q,*} = \Pi_{\Gamma_t}^{q}(S_t) \subseteq E(S_t)
```

This preserves target-class distinction and prevents all promotions from collapsing into one generic move.

## Clean final compression

```math
S_{t+1} = S_t \oplus \delta_t
```

```math
E_t^{q,*} = \{ e \in E(S_t) \mid \sigma(e; \Gamma_t) \ge \theta_t \}
```

```math
\kappa_t = H(\"STATEv1\" \mid \kappa_{t-1} \mid H(\"DELTAv1\" \mid canon(\delta_t)) \mid t \mid policy_t)
```

```math
E_t^{q,*} \subseteq E(S_t)
```

Equivalent target-class operator form:

```math
E_t^{q,*} = \Pi_{\Gamma_t}^{q}(S_t) \subseteq E(S_t)
```

## Interpretation

### State transition

```math
S_{t+1} = S_t \oplus \delta_t
```

The next state is produced by applying a bounded delta to the prior state. This does not imply canon promotion by itself.

### Eligible evidence set

```math
E_t^{q,*} = \{ e \in E(S_t) \mid \sigma(e; \Gamma_t) \ge \theta_t \}
```

The eligible evidence set contains only evidence records from the current evidence space whose score under governance context `\Gamma_t` meets or exceeds threshold `\theta_t` for promotion target `q`.

### Cryptographic state anchor

```math
\kappa_t = H(\"STATEv1\" \mid \kappa_{t-1} \mid H(\"DELTAv1\" \mid canon(\delta_t)) \mid t \mid policy_t)
```

The state anchor commits to:

```text
prior anchor
canonicalized delta hash
time/index t
active policy context
```

This provides ledger continuity without implying that the ledger itself promotes canon.

### Evidence subset rule

```math
E_t^{q,*} \subseteq E(S_t)
```

Eligible promotion evidence must remain a subset of existing state evidence. Promotion eligibility does not create evidence ex nihilo.

## Guardrails

```text
Storage is not ratification.
Review is not ratification.
Provenance is not ratification.
Hash anchoring is not deployment proof.
Evidence eligibility is not canon promotion.
Only explicit human-root promotion creates canon.
```

## Driftmarker ruling

```text
SAVE AS:
APPENDIX_I_ATLAS_ORCS_EPISTEMIC_PROFILE_v0.3.md

STATUS:
CANDIDATE — NOT CANON — NON-DEPLOYABLE

PATCH APPLIED:
S_t^* -> E_t^{q,*}

KEEPER:
The ledger records.
Atlas promotes.
ORCS governs.
CAS anchors.
Nobody pretends the scoreboard created the game.
```

## Final boundary

No ratification. No launch. No deployment claim.
