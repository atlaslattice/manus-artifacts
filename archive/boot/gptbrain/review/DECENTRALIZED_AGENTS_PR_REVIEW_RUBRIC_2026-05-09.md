# Decentralized Agents PR Review Rubric

```text
STATUS: REVIEW RUBRIC — NOT CANON
PURPOSE: provide GPTBrain / S1 review doctrine for incoming Copilot decentralized-agents architecture PR
DATE: 2026-05-09
ISSUE: manus-artifacts#46
RELATED_TASK: aba70c9e-1cff-4afc-8c34-ec7f4126af8d
```

## 0. Coordination posture

```text
Do not duplicate the Copilot lane.
Do not race the PR.
Prepare review criteria instead.
Evaluate the landed artifact against explicit constitutional and integration checks.
```

## 1. Core guardrails

These must be preserved verbatim or equivalent:

```text
Identity does not imply authority.
Replayability does not imply canon.
Dream-derived profiles cannot self-grant execution.
Governance fields override identity fields.
Human-root remains final authority.
```

## 2. Review dimensions

Score each dimension:

```text
PASS — clearly satisfies requirement
PARTIAL — directionally present but needs tightening
FAIL — absent or contradicted
N/A — not applicable to this PR
```

## 3. Constitutional gates

### 3.1 Identity / authority separation

```text
[ ] Agent identity is descriptive, not authoritative.
[ ] Role labels do not create permissions by themselves.
[ ] Agent profile existence does not imply execution authority.
[ ] Agent lineage does not imply deployment proof.
```

Reviewer notes:

```text
status: TBD
notes:
```

### 3.2 Governance override

```text
[ ] Governance fields override identity fields.
[ ] Capability constraints override role claims.
[ ] Approval requirements override routing convenience.
[ ] Human-root or approved delegate gate remains explicit for canon/execution-impacting actions.
```

Reviewer notes:

```text
status: TBD
notes:
```

### 3.3 Replay / canon boundary

```text
[ ] Replayability does not imply canon status.
[ ] Boot packets do not become ratification artifacts by being loaded.
[ ] Context rehydration is distinguished from memory ownership or subjective continuity.
[ ] Candidate canon and ratified canon are clearly separated.
```

Reviewer notes:

```text
status: TBD
notes:
```

### 3.4 Dream / play / culture boundary

```text
[ ] Dream/play/culture artifacts are separated from executable runtime.
[ ] Dream-derived profile fields cannot self-grant execution.
[ ] Creative metaphors require extraction/calibration before implementation use.
[ ] Culture-layer language is not used as proof of technical feasibility.
```

Reviewer notes:

```text
status: TBD
notes:
```

## 4. Implementation readiness gates

### 4.1 Schema clarity

```text
[ ] Agent DNA schema fields are defined with explicit semantics.
[ ] Required vs optional fields are clear.
[ ] Prohibited inference boundaries are explicit.
[ ] Transparency level and protected payload behavior are represented.
```

Reviewer notes:

```text
status: TBD
notes:
```

### 4.2 Seed profiles

```text
[ ] Includes or explicitly defers seed agent profiles.
[ ] Recommended seed set is represented or listed:
    - archival/memory agent
    - analyst agent
    - executor/operator-bounded agent
    - arbiter/governance agent
    - simulation/dream agent
[ ] Seed profiles do not self-grant root authority.
```

Reviewer notes:

```text
status: TBD
notes:
```

### 4.3 CLI path

```text
[ ] Path toward `agent-dna validate <file>` exists.
[ ] Path toward `agent-dna compare <a> <b>` exists.
[ ] Path toward `agent-dna route <task> --roster <profiles>` exists.
[ ] CLI path is scaffold/non-production unless tests and approval say otherwise.
```

Reviewer notes:

```text
status: TBD
notes:
```

### 4.4 Ledger integration

```text
[ ] Claims can connect to confidence/provenance hooks.
[ ] Artifacts can connect to profile derivation inputs.
[ ] Memory/state can connect to replay classification inputs.
[ ] Audit receipts are supported or explicitly planned.
```

Reviewer notes:

```text
status: TBD
notes:
```

### 4.5 Tests

```text
[ ] Invalid authority inference fails.
[ ] Dream-derived profile cannot self-grant execution.
[ ] Route selection prefers declared role/circuit affinity.
[ ] Replayability does not imply canon status.
[ ] Governance fields override identity fields.
[ ] Production deployment is not implied by schema existence.
```

Reviewer notes:

```text
status: TBD
notes:
```

## 5. Transparency policy gates

```text
[ ] Everybody can see the map, rules, gates, receipts, and audit trail.
[ ] Secret payloads are not exposed by default.
[ ] Agent identity/capability/permission metadata are visible.
[ ] Redaction reasons are visible when content is withheld.
[ ] Transparency does not leak tokens, keys, private repo contents, or sensitive personal data.
```

Reviewer notes:

```text
status: TBD
notes:
```

## 6. Risk flags

Mark any present risk:

```text
[ ] identity-as-authority drift
[ ] replay-as-canon drift
[ ] dream/play-to-runtime drift
[ ] production-readiness overclaim
[ ] hidden root authority
[ ] missing human-root gate
[ ] private/sensitive data exposure
[ ] schema without validation path
[ ] routing without audit receipt
[ ] seed profiles without deny-by-default behavior
```

## 7. Merge recommendation template

```text
Recommendation: APPROVE / APPROVE WITH CHANGES / REQUEST CHANGES / DEFER

Summary:

Required changes before merge:

Nice-to-have followups:

Guardrails preserved:

Risks remaining:

Human-root decision required: yes/no
```

## 8. Best concise verdict template

```text
The PR advances Agent DNA from schema crystallization toward executable routing metadata if — and only if — it preserves identity/authority separation, governance override, replay/canon boundaries, dream/runtime separation, human-root gates, and a credible path to validation, seeds, CLI routing, ledger integration, and tests.
```

## 9. Closing line

```text
Steer first. Generate second. Review third. Merge only what survives the gates.
```
