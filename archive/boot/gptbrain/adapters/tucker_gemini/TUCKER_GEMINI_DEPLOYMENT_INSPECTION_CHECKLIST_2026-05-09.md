# Tucker / Gemini Deployment Inspection Checklist

```text
STATUS: DEPLOYMENT INSPECTION CHECKLIST — NOT CANON
MODE: WORK_OUTPUT
DATE: 2026-05-09
SCOPE: Tucker/Gemini adapter deployability inspection
RELATED_ISSUES: manus-artifacts#22, #25, #26
DEPLOYMENT_STATUS: NOT DEPLOY-READY BY ITSELF
SWARM_STATUS: BLOCKED / NOT APPLICABLE FROM CURRENT EVIDENCE
HUMAN_ROOT_GATE: required before deployment or live Gemini execution
```

## 0. Purpose

This checklist exists to prevent a false upgrade from:

```text
adapter scaffold exists
```

to:

```text
service is deployable
```

The Tucker/Gemini lane has meaningful implementation scaffold progress, but current evidence does not establish deployment readiness, Swarm readiness, or production authorization.

## 1. Current safe classification

```text
Activity type: adapter scaffold + cross-repo provenance wiring
Implementation status: meaningful progress
Deployment readiness: still not deploy-ready by itself
Swarm readiness: still blocked / not applicable from current evidence
```

## 2. Concrete artifacts now available

```text
archive/boot/gptbrain/adapters/tucker_gemini/README.md
archive/boot/gptbrain/adapters/tucker_gemini/TUCKER_GEMINI_RUNTIME_ADAPTER_SPEC_2026-05-09.md
archive/boot/gptbrain/adapters/tucker_gemini/tucker_gemini_adapter.py
archive/boot/gptbrain/adapters/tucker_gemini/test_tucker_gemini_adapter.py
archive/boot/gptbrain/adapters/tucker_gemini/source_manifest.yaml
```

## 3. Supported adapter modes

```text
REPO_TRACE_ONLY
DRY_RUN_ONLY
MOCK_GEMINI
LIVE_GEMINI — blocked by default
```

## 4. Deployment inspection questions

### 4.1 Service boundary

```text
[ ] Is the adapter intended to remain library-only?
[ ] Is there a service process that should consume it?
[ ] Is there a CLI entrypoint?
[ ] Is there an HTTP/MCP/server entrypoint?
[ ] Is Tucker itself invoked, or only referenced as provenance?
[ ] Is Gemini live execution in scope or explicitly deferred?
```

Current assessment:

```text
Library/scaffold only from current evidence. No service boundary proven.
```

### 4.2 Packaging

```text
[ ] pyproject.toml / setup.cfg / requirements.txt exists for this adapter
[ ] dependencies are explicit
[ ] Python version is pinned
[ ] import paths work from repo root and adapter directory
[ ] adapter can be installed or invoked consistently
[ ] package name / module namespace is defined
```

Current assessment:

```text
Not proven. Existing tests imply local execution, not deploy packaging.
```

### 4.3 Containerization

```text
[ ] Dockerfile exists
[ ] base image pinned
[ ] non-root user configured where feasible
[ ] build context minimized
[ ] local docker build tested
[ ] container runs tests successfully
[ ] container starts a defined process
```

Current assessment:

```text
No container build definition observed for Tucker/Gemini adapter lane.
```

### 4.4 Swarm / Compose

```text
[ ] docker-compose.yml or docker-stack.yml exists
[ ] service image tag defined
[ ] networks defined
[ ] volumes defined
[ ] restart policy defined
[ ] resource limits defined
[ ] rollback config defined
[ ] placement constraints defined or explicitly deferred
```

Current assessment:

```text
No Swarm or Compose manifest observed for this adapter lane.
```

### 4.5 Config and secrets

```text
[ ] required env vars documented
[ ] GEMINI_API_KEY handling documented
[ ] GEMINI_API_KEY presence does not authorize live calls
[ ] live execution requires human-root approval
[ ] secrets never committed
[ ] Docker secrets or equivalent strategy defined
[ ] secret rotation plan exists or explicitly deferred
```

Current assessment:

```text
Safety boundary exists. Deployment-grade secrets policy not yet implemented.
```

### 4.6 Health, logs, telemetry

```text
[ ] readiness check exists
[ ] liveness check exists
[ ] logs go to stdout/stderr or documented sink
[ ] structured audit receipts are persisted or emitted
[ ] failure modes are observable
[ ] metrics are defined or explicitly deferred
```

Current assessment:

```text
Adapter receipts exist conceptually. Service health/telemetry not established.
```

### 4.7 Runtime validation

```text
[ ] unit tests pass locally
[ ] CI runs adapter tests
[ ] dry-run mode tested
[ ] mock mode tested
[ ] live mode blocked by default tested
[ ] no-network/no-secrets test enforced
[ ] smoke test exists for chosen service boundary
```

Current assessment:

```text
Unit-test scaffold exists. CI integration still pending after S7 hygiene checks stabilize.
```

### 4.8 Security / permissions

```text
[ ] live Gemini execution disabled by default
[ ] Tucker code invocation disabled by default
[ ] data sent externally is summarized and approval-gated
[ ] audit event generated for proposed live call
[ ] filesystem/network scopes documented
[ ] least-privilege execution plan exists
```

Current assessment:

```text
Core safety invariants are present. Deployment permission model still needs formalization.
```

### 4.9 Rollback and operator workflow

```text
[ ] preflight checklist exists
[ ] deploy command documented
[ ] rollback command documented
[ ] operator go/no-go checkpoint documented
[ ] expected successful output documented
[ ] expected failure output documented
```

Current assessment:

```text
Not present. Deployment remains blocked.
```

## 5. Deployment blockers

```text
BLOCKER 1 — No service boundary proven.
BLOCKER 2 — No container/Swarm manifest.
BLOCKER 3 — No deployment secrets policy.
BLOCKER 4 — No healthcheck/readiness endpoint.
BLOCKER 5 — No rollback procedure.
BLOCKER 6 — No CI evidence attached to deployment path.
BLOCKER 7 — Human-root approval not requested or granted for live execution.
```

## 6. Preserved guardrails

```text
Tucker referenced is not Tucker invoked.
Gemini configured is not Gemini authorized.
Readable provenance is not executable permission.
Adapter scaffold is not deploy readiness.
Mock output is not model output.
Dry-run receipt is not live execution.
```

## 7. Recommended next steps

```text
1. Keep Tucker/Gemini classified as scaffold, not deployable service.
2. Add adapter tests to CI after PR #15 stabilizes.
3. Add claim/artifact registry entries with commit SHA provenance.
4. Decide whether adapter should remain library-only or become a service.
5. If service-capable, create a separate deployment-design issue before Docker/Swarm work.
6. Do not enable LIVE_GEMINI until human-root approval, secrets policy, audit receipt, and tests exist.
```

## 8. Status line

```text
Real wiring, no overclaim.
Strong scaffold progress, still not deploy-ready by itself.
```
