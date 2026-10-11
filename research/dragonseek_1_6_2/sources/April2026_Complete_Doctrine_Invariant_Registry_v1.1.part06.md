ance v6.0 vs Fiction-Derived Failure Mode v6.0.2) | Multi-version drift | HIGH | §3.3 — Council Round + Convenor |
| **DR-2** | **D-61 v6.0.4 cross-reference drift** (Constitutional Scribe error) — referenced "Constitutional Validator / Project Glasswing" not matching v6.0.2 ratification "Operator Override Inviolability" | v6.0.4 §C.1 | HIGH | §3.5 — Council Round + Convenor |
| **DR-3** | Manus v1.5 §14.1 "D-61 Open-Weight Audit" (caught by v1.5 evaluation; Manus v1.7 fix attempt) | Manus v1.5 propagation from DR-2 | HIGH | Resolved in Manus v1.7; underlying §3.5 conflict remains |
| **DR-4** | **Manus v1.7 D-73-75 reassignment** — replaced canonical Naming Authority/Drift Blocker/Notion Control Plane with Social Credit/Data Residency/Cultural Frame | Manus v1.7 §14.1a | HIGH | §3.8 — Council Round + Convenor; Notion AI inventory supports v6.0.5 Version A |
| **DR-5** | Manus v1.7 INV-20 + INV-21 marked "Locked Since v1.7" without Council ratification | Manus v1.7 §0.1 | MEDIUM | §2.2 — Council Round disposition; Manus v1.7 §5 Convenor Disposition Items confirms ratification deferred |
| **DR-6** | **INV-17 dual-naming** (Provenance vs Dividend Rail) | v6.0 baseline + Manus v1.5/v1.7 + Notion AI silence | MEDIUM | §2.2 — recovery from `invariants_registry.py` |
| **DR-7** | **D-11 dual-naming** (Honest Naming vs Metabolic Accountability) | v6.0+ corpus + Manus v1.5/v1.7 + Notion AI confirmation | MEDIUM | §3.1 — recovery + disposition |
| **DR-8** | Doctrines 1-50 + INV-1-16 canonical text not directly accessible in current session | Pre-v6.0 corpus | MEDIUM | Manus archive deep-dive (Phase 2) — **partially resolved by Notion AI inventory in v1.1** |
| **DR-9** | Manus v1.7 §14.1 Doctrine summary expansion (4 → 10) does not include all v1.5 evaluation recommendations (12-15 representative) | Manus v1.7 partial fix | LOW | Acceptable Build Seat operational decision |
| **DR-10** | Manus v1.7 §3.4 M24 description includes configurability per v1.5 evaluation, but Three-Body frame default count text could be more explicit | Manus v1.7 | LOW | Acceptable; refinement if Council disposes |
| **DR-11 (NEW v1.1)** | **INV-0 (Nobody Dies) missed entirely in registry v1.0** — foundational Invariant not surfaced in v6.0+ corpus | Constitutional Scribe v1.0 oversight (Notion AI catch) | MEDIUM-HIGH | v1.1 integrates; honest disclosure; Manus archive deep-dive should verify |
| **DR-12 (NEW v1.1)** | **INV-1 through INV-16 specific names + INV-25-37 specific names + INV-31a/31b/32a sub-specs** missing from registry v1.0 | Constitutional Scribe v1.0 oversight (Notion AI catch) | MEDIUM | v1.1 integrates per Notion AI inventory |
| **DR-13 (NEW v1.1)** | **5 unnumbered "Doctrine" artifacts** (Civilian AI Oversight, Human Trigger, Data Sovereignty & Preservation, Shielded Voice, Open Source) not in registry v1.0 | Constitutional Scribe v1.0 oversight (Notion AI catch) | LOW | §3.11 — Council disposition on registry vs domain-doctrine status |
| **DR-14 (NEW v1.1)** | **`toolchain/invariants_registry.py` "39 invariants" claim** vs separate INV-18, INV-19, INV-20, INV-21 additions — count reconciliation pending | Multiple sources (Notion AI + v6.0+ corpus + Manus v1.7) | MEDIUM | Manus archive deep-dive Phase 2 — load registry.py content |

**Total drift events**: 14 (4 HIGH, 6 MEDIUM, 4 LOW; up from 10 in v1.0)

---

## §6 Recommended Source-of-Truth Lock Per Notion AI

Per Notion AI's recommendation (§C of their report) + my registry compilation:

### §6.1 INV Source of Truth

**Primary**: `toolchain/invariants_registry.py` (in atlaslattice/ GitHub org)
**Reason**: Notion AI cites this file as canonical "39 invariants registry"; multiple Notion canonical pages reference it as source of truth.
**Action required**: 
1. Manus archive deep-dive Phase 2: load file content into Notion canonical for Constitutional Scribe direct visibility
2. Reconcile with INV-18 (v6.0.4 ratification), INV-19 (v6.0.6 ratification), INV-20-21 (Manus v1.7 PROPOSED) if not already in registry.py
3. Lock as authoritative INV registry once reconciled

**Secondary references** (ratification provenance):
- v6.0.4 patch document for INV-18 ratification text + originator
- v6.0.6 patch document for INV-19 ratification text + originator
- Notion canonical pages for INV-25, INV-27, INV-28, INV-29 detailed specifications
- AHCEP v1.0 for INV-31a, INV-31b, INV-32a sub-specifications
- ConstitutionalRouter v0.1 for INV-33-36 origin specifications
- DISTRIBUTED_AGENCY_PRINCIPLES.md for INV-37 specification

### §6.2 Doctrine Source of Truth

**Primary**: Aluminum OS v6.0.6 (most recent ratified canonical Aluminum OS document)
**Reason**: Most recent comprehensive Doctrine integration; explicitly references full ratification chain v6.0 → v6.0.6.
**Action required**:
1. Constitutional Scribe authors v6.0.7 reconciliation patch resolving:
   - DR-1 (D-60 conflict)
   - DR-2 / DR-3 (D-61 conflict)
   - DR-4 (D-73-75 conflict — high confidence resolution per Notion AI silence on Manus v1.7 alternate)
   - DR-7 (D-11 name drift)
2. v6.0.7 incorporates pre-v6.0 Doctrines 1-50 from Manus archive deep-dive recovery
3. Lock as authoritative Doctrine registry post-Council ratification

**Secondary references** (substrate provenance):
- v6.0 baseline through v6.0.6 patches for ratification chain
- Manus Build Plans v1.0/v1.5/v1.7 for operational integration patterns
- Notion canonical pages for unnumbered Doctrine artifacts

### §6.3 Domain Doctrine Registry (NEW in v1.1)

**Per Notion AI surfacing of unnumbered Doctrine artifacts + Convenor "include everything" disposition**:

**Recommendation**: maintain SEPARATE Domain Doctrines registry (NOT consuming numbered Doctrine slots) for:
- Civilian AI Oversight Doctrine (Artifact #65)
- Human Trigger Doctrine
- Data Sovereignty & Preservation Doctrine
- Shielded Voice Doctrine (Artifact #70)
- Open Source Doctrine (Artifact #60)

**Why separate registry**: numbered Doctrine registry is **constitutional substrate** for Aluminum OS (governs system behavior). Domain Doctrines are **subject-matter-specific governance** (apply to specific operational domains like military AI oversight, surveillance, etc.). Conflating reduces clarity of constitutional reference.

**Per Council disposition**: option exists to fold any/all into numbered registry as new D-83+ entries.

---

## §7 Resolution Sequence (Updated for v1.1)

**Phase A — Verify (no resolution yet)**:
1. Council seats verify own ratifications aga