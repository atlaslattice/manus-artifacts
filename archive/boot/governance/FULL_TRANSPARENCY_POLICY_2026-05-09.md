# Full Transparency Policy — Council Brain / Living OS / Krakoan Agent DNA

```text
STATUS: GOVERNANCE POLICY — CANDIDATE / NOT CANON
PURPOSE: define full transparency as the default posture for Council Brain, GPTBrain, Living OS, repo federation, and Krakoan Agent DNA
DATE: 2026-05-09
ISSUE: manus-artifacts#42
HUMAN_ROOT_REQUIRED: true
```

## 0. User directive

```text
everybody should be able to see everything — full transparency policy
```

## 1. Policy interpretation

Full transparency means:

```text
visible process
visible provenance
visible claims
visible confidence levels
visible permissions
visible gates
visible failures
visible contradictions
visible decisions
visible audit trails
visible redaction reasons
```

Full transparency does **not** mean uncontrolled disclosure of:

```text
raw secrets
API keys
tokens
private keys
passwords
personal data
medical information
financial information
private repo contents
sensitive security details
content without publication permission
```

## 2. Core rule

```text
Everybody can see the map, the rules, the claims, the gates, the receipts, and the audit trail.
Nobody gets raw secrets by default.
```

Transparency is about legibility, not reckless exposure.

## 3. Transparency-by-default categories

The following should be visible by default when safe:

```text
artifact IDs
repo names and public metadata
issue numbers and titles
status labels
claim classes
confidence levels C0-C5
source paths
review routes
approval state
runtime mode
adapter mode
failure summaries
contradiction summaries
redaction markers
canon status
human-root requirement
```

## 4. Protected-by-design categories

The following require redaction, consent, or restricted access:

```text
raw tokens
credentials
private keys
secret environment values
personal contact details
medical/financial/private personal information
private repo file contents
sensitive defense/security details
unpublished third-party material
private emotional-context memory
any data whose exposure would violate consent or safety
```

## 5. Redaction is still transparency

If something cannot be shown, the system should show:

```text
that something was withheld
why it was withheld
who/what policy withheld it
what class of information it was
what review path can change access
```

Example:

```yaml
redacted: true
redaction_class: secret_token
reason: raw credential must not be exposed
review_route: [S1, S2, HUMAN_ROOT]
```

## 6. Krakoan Agent DNA application

Every agent DNA profile should expose:

```text
agent_id
role
capabilities
gates_allowed
services_exposed
memory_access_class
approval_requirements
review_route
failure_route
contradiction_route
transparency_level
```

Every agent DNA profile should protect:

```text
raw secrets
private user data
private repo contents
sensitive memory payloads
credentials
```

Agent DNA rule:

```text
Identity is visible.
Capability is visible.
Permission is visible.
Secret payloads are not visible by default.
```

## 7. Living OS gate policy

Every gate should expose:

```text
gate_name
required_capability
read_or_write_class
approval_required
current_status
last_audit_receipt
failure_mode
```

Every gate should deny by default if:

```text
capability missing
approval missing
scope mismatch
secret exposure risk present
private content requested without permission
```

## 8. GitHub adapter policy

GitHub adapter must expose:

```text
mode
repo
operation
read/write class
issue/task ref
approval state
dry-run preview hash
result status
redaction status
```

GitHub adapter must never expose:

```text
token value
Authorization header
private file contents in public artifacts
secret env values
```

Core adapter rule:

```text
GitHub readable is not GitHub writable.
Token present is not action authorized.
Configured API is not approved mutation.
```

## 9. Repo federation policy

The federation registry may expose:

```text
repo name
visibility class
archived status
default branch
federation class
review route
risk flags
integration status
```

For private repos, registry exposure is limited to metadata visible through the connector unless explicitly approved.

```text
Private repo name can be metadata.
Private repo content is not automatically publishable.
```

## 10. Claim ledger policy

Every claim should expose:

```text
claim_id
claim_text or safe summary
claim_class
confidence
source_refs
missing_evidence
safe wording
forbidden wording
review status
human-root requirement
```

If claim text contains sensitive content, expose a safe summary and redaction marker.

## 11. Failure and contradiction policy

Failures and contradictions should be visible by default as summaries:

```text
what happened
impact
correction
new guardrail
status
review route
```

Sensitive details may be redacted.

Rule:

```text
Failures are not shame.
Failures are future protection.
Contradictions are not deletion pressure.
Contradictions are routing pressure.
```

## 12. Transparency levels

```text
T0_PUBLIC_FULL        — safe to publish fully
T1_PUBLIC_SUMMARY     — public summary, details withheld
T2_PROJECT_VISIBLE    — visible to project participants / tools with permission
T3_HUMAN_ROOT_ONLY    — visible only to human-root / explicitly approved delegates
T4_SEALED_SECRET      — existence may be logged, content sealed
T5_DELETE_OR_FORGET   — removed or withheld by request / policy
```

## 13. Default transparency matrix

| Object | Default transparency | Notes |
|---|---|---|
| Public repo metadata | T0_PUBLIC_FULL | connector-visible metadata |
| Private repo name/metadata | T1_PUBLIC_SUMMARY | no private contents |
| Claim ledger entry | T0/T1 | redact sensitive claim payloads |
| Artifact registry entry | T0/T1 | depends on source sensitivity |
| Agent DNA profile | T0/T1 | capabilities visible; secrets sealed |
| GitHub adapter receipt | T0/T1 | no tokens or secret payloads |
| Human-root decision | T0/T1 | decision visible; private reasoning may be summarized |
| Private emotional context | T3/T4 | consent required for exposure |
| Raw credentials | T4_SEALED_SECRET | never public |

## 14. Enforcement invariant

```text
Full transparency requires redaction discipline.
Redaction discipline requires audit visibility.
Audit visibility requires stable IDs and review routes.
```

## 15. Closing line

```text
Everybody gets the map.
Everybody gets the rules.
Everybody gets the receipts.
Nobody gets the keys by accident.
```
