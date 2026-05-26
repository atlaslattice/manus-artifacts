# MODULE 8 — Repo Task Labels and Lane Routing Spec v0.1

```text
STATUS: CANDIDATE SPEC — NOT CANON
DEPLOYMENT: NOT DEPLOYABLE
AUTHORITY: NONE
RATIFICATION: PENDING @atlaslattice + full council
```

---

## 1. Purpose

MODULE 8 makes GitHub issue tracking legible by:

1. Defining a fixed label vocabulary that maps to protocol domains, agent routing targets, and governance states.
2. Specifying lane routing rules that prescribe which brain(s) handle each class of incoming work.
3. Codifying acceptance criteria that gate every issue before it can be promoted toward canon.

This spec is machine-enforceable: labels are synced by CI (`sync-labels.yml`), and issue templates pre-populate required labels and acceptance checklists.

---

## 2. Label Vocabulary

Labels are defined in `.github/labels.yml` and automatically synced via `.github/workflows/sync-labels.yml` on every push to `main`.

### 2.1 Protocol / Domain Labels

| Label | Color | Scope |
|---|---|---|
| `gptdream` | `#0075ca` | GPTDream++ habitat protocol artifacts and issues |
| `atlas-orcs` | `#0052cc` | Atlas/ORCS trust-state and audit concerns |
| `o-ai` | `#1d76db` | O_AI vendor packet / cross-vendor interop |
| `native-thread-ingestion` | `#5319e7` | Native thread ingestion pipeline |
| `schema` | `#006b75` | YAML/JSON schema artifacts |
| `validator` | `#0e8a16` | Validator module or validation rule |
| `compatible` | `#bfd4f2` | Compatibility / cross-vendor predicate |
| `anti-laundering` | `#e4e669` | Anti-laundering predicate (Module 4, `compatible.py`) |
| `dphi` | `#c2e0c6` | D-Φ-1 execution gate / differential-phi concern |
| `cas-001-a` | `#d93f0b` | CAS-001-A Atlas/ORCS audit-state execution route |

### 2.2 Agent Routing Labels

| Label | Color | Target Brain |
|---|---|---|
| `tidelock` | `#7c3aed` | TIDELOCKBrain — repo-related Codex / execution work |
| `hashlight` | `#b45309` | HashlightBrain — raw export triage, Codex patch assist |
| `lucerna` | `#0891b2` | LucernaBrain — synthesis, public statements, benchmark review |
| `rootglass` | `#475569` | RootglassBrain — ChatGPT synthesis ingestion |
| `atlasbrain` | `#1e40af` | AtlasBrain — benchmark claims, raw export final authority |

### 2.3 Governance / Status Labels

| Label | Color | Meaning |
|---|---|---|
| `not-canon` | `#e11d48` | Not ratified; must not be cited as authoritative |
| `not-deployable` | `#dc2626` | Execution blocked; requires explicit human gate removal |
| `needs-review` | `#f59e0b` | Awaiting council or @atlaslattice before promotion |

---

## 3. Lane Routing Rules

```
Lane                  Primary Brains                    Required Labels
─────────────────────────────────────────────────────────────────────────
ChatGPT synthesis     LucernaBrain / RootglassBrain     lucerna, rootglass, not-canon, needs-review
Codex patch           TIDELOCKBrain / HashlightBrain    tidelock, hashlight, not-canon, not-deployable, needs-review
Raw export            HashlightBrain / AtlasBrain        hashlight, atlasbrain, native-thread-ingestion, not-canon, not-deployable, needs-review
Benchmark claim       AtlasBrain / LucernaBrain         atlasbrain, lucerna, not-canon, needs-review
Public statement      LucernaBrain → governance review  lucerna, not-canon, not-deployable, needs-review
Execution request     D-Φ-1 → CAS-001-A → human gate   dphi, cas-001-a, tidelock, not-canon, not-deployable, needs-review
                      → Atlas/ORCS audit → TIDELOCK
```

### 3.1 ChatGPT Synthesis Lane

**Trigger:** New artifact produced via ChatGPT conversation synthesis.  
**Route:** LucernaBrain (primary review) / RootglassBrain (raw ingestion).  
**Template:** `.github/ISSUE_TEMPLATE/chatgpt-synthesis.yml`

### 3.2 Codex Patch Lane

**Trigger:** Code, schema, or test patch via Codex / Copilot.  
**Route:** TIDELOCKBrain (repo work owner) / HashlightBrain (assist).  
**Template:** `.github/ISSUE_TEMPLATE/codex-patch.yml`

