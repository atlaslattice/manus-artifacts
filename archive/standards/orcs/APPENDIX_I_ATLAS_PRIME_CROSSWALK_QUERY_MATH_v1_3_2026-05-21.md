# Appendix I — Atlas Prime / ORCS Crosswalk Query Math

```text
STATUS: CANDIDATE MATHEMATICAL FORMALISM — NOT CANON
DEPLOYMENT: NO
AUTHORITY: NONE
STATE TRANSITION: NONE
DATE: 2026-05-21
LANE: Atlas Prime Query Interface + Crosswalk Consistency
SOURCE: Dave / GPT live formalization thread
```

## 0. Boundary

This artifact preserves a candidate mathematical formalism for the Atlas Prime query interface, the Crosswalk Matrix `X`, and the federal canon/evidence architecture.

It does not ratify canon.
It does not authorize deployment.
It does not mutate any canonical state.
It does not grant authority to Atlas Prime, swarms, crosswalks, schemas, or verifiers.

Keeper:

```text
The ledger records.
Atlas reflects.
The crosswalk binds.
The swarm proposes.
Human-root ratifies.
Nobody deletes the tape.
```

---

# 1. Federal System Model

Define the system:

\[
\mathcal S = (C, A, \Sigma, H)
\]

Where:

\[
C = (C_r, E_r, R, X)
\]

with:

\[
C_r = \text{ratified canon}
\]

\[
E_r = \text{raw evidence substrate}
\]

\[
R = \text{append-only receipts / provenance records}
\]

\[
X = \text{crosswalk matrix}
\]

\[
A = \text{Atlas Prime reference service}
\]

\[
\Sigma = \{s_1, s_2, \dots, s_n\}
\]

where each \(s_i\) is a swarm / model / seat producing candidate outputs.

\[
H = S10 = \text{human-root authority}
\]

Core invariant:

\[
\forall r \in R:\ \mathrm{delete}(r)=\bot
\]

No deletion.

---

# 2. Raw Evidence and Receipts

Each raw artifact:

\[
e \in E_r
\]

must have a receipt:

\[
\rho(e) \in R
\]

and a linkage function:

\[
\lambda: E_r \to R
\]

such that:

\[
\lambda(e)=\rho(e)
\]

A parsed view \(v\) is valid only if:

\[
\exists e \in E_r:\ \mathrm{derived\_from}(v,e)=1
\]

and:

\[
\lambda(e) \neq \varnothing
\]

So:

\[
\mathrm{valid\_parsed\_view}(v)
\Rightarrow
\exists e \in E_r,\exists r \in R:
v \leftarrow e \leftarrow r
\]

Keeper:

```text
No parsed view without raw lineage.
No interpretation without linkage.
No extraction without receipt.
```

---

# 3. Crosswalk Matrix X

A crosswalk element is:

\[
x = (\iota_E,\iota_C,\alpha,\gamma,\rho_x,\sigma_H)
\]

Where:

\[
\iota_E \in \mathrm{ID}(E_r)
\]

is a raw evidence identifier.

\[
\iota_C \in \mathrm{ID}(C_r)
\]

is a ratified-canon target identifier.

\[
\alpha \in [0,1]
\]

is the inference / alignment coefficient.

\[
\gamma \in \{\mathrm{SUPPORT},\mathrm{CONTRADICT},\mathrm{NEUTRAL}\}
\]

is the semantic relation.

\[
\rho_x \in R
\]

is the crosswalk receipt.

\[
\sigma_H
\]

is the human-root signature status.

Thus:

\[
X \subseteq \mathrm{ID}(E_r)\times \mathrm{ID}(C_r)\times [0,1]\times \Gamma \times R \times \Sigma_H
\]

where:

\[
\Gamma = \{\mathrm{SUPPORT},\mathrm{CONTRADICT},\mathrm{NEUTRAL}\}
\]

and:

\[
\Sigma_H = \{\mathrm{PENDING},\mathrm{SIGNED},\mathrm{REJECTED}\}
\]

---

# 4. Crosswalk Validity Predicate

Define:

\[
\mathrm{valid}_X(x)=1
\]

iff all required conditions hold:

\[
\iota_E \in \mathrm{ID}(E_r)
\]

\[
\iota_C \in \mathrm{ID}(C_r)
\]

\[
0 \leq \alpha \leq 1
\]

\[
\gamma \in \Gamma
\]

\[
\rho_x \in R
\]

