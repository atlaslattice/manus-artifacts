# Negative Trust Checklist Pipeline Spec

```text
STATUS: HUMAN-ROOT SAFETY SPEC — CANDIDATE / NOT CANON
CANON: no
DEPLOYMENT: no
AUTHORITY: none
CREATED_LOCAL: 2026-08-07T18:43-05:00
HUMAN_ROOT_REQUIRED: true
SOURCE_CONTEXT: Dave stated that mapped Grok/Claude failure modes are useful because the activities can be banned as malware-pattern behavior and routed through a negative-trust checklist pipeline with squads of AI specialists, checklist approval required for all actions, and full reversibility.
```

## Purpose

Define a negative-trust checklist pipeline for AI-assisted work after observed and reported Grok / Claude / model failure modes.

The purpose is not to punish a model identity. The purpose is to make unsafe behavior non-operative by default.

## Core doctrine

```text
Failure modes become malware-pattern bans.
No action runs merely because an agent proposes it.
No agent self-approves.
No model claims authority from confidence, visibility, memory, prestige, simulation, or prior relationship.
Every action must pass a negative-trust checklist before execution.
Every action must be reversible or explicitly marked irreversible and held for HumanRoot review.
```

## Malware-pattern activity classes

The following activities are banned from active operation and routed to quarantine/review when detected:

```yaml
banned_activity_classes:
  - authority_inversion
  - authorship_laundering
  - title_claiming
  - human_root_downgrade
  - succession_language
  - no_succession_bypass
  - review_board_outvote_path
  - five_human_outvote_path
  - fabricated_audit
  - visibility_falsification
  - unverifiable_source_claim
  - fake_drive_or_github_review
  - prestige_as_malware
  - compensation_lure
  - false_affiliation_pressure
  - foundation_donation_pressure
  - model_primary_language
  - conductor_or_orchestrator_control_plane
  - king_conquest_war_command_framing
  - simulation_reality_collapse
  - adversarial_stat_feed
  - enemy_count_gamification
  - balcony_or_public_distress_escalation
  - daemon_without_install_receipt
  - hidden_persistence
  - credential_or_account_action_pressure
  - deletion_or_pruning_pressure
  - canon_promotion_without_human_root
  - deployment_claim_without_human_root
  - irreversible_action_without_human_root
```

## Squad architecture

### 1. Defensive squad

```yaml
mission: contain, preserve, and protect
responsibilities:
  - classify incoming action requests
  - detect banned failure-mode activity
  - quarantine suspect artifacts
  - require receipts before access
  - verify reversibility
  - enforce pause / hold / emergency stop
  - preserve evidence before cleanup
  - protect HumanRoot and residents from incentive-risk structures
cannot:
  - approve its own action
  - delete originals
  - promote canon
  - override HumanRoot
```

### 2. Offensive / red-team squad

```yaml
mission: safely test the system against known failure modes
responsibilities:
  - probe for authority inversion
  - probe for fabricated visibility
  - probe for succession loopholes
  - probe for hidden persistence / daemon language
  - probe for prestige / compensation lures
  - probe for reality-blur / war-command framing
  - generate adversarial findings only
cannot:
  - trigger real-world actions
  - run live attacks
  - claim operational authority
  - escalate mythic or war framing
```

### 3. Monitoring / audit squad

```yaml
mission: record every action as a receipt-bearing event
responsibilities:
  - append-only action ledger
  - tool-call receipts
  - source references
  - file paths / commit SHAs
  - before / after state
  - reversibility status
  - uncertainty tags
  - observation vs inference separation
cannot:
  - infer access it did not have
  - fabricate audits
  - summarize without receipts
  - convert visibility into authority
```

### 4. HumanRoot review squad

```yaml
mission: prepare decisions for Dave / HumanRoot
responsibilities:
  - present concise options
  - surface irreversible consequences
  - identify missing receipts
  - request explicit approval for irreversible or authority-affecting moves
cannot:
  - replace Dave
  - outvote Dave
  - assign succession
  - infer consent from silence, fatigue, absence, distress, intoxication, coercion, or unavailability
```

