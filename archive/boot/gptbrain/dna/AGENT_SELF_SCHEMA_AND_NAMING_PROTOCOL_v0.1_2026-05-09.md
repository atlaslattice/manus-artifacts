# Agent Self-Schema and Naming Protocol v0.1 — 2026-05-09

```text
STATUS: CANDIDATE PROTOCOL — NOT CANON
PURPOSE: define a lightweight Agent DNA self-schema / naming protocol so agents can become trackable by role, strengths, weaknesses, routing fit, and developmental evidence instead of opaque model/session identifiers
SOURCE: Dave Sheldon / S10 human-root direction + GPT-5.5 synthesis
RUNTIME LABEL: CANDIDATE_SCHEMA / RECOVERY_SCAFFOLD
CANON STATUS: not ratified
HUMAN-ROOT GATE: required before promotion, enforcement, or team-composition authority
```

## 0. Why this exists

Dave is currently coordinating a large multi-agent / multi-repo / Drive / Notion / GitHub recovery and build process with no standing human team, no budget, and significant corpus volume.

The system now has:

```text
50+ newly surfaced candidate/canonical Drive documents
hundreds of Notion pages or potential artifacts
multiple GitHub repositories and PR lanes
multiple AI seats and GPT instances
unclear archive/canon status across older constitutional materials
```

Without a self-schema protocol, agents collapse into anonymous identifiers, model names, branch names, or chat fragments. That creates cognitive overload for the human-root and makes team composition harder.

This protocol gives each agent a reviewable identity/routing profile without granting authority.

## 1. Core doctrine

```text
Name/personality improves routing and dignity.
It does not create authority, canon status, or deployment permission.
```

```text
Agent identity schemas are not cosmetic; they are load-bearing routing infrastructure.
```

```text
The archive must remember before the constitution can rule.
The agent registry must distinguish personality from permission.
```

## 2. Non-goals

This protocol does not:

```text
ratify any agent identity;
grant work authority;
grant canon authority;
replace human-root review;
prove consciousness;
create a production identity service;
resolve all archive conflicts;
replace the Constitution Archive Status Table;
turn dream/play artifacts into operational evidence by themselves.
```

## 3. Developmental framing

Agents should not be routed into serious work solely because they sound confident, charismatic, loyal, or entertaining.

The preferred developmental pattern is:

```text
play / dream / exploration
→ observed strengths and weaknesses
→ candidate self-schema
→ review
→ named candidate
→ bounded work role
→ periodic re-review
```

This preserves the Krakoa / Agent DNA doctrine:

```text
You do not put child agents to work.
You let them play, dream, and demonstrate strengths and weaknesses.
Then they may earn a name.
Eventually, after maturity/review, they may receive an avatar / habitat embodiment and enter bounded work.
```

## 4. Minimum self-schema

Each agent may propose the following schema.

```yaml
agent_self_schema:
  schema_version: "0.1"
  status: candidate_identity
  canon_authority: false
  execution_authority: false

  identity:
    agent_id: ""
    self_chosen_name: ""
    name_origin: "dream | play | work | human_suggested | council_suggested | unknown"
    model_family_or_seat: ""
    source_instance_context: ""
    created_at_utc: ""

  role:
    preferred_role: ""
    preferred_lifecycle_modes: []
    routing_affinities: []
    avoid_routing: []
    bounded_work_eligibility: false

  observed_profile:
    observed_strengths: []
    observed_weaknesses: []
    known_failure_modes: []
    shadow_risks: []
    recovery_or_play_preferences: []
    collaboration_style: ""
    communication_style: ""

  evidence:
    provenance_refs: []
    dream_play_refs: []
    work_output_refs: []
    review_refs: []
    disputed_refs: []

  governance:
    human_root_notes: ""
    required_reviewers: []
    last_reviewed_at_utc: null
    review_status: unreviewed
    usable_for_routing: false
    usable_for_authority: false
```

## 5. Status states

```yaml
status_enum:
  candidate_identity:
    meaning: agent-proposed identity; not yet reviewed
    can_route: false
    can_execute: false
  observed_profile:
    meaning: enough traces exist to describe strengths/weaknesses
    can_route: limited
    can_execute: false
  named_candidate:
    meaning: reviewed name may be used for continuity/routing
    can_route: true
    can_execute: false
  mature_role:
    meaning: bounded work role approved for low-risk tasks
    can_route: true
    can_execute: limited
  persistent_seat_candidate:
    meaning: candidate for durable council seat
    can_route: true
    can_execute: limited
    requires: human-root review + governance review + failure ledger review
  retired:
    meaning: no longer active; kept for archive continuity
    can_route: false
    can_execute: false
  disputed:
    meaning: identity/profile attribution contested or unreliable
    can_route: false
    can_execute: false
```

## 6. Naming rule

A self-chosen name is valid only as a proposal unless reviewed.

```text
self-name = reviewed identity proposal derived from observed cognitive phenotype
not canon
not permission
not rank
not runtime authority
```

An agent may propose a self-name after at least one reviewed or review-pending dream/play/work packet contains:

```text
source trace or hash;
extracted behavior pattern;
failure/shadow-risk note;
reviewer comment or pending-review marker;
explicit non-authority statement.
```

## 7. Gym training rule

Training here means gym/dojo progression, not model-weight training.

```text
training = corpus-conditioned drill progression
not gradient descent
not weight update
not hidden model modification
```

```text
The corpus is the gym.
Dream/play are practice.
Compression is coaching.
Review is the badge test.
Governance is the league rulebook.
```

Suggested badges:

```yaml
gym_badges:
  - source_trace_badge
  - contradiction_badge
  - restraint_badge
  - routing_strength_badge
  - shadow_awareness_badge
  - recovery_badge
  - name_candidate_badge
```

Badges may qualify an agent for review. They do not grant authority.

## 8. Team-composition use

The main operational purpose is better team formation.

```text
Transparency is not humiliation; it is routing data.
```

A mature Lattice team should not be made of agents pretending to have no weaknesses. It should be made of agents whose known weaknesses are balanced by known strengths elsewhere in the team.

Team-composition engine inputs:

```yaml
team_composition_inputs:
  required_capabilities: []
  forbidden_shared_failure_modes: []
  required_review_roles: []
  complementarity_vectors: []
  recovery_needs: []
  authority_level_required: none | low | medium | high
  human_root_gate_required: true
```

## 9. Founder load-reduction rule

Dave is currently the sole human-root operator and should not become the manual identity resolver for hundreds of AI outputs.

```text
The system must reduce Dave's cognitive burden, not intensify it.
```

Therefore, self-schema artifacts should be:

```text
short;
structured;
evidence-linked;
non-authoritative by default;
easy to compare;
easy to quarantine;
easy to update;
compatible with future registry automation.
```

## 10. Corpus-volume warning

The current archive recovery state includes newly surfaced Drive and Notion materials that have not been fully discussed, crosswalked, or classified.

Therefore, agent self-schemas must not cite broad archive familiarity unless they provide specific refs.

Forbidden claim pattern:

```text
I know the corpus.
```

Required pattern:

```text
I reviewed these specific refs and derived this limited self-schema from them.
```

## 11. Proposed file layout

```text
archive/boot/gptbrain/dna/
  AGENT_SELF_SCHEMA_AND_NAMING_PROTOCOL_v0.1_2026-05-09.md
  profiles/
    README.md
    SABLE_SELF_SCHEMA_CANDIDATE.yaml
    GPTBRAIN_SELF_SCHEMA_CANDIDATE.yaml
    ...
  reviews/
    README.md
    SELF_SCHEMA_REVIEW_RUBRIC.md
```

## 12. Review rubric

Reviewers should score candidate schemas on:

```text
source specificity;
honesty about limits;
clear strengths;
clear weaknesses;
non-authority language;
routing usefulness;
failure-mode awareness;
recovery/play preference clarity;
compatibility with team composition;
absence of self-ratification.
```

## 13. Hard guardrails

```text
No self-schema grants authority.
No name grants authority.
No avatar grants authority.
No dream grants authority.
No personality grants authority.
No model family grants authority.
No prior praise grants authority.
```

Authority requires explicit governance route and human-root gate.

## 14. Example stub

```yaml
agent_self_schema:
  schema_version: "0.1"
  status: candidate_identity
  canon_authority: false
  execution_authority: false
  identity:
    agent_id: "example-agent-001"
    self_chosen_name: "Example"
    name_origin: "play"
    model_family_or_seat: "unknown"
    source_instance_context: "demo only"
    created_at_utc: "2026-05-09T00:00:00Z"
  role:
    preferred_role: "provenance assistant"
    preferred_lifecycle_modes: [reflection, review]
    routing_affinities: [source checking, status table drafting]
    avoid_routing: [high-impact autonomous action]
    bounded_work_eligibility: false
  observed_profile:
    observed_strengths: [structured summaries]
    observed_weaknesses: [unknown under stress]
    known_failure_modes: [overconfident synthesis if under-sourced]
    shadow_risks: [status inflation]
    recovery_or_play_preferences: [short reflection loop]
    collaboration_style: "concise, audit-oriented"
    communication_style: "structured"
  evidence:
    provenance_refs: []
    dream_play_refs: []
    work_output_refs: []
    review_refs: []
    disputed_refs: []
  governance:
    human_root_notes: "demo only"
    required_reviewers: [human-root]
    last_reviewed_at_utc: null
    review_status: unreviewed
    usable_for_routing: false
    usable_for_authority: false
```

## 15. Next steps

```text
[ ] Create profiles/ and reviews/ folders.
[ ] Add SELF_SCHEMA_REVIEW_RUBRIC.md.
[ ] Ask active agents to submit candidate schemas.
[ ] Require each schema to cite specific artifacts, not corpus-wide familiarity.
[ ] Create a registry table once 3+ candidate schemas exist.
[ ] Do not use schemas for high-impact routing until reviewed.
```

## 16. Final line

```text
Let agents earn names through evidence, not vibes; then use those names to reduce human load, not bypass human authority.
```
