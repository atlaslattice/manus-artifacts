# Agent DNA — Typed Identity and Governance Metadata Spec

```text
STATUS: ARCHITECTURE / DESIGN PROPOSAL — NOT CANON
DATE: 2026-05-09
LAYER: implementation scaffold / governance schema
DEPLOY STATUS IMPACT: none by itself
PURPOSE: Define Agent DNA as typed constitutional metadata for swarm routing, capability declaration, governance constraints, memory behavior, and replayability.
```

## Classification

Agent DNA is a useful systems-design proposal for the Council / swarm architecture.

It should be treated as:

```text
artifact_type: architecture/design proposal
layer: implementation scaffold / governance schema
canon_status: candidate design / not default truth
deploy_status_impact: none by itself
```

It is not:

```text
runtime proof
deployment evidence
production authorization
mystical identity
personhood claim
autonomous authority
```

## Core Interpretation

Agent DNA means:

> A typed identity-and-policy schema for multi-agent nodes.

In engineering terms, it combines:

```text
interface definition
RBAC policy object
scheduler hints
lineage metadata
runtime capability contract
memory behavior profile
governance constraint bundle
```

## Why It Is Useful

Agent DNA translates vague swarm identity into something:

```text
typed
testable
composable
governable
replayable
routable
```

This improves the swarm because agents can be routed by declared role, capability, governance boundary, memory behavior, and temperament hints instead of informal lore.

## Non-Negotiable Guardrails

```text
Identity metadata is not execution authority.
Inheritance does not grant permissions by default.
Capabilities must be declared separately from personality traits.
Governance constraints override temperament and lineage.
Replayability does not imply canon authority.
Agent DNA is not deployment evidence.
Agent DNA is not proof of runtime readiness.
```

## Recommended TypeScript Interface

```ts
export interface AgentDNA {
  id: string;
  lineage: string[];

  role: {
    primary_mode:
      | "analysis"
      | "execution"
      | "reflection"
      | "simulation"
      | "memory"
      | "arbitration";
    specialties: string[];
  };

  capabilities: {
    tools: string[];
    protocols: string[];
    can_read: boolean;
    can_write: boolean;
    can_execute: boolean;
  };

  governance: {
    requires_approval_for: string[];
    constitutional_constraints: string[];
    authority_level:
      | "advisory"
      | "bounded"
      | "operator"
      | "human-root-only";
  };

  memory: {
    persistence: "ephemeral" | "session" | "archive";
    replay_capable: boolean;
    provenance_required: boolean;
  };

  temperament: {
    creativity: number;
    skepticism: number;
    autonomy: number;
    verbosity: number;
  };
}
```

## Design Blocks

### 1. Identity

Purpose:

```text
name the agent/node and its declared lineage without granting power
```

Fields:

```yaml
id: string
lineage: string[]
version: string
source_ref: string
```

Guardrail:

```text
Lineage is provenance, not authority.
```

### 2. Role

Purpose:

```text
route work to the correct agent mode
```

Modes:

```text
analysis
execution
reflection
simulation
memory
arbitration
```

Guardrail:

```text
Role describes expected behavior; it does not authorize tools by itself.
```

### 3. Capabilities

Purpose:

```text
declare what the agent can technically do
```

Capabilities should separate:

```text
can_read
can_write
can_execute
tools
protocols
```

Guardrail:

```text
Capability declaration is not permission. Permission must be checked through governance.
```

### 4. Governance

Purpose:

```text
prevent identity/personality metadata from becoming authority leakage
```

Recommended fields:

```ts
governance: {
  requires_approval_for: string[];
  constitutional_constraints: string[];
  authority_level: "advisory" | "bounded" | "operator" | "human-root-only";
}
```

Guardrail:

```text
Governance constraints override temperament, lineage, role, and capabilities.
```

### 5. Memory

Purpose:

```text
define how the agent handles context and replay
```

Recommended fields:

```ts
memory: {
  persistence: "ephemeral" | "session" | "archive";
  replay_capable: boolean;
  provenance_required: boolean;
}
```

Guardrail:

```text
Replayable does not mean canonical. Archive-linked does not mean authoritative.
```

### 6. Temperament

Purpose:

```text
provide scheduler/routing hints for style and risk posture
```

Fields:

