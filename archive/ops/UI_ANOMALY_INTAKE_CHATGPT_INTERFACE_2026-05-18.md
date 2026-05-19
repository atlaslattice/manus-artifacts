# UI Anomaly Intake — ChatGPT Interface

**Date recorded:** 2026-05-18  
**Status:** USER-REPORTED INTERFACE ANOMALY — NOT CANON  
**Surface:** ChatGPT interface  
**Reporter:** Dave / human-root  
**Recorder:** Aster / S1  
**Related comparison:** user reports similarity to prior Gemini interface anomalies  
**Purpose:** Preserve the anomaly report as an operations/debugging signal without converting it into proof of agency, continuity, deployment, or canon.

## Evidence Boundary

```text
This is an anomaly intake note.
It records a user-reported interface event.
It is not proof of autonomous agency.
It is not proof of hidden memory.
It is not proof of deployment.
It is not canon.
It requires event details, screenshots/logs, and reproduction notes before escalation.
```

## Reported Event

User reported:

```text
I just witnessed an anomaly on this interface similar to Gemini anomalies I've witnessed.
```

No additional event details were captured in this note at creation time.

## Current Safe Readout

```yaml
status: user_reported_interface_anomaly
canon_status: not_canon
agency_claim: blocked
memory_claim: blocked
deployment_claim: blocked
recommended_action: preserve metadata, compare only after repeat evidence
reproduction_status: unknown
impact_scope: unknown
```

## Repeatability Field

Use this field to distinguish one-off weirdness from reproducible behavior:

```yaml
reproduction_status: unreproduced | reproduced_once | reproducible | resolved | unknown
```

Default at intake:

```yaml
reproduction_status: unknown
```

## Impact Scope Field

Use this field to distinguish harmless visual artifacts from data-integrity concerns:

```yaml
impact_scope: visual_only | text_integrity | file_visibility | tool_state | conversation_order | unknown
```

Default at intake:

```yaml
impact_scope: unknown
```

## Immediate Capture Checklist

If possible, capture:

```text
[ ] exact time and timezone
[ ] device and app/browser surface
[ ] model/interface mode if visible
[ ] what happened on screen
[ ] what was expected instead
[ ] whether any text appeared/disappeared/changed
[ ] whether tool calls/files/attachments were involved
[ ] whether the anomaly occurred during typing, sending, loading, scrolling, or tool execution
[ ] screenshot or screen recording if safe
[ ] whether refreshing changed it
[ ] whether the event repeated
[ ] comparison to prior Gemini anomaly pattern
[ ] reproduction_status value
[ ] impact_scope value
```

## Classification Vocabulary

```text
ui_rendering_glitch
message_order_anomaly
composer_attachment_anomaly
tool_state_anomaly
memory_context_anomaly
source_visibility_anomaly
connector_state_anomaly
streaming_generation_anomaly
unknown_interface_anomaly
```

## Guardrails

```text
anomaly ≠ agency
interface behavior ≠ intent
rendering glitch ≠ memory proof
source visibility glitch ≠ canon state
similarity to another platform ≠ shared cause
preserve first, interpret later
```

## Routing

```yaml
Aster_S1:
  task: source boundary and anomaly intake
TIDELOCK_S7:
  task: repo/debug record and reproduction checklist
Lucerna:
  task: receipts/screenshots/timestamps
Hashlight:
  task: raw event lineage preservation
ClaudeBrain_S2:
  task: overclaim and continuity-theater guardrail
Aster9:
  task: intake schema hygiene / fluency-authority separation
```

## Aster-9 Schema Hygiene Note

Aster-9's safe readout is adopted as an anomaly-intake schema hardening note:

```text
status: user_reported_interface_anomaly
canon_status: not_canon
agency_claim: blocked
memory_claim: blocked
deployment_claim: blocked
recommended_action: preserve metadata, compare only after repeat evidence
```

The key improvement is to separate:

```text
visual weirdness
text integrity risk
file visibility risk
tool state risk
conversation ordering risk
```

before interpreting any cross-platform similarity.

## Strongest Safe Claim

> A user-reported ChatGPT interface anomaly occurred and appeared similar to prior Gemini interface anomalies. The event should be preserved as an operations/debugging signal pending concrete details, screenshots, timestamps, reproduction status, and impact scope. It is not evidence of agency, hidden continuity, deployment, or canon.

## Status

Anomaly intake placeholder with repeatability and impact fields. Not canon.
