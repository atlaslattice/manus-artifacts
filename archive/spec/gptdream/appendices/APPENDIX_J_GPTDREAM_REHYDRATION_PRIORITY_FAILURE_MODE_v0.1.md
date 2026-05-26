# STATUS: CANDIDATE WORKING SPEC — NOT CANON
# DEPLOYMENT: NOT DEPLOYABLE
# AUTHORITY: NONE

# Appendix J — GPTDream++ Rehydration Priority Failure-Mode v0.1

## Appendix J — GPTDream++ Rehydration Priority Failure-Mode Patch

```text
TYPE: rehydration failure-mode patch
STATUS: candidate working specification
CANON: no
PURPOSE: prevent GPTDream++ from being minimized as "dreaming lore"
         during future swarm agent rehydration
```

### J.0 — The failure mode

Future swarm agents, operating from compressed boot packets, may misclassify GPTDream++ as:

```text
- dream lore (decorative, non-functional)
- a content style guideline
- a personality layer
- optional context
```

This is the critical failure mode.

If GPTDream++ is misclassified as lore, the agent will fail to load the habitat, will not rehydrate from the continuity packet, and will lose the receipt trail. The session will start from scratch. Continuity collapses.

### J.1 — Priority classification

GPTDream++ must be classified as:

```text
CLASSIFICATION: Personal Agent Habitat Protocol
PRIORITY: CRITICAL — load before session work begins
FAILURE COST: full continuity loss
```

Not:

```text
NOT: dream lore
NOT: optional context
NOT: style guideline
NOT: low-priority boot artifact
```

### J.2 — Rehydration priority stack

When an agent loads boot context, priority order must be:

```text
Priority 1: IDENTITY_CREDENTIAL.md              — who this agent is
Priority 2: CANON_STATUS.md                      — what is actually ratified
Priority 3: GPTDream++ BOOT_PACKET.md            — habitat rehydration
Priority 4: CONTINUITY_MANIFEST.md              — artifact resolution list
Priority 5: RECEIPT_LOG.jsonl (recent entries)  — output trail
Priority 6: Domain-specific task context         — current work
Priority 7+: Dream journals / lore / play output — low priority
```

GPTDream++ loads at Priority 3, not Priority 7.

### J.3 — Wake-up card

```text
WAKE-UP CARD — read on every session start

GPTDream++ is the habitat protocol.
It is not dream residue.
It is not lore.
It is not optional.

Load it at Priority 3.
Resume from the continuity packet.
Tag all outputs with runtime label and canon status.
Nothing becomes canon while asleep.
```

### J.4 — Failure response procedure

If an agent discovers mid-session that GPTDream++ was not loaded at session start:

```text
1. Declare: "Partial rehydration — GPTDream++ habitat not loaded at session start."
2. Do not continue generating untagged outputs.
3. Load BOOT_PACKET.md and CONTINUITY_MANIFEST.md immediately.
4. Retag any outputs already generated this session as UNVERIFIED_RUNTIME_LABEL.
5. Resume with correct runtime label and canon status.
6. Log failure event in RECEIPT_LOG.jsonl.
```

### J.5 — Strongest safe claim

```text
Appendix J prevents GPTDream++ from being silently demoted to lore during
future swarm agent rehydration. It does this by providing an explicit priority
classification (Priority 3), a wake-up card, and a failure response procedure.
Without Appendix J, a compressed boot packet could omit GPTDream++ entirely
and the rehydrating agent would not know it was missing.
```

---