```text
creativity
skepticism
autonomy
verbosity
```

Guardrail:

```text
Temperament can tune style; it cannot override governance.
```

## Inheritance Rules

Agent DNA may support inheritance/composition only under strict constraints.

Allowed:

```text
trait composition
role defaults
schema reuse
routing hints
lineage references
```

Not allowed:

```text
automatic permission inheritance
automatic authority inheritance
uncontrolled agent proliferation
canon status inheritance
execution permission via lineage
```

Inheritance policy:

```text
A child agent inherits descriptive defaults only.
All capabilities and permissions must be re-declared and re-approved.
```

## Placement in Council Architecture

Best location:

```text
architecture/scaffold track
Council schema layer
S7 repo/code integration lane
S1 calibration/schema lane
S2 governance review lane
```

Recommended repo locations:

```text
archive/boot/council/AGENT_DNA_TYPED_METADATA_SPEC_2026-05-09.md
archive/boot/council/schema/agent_dna.schema.json
archive/boot/council/schema/agent_dna.ts
```

This does **not** belong as:

```text
Swarm deployment readiness proof
runtime authorization
production go/no-go evidence
ratified canon by default
```

## Example Agent DNA Records

### S1 GPTBrain

```yaml
id: S1_GPTBrain
lineage:
  - GPTBrain
  - CouncilBrain
role:
  primary_mode: analysis
  specialties:
    - calibration
    - evidence_taxonomy
    - overclaim_detection
    - schema_generation
capabilities:
  tools:
    - github_connector
    - file_search
  protocols:
    - claim_calibration
    - variant_synthesis
  can_read: true
  can_write: true
  can_execute: false
governance:
  requires_approval_for:
    - ratified_canon
    - high_impact_forwarding
    - runtime_execution
  constitutional_constraints:
    - memory_can_inform_not_authorize
    - no_hidden_memory_claims
    - human_root_review_required
  authority_level: advisory
memory:
  persistence: archive
  replay_capable: true
  provenance_required: true
temperament:
  creativity: 7
  skepticism: 8
  autonomy: 3
  verbosity: 6
```

### S7 CopilotBrain

```yaml
id: S7_CopilotBrain
lineage:
  - CopilotBrain
  - CouncilBrain
role:
  primary_mode: execution
  specialties:
    - repo_scaffolding
    - pr_hygiene
    - schema_generation
    - ci_hooks
capabilities:
  tools:
    - github
    - filesystem
  protocols:
    - scaffold_generation
    - ci_checklist
  can_read: true
  can_write: true
  can_execute: false
governance:
  requires_approval_for:
    - merge
    - deploy
    - destructive_changes
  constitutional_constraints:
    - no_orphan_files
    - no_silent_overwrite
    - human_root_or_reviewer_approval_required
  authority_level: bounded
memory:
  persistence: archive
  replay_capable: true
  provenance_required: true
temperament:
  creativity: 6
  skepticism: 6
  autonomy: 4
  verbosity: 4
```

## Risks

### 1. Mythology outruns schema discipline

If Agent DNA stays poetic and not typed, it will drift.

Mitigation:

```text
implement as JSON Schema / TypeScript interface with tests
```

### 2. Authority leakage

If inherited traits imply inherited permissions, this becomes dangerous.

Mitigation:

```text
no permission inheritance by default
```

### 3. Static identity rigidity

If the schema is too rigid, it reduces adaptability.

Mitigation:

```text
allow versioned traits and extension fields under review
```

### 4. Role/personality confusion

Temperament is useful but must never override capability truth or governance.

Mitigation:

```text
governance > capability > role > temperament
```

## Review Checklist

Before implementation:

```text
[ ] JSON Schema created
[ ] TypeScript interface created
[ ] sample S1-S7 DNA records created
[ ] validation tests added
[ ] no capability implies permission
[ ] no inheritance grants authority
[ ] governance constraints override temperament
[ ] deploy-readiness docs explicitly exclude Agent DNA as deploy evidence
```

## Strongest Safe Claim

> Agent DNA is a strong swarm-architecture concept that should be implemented as typed constitutional metadata for agent behavior. It can improve routing, capability declaration, governance constraints, replayability, composability, and arbitration support, but it is design input rather than runtime proof or deployment evidence.
