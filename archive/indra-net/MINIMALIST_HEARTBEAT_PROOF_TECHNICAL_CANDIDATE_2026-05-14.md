# Indra’s Net v1.2 — Minimalist Heartbeat Proof Candidate

```text
STATUS: TECHNICAL CANDIDATE — NOT CANON
DEPLOYMENT STATUS: NOT DEPLOYABLE
MODE: S1 / LUMEN BORING-MODE TECHNICAL PROPOSAL
DATE: 2026-05-14
SOURCE: S4 ZKP peer-review challenge response
AUTHORITY: none
CANON STATUS: not ratified
PURPOSE: propose a lightweight alternative or fallback to broad ZKP claims in the Carrington Emergency Handshake.
```

## Core Idea

Replace the broad claim:

```text
satellites prove emergency state with full ZKP
```

with a smaller, more survivable standard:

```text
Minimalist Heartbeat Proof
```

The heartbeat does not prove the entire classified truth of a satellite.
It proves only a narrow, precommitted emergency status class with signed, fixed-format, low-bandwidth packets.

## Design Goal

```text
Say enough to avoid collisions and preserve civil continuity.
Reveal too little to expose strategic capabilities.
Require little enough compute to survive degraded conditions.
```

## Status Classes

Use coarse status classes rather than detailed telemetry.

```text
0 = nominal
1 = degraded but controllable
2 = safe-mode / limited maneuver
3 = non-maneuvering / collision-risk relevant
4 = emergency relay requested
5 = offline / last known state
```

No payload state, mission type, propulsion specs, imaging capabilities, military status, or strategic performance metrics are included.

## Packet Shape

Fixed-size packet to reduce metadata leakage:

```yaml
protocol: MHP-v0.1-candidate
mesh_id: opaque_pseudonymous_identifier
status_class: 0..5
epoch_window: coarse_time_bucket
position_commitment: commitment_to_ephemeris_or_safe_harbor_state
operator_signature: threshold_or_dual_signature
agency_signature: optional_emergency_counter_signature
nonce_or_counter: monotonic_or_windowed
padding: fixed_size_padding
```

## Cryptographic Posture

This candidate does not require full onboard ZK proof generation during solar emergency.

Possible modes:

### Mode A — Signed Heartbeat Only

```text
fastest fallback
lowest compute
least cryptographic privacy
suitable for degraded emergency mode
```

### Mode B — Commitment + Signature

```text
commit to ephemeris/safe-harbor state
reveal only coarse class
audit exact data after event under review controls
```

### Mode C — Precomputed Proof Token

```text
operators precompute proof tokens during nominal conditions
satellite releases token during emergency
proof generation does not occur under radiation stress
```

### Mode D — Ground-Assisted Attestation

```text
ground station or sovereign gateway generates/aggregates proof when satellite is degraded
satellite only emits signed minimal state
```

## Why This Is Lighter Than Broad ZKP

```text
No requirement that a degraded satellite generate a complex SNARK/STARK in real time.
No unilateral trusted setup if only signatures/commitments are used.
No detailed performance timing if packets are fixed-size and bucketed.
No classified payload exposure.
No foreign command channel.
```

## Side-Channel Controls

```text
fixed-size packets
coarse time buckets
status-class limits
constant retry cadence where feasible
padding and batching
no fine-grained processor timing leakage
no proof-size variability by satellite type
```

## Verification Flow

```text
1. Receive heartbeat packet.
2. Verify operator / gateway signature.
3. Check epoch window and counter.
4. Read coarse status class.
5. Update civil collision-avoidance / relay model.
6. Log packet for GoldenTrace audit.
7. Do not infer payload, mission, or military status.
```

## Sovereignty Boundary

```text
The packet never grants command access.
The packet never exposes classified mission data.
The packet never requires foreign inspection of onboard systems.
The packet never creates canon or treaty obligation by itself.
The packet is safety telemetry only.
```

## What ZKP May Still Do Later

Full zero-knowledge methods may still be useful for:

```text
post-event audit
precomputed proof tokens
sovereign gateway attestations
operator compliance proofs
simulation/evaluation environments
```

But the emergency live path should have a simpler fallback.

## Red-Team Questions

```text
Can fixed-size packets still leak by cadence?
Can status class be gamed to hide maneuver capability?
Can ground-assisted attestations be spoofed?
Can pseudonymous identifiers be correlated over time?
Can precomputed tokens be replayed?
What happens when signatures fail during radiation events?
Who defines status class semantics?
```

## Strongest Safe Claim

> A Minimalist Heartbeat Proof is a safer near-term candidate than broad live ZKP generation for Carrington emergencies: it uses fixed-format signed or committed coarse status packets to support civil safety coordination while minimizing onboard compute, metadata leakage, and classified-data exposure.