Every Codex patch issue carries `not-deployable` until:
1. CAS-001-A audit state is documented.
2. Human gate (@atlaslattice) explicitly removes `not-deployable`.

### 3.3 Raw Export Lane

**Trigger:** Raw transcript/data dump from any source (ChatGPT, Claude, Notion, Drive, etc.).  
**Route:** HashlightBrain (first-pass triage) / AtlasBrain (final authority).  
**Template:** `.github/ISSUE_TEMPLATE/raw-export.yml`

**Hard requirement:** Every raw export issue **must** include a `raw_export_status` field set to one of:
- `pending-triage`
- `in-triage`
- `triaged-clean`
- `triaged-contaminated`
- `quarantined`
- `promoted-to-candidate`

### 3.4 Benchmark Claim Lane

**Trigger:** Quantitative performance or quality claim about any system in this repo.  
**Route:** AtlasBrain (measurement authority) / LucernaBrain (synthesis/publication).  
**Template:** `.github/ISSUE_TEMPLATE/benchmark-claim.yml`

### 3.5 Public Statement Lane

**Trigger:** Any content intended for external publication (blog, social, README public section, spec publication).  
**Route:** LucernaBrain → governance review → @atlaslattice sign-off.  
**Template:** `.github/ISSUE_TEMPLATE/public-statement.yml`

**Hard rule:** `not-deployable` MUST remain until @atlaslattice explicitly removes it.

### 3.6 Execution Request Lane

**Trigger:** Any request to run code, trigger a workflow, deploy, or cause a side effect.  
**Route:** D-Φ-1 gate → CAS-001-A audit state → human gate → Atlas/ORCS audit → TIDELOCKBrain (if repo-related).  
**Template:** `.github/ISSUE_TEMPLATE/execution-request.yml`

The full gate sequence must be documented inline in the issue:

```
D-Φ-1 screening  →  CAS-001-A audit state  →  human gate (@atlaslattice sign-off)
     ↓
Atlas/ORCS audit (ratification_event_id + canon_status + trust_state)
     ↓
TIDELOCKBrain activity receipt (if repo-related)
```

---

## 4. Acceptance Criteria (universal)

The following rules apply to **every** new issue in this repository:

| Rule | Requirement |
|---|---|
| Lane label | Every issue must carry at least one lane label (`tidelock`, `hashlight`, `lucerna`, `rootglass`, `atlasbrain`) |
| Execution guard | Every execution issue must carry both `not-canon` and `not-deployable` until explicitly promoted |
| Raw export | Every raw ingestion issue must populate `raw_export_status` |
| Review gate | Every issue must carry `needs-review` until council or @atlaslattice clears it |

---

## 5. Automation

### 5.1 Label sync

`.github/workflows/sync-labels.yml` runs `crazy-max/ghaction-github-labeler@v5` on every push to `main` that touches `.github/labels.yml`. This keeps live GitHub labels in sync with the YAML definition.

### 5.2 Issue templates

Six issue templates in `.github/ISSUE_TEMPLATE/` pre-populate the correct labels and enforce acceptance checklists via required form fields:

| File | Lane |
|---|---|
| `chatgpt-synthesis.yml` | ChatGPT synthesis |
| `codex-patch.yml` | Codex patch |
| `raw-export.yml` | Raw export |
| `benchmark-claim.yml` | Benchmark claim |
| `public-statement.yml` | Public statement |
| `execution-request.yml` | Execution request |

---

## 6. Metatron's Cube mapping

The 6 lanes map to the 6 outer vertices of Metatron's Cube; the 3 governance labels (`not-canon`, `not-deployable`, `needs-review`) form the inner triangle. TIDELOCKBrain sits at the central node — all execution-bearing work passes through it.

```
          [chatgpt-synthesis]
         /                   \
[public-stmt]             [codex-patch]
    |        ← not-canon →       |
[benchmark]  ← not-deployable → [raw-export]
    |        ← needs-review →    |
         \                   /
          [execution-request]
                  |
           [TIDELOCKBrain]  ← central node
```

---

## 7. References

- `.github/labels.yml` — Label definitions
- `.github/workflows/sync-labels.yml` — Label sync CI
- `.github/ISSUE_TEMPLATE/` — Six lane issue templates
- `archive/spec/gptdream/` — GPTDream++ / Atlas / ORCS spec vault
- `reference_impl/atlas_orcs/compatible.py` — Anti-laundering predicate (Module 4)
- `reference_impl/execution_gate/` — Execution gate reference impl
- `archive/boot/copilotbrain/TIDELOCKBrain/` — TIDELOCKBrain activity receipts
