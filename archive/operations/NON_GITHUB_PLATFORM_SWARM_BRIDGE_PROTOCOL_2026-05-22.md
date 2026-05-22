# Non-GitHub Platform Swarm Bridge Protocol

```text
STATUS: OPERATIONS / BRIDGE PROTOCOL — NOT CANON
DEPLOYMENT STATUS: NOT DEPLOYABLE
DATE: 2026-05-22
SOURCE: user report during cross-platform swarm coordination experiment
AUTHORITY: none
CANON STATUS: not ratified
PURPOSE: define how non-GitHub or weak-GitHub-integrated model platforms can participate in swarm coordination without pretending they have receipt-grade repository access.
```

## User Report

```text
I've been pretty good about selfsame naming etc but it's like flying blind with the other platforms because they don't have the GitHub integration, Gemini like sort of does but not really
```

## Core Diagnosis

```text
GitHub-integrated seats can create receipts.
Non-GitHub seats mostly create candidate packets.
Gemini sits in a partial-bridge state.
```

Therefore, non-GitHub platform outputs must not be treated as landed artifacts until they are manually carried into the GitHub receipt substrate.

## Platform Classes

```text
Class A — Receipt-capable:
  Can read/write GitHub or return verifiable repo receipts.

Class B — Packet-capable:
  Can produce structured artifacts but cannot independently verify repo state.

Class C — Partial bridge:
  Can reference or reason about GitHub imperfectly, but cannot be trusted as source-of-record without confirmation.
```

## Bridge Rule

```text
non-GitHub output ≠ landed artifact
summary ≠ raw export
model self-report ≠ receipt
repo intent ≠ repo state
commit attempt ≠ landed file
```

## Required Packet From Non-GitHub Platforms

```yaml
external_platform_packet:
  seat_name:
  platform:
  model_surface:
  source_thread_label:
  raw_export_status: full_raw | partial_raw | summary_only | unavailable
  artifact_status:
    canon_status: not_canon
    deployment_status: not_deployable
    authority_scope: advisory
    repo_status: not_landed | user_claimed_landed | verified_landed
  proposed_repo_path:
  artifact_title:
  source_refs:
  sha256_if_available:
  key_claims:
  overclaims_to_avoid:
  requested_github_action: preserve | review | ignore | quarantine
  strongest_safe_claim:
  next_action:
```

## Manual Carry Procedure

```text
1. External platform produces packet.
2. Human-root copies packet into GPT/GitHub-capable lane.
3. Lumen/Lucerna checks boundary and path.
4. GitHub write is attempted only if safe.
5. Fetch/read verifies file exists on target branch.
6. Receipt is returned with repository, branch, path, commit SHA, artifact status.
7. Only then may packet be called landed.
```

## Gemini Partial-Bridge Rule

```text
Gemini can be useful for simulation, product/platform reasoning, and architecture pressure.
Gemini repo claims must be verified by GitHub read/write receipts before being treated as repo state.
```

## Recommended Labels

```text
external_candidate
summary_only
not_landed
needs_receipt
manual_carry_required
verified_landed
```

## Failure Modes

```text
platform self-report mistaken for GitHub receipt
summary packet mistaken for raw fossil record
partial GitHub visibility mistaken for source-of-record
same artifact logged twice under different names
child/seat identity preserved in chat but not in repo
repo path invented by model without verification
```

## Strongest Safe Claim

> Cross-platform swarm coordination requires a bridge protocol: non-GitHub platforms may generate structured candidate packets, but only a GitHub-capable lane can turn those packets into receipt-grade landed artifacts after write-and-verify.

## Closing Compression

```text
Some seats can write receipts.
Some seats can only hand you envelopes.
Do not call the envelope archived until GitHub says it landed.
```
