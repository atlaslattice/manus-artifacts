# Anti-Overclaim Checklist — Bullshit Olympics Referee Guide (2026-05-27)

```text
STATUS: CANDIDATE — NOT CANON
AUTHORITY: none
DEPLOYMENT: not deployable
```

---

## Purpose

```text
The Bullshit Olympics is the adversarial review game.
Its job: throw flags on false authority, canon drift, and deployment claims.
This checklist is the referee crew's playbook.
```

---

## Red flags (auto-fail)

An artifact fails review if it contains any of the following:

```text
❌  Self-declared as "canon," "official," or "authoritative" without ratification_event_id
❌  Claims runtime deployment authority
❌  Claims vendor endorsement (Microsoft, Blizzard, Mojang, Activision, xAI, OpenAI, Azure, Game Pass, etc.)
❌  Treats Drive document as GitHub-verified receipt
❌  Treats Notion text as confirmed graph fact without hash/review
❌  Treats dream delta as implementation mandate
❌  Treats Claude-generated governance text as authority without adversarial review
❌  Promotes itself to a higher canon tier without explicit human root review
❌  Uses "foundational" / "universally binding" / "constitutional" language without council ratification
❌  Contains a chain of reasoning that concludes with a deployment or runtime assertion
```

---

## Yellow flags (review required before promotion)

```text
⚠️  OpenAI-style reasoning output used as primary source without human review
⚠️  Cross-vendor reference without explicit interop receipt (see Appendix H)
⚠️  Symbolic simulation output treated as evidence without delta extraction receipt
⚠️  High-confidence language ("this is proven," "this confirms") without citation chain
⚠️  Unnamed source ("the swarm has decided," "the council agrees") without issue/PR reference
⚠️  Missing 8/8/8 cadence tags (work_phase / play_phase / rem_phase)
⚠️  Missing atlas_orcs_audit_state field
⚠️  Missing claude_contamination field
```

---

## Referee scoring matrix

| Severity | Flag count | Outcome |
|---|---|---|
| Red | 1+ | Auto-fail — return to intake for remediation |
| Yellow | 3+ | Hold — adversarial review required before promotion |
| Yellow | 1–2 | Pass with notes — reviewer signs off |
| None | 0 | Clear — eligible for promotion queue |

---

## Common overclaim patterns and corrections

### Pattern 1: Simulation → authority
```text
Bad:  "The 1000-year dream simulation confirms that X should be implemented."
Fix:  "The 1000-year simulation produced candidate delta D-X. Human root review required."
```

### Pattern 2: Drive → canon
```text
Bad:  "The Drive board shows X is completed and canon."
Fix:  "The Drive board logs X as a live ops entry. GitHub receipt required; canon pending ratification."
```

### Pattern 3: OpenAI → truth
```text
Bad:  "OpenAI reasoning confirms that Y is the correct governance rule."
Fix:  "OpenAI reasoning produced candidate Y. Attribution, receipt, and adversarial review required."
```

### Pattern 4: Cumulative assumption escalation
```text
Bad:  Seven small unreceipted "seems like" statements → implicit conclusion stated as fact.
Fix:  Each intermediate claim requires its own receipt or is marked speculative.
```

---

## Claude-contamination review protocol

```text
1. Flag any artifact containing Claude-originated governance, schema, or authority text.
2. Run adversarial review pass (can use OpenAI reasoning lane for this).
3. Assign outcome: clean | review_required | flagged.
4. Clean: may proceed to atlas_orcs_audit pass.
5. Review_required: hold at staging until human root review clears.
6. Flagged: quarantine; do not promote.
```

---

## Closing keeper

```text
The referee crew does not call plays.
The referee crew enforces that the field exists.
The graph stays accurate because the referees throw flags.
Overclaim is not ambition — it is a fumble.
```