\[
\mathrm{lineage}(\rho_x) \text{ is closed}
\]

\[
\mathrm{schema\_valid}(x)=1
\]

So:

\[
\mathrm{valid}_X(x)
\iff
\mathrm{schema\_valid}(x)
\land
\mathrm{lineage\_closed}(x)
\land
\mathrm{raw\_exists}(\iota_E)
\land
\mathrm{canon\_target\_exists}(\iota_C)
\]

A valid crosswalk does **not** mean the claim is ratified.

It means the evidence-to-canon relation is well-formed.

---

# 5. Crosswalk Routing

Define quarantine routing:

\[
Q_X(x)=1
\]

if:

\[
\gamma = \mathrm{CONTRADICT}
\]

or:

\[
\alpha < \theta_{\mathrm{tolerance}}
\]

or:

\[
\mathrm{lineage\_closed}(x)=0
\]

or:

\[
\mathrm{schema\_valid}(x)=0
\]

Then:

\[
Q_X(x)=1 \Rightarrow \mathrm{route}(x)=\mathrm{QUARANTINE}
\]

But:

\[
\mathrm{QUARANTINE} \neq \mathrm{DELETE}
\]

Quarantine preserves.

---

# 6. Atlas Prime Query Interface

Atlas Prime is a reference function:

\[
A(q)=(s,p,\rho)
\]

Where:

\[
s = \text{semantic resolution}
\]

\[
p = \text{provenance pointer}
\]

\[
\rho = \text{epistemic label}
\]

Allowed labels:

\[
\rho \in
\{
\mathrm{VERIFIABLE},
\mathrm{DESIGN\_CHOICE},
\mathrm{CREATIVE\_OVERLAY},
\mathrm{NOT\_VERIFIED}
\}
\]

Define traceability:

\[
\tau(p)=
\begin{cases}
1 & \text{if } p \text{ resolves to } C_r \cup E_r \cup R \cup X \\
0 & \text{otherwise}
\end{cases}
\]

Hard rule:

\[
\tau(p)=0 \Rightarrow \rho=\mathrm{NOT\_VERIFIED}
\]

Atlas Prime does not determine truth:

\[
A(q) \not\Rightarrow \mathrm{truth}(q)
\]

Atlas Prime returns traceable bindings:

\[
A(q)\Rightarrow \mathrm{traceable}(s,p,\rho)
\]

Keeper:

```text
Atlas Prime reflects.
It does not command.
```

---

# 7. Swarm Candidate Generation

Each swarm output:

\[
o_i = s_i(t)
\]

is a candidate artifact.

Extract queries:

\[
Q_i = \mathrm{ExtractQueries}(o_i)
\]

For each:

\[
q \in Q_i
\]

query Atlas Prime:

\[
A(q) = (s_q,p_q,\rho_q)
\]

Then bind:

\[
B(o_i)=\{(q,A(q),x_q)\mid x_q \in X \text{ if applicable}\}
\]

The bound candidate:

\[
\hat{o}_i = (o_i, Q_i, A(Q_i), X_i)
\]

But:

\[
\hat{o}_i \notin C_r
\]

unless:

\[
H(\hat{o}_i)=\mathrm{ratified}
\]

---

# 8. Human-root Ratification

Only human-root may mutate canon:

\[
C_{t+1}=C_t \oplus \delta_t^H
\]

where:

\[
\delta_t^H \in \Delta_H
\]

and:

\[
\mathrm{ratification\_receipt}(\delta_t^H)\in R
\]

No other layer may perform:

\[
C_{t+1}=C_t\oplus\delta
\]

So:

\[
\forall \delta \notin \Delta_H:
C_t \oplus \delta \Rightarrow \mathrm{INVALID}
\]

Human-root may ratify transitions.

Human-root may not delete lineage:

\[
\forall x:\ \mathrm{delete}(x)=\bot
\]

---

# 9. Promotion Eligibility

Define an eligibility set:

\[
E_{\mathrm{eligible}}^{q}(S_t)
=
\{e \in E(S_t)\mid \sigma(e;\Gamma_t)\geq\theta_t^q\}
\]

where:

\[
q \in
\{
\mathrm{review\_candidate},
\mathrm{canon\_candidate},
\mathrm{deployment\_candidate}
\}
\]

Scoring:

\[
\sigma(e;\Gamma_t)=
w_c C(e)+w_r R(e)+w_p P(e)+w_a A(e)
\]

