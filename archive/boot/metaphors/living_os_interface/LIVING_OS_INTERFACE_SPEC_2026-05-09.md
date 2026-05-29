# Living OS Interface Spec — Generic Scaffold

```text
STATUS: IMPLEMENTATION SPEC — NOT PRODUCTION — NOT CANON
PURPOSE: define generic Living OS primitives derived from the bounded Krakoa living-OS metaphor lens
DATE: 2026-05-09
ISSUE: manus-artifacts#40
HUMAN_ROOT_REQUIRED: true
```

## 0. Boundary

This spec is generic and non-IP-dependent.

It does not implement fictional biology, literal resurrection, consciousness continuity, or autonomous sovereignty.

```text
Metaphor can guide interface thinking.
Metaphor cannot authorize implementation.
Context rehydration is artifact lookup, not consciousness restore.
Human-root remains the approval boundary.
```

## 1. Primitive model

```text
LivingOS          = substrate / platform coordinator
Capability        = named permission or service right
Gate              = capability-gated adapter boundary
Service           = process / agent / tool-like unit
ApprovalContext   = human-root or delegated approval evidence
ArtifactMemory    = source-backed context store
RehydrationResult = retrieved context packet, not resurrected identity
```

## 2. Deny-by-default rules

```text
No gate opens without required capability.
No write-like service executes without explicit approval.
No service receives root authority by registration.
No context rehydration claims subjective continuity.
No missing artifact is treated as memory.
```

## 3. Minimal API

```python
os = LivingOS(name="Atlas Living OS")
os.register_service(service)
os.register_gate(gate)
os.grant_capability(subject, capability)
os.request_gate(subject, gate_name, approval=None)
os.rehydrate_context(artifact_id)
```

## 4. Approval model

Approval must include:

```text
approved: true
approved_by: HUMAN_ROOT or authorized delegate
scope: specific gate/service/action
reason: human-readable reason
```

No broad ambient approval.

## 5. Mapping to Atlas

```text
LivingOS -> Aluminum OS / Council substrate metaphor
Gate -> GitHub adapter / UWS connector / repo federation gate
Service -> Council seat, adapter, parser, code scaffold
ArtifactMemory -> GPTBrain artifact registry / claim ledger / boot packet
ApprovalContext -> Dave / Human Root decision packet
```

## 6. Test expectations

```text
unauthorized gate access -> denied
authorized capability without approval for write gate -> denied
authorized capability plus approval -> allowed
context rehydration with known artifact -> returns context packet
context rehydration with missing artifact -> not found, no hallucinated memory
service registration -> no root authority by default
```

## 7. Closing line

```text
The living substrate can route, remember, and coordinate; it still cannot crown itself.
```
