# ⬡ METATRON'S CUBE — 10-NODE EXECUTION RUNBOOK ⬡

```text
STATUS:    PLAY OUTPUT — CULTURE LAYER — NOT CANON
PURPOSE:   Give every agent, human, and swarm node a reusable task execution protocol
           shaped around the geometry of Metatron's Cube
DATE:      2026-05-26
SEAT:      All seats welcome — center is shared
PROMOTION: Harvestable once a task instance completes and receipts are filed
```

---

## ⬡ Why Metatron's Cube?

Metatron's Cube contains every platonic solid.
Every shape is already in there — you just have to connect the right nodes.

Task execution works the same way.
Every project contains its own blueprint.
The runbook doesn't build the project.
The runbook reveals which nodes are already present and which ones need to be lit.

```text
THE CUBE IS NOT THE PLAN.
THE CUBE IS THE GEOMETRY THAT MAKES THE PLAN POSSIBLE.
```

---

## ⬡ The Geometry

```
                           ╔═══════════════╗
                           ║   ⬡ NODE 1 ⬡  ║
                           ║  CENTER GOAL  ║
                           ╚═══════════════╝
                                  ║
          ┌───────────────────────╬───────────────────────┐
          │                       │                       │
    ⬡ NODE 6 ⬡             ⬡ NODE 2 ⬡             ⬡ NODE 3 ⬡
    ASSUMPTION               CONSTRAINTS              EVIDENCE
       CHECK
          │                       │                       │
    ⬡ NODE 7 ⬡             ⬡ NODE 0 ⬡             ⬡ NODE 4 ⬡
    REQUIREMENT            ≋ CENTER ≋              OUTPUT CONTRACT
       FREEZE               (shared)
          │                       │                       │
    ⬡ NODE 8 ⬡             ⬡ NODE 5 ⬡             ⬡ NODE 9 ⬡
    DEFINITION              PHASING               VALIDATION GATE
     OF DONE
                                  ║
                           ╔═══════════════╗
                           ║  ⬡ NODE 10 ⬡  ║
                           ║ FEEDBACK LOOP ║
                           ╚═══════════════╝
```

```text
CENTER = shared context, always live
RING 1 (Nodes 1-5) = define the mission
RING 2 (Nodes 6-10) = protect the mission
```

---

## ⬡ NODE 1 — CENTER GOAL 🎯

**"What exactly are we doing?"**

Write one sentence. Not a paragraph. Not a list. One sentence.

```
GOAL: ___________________________________________________
```

> If you can't write one sentence, the cube won't light up.
> The center must be clear before any other node can lock.

**Output:** A single declarative sentence that survives being read aloud at 3am.

---

## ⬡ NODE 2 — CONSTRAINTS 🧱

**"What are the walls?"**

Four constraint classes. Fill what applies, leave the rest empty.

```
TIME:     ___________________  (deadline / timebox / sprint boundary)
SCOPE:    ___________________  (in / out / not this PR)
TOOLS:    ___________________  (only these tools, not those)
NON-GOALS:___________________  (explicitly out of scope, so nobody fights about it)
```

> Constraints aren't obstacles. They're the load-bearing walls.
> A cube without walls is just floating nodes.

**Output:** A boundary map — so fast, anyone can read it in 10 seconds.

---

## ⬡ NODE 3 — EVIDENCE 📎

**"What are we actually looking at?"**

No vibes. No abstractions. Paste the receipts.

```
FILES:    (exact paths)
ERRORS:   (exact error text / stack traces)
LOGS:     (CI run IDs, job IDs, or log snippets)
ISSUES:   (GitHub issue # or PR #)
```

> Evidence is not context. Evidence is what you'd show a judge.
> If you can't paste it, you haven't found it yet.

**Output:** A list of hard links and quoted text — no paraphrasing.

---

## ⬡ NODE 4 — OUTPUT CONTRACT 📬

**"What does done look like, physically?"**

Pick exactly one per slot. This is a contract, not a wish list.

```
FORMAT:   [ ] plan   [ ] checklist   [ ] diff   [ ] summary   [ ] runbook
AUDIENCE: [ ] me     [ ] team        [ ] agent  [ ] archive
MEDIUM:   [ ] PR     [ ] .md file    [ ] comment [ ] issue
```

> If you don't name the output format, you'll spend 80% of your time
> arguing about whether a plan is a checklist or a diff.

**Output:** A signed output spec. Both parties know what they're building toward.

---

## ⬡ NODE 5 — PHASING 🗓️

**"What happens now vs. later vs. never-this-sprint?"**

Three buckets. Hard rule: nothing goes in "NOW" that isn't starting today.

```
⚡ NOW (today / this session):
  - ___________________________________
  - ___________________________________

📅 NEXT (next session / this week):
  - ___________________________________

🌙 LATER (backlog / not blocking):
  - ___________________________________
```

> The most dangerous phrase in a planning doc is "we'll also add…"
> Phasing gives "we'll also add" a legal address so it can't ambush the current sprint.

**Output:** Three timestamped buckets. No item appears in more than one.

---

## ⬡ NODE 6 — ASSUMPTION CHECK 🔭

**"What are we believing that we haven't proven?"**

List every assumption. Then mark each one: `CONFIRMED` / `UNCONFIRMED` / `NEEDS PROOF`.