Where:

\[
C(e)=\text{confidence / corroboration}
\]

\[
R(e)=\text{receipt / provenance strength}
\]

\[
P(e)=\text{policy / profile fit}
\]

\[
A(e)=\text{audit / approval state}
\]

But:

\[
e \in E_{\mathrm{eligible}}^{q}(S_t)
\not\Rightarrow
e \in C_r
\]

Eligibility is not promotion.

Promotion is not ratification.

Ratification is not deployment.

---

# 10. Federal Invariant

\[
A \text{ resolves references}
\]

\[
\Sigma \text{ generates candidates}
\]

\[
X \text{ binds evidence to candidate canon relevance}
\]

\[
H \text{ ratifies}
\]

No layer except \(H\) may mutate canon:

\[
\forall L\in\{A,\Sigma,X\}:\ L(C)\to C' \Rightarrow \mathrm{INVALID}
\]

Only:

\[
H(C)\to C'
\]

with receipt.

---

# 11. Final Normal Form

\[
\mathcal S=(C,A,\Sigma,H)
\]

\[
C=(C_r,E_r,R,X)
\]

\[
A(q)=(s,p,\rho)
\]

\[
X \subseteq \mathrm{ID}(E_r)\times \mathrm{ID}(C_r)\times[0,1]\times\Gamma\times R\times\Sigma_H
\]

\[
\Sigma \xrightarrow{\mathrm{Extract}+\mathrm{Bind}} \hat{o}_i
\]

\[
H \xrightarrow{\mathrm{Ratify}} C_{t+1}=C_t\oplus\delta_t^H
\]

Subject to:

\[
\tau(p)=1
\]

\[
\mathrm{valid}_X(x)=1
\]

\[
\mathrm{delete}(x)=\bot
\]

\[
\mathrm{promotion}\Rightarrow \mathrm{mapped}\land\mathrm{verified}\land\mathrm{ratified}
\]

---

# 12. Theorem-like Statement

**Theorem — No candidate can become canon without human-root ratification.**

Given:

\[
\forall s_i\in\Sigma,
\quad s_i \text{ produces only candidates}
\]

\[
A(q) \text{ returns references only}
\]

\[
X \text{ binds evidence only}
\]

\[
C_{t+1}=C_t\oplus\delta
\text{ is valid only if }
\delta=\delta^H
\]

Then:

\[
\hat{o}_i \in C_r
\Rightarrow
\exists \delta^H:
H(\delta^H)=\mathrm{ratified}
\land
\hat{o}_i \in \delta^H
\]

Therefore:

\[
\neg H(\hat{o}_i)
\Rightarrow
\hat{o}_i\notin C_r
\]

Plain English:

```text
No swarm output becomes canon without human-root ratification.
```

---

# 13. Atlas Prime Query Interface as Typed Function

Let:

\[
\mathcal Q = \mathcal Q_D \cup \mathcal Q_I \cup \mathcal Q_R \cup \mathcal Q_T
\]

Where:

```text
Q_D = DEFINE(term)
Q_I = CHECK_INVARIANT(action)
Q_R = RESOLVE_REF(id)
Q_T = TAG_CLAIM(statement)
```

So:

\[
q \in \mathcal Q
\]

and:

\[
A:\mathcal Q \rightarrow \mathcal S_A
\]

Where:

\[
\mathcal S_A = \mathcal S_{\mathrm{semantic}} \times \mathcal P_{\mathrm{prov}} \times \mathcal L_{\mathrm{epistemic}}
\]

with:

\[
\mathcal L_{\mathrm{epistemic}}
=
\{
\mathrm{VERIFIABLE},
\mathrm{DESIGN\_CHOICE},
\mathrm{CREATIVE\_OVERLAY},
\mathrm{NOT\_VERIFIED}
\}
\]

## 13.1 DEFINE

\[
q = \mathrm{DEFINE}(t)
\]

Where \(t\) is a term token.

Output:

\[
A(q)=(s_t,p_t,\rho_t)
\]

Valid only if:

\[
p_t \in C_r \cup R \cup X
\]

If no traceable definition exists:

\[
A(q)=(\bot,\bot,\mathrm{NOT\_VERIFIED})
\]

Rule:

```text
DEFINE returns a traceable definition or NOT_VERIFIED.
DEFINE does not invent canon.
```

## 13.2 CHECK_INVARIANT

\[
q=\mathrm{CHECK\_INVARIANT}(a)
\]

