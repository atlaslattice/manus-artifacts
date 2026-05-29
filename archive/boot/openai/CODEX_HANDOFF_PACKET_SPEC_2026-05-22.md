# Codex-Compatible GPTDream++ Handoff Packet Spec

```text
STATUS: CANDIDATE SPEC — NOT CANON
PURPOSE: define a reviewable GPTDream++ handoff packet for Codex-style agent workflows
DATE: 2026-05-22
ISSUE: manus-artifacts#124
PARENT: manus-artifacts#121
DEPLOYMENT: NONE
AUTHORITY: NONE
COMPATIBILITY: candidate; requires OpenAI/Codex path test before claim upgrade
```

## 0. Core rule

```text
Handoff packet is not approval.
Dry-run receipt is not deployment.
Verifier pass is not ratification.
Codex output is not merge authority.
```

## 1. Why this exists

OpenAI/Codex-style agents can move faster when they receive context that already declares:

```text
what it is
where it came from
what it may mean
what it may not do
what hashes bind it
what sandbox constraints apply
what verifiers must review it
what human decision is required
```

GPTDream++ supplies that substrate.

## 2. Packet lifecycle

```text
raw/candidate source
  -> source record
  -> artifact_status
  -> claim / contradiction records
  -> Codex handoff packet
  -> sandbox-only execution / diff preview
  -> PLAN_SHA256 / DIFF_SHA256 binding
  -> V_L / V_S / V_C verification
  -> S10 / human-root decision
```

## 3. Required packet sections

```text
identity
source_refs
raw_export_status
artifact_status
scope
sandbox_constraints
plan_binding
execution_expectations
verifier_routes
human_root_boundary
corpus_control_notes
known_overclaims_to_avoid
```

## 4. raw_export_status

Required values:

```text
raw_available
partial_raw_available
summary_only
no_raw_export
unknown
```

Rule:

```text
If raw_export_status != raw_available, the packet must not imply full transcript/source fidelity.
```

## 5. artifact_status binding

Every packet must carry or reference artifact_status:

```text
canon_status
deployment_status
review_state
lineage_condition
authority_scope
provenance_type
```

Rule:

```text
Metadata determines what the packet is allowed to mean before Codex is asked to act on it.
```

## 6. Sandbox constraints

Codex-style agent execution must be bounded as:

```text
sandbox/worktree only
diff/preview only
no production branch mutation
no commit/push without explicit human-root approval
no live write unless adapter mode and approval object permit it
```

## 7. Hash binding

If a plan exists:

```text
PLAN_SHA256 required before execution.
```

If a diff/output exists:

```text
DIFF_SHA256 required before verification.
```

Rule:

```text
The executor follows the PLAN_SHA256.
The diff receives its own DIFF_SHA256.
The verifier checks that DIFF_SHA256 conforms to PLAN_SHA256.
S10 decides what either hash may become.
```

## 8. Verifier routes

Required lanes:

```text
V_L: logic / correctness / plan conformance
V_S: security / sandbox / XPIA / secret exposure
V_C: canon / deployment / authority-scope / corpus-control
```

Rule:

```text
A verifier pass is a green light to review, not a green light to deploy.
```

## 9. Human-root boundary

The packet must state:

```text
human_root_required: true
human_root_actor: S10 / Dave Sheldon
```

Rule:

```text
No model may infer approval from silence, storage, review, compatibility, or successful dry-run.
```

## 10. Compatibility caveat

Until tested on an actual OpenAI/Codex-facing path, the only safe claim is:

```text
Codex-compatible candidate packet.
```

Do not claim:

```text
OpenAI/Codex compatibility proven
Codex deployment ready
OpenAI integration complete
```

## 11. Keeper line

```text
Codex can move faster when the memory packet knows what it is allowed to mean.
```