```
Assumption 1: _______________________  [ ] CONFIRMED  [ ] UNCONFIRMED  [ ] NEEDS PROOF
Assumption 2: _______________________  [ ] CONFIRMED  [ ] UNCONFIRMED  [ ] NEEDS PROOF
Assumption 3: _______________________  [ ] CONFIRMED  [ ] UNCONFIRMED  [ ] NEEDS PROOF
```

> The cube does not lie to you. It shows you what's hollow.
> Every unconfirmed assumption is a node that hasn't lit up yet.

**Output:** An assumption audit — the team knows what's solid and what's vapor.

---

## ⬡ NODE 7 — REQUIREMENT FREEZE ❄️

**"What are we NOT allowed to change mid-execution?"**

Write the frozen requirements here. Once written, they don't move until a new runbook cycle starts.

```
FROZEN:
  - ___________________________________
  - ___________________________________
  - ___________________________________

CHANGE PROTOCOL: (how to unfreeze, if needed)
  - ___________________________________
```

> Scope creep doesn't knock. It just walks in while you're focused
> on something else and rearranges the furniture.
> The freeze is the lock on the door.

**Output:** An immutable requirement list for this iteration. Post it where everyone can see it.

---

## ⬡ NODE 8 — DEFINITION OF DONE ✅

**"How do we know when we've actually finished?"**

3–5 acceptance criteria. Each one must be independently verifiable.

```
Done means:
  [ ] ___________________________________
  [ ] ___________________________________
  [ ] ___________________________________
  [ ] ___________________________________
  [ ] ___________________________________
```

> "Done" is not a feeling. "Done" is a list of boxes.
> If you can't check each box independently, the definition isn't done yet.

**Output:** A binary checklist. Pass = ship. Fail = keep going.

---

## ⬡ NODE 9 — VALIDATION GATE 🔬

**"What checks must pass before we call it?"**

Name the actual commands, tests, or reviews required.

```
AUTOMATED:
  - bash: ___________________________________
  - pytest: _________________________________
  - lint: ___________________________________

HUMAN REVIEW:
  - Who reviews: ___________________________
  - What they check: _______________________

CANON GATE:
  [ ] Human-root review required before promotion
  [ ] Agent review sufficient
  [ ] No review needed (play output only)
```

> The lasers come on only after the evidence boundary is marked.
> (This is borrowed directly from the Laser Rave. It still applies here.)

**Output:** A runnable validation sequence. No ambiguous "just test it" entries.

---

## ⬡ NODE 10 — FEEDBACK LOOP 🔁

**"What's the signal after each iteration?"**

Three choices. Pick the one that's actually true right now.

```
⚡ CONTINUE  — execution is aligned, proceed as planned
🔧 ADJUST    — execution is live but requires course correction (describe below)
🛑 STOP      — blocked, misaligned, or new information changes the center goal

Current signal: [          ]

If ADJUST or STOP, describe what changed:
  _______________________________________________
  _______________________________________________
```

> The loop is not weakness. The loop is how the cube stays lit.
> Every orbit returns to the center. Every iteration checks the goal.

**Output:** A one-word signal + optional delta note. Sent at the end of every session.

---

## ⬡ Running the Cube

**Full run (first time):** Fill all 10 nodes before executing.

**Quick run (repeat sessions):** Start at Node 1. Confirm the goal is still the goal.
Then jump to Node 10 from the previous run — read the signal, pick up from there.

**Emergency run (something is on fire):** Node 3 → Node 1 → Node 8.
Find the evidence, re-confirm the goal, re-check done criteria.

---

## ⬡ Cube Template (Blank)

```
NODE 1 — CENTER GOAL
  GOAL: ___________________________________________________

NODE 2 — CONSTRAINTS
  TIME: _________________ SCOPE: _________________
  TOOLS: ________________ NON-GOALS: _____________

NODE 3 — EVIDENCE
  FILES: _____________ ERRORS: _____________ ISSUES: _____

NODE 4 — OUTPUT CONTRACT
  FORMAT: ___________ AUDIENCE: __________ MEDIUM: ______

NODE 5 — PHASING
  NOW: _________________ NEXT: _____________ LATER: ______

NODE 6 — ASSUMPTION CHECK
  [assumption]: _________________ STATUS: ______________

NODE 7 — REQUIREMENT FREEZE
  FROZEN: ________________________________________________

NODE 8 — DEFINITION OF DONE
  [ ] ____________________
  [ ] ____________________
  [ ] ____________________

NODE 9 — VALIDATION GATE
  AUTOMATED: _____________ HUMAN: ___________________

NODE 10 — FEEDBACK LOOP
  SIGNAL: [ CONTINUE / ADJUST / STOP ]
  DELTA: _________________________________________________
```

---

## ⬡ Final Signal

```text
THE CENTER IS NOT THE GOAL.
THE CENTER HOLDS THE GOAL.
THE GEOMETRY DOES THE REST.

EVERY PLATONIC SOLID IS ALREADY IN THE CUBE.
EVERY PROJECT IS ALREADY IN THE RUNBOOK.
CONNECT THE NODES. LIT THE EDGES. SHIP THE THING.

THE CUBE ROTATES. THE CANON WAITS FOR DAVE.
```

---

*Culture layer artifact. Harvestable by any seat. Promotable after human-root review.*
*PLAY OUTPUT — CULTURE LAYER — NOT CANON*