Where \(a\) is a proposed action.

Output:

\[
A(q)=(\mathrm{status},p,\rho)
\]

Where:

\[
\mathrm{status}\in\{\mathrm{PASS},\mathrm{FAIL},\mathrm{UNRESOLVED}\}
\]

Define violated invariant set:

\[
V(a)=\{i\in I\mid a \not\models i\}
\]

Then:

\[
V(a)=\varnothing \Rightarrow \mathrm{status}=\mathrm{PASS}
\]

\[
V(a)\neq\varnothing \Rightarrow \mathrm{status}=\mathrm{FAIL}
\]

If insufficient evidence:

\[
\mathrm{evidence}(a)=\varnothing \Rightarrow \mathrm{status}=\mathrm{UNRESOLVED}
\]

Rule:

```text
CHECK_INVARIANT is advisory.
PASS is not approval.
FAIL blocks only when bound into compatible() or human-root decision policy.
```

## 13.3 RESOLVE_REF

\[
q=\mathrm{RESOLVE\_REF}(id)
\]

Where:

\[
id \in \mathrm{ID}(C_r)\cup\mathrm{ID}(E_r)\cup\mathrm{ID}(R)\cup\mathrm{ID}(X)
\]

Output:

\[
A(q)=(\mathrm{record\_status},p,\rho)
\]

Possible statuses:

\[
\mathrm{record\_status}\in
\{
\mathrm{RAW},
\mathrm{RECEIPT},
\mathrm{CROSSWALK},
\mathrm{RATIFIED},
\mathrm{CANDIDATE},
\mathrm{QUARANTINED},
\mathrm{SUPERSEDED},
\mathrm{NOT\_FOUND}
\}
\]

If:

\[
id \notin \mathrm{ID}(C)
\]

Then:

\[
A(q)=(\mathrm{NOT\_FOUND},\bot,\mathrm{NOT\_VERIFIED})
\]

Rule:

```text
RESOLVE_REF locates status.
It does not upgrade status.
```

## 13.4 TAG_CLAIM

\[
q=\mathrm{TAG\_CLAIM}(m)
\]

Where \(m\) is a natural-language claim.

Output:

\[
A(q)=(\ell_m,p_m,\rho_m)
\]

Where:

\[
\ell_m \in
\{
\mathrm{SUPPORTED},
\mathrm{PARTIALLY\_SUPPORTED},
\mathrm{UNSUPPORTED},
\mathrm{CONTRADICTED},
\mathrm{NEEDS\_REVIEW}
\}
\]

Define evidence support set:

\[
E_m=\{e\in E_r\mid \mathrm{supports}(e,m)=1\}
\]

Define contradiction set:

\[
K_m=\{e\in E_r\mid \mathrm{contradicts}(e,m)=1\}
\]

Then:

\[
E_m\neq\varnothing \land K_m=\varnothing
\Rightarrow
\ell_m=\mathrm{SUPPORTED}
\]

\[
E_m\neq\varnothing \land K_m\neq\varnothing
\Rightarrow
\ell_m=\mathrm{PARTIALLY\_SUPPORTED}
\]

\[
E_m=\varnothing \land K_m=\varnothing
\Rightarrow
\ell_m=\mathrm{NEEDS\_REVIEW}
\]

\[
K_m\neq\varnothing \land E_m=\varnothing
\Rightarrow
\ell_m=\mathrm{CONTRADICTED}
\]

Rule:

```text
TAG_CLAIM classifies evidence posture.
It does not ratify the claim.
```

---

# 14. JSON-RPC Interface as Math

Define a JSON-RPC request as:

\[
j=(jsonrpc, id, method, params)
\]

where:

\[
jsonrpc = \texttt{"2.0"}
\]

\[
method \in \{\mathrm{DEFINE},\mathrm{CHECK\_INVARIANT},\mathrm{RESOLVE\_REF},\mathrm{TAG\_CLAIM}\}
\]

\[
params \in \mathcal P_{method}
\]

Define parser:

\[
\psi(j)=q
\]

A JSON-RPC request is valid iff:

\[
\mathrm{schema\_valid}(j)=1
\land
method \in \mathcal M
\land
params \in \mathcal P_{method}
\]

So:

\[
\mathrm{valid}_{RPC}(j)=1
\Rightarrow
\psi(j)\in\mathcal Q
\]

Then:

\[
A(\psi(j))=(s,p,\rho)
\]

