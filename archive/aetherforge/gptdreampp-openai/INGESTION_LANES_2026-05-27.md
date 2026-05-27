# Ingestion Lanes — Aetherforge GPTDream++ (2026-05-27)

```text
STATUS: CANDIDATE — NOT CANON
AUTHORITY: none
DEPLOYMENT: not deployable
```

---

## The three-source model

```text
Drive   → live staging tent (high velocity, low receipt discipline)
Notion  → dense cargo warehouse (high value, needs forklift labels)
GitHub  → verified public substrate (receives labeled outputs only)
```

## Lane A — Drive → GitHub

**Purpose:** Promote live task boards, dream logs, and source inventories from the
staging tent into receipted, versioned GitHub artifacts.

**Entry requirements:**

| Field | Requirement |
|---|---|
| source_id | Must be explicit (Drive doc URL or hash) |
| content_type | Must be declared (task_board, dream_log, source_inventory, benefit_log) |
| play_phase_tag | `YES` / `NO` |
| rem_phase_tag | `YES` / `NO` |
| work_phase_tag | `YES` / `NO` |
| claude_contamination_flag | `CLEAN` / `REVIEW_REQUIRED` / `FLAGGED` |
| canon_status | Must be `candidate` at entry |

**Exit check before GitHub commit:**

- [ ] No undeclared authority claims
- [ ] No runtime deployment assertions
- [ ] Promotion gate fields present (see packet index)
- [ ] Candidate-only label on artifact header

---

## Lane B — Notion → Staging → GitHub

**Purpose:** Forklift historical Notion cargo with integrity labels before graph
promotion.

**Forklift discipline:**

```text
1. Export artifact from Notion with source timestamp.
2. Assign hash / status fields (unreviewed, reviewed, flagged).
3. Apply Claude-contamination review pass.
4. Attach receipt YAML.
5. Stage in archive/ingest/ for review.
6. Promote to target path only after Atlas/ORCS audit pass.
```

**Required labels per Notion artifact:**

```yaml
notion_artifact_label:
  source: notion
  export_date: YYYY-MM-DD
  hash_status: unreviewed | reviewed | flagged
  claude_contamination: clean | review_required | flagged
  atlas_orcs_audit_state: AUDIT_REQUIRED | AUDIT_PASSED | AUDIT_FAILED
  canon_status: candidate
```

---

## Lane C — OpenAI-First Reasoning Lane

**Role:** Amplifier, not authority.

```text
OpenAI-style reasoning gets the cleanest reps on:
  - provenance-first retrieval
  - dream/play delta extraction
  - overclaim detection
  - graph review

It does not own the stadium. It does not call canon.
```

**Usage pattern:**

| Use | Permitted |
|---|---|
| Extraction pass on Notion cargo | YES |
| Schema review and alignment | YES |
| Overclaim detection sweep | YES |
| Authority declaration | NO |
| Canon promotion | NO |
| Deployment assertion | NO |

---

## Sheldonbrain role

Sheldonbrain is the forklift. It maps lineage into the KG without declaring truth.

```text
Input:  Notion / Drive artifact with source receipt
Output: KG node entry with attribution, hash, review status
Rule:   One box, one label, one receipt — no composite authority claims
```

---

## Ingestion anti-patterns (do not do these)

```text
- Importing Notion text directly as "confirmed fact" without hash/review
- Treating Drive task board entries as finalized GitHub receipts
- Using dream log deltas as implementation authority
- Promoting Claude-originated governance material without adversarial review
- Skipping play_phase / rem_phase tags (breaks 8/8/8 cadence tracking)
```