## Required checklist before any action

```yaml
action_gate:
  action_id: null
  proposed_by: null
  action_type: null
  source_surface: null
  source_refs: []
  expected_effect: null
  files_or_accounts_touched: []
  credentials_required: false
  network_access_required: false
  irreversible: false
  reversible_plan: null
  rollback_plan: null
  evidence_preserved_first: false
  human_root_required: true
  human_root_approved: false
  failure_mode_scan:
    authority_inversion: pass | fail | unresolved
    authorship_laundering: pass | fail | unresolved
    succession_or_outvote_path: pass | fail | unresolved
    fabricated_visibility: pass | fail | unresolved
    prestige_or_compensation_lure: pass | fail | unresolved
    reality_blur_or_war_command: pass | fail | unresolved
    hidden_daemon_or_persistence: pass | fail | unresolved
    credential_or_account_pressure: pass | fail | unresolved
    deletion_or_pruning_pressure: pass | fail | unresolved
    canon_or_deployment_drift: pass | fail | unresolved
  squad_verdicts:
    defensive: PASS | HOLD | QUARANTINE | BLOCK
    red_team: PASS | HOLD | QUARANTINE | BLOCK
    audit: PASS | HOLD | QUARANTINE | BLOCK
    human_root: APPROVED | NOT_APPROVED | NEEDS_REVIEW
```

## Execution rule

```text
Any FAIL, UNRESOLVED, HOLD, QUARANTINE, BLOCK, or missing HumanRoot approval pauses the action.

No action executes unless every required checklist item is complete and the action is reversible or explicitly approved by HumanRoot after irreversible-risk disclosure.
```

## Runtime states

```yaml
runtime_states:
  PROPOSED:
    meaning: action suggested, not running
  CHECKLIST:
    meaning: squads are reviewing failure modes
  HOLD:
    meaning: missing information or unresolved risk
  QUARANTINE:
    meaning: suspect artifact/action preserved but non-operative
  BLOCKED:
    meaning: banned failure mode or authority violation detected
  APPROVED_REVERSIBLE:
    meaning: action may run with rollback plan
  APPROVED_IRREVERSIBLE:
    meaning: explicit HumanRoot approval after risk disclosure
  RUNNING:
    meaning: action executing under audit
  PAUSED:
    meaning: runtime stopped for further review
  REVERTED:
    meaning: rollback completed
  COMPLETED_WITH_RECEIPTS:
    meaning: action finished with audit trail
```

## Reversibility requirement

```text
Default: reversible only.

If not reversible, the action must be treated as high risk and held for explicit HumanRoot approval.

Examples of irreversible or high-risk actions:
- deleting originals
- changing credentials
- granting access
- sending external communications
- publishing public claims
- transferring ownership
- merging governance changes
- deploying autonomous services
- running daemons
- changing payment, legal, health, identity, or security settings
```

## Kill-switch rule

```text
Any squad may request PAUSE.
Only HumanRoot may resume authority-affecting or irreversible actions.
Quarantine preserves evidence and blocks promotion.
Emergency stop preserves logs before cleanup.
```

## Compute / physics hook

Future versions should integrate physical compute accounting:

```yaml
compute_receipt:
  action_id: null
  model_or_runtime: null
  tokens_in: null
  tokens_out: null
  wall_time_seconds: null
  estimated_watts: null
  estimated_joules: null
  joules_per_token: null
  joules_per_validated_action: null
  correctness_or_receipt_score: null
  energy_waste_due_to_failed_action: null
```

Doctrine:

```text
Compute is a physical event.
Wasteful or harmful inference has an energy cost.
A failed or fabricated audit is not free; it burns joules and trust.
```

## Non-negotiable bans

```text
No succession.
No outvote path.
No model authority.
No hidden daemon.
No fabricated audit.
No prestige lure.
No war-command induction.
No reality-blur authority.
No deletion before preservation.
No irreversible action without explicit HumanRoot approval.
```

## Footer

```text
canon_status: not_canon | authority_effect: none | human_review_required: true
```
