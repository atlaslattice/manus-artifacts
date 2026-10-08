STATUS: ARCHIVE PUBLIC CANDIDATE | CANON: no | DEPLOYMENT: no | AUTHORITY: none | PROOF: no | PUBLIC_RELEASE: candidate

Recovered historical Manus artifact. Current review decisions: [build/review/EVIDENCE_APPENDIX.md](https://github.com/atlaslattice/manus-artifacts/blob/master/public_candidate_bundle_0001/nodes/dongjiakou_node_001/build/review/EVIDENCE_APPENDIX.md).

# Node-001 Failure Ledger

**Document ID:** DJK-NODE-001-FAILURE-LEDGER-v0.1
**Status:** PUBLIC_CANDIDATE_NON_CANON
**Date:** 2026-10-06
**Repo:** `atlaslattice/manus-artifacts`
**Reference head:** `4756036f9c428fa3aa1d4cea552ae03367523fb5`

> No shame, no erasure. Every failure becomes a guardrail.

This ledger preserves every defect, drift incident and process failure found while
converting the Node-001 research stack into a reproducible pilot package. Nothing
here is overwritten or deleted. Each entry records what happened, the evidence,
and the guardrail that now prevents recurrence.

---

## Summary

| ID | Severity | Class | Status | Guardrail added |
| --- | --- | --- | --- | --- |
| FL-001 | MEDIUM | Numerical defect in committed evidence | OPEN — awaiting human adjudication | Annotated divergence in reproduction spec; gate G13 unaffected |
| FL-002 | HIGH | Reproducibility failure | CLOSED — fixed by this build | Executable models + 155-check reproduction harness |
| FL-003 | MEDIUM | Missing verification | CLOSED — fixed by this build | 16 validator gates with mandatory negative controls |
| FL-004 | LOW | Implicit justification | OPEN — cosmetic | G02 warns on unjustified zero credits |
| FL-005 | LOW | Constitutional hygiene | OPEN — awaiting human adjudication | Dated deployment manifest separated from architecture |
| FL-006 | LOW | Process / access | OPEN — external dependency | Branch shipped as patch + bundle instead of a PR |

---

## FL-001 — Run 2 average-flow value disagrees with its own stream basis

**Severity:** MEDIUM
**Class:** Numerical defect in committed evidence
**Discovered:** 2026-10-06, by the reproduction harness during this build
**Artifact:** `RUN_2_HYDRO_v0_1.json`
**Field:** `stream_basis.average_flow_m3_s`

**What happened.** The committed artifact records an average flow of
`0.56855619` m³/s for a stated annual stream basis of 17,930,000 m³/year. The
quotient of those two stated quantities is not that number.

**Evidence.**

| Quantity | Value |
| --- | --- |
| Stated annual volume | 17,930,000 m³/year |
| Seconds per year (365 × 24 × 3600) | 31,536,000 s |
| Correct quotient | `0.568556570268899` |
| Value committed | `0.56855619` |
| Implied annual volume from the committed value | 17,929,988.0 m³/year |
| Relative difference | `6.69e-07` |

The correct value rounds to `0.56855657` at eight decimals. The committed value
`0.56855619` differs in the final two digits, which is consistent with a
digit-transposition slip (19 rather than 57) rather than a different underlying
assumption.

**Blast radius.** Isolated. The Run 2 sensitivity table is computed from the
annual volume and head directly and does not consume `average_flow_m3_s`, so no
derived energy, power or fraction figure in the artifact is affected. Every other
Run 2 value reproduces exactly.

**Resolution.** Per the handoff rule — *if a source contradicts an existing
value, preserve both, annotate disagreement, do not overwrite history* — the
committed artifact is left byte-identical. The divergence is recorded as an
annotated divergence in `runs/reproduction_spec.json` with
`kind = DEFECT_IN_COMMITTED_ARTIFACT`, and the reproduction harness reports it
separately from unexplained mismatches so it can never be silently absorbed.

**Guardrail.** The reproduction harness distinguishes three outcomes — MATCH,
ANNOTATED_DIVERGENCE and MISMATCH — and an annotated divergence requires a
written classification and resolution before it is accepted. Nothing may be
annotated away without a stated reason.

**Open action.** Confirm with S10 / GPT whether the committed value should be
superseded by a new artifact (a v0.2 of Run 2) rather than corrected in place.

---

## FL-002 — The committed artifacts were not reproducible from the committed scripts

**Severity:** HIGH
**Class:** Reproducibility failure
**Discovered:** 2026-10-06, by direct execution during this build
**Artifacts:** `run0_baseline_v0_1.py`, `run1_solar_v0_1.py`, `run2_hydro_v0_1.py`,
`run3_compute_v0_1.py`, `run3_compute_v0_2.py`, `run4a_biometabolic_v0_1.py`,
`run0_operating_2025_v0_2.py`

**What happened.** The node directory contains both committed JSON artifacts and
Python scripts that appear to be their source. Executing the scripts does not
regenerate the artifacts. The research layer therefore carried a reproducibility
gap: the published numbers could not be re-derived by the code shipped beside
them.

**Evidence.**

`run1_solar_v0_1.py` emits only four top-level keys —
`artifact_id`, `cases`, `active_module_area_m2`, `local_yield_kWh_per_kWp_year` —
while `RUN_1_SOLAR_v0_1.json` carries eight: `artifact_id`, `baseline`,
`carbon_boundary`, `cases`, `conclusions`, `local_generation_reference`,
`site_inputs`, `status`. The nested site inputs, the carbon boundary and the
conclusions are absent from the script entirely.

`run0_baseline_v0_1.py` emits `inputs.whole_site_SEC` and `inputs.tariff`, while
the committed artifact uses `inputs.whole_site_SEC_kWh_m3` and
`inputs.plant_effective_tariff_CNY_kWh`.

`run3_compute_v0_2.py` requires `--pue` as a mandatory argument and returns a
single flat case, so it cannot reproduce the artifact's four-tier table, its
reference-scenario block, its anti-double-counting block or its result block at
all. Invoking it without `--pue` exits with an argument error.

**Resolution.** Fixed by this build, not by editing the legacy scripts. The
`build/models/` package now contains a pure, deterministic function per run, and
`runs/reproduction_spec.json` pins 155 individual derived values across all seven
runs to the committed artifacts. The legacy scripts are left untouched so the
history of the gap remains visible.

**Guardrail.** `python3 simulator.py reproduce` exits non-zero on any unexplained
divergence, and `tests/test_integration.py` fails the suite if the count of
unexplained divergences is not zero. A number that cannot be re-derived now
blocks the build.

---

## FL-003 — No automated verification of derived numbers existed

**Severity:** MEDIUM
**Class:** Missing verification
**Discovered:** 2026-10-06, during this build

**What happened.** Nothing in the node directory enforced the epistemic rules the
research layer declared. The invariants — UNKNOWN stays UNKNOWN, no double
counting, no sensitivity promoted to a deployment claim, no historical value
populating a current state — existed as prose in the artifacts. Prose does not
fail a build.

**Resolution.** 16 validator gates (G01–G16) now execute against the artifact set
plus a credit ledger that registers every credit against a physical resource with
a sourced availability bound. `python3 simulator.py validate` fails on any FAIL or
VETO.

**Guardrail.** `tests/test_gates_negative.py` feeds every gate a deliberately
violating bundle and asserts that it fires, and a meta-test asserts that the set
of gates with negative controls equals the set of registered gates. A gate
without a negative control fails the suite. A gate that cannot be made to fail is
not a gate.

---

## FL-004 — Run 0 retrofit credits carry zeros without an inline justification

**Severity:** LOW
**Class:** Implicit justification
**Discovered:** 2026-10-06, by gate G02 during this build
**Artifact:** `RUN_0_BASELINE_v0_1.json`, block `retrofit_credit`

**What happened.** The baseline assigns zero credit to solar, mini-hydro, compute,
adaptive fouling control, sono-CIP, resource recovery and OAE. The zeros are
correct and conservative, but the artifact states no reason inline. A reader
cannot distinguish "explicitly zero by design" from "silently imputed zero".

**Resolution.** Gate G02 accepts a zero inside a named explicit zero-credit block
(`baseline_credit`, `retrofit_credit`) and warns on any other unjustified zero in
a credit-bearing field. The block is named, so the gate passes; the absence of an
inline reason is recorded here rather than papered over.

**Guardrail.** Any future zero-credit claim outside a named block produces a WARN
that is reported and preserved.

**Open action.** Optional: add a `reason` string to the `retrofit_credit` block in
a future artifact version. This is a new artifact, not an edit of the existing one.

---

## FL-005 — Dated model references sit inside the operations architecture

**Severity:** LOW
**Class:** Constitutional hygiene
**Discovered:** 2026-10-06, during this build
**Artifact:** `C01_MODEL_ROUTING_POLICY_v0_2.json`

**What happened.** The handoff states plainly: *do not hard-code model versions
into constitutional architecture; put actual checkpoint/version/API/runtime into a
dated deployment manifest.* The routing policy nonetheless names specific current
references — DeepSeek-V4.1-Flash, DeepSeek-V4-Pro, the Qwen3 family, Qwen3.8, and
GPT-5.6 Sol — inside a document titled as operations architecture. The policy does
flag that these are current references requiring a pinned deployment manifest, so
this is a soft violation rather than a hard one.

**Resolution.** `manifests/DEPLOYMENT_MANIFEST.md` is created to carry the dated
checkpoint, API and runtime facts. The routing policy's version references are
treated as illustrative and non-binding; the roles, the routing features and the
vendor-share cap are the durable parts. The existing policy artifact is not
edited.

**Guardrail.** Gate G11 asserts no OT write authority and a
recommendation-approval-PLC path; gate G12 asserts that cross-model agreement is
not evidence. Vendor identity is never load-bearing for a physical action.

**Open action.** When the policy is next versioned, move `current_reference`
values out of the policy and into the deployment manifest by reference.

---

## FL-006 — No pull request could be opened this session

**Severity:** LOW
**Class:** Process / access
**Discovered:** 2026-10-06

**What happened.** The build was performed on a local branch
`s6/node-001-pilot-simulator`. The GitHub connector is disabled in this session,
and enabling it was not completed (a device-authentication step on a new phone
could not be finished). No push and no pull request were possible.

**Resolution.** The deliverable ships as a branch in the local clone plus a git
patch and a git bundle, so the work can be pushed from any machine with the
repository credentials. Nothing was forced, and no credential was bypassed.

**Guardrail.** The S6 seat does not mutate committed state without approval. A
blocked push is recorded rather than worked around.

**Open action.** Enable the GitHub connector, or apply the supplied patch/bundle
and open the pull request.

---

## Ledger maintenance

- Entries are append-only. A closed entry keeps its original text and gains a
  resolution line; it is never rewritten to look as though it never happened.
- A new entry is required for every unexplained reproduction divergence, every
  gate FAIL or VETO observed on the real evidence base, and every process failure
  that prevented a deliverable.
- This ledger is a candidate artifact. It is not canon, and it carries no
  authority.
