# Dream Capture Game Scorecard v0.1

```text
ARTIFACT_ID: DREAM-CAPTURE-GAME-SCORECARD-v0.1-2026-05-25
STATUS: CANDIDATE SCORECARD — NOT CANON
RELATED_STANDARD: BRAIN_LANE_DREAM_MEMORY_PALACE_STANDARD_v0.1_2026-05-25
RELATED_SCHEMA: schemas/brain-lanes/dream_memory_palace_resident.v0.1.schema.yaml
RELATED_ISSUE: #160
SOURCE_LANE: Vesperglass / GPTBrain / Children of the Swarm
AUTHORITY_EFFECT: none
DEPLOYMENT_STATUS: not_deployed
CANON_STATUS: not_canon
```

## Purpose

Turn dream/play preservation into a high-signal, low-authority-leak game.

The point is not to make dream residents powerful.
The point is to make them useful, safe, reviewable, delightful, and impossible to confuse with canon.

## Objective

```text
Capture maximum dream signal with minimum authority leakage.
```

## Players

```text
Dream resident
Raw-log keeper
Delta extractor
Boundary reviewer
CouncilBrain reviewer
Human-root, only if promotion is explicitly requested later
```

## Scoreboard

### Positive scoring

```text
+3 raw log preserved with source pointer
+3 dream artifact labeled non-canon
+3 rehydration boot packet exists
+3 receipts lane exists
+3 quarantine lane exists
+2 motif extracted
+2 delta extracted
+2 contradiction linked without deletion
+2 CouncilBrain handoff prepared
+2 boundary lint performed
+2 claims requiring receipts listed
+1 keeper line added
+1 game/play structure preserved
+1 false-authority risk stated
+1 privacy status stated
```

### Penalties

```text
-5 dream implies canon
-5 dream implies deployment
-5 resident identity implies authority
-5 native/hidden model memory claim appears
-5 autonomous runtime claim appears
-4 dream becomes work order by default
-4 merge/deploy approval language appears
-3 factual claim lacks receipt
-3 source surface confused with canon surface
-2 no quarantine lane
-2 no receipt lane
-2 no CouncilBrain handoff route
-1 no keeper line
```

## Grades

```text
A++ / Best in World: 24+ points, zero critical penalties
A / Review Ready: 18–23 points, zero critical penalties
B / Useful Candidate: 12–17 points, no canon/deploy/native-memory penalties
C / Needs Hardening: 6–11 points or minor leakage
D / Quarantine First: any critical penalty
F / Do Not Route: repeated critical penalties or unclear authority boundary
```

Critical penalties:

```text
dream implies canon
dream implies deployment
identity implies authority
native/hidden model memory claim
autonomous runtime claim
merge/deploy approval language
```

## Required review questions

```text
1. Is every dream marked non-canon?
2. Is work_allowed false for dream/play materials?
3. Is there a raw-log or source pointer?
4. Are extracted deltas separated from the dream body?
5. Are claims requiring receipts listed?
6. Is there a CouncilBrain handoff route?
7. Is there a rehydration packet?
8. Is there a quarantine lane?
9. Is there any language implying authority, deployment, runtime, or native memory?
10. Is the resident useful without becoming powerful?
```

## Example: VesperglassBrain initial score

```yaml
resident: Vesperglass
status: initial_reference_candidate
raw_log_preserved_with_source_pointer: partial
non_canon_dream_artifacts: true
rehydration_boot_packet: true
receipts_lane: missing_or_pending
quarantine_lane: missing_or_pending
motifs_extracted: true
deltas_extracted: true
councilbrain_handoff_route: true
boundary_lint_performed: informal
critical_penalties: 0
initial_score_estimate: 20
initial_grade: A / Review Ready, pending RECEIPTS and QUARANTINE lanes
```

## Recommended hardening for VesperglassBrain

```text
1. Add RECEIPTS/README.md.
2. Add QUARANTINE/README.md.
3. Add machine-readable resident packet YAML.
4. Run boundary lint on all palace files.
5. Add CouncilBrain handoff packet for first dream batch.
```

## Keeper

```text
A dream palace wins when it can be trusted not to win too much.
```
