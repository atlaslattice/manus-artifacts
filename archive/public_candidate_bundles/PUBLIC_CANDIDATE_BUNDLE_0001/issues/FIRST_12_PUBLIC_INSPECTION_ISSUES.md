# First 12 Public Inspection Issues

Status: candidate staging material  
Canon: no  
Deployment: no  
Authority: none  

## Purpose

Seed the first 12 GitHub issue templates for public inspection of representative
artifacts in PUBLIC_CANDIDATE_BUNDLE_0001.

These issue templates allow any reviewer to open a bounded inspection issue for
a specific artifact without granting canon status, deployment status, or
authority.

## Issue template format

Each issue should use the following body structure:

```markdown
## Artifact inspection request

**Artifact ID:** [ARTIFACT_ID]  
**Artifact path:** [path in repo]  
**Inspection scope:** [one of: receipt check | claim review | release gate | forkability check]

## Inspection checklist

- [ ] source_receipt_status verified
- [ ] public_release_status field present
- [ ] privacy_status field present
- [ ] license_status field present
- [ ] canon_status: not_canon confirmed
- [ ] no secrets, credentials, or private data
- [ ] no unsupported authority claims

## Blockers found

[List blockers or write "none found at this stage"]

## Receipts missing

[List missing receipts or write "no gaps found at this stage"]

## Strongest safe claim

[One sentence only — no crowns, no canon]

## Status

canon_status: not_canon  
deployment_status: inert  
authority_scope: advisory_only  
```

---

## 12 seed inspection topics

### Issue 1 — Bundle manifest review

**Title:** `[INSPECT] PUBLIC_CANDIDATE_BUNDLE_0001 — bundle manifest`  
**Label:** `inspection`, `public-candidate`  
**Scope:** receipt check  
**Artifact:** `archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/BUNDLE_0001_FILE_MANIFEST.yaml`  
**Key question:** Are all planned files accounted for? Are all blockers visible?

---

### Issue 2 — License strategy review

**Title:** `[INSPECT] PUBLIC_CANDIDATE_BUNDLE_0001 — license strategy`  
**Label:** `inspection`, `license`  
**Scope:** release gate  
**Artifact:** `archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/LICENSE_STRATEGY_PENDING.md`  
**Key question:** What is the minimum required license decision before any artifact is released?

---

### Issue 3 — PublicReleaseStatus schema review

**Title:** `[INSPECT] PUBLIC_CANDIDATE_BUNDLE_0001 — PublicReleaseStatus schema`  
**Label:** `inspection`, `schema`  
**Scope:** claim review  
**Artifact:** `archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/schemas/PublicReleaseStatus.yaml`  
**Key question:** Do the enum values and `publish_allowed_only_if` rules block unsafe publication by default?

---

### Issue 4 — Graph-is-not-canon FAQ review

**Title:** `[INSPECT] PUBLIC_CANDIDATE_BUNDLE_0001 — graph-is-not-canon FAQ`  
**Label:** `inspection`, `docs`  
**Scope:** claim review  
**Artifact:** `archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/docs/GRAPH_IS_NOT_CANON_FAQ.md`  
**Key question:** Is the FAQ language clear enough that a new reader cannot mistake graph centrality for authority?

---

### Issue 5 — PR checklist review

**Title:** `[INSPECT] PUBLIC_CANDIDATE_BUNDLE_0001 — PR checklist`  
**Label:** `inspection`, `docs`  
**Scope:** forkability check  
**Artifact:** `archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/PR_CHECKLIST.md`  
**Key question:** Does the checklist block merges without receipts and release status fields?

---

### Issue 6 — Archivist Trust Failure Protocol review

**Title:** `[INSPECT] PUBLIC_CANDIDATE_BUNDLE_0001 — archivist trust failure protocol`  
**Label:** `inspection`, `docs`, `adversarial`  
**Scope:** claim review  
**Artifact:** `archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/docs/ARCHIVIST_TRUST_FAILURE_PROTOCOL.md`  
**Key question:** Does the protocol prevent deletion? Does the sidecar format preserve contamination evidence?

---

### Issue 7 — Sensitive Term Release Gate review

**Title:** `[INSPECT] PUBLIC_CANDIDATE_BUNDLE_0001 — sensitive term release gate`  
**Label:** `inspection`, `docs`, `public-safety`  
**Scope:** release gate  
**Artifact:** `archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/docs/SENSITIVE_TERM_RELEASE_GATE.md`  
**Key question:** Are all five gated term categories complete? Is the hold rule clear?

---

### Issue 8 — Toy graph demo review

**Title:** `[INSPECT] PUBLIC_CANDIDATE_BUNDLE_0001 — toy graph demo`  
**Label:** `inspection`, `demo`, `graph`  
**Scope:** forkability check  
**Artifact:** `archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/examples/toy_graph_demo/README.md`  
**Key question:** Does the demo use sample data only? Does it demonstrate the graph doctrine without real cargo?

---

### Issue 9 — Module 11 packet review

**Title:** `[INSPECT] PUBLIC_CANDIDATE_BUNDLE_0001 — Module 11 forkability packet`  
**Label:** `inspection`, `module-packet`  
**Scope:** claim review  
**Artifact:** `archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/module_packets/MODULE_11_PUBLIC_GITHUB_FORKABILITY_EXCELLENCE.md`  
**Key question:** Are all 12 tasks confirmed or identified? Are the blockers, missing receipts, and safest next actions accurate?

---

### Issue 10 — SRC-DRIVE-500IP-CHARTER-A receipt gap

**Title:** `[RECEIPT GAP] SRC-DRIVE-500IP-CHARTER-A — full raw export missing`  
**Label:** `receipt-gap`, `blocker`  
**Scope:** receipt check  
**Artifact:** `archive/knowledge_graph/receipts/batch_003/` (expected)  
**Key question:** What is the current export status? What is the path to a verified SHA-256 receipt?

---

### Issue 11 — SRC-DRIVE-MISSION-EVIDENCE-PLAN receipt gap

**Title:** `[RECEIPT GAP] SRC-DRIVE-MISSION-EVIDENCE-PLAN — full raw export missing`  
**Label:** `receipt-gap`, `blocker`  
**Scope:** receipt check  
**Artifact:** `archive/knowledge_graph/receipts/batch_003/` (expected)  
**Key question:** What is the current export status? What is the path to a verified SHA-256 receipt?

---

### Issue 12 — Bundle 0001 public-safety review

**Title:** `[RELEASE GATE] PUBLIC_CANDIDATE_BUNDLE_0001 — full public-safety review`  
**Label:** `release-gate`, `public-safety`, `blocker`  
**Scope:** release gate  
**Artifact:** all files in `archive/public_candidate_bundles/PUBLIC_CANDIDATE_BUNDLE_0001/`  
**Key question:** Is any artifact in the bundle unsafe for public GitHub visibility? Is the bundle release-gate language strong enough?

---

## Keeper

Opening an inspection issue does not make an artifact canon.  
Completing an inspection checklist does not authorize release.  
Every issue is review pressure, not ratification.  
Human-root owns the whistle.
