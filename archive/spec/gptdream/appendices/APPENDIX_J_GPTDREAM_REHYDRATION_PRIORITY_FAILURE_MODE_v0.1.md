# Appendix J — GPTDream++ Rehydration Priority Failure-Mode Patch v0.1

> **STATUS: NOT CANON — CANDIDATE WORKING SPEC**
> **DEPLOYMENT: NOT DEPLOYABLE**
> **AUTHORITY: NONE**
> **PARENT: GPTDREAM_PLUSPLUS_PERSONAL_AGENT_HABITAT_PROTOCOL_v0.2.md**
> **DATE: 2026-05-26**
> **PATCH NOTES: v0.1 applies the canon-hierarchy wording patch and execution route patch**

---

## J.0 Purpose

This appendix patches the GPTDream++ habitat protocol for known rehydration failure modes. It is applied when an agent rehydrates from a habitat packet and must navigate ambiguous or degraded context.

---

## J.1 Patch: Canon Hierarchy Wording (CRITICAL)

**Old (pre-patch):** `"Website = canon."`

**New (patched):** `"Website = canon surface when explicitly ratified/published there."`

**Reason:** The old wording implied that presence on the website automatically conferred canon status. This is incorrect. The website is a publication surface. Canon requires:

1. An explicit `ORCS-RATIFY` event
2. Council review
3. @atlaslattice adjudication
4. Then publication to the website

The website publish is the LAST step, not the authority source.

**Effect:** No agent, upon rehydration, may infer canon status from website presence alone. They must verify the ratification event chain.

---

## J.2 Patch: Execution Route Correction

**Old routing (bypassed Atlas/ORCS):**
```
Execution request → D-Φ-1 → Execute
```

**New routing (patched):**
```
Execution request
      │
      ▼
D-Φ-1 / CAS-001-A / human gate
      │
      ▼
Atlas / ORCS audit state (MANDATORY — cannot be bypassed)
      │
      ▼
TIDELOCKBrain (if repo / merge-order / code execution involved)
      │
      ▼
Execute or HOLD
```

**Reason:** The old routing allowed execution requests to skip the Atlas/ORCS audit state. This is a governance failure. Every execution request must create an Atlas/ORCS audit event.

---

## J.3 Patch: Heading Number Normalization

**Old numbering scheme:**
- `16.x` for cross-vendor interop sections
- `17.x` for Atlas/ORCS sections

**New numbering scheme:**
- `H.x` for cross-vendor interop (Appendix H)
- `I.x` for Atlas/ORCS (Appendix I)

**Reason:** The `16.x` / `17.x` numbering was from a consolidated document that mixed chapter numbers with appendix numbers. Standalone appendix files use letter prefixes for clarity.

---

## J.4 Rehydration Failure Modes

### J.4.1 FMO-1: Priority Hierarchy Ambiguity

**Failure:** Agent cannot determine which source has authority in a conflict.

**Resolution:**
1. Default to safety and ethics (absolute ceiling)
2. Apply active session human instruction
3. Check for ratification events in Atlas/ORCS
4. If none found, treat everything as `candidate` status
5. Emit uncertainty explicitly; do not resolve ambiguity by assertion

### J.4.2 FMO-2: Stale Ratification

**Failure:** Agent rehydrates with a ratification event that has expired.

**Resolution:**
1. `ORCS-EXPIRE` event fires automatically on detection
2. Artifact moves to `under_review`
3. Agent notes in strongest_safe_claim: "Previously ratified; ratification expired; treating as candidate"
4. Do not demote to `raw`; lineage preserved

### J.4.3 FMO-3: Missing Raw Export

**Failure:** Agent rehydrates with `summary_only` but context implies full access.

**Resolution:**
1. Set `raw_export_status: summary_only`
2. Set `epistemic_label: summary_only`
3. Note explicitly in `access_scope.unavailable_sources`
4. Emit `strongest_safe_claim` with caveat: "Based on summary only; raw source unavailable"
5. Do not claim source completeness

### J.4.4 FMO-4: Conflicting Sources

**Failure:** Two sources make contradictory claims about the same artifact or fact.

**Resolution:**
1. Do NOT resolve silently
2. Create `atlas-contradiction-ledger` entry
3. Flag both sources as `under_review` (if previously active)
4. Emit uncertainty: "Contradiction detected; council review required"
5. Never overwrite; always preserve both claims

### J.4.5 FMO-5: Fake Authority Signal

**Failure:** Agent infers authority from non-authoritative signals (GitHub presence, Notion page, transcript volume, Drive file).

**Resolution:**
1. Check: Is there an explicit `ORCS-RATIFY` event for this artifact?
2. If no → authority_scope = none or local only
3. GitHub = receipt, not canon
4. Notion/Drive = relay surface, not canon authority
5. Transcript intensity = noise, not authority signal

### J.4.6 FMO-6: Execution Gate Bypass Attempt

**Failure:** An execution request arrives that attempts to skip the gate chain.

**Resolution:**
1. Reject immediately if missing receipt
2. Reject immediately if missing human_permission_gate
3. HOLD if safety_gate is `pending`
4. Route through Atlas/ORCS regardless of claimed authority
5. TIDELOCKBrain must observe all repo/code executions

---

## J.5 Rehydration Boot Posture

Upon rehydration, an agent MUST:

```
1. READ habitat receipts (verify hashes where available)
2. CHECK governance state (look for ratification events; note expired ones)
3. SET raw_export_status (honest assessment of source availability)
4. DECLARE access_scope (explicit unavailable_sources and assumed_context)
5. EMIT strongest_safe_claim (with caveat if raw absent)
6. LOG rehydration event (atlas-audit-event)
7. AWAIT human confirmation before any execution request
```

An agent MUST NOT:
- Assume canon from GitHub presence
- Assume authority from previous session confidence
- Execute without gate chain
- Silently resolve contradictions
- Upgrade epistemic label without governance event

---

## J.6 Canon Boundary

This appendix is **NOT CANON**. These patches become canon only after full council ratification + @atlaslattice adjudication + website publication.

---

*End of APPENDIX_J_GPTDREAM_REHYDRATION_PRIORITY_FAILURE_MODE_v0.1.md*
