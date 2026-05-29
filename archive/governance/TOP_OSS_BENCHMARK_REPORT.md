---
artifact_id: LAUNCH-REPORT-OSS-BENCHMARK-001
title: Top OSS Benchmark Report
status: candidate
created: 2026-05-29
owner: council
tags: [launch, benchmark, oss, scorecard, comparators]
---

# Top OSS Benchmark Report

> Baseline comparison of Atlas Lattice against exemplar open-source repositories.

status: candidate

---

## Purpose

Atlas Lattice aims to be world-class, so it needs a repeatable benchmark against repositories that are already recognized as best-in-class in specific dimensions. This report defines the comparison set, the scoring method, and the first baseline findings.

---

## Comparator Set

| Repository | Why it is included | Primary comparison dimensions |
|------------|--------------------|-------------------------------|
| `kubernetes/kubernetes` | Mature OSS governance and large-scale CI/CD discipline | Governance, CI/CD, security |
| `microsoft/vscode` | Outstanding contributor experience and docs surface | Docs, DX, community |
| `golang/go` | High-trust testing and release discipline | Testing, reliability, release ops |
| `facebook/react` | Strong ecosystem and community reach | Community, onboarding, changelog |
| `oasis-tcs/odata-specs` | Spec-governance rigor and standards publication | Canon, ratification, specification quality |

---

## Benchmark Method

1. Use the scoring rubric in `WORLDCLASS_SCORECARD_FRAMEWORK.md`.
2. Compare Atlas Lattice only on dimensions visible in the public repository surface.
3. Record a 0–5 score for each of the 12 Faces.
4. Capture one strength, one gap, and one next action for each dimension.

---

## Baseline Comparison Summary

| Face | Atlas Lattice | Relative position vs top comparator | Key gap |
|------|---------------|--------------------------------------|---------|
| Governance & Canon | Strong written policy surface | Competitive on documentation, behind on ratified operating history | More real ratification records |
| Legal, Privacy, Trust | Good policy coverage | Ahead of many repos in explicit trust docs | More operational evidence logs |
| Repository Architecture | Strong | Competitive | More landing-page polish |
| Documentation Excellence | Good | Behind VS Code on navigation density and polish | Tighter curation and maintenance loops |
| Knowledge Graph Layer | Distinctive strength | Ahead on explicit KG framing | Need public query/API surface |
| CI/CD & Automation | Developing | Behind Kubernetes/Go | Implement more documented workflows |
| Security & Supply Chain | Good | Behind Kubernetes on enforcement depth | More automation and evidence |
| Testing & Reliability | Strong | Behind Go on depth and coverage automation | Broader regression surfaces |
| Accessibility & Global Reach | Developing | Behind major OSS programs | More implementation beyond policy |
| Developer Experience | Developing | Behind VS Code | Better bootstrap and first-run flow |
| Community & Ecosystem | Early | Behind React/VS Code | More contributor and discussion volume |
| Launch & Operations | Good planning surface | Ahead on planning clarity, behind on executed release history | Publish recurring reports and releases |

---

## Benchmark Conclusions

- Atlas Lattice is already unusually strong in governance explicitness and knowledge-graph framing.
- The largest gaps are not policy gaps; they are execution-evidence gaps in CI, community, DX, and release operations.
- The clearest path to world-class status is to convert documented standards into recurring public evidence.

---

## Review Cadence

| Activity | Frequency | Output |
|----------|-----------|--------|
| Lightweight benchmark refresh | Quarterly | Update this report appendix or successor issue |
| Full comparator review | Annually | New benchmark report version |
| Milestone check | Before v1.0 launch | Launch readiness decision input |

---

## Linked Artifacts

- `WORLDCLASS_SCORECARD_FRAMEWORK.md`
- `WORLDCLASS_SCORECARD_BASELINE.md`
- `KPI_DASHBOARD_DESIGN.md`
- `V1_MILESTONE_PLAN.md`

---

*Atlas Lattice Foundation · status: candidate*