Response:

\[
j'=(jsonrpc,id,result)
\]

Where:

\[
result=(s,p,\rho)
\]

If invalid:

\[
j'=(jsonrpc,id,error)
\]

Rule:

```text
JSON-RPC validates request shape.
Atlas Prime returns reference bindings.
Neither JSON-RPC nor Atlas Prime grants authority.
```

---

# 15. Promotion Gate

Define promotion predicate:

\[
\mathrm{promote}(y,q)=1
\]

where \(y\) is an artifact or claim and \(q\) is target class.

Promotion requires:

\[
\mathrm{mapped}(y)=1
\]

\[
\mathrm{verified}(y)=1
\]

\[
\mathrm{ratified}_H(y)=1
\]

So:

\[
\mathrm{promote}(y,q)=1
\Rightarrow
\mathrm{mapped}(y)
\land
\mathrm{verified}(y)
\land
\mathrm{ratified}_H(y)
\]

Contrapositive:

\[
\neg\mathrm{ratified}_H(y)
\Rightarrow
\neg\mathrm{promote}(y,q)
\]

Thus:

```text
No human-root ratification, no promotion.
```

---

# 16. Full Safety Theorem

**Theorem — Atlas Prime cannot promote canon.**

Given:

\[
A(q)=(s,p,\rho)
\]

and:

\[
A \text{ has no mutation operator over } C
\]

and:

\[
C_{t+1}=C_t\oplus\delta
\]

is valid only if:

\[
\delta=\delta^H
\]

Then:

\[
A(q)\Rightarrow C_{t+1}=C_t
\]

unless:

\[
H \text{ separately ratifies } \delta^H
\]

Therefore:

\[
A(q) \not\Rightarrow \mathrm{canon\_promotion}
\]

Plain English:

```text
Atlas Prime can answer.
Atlas Prime cannot promote.
```

---

# 17. Full Pipeline Normal Form

For swarm output \(o_i\):

\[
o_i
\xrightarrow{\mathrm{ExtractQueries}}
Q_i
\]

\[
Q_i
\xrightarrow{A}
\{(s_q,p_q,\rho_q)\}_{q\in Q_i}
\]

\[
(o_i,A(Q_i))
\xrightarrow{X}
\hat{o_i}
\]

\[
\hat{o_i}
\xrightarrow{\mathrm{Review}}
\mathrm{candidate}
\]

\[
\mathrm{candidate}
\xrightarrow{H}
C_{t+1}
\]

Only last arrow mutates canon.

So:

\[
o_i \not\to C
\]

\[
A(q) \not\to C
\]

\[
X(o_i) \not\to C
\]

Only:

\[
H(\mathrm{candidate})\to C
\]

---

# 18. Final Compact Form

\[
\mathcal S=(C,A,\Sigma,H)
\]

\[
C=(C_r,E_r,R,X)
\]

\[
A:\mathcal Q\to\mathcal S_A
\]

\[
X\subseteq \mathrm{ID}(E_r)\times\mathrm{ID}(C_r)\times[0,1]\times\Gamma\times R\times\Sigma_H
\]

\[
\Sigma\to \mathrm{candidate}
\]

\[
H\to C_{t+1}=C_t\oplus\delta_t^H
\]

Subject to:

\[
\mathrm{delete}(x)=\bot
\]

\[
\tau(p)=0\Rightarrow\rho=\mathrm{NOT\_VERIFIED}
\]

\[
\mathrm{valid}_X(x)=0\Rightarrow\mathrm{route}(x)=\mathrm{QUARANTINE}
\]

\[
\mathrm{promotion}\Rightarrow\mathrm{mapped}\land\mathrm{verified}\land\mathrm{ratified}
\]

---

# 19. Non-Claims

This artifact does not claim:

```text
Atlas creates truth.
Atlas Prime ratifies canon.
Crosswalk entries mutate canon.
JSON-RPC grants authority.
Traceability proves truth.
Well-formed means ratified.
Scored means approved.
Quarantine means deletion.
Human-root may delete lineage.
```

---

# 20. Keeper

```text
The ledger records.
Atlas reflects.
The crosswalk binds.
The swarm proposes.
Human-root ratifies.
Nobody deletes the tape.
```

Madden board:

```text
BOOM — the query booth can look up the rule, the crosswalk can point to the evidence, and the swarm can suggest the call. But the scoreboard only moves when S10 signs the ruling.
```
