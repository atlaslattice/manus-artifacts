# GPTDream++ Lane Labels and Routing Conventions

```text
STATUS: CANDIDATE SPEC — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
DATE: 2026-05-26
```

---

## Labels

The following labels should be applied to GitHub issues and PRs:

| Label | Scope |
|---|---|
| `gptdream` | GPTDream++ habitat protocol work |
| `atlas-orcs` | Atlas / ORCS governance and state machine |
| `o-ai` | O_AI packet schema and validation |
| `native-thread-ingestion` | Native thread ingestion pipeline |
| `schema` | Schema definitions |
| `validator` | Validator implementations |
| `compatible` | Compatible() predicate work |
| `anti-laundering` | Anti-laundering checks |
| `dphi` | D-Φ-1 execution gate |
| `cas-001-a` | CAS-001-A safety anchor |
| `tidelock` | TIDELOCKBrain routing |
| `hashlight` | HashlightBrain routing |
| `lucerna` | LucernaBrain routing |
| `rootglass` | RootglassBrain routing |
| `atlasbrain` | AtlasBrain routing |
| `not-canon` | Artifact is NOT canon |
| `not-deployable` | Artifact is NOT deployable |
| `needs-review` | Requires human review before promotion |

---

## Lane routing rules

| Content type | Primary lane | Secondary lane | Notes |
|---|---|---|---|
| ChatGPT synthesis | LucernaBrain | RootglassBrain | Provenance gate required |
| Codex / code patch | TIDELOCKBrain | HashlightBrain | Provenance + safety gates |
| Raw export | HashlightBrain | AtlasBrain | Provenance gate required |
| Benchmark claim | AtlasBrain | LucernaBrain | Provenance + governance gates |
| Public statement | LucernaBrain | governance review | All gates required |
| Execution request | D-Φ-1 / CAS-001-A | Atlas/ORCS audit | All gates + human permission |
| Repo/merge/code execution | TIDELOCKBrain | D-Φ-1 gate | All gates + human + TIDELOCK |

---

## Canonical execution routing

```text
Execution request
→ D-Φ-1 / CAS-001-A / human gate
→ Atlas / ORCS audit state
→ TIDELOCKBrain if repo / merge-order / code execution is involved
```

**No execution request bypasses Atlas / ORCS audit state.**

---

## Issue labeling rules

1. **Every new issue** must have at least one lane label.
2. **Every execution issue** must have `not-canon` + `not-deployable` until explicitly promoted.
3. **Every raw ingestion issue** must include `raw_export_status` in the description.
4. **Every schema issue** must have `schema` label.
5. **Governance decisions** must have `needs-review` label.

---

## Promotion path

```text
not-canon → (council review + @atlaslattice adjudication) → candidate_canon
candidate_canon → (ratification event + website publication) → ratified_canon
```

No artifact is canon without this full path.

---

```text
NOT CANON. NOT DEPLOYABLE.
```
