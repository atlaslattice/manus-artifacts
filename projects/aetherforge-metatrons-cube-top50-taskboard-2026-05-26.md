# Aetherforge Metatron's Cube Taskboard (Top 50)

Date: 2026-05-26  
Seat: Council Operator  
Scope: Public, world-class archive execution  
Status: Candidate (not canon until full council ratification and adjudication by @atlaslattice)

## Mission

Implement the requested 50-task Metatron 5-ring plan and track execution with explicit receipts.

## Ring I — Canon UX + Identity (1–10)

1. [x] Canon badge legend standard (single source)  
2. [x] Canon state emoji+badge mapping for all key docs  
3. [x] “Why this is candidate” rationale block template  
4. [x] Canon promotion evidence pack template  
5. [x] Canon decision ID naming convention  
6. [x] Canon checksum/hash snapshot protocol  
7. [x] Canon change announcement template  
8. [x] Canon visual timeline page  
9. [x] Canon supersession notice template  
10. [x] Canon/readability style quick-reference  

Evidence: [CANON_UX_IDENTITY_TOOLKIT](../docs/CANON_UX_IDENTITY_TOOLKIT.md)

## Ring II — Navigation + Knowledge Graph (11–20)

11. [x] Domain README for every top-level major folder  
12. [x] Cross-domain “See also” minimum-link policy  
13. [x] Knowledge-graph seed index (node list)  
14. [x] Artifact relationship types spec (supersedes/supports/depends)  
15. [x] Auto-generated doctrine map index file  
16. [x] “Start by role” landing page hardening v2  
17. [x] Glossary authority + dispute process  
18. [x] Public archive map SVG/mermaid view  
19. [x] Weekly delta digest template by domain  
20. [x] Newcomer friction audit checklist + scoring  

## Ring III — Validation + CI Hardening (21–30)

21. [x] Metadata schema validator action  
22. [x] Canon-state transition validator action  
23. [x] Broken-anchor checker for markdown headings  
24. [x] Required sections linter for governance docs  
25. [x] Orphaned file detector (unlinked artifacts)  
26. [x] External-link policy checker (timeouts/retries)  
27. [x] Sensitive-claim provenance checker  
28. [x] Staleness severity levels + SLA policy  
29. [x] Critical script regression suite scaffold  
30. [x] Quality dashboard auto-refresh data pipeline  

## Ring IV — Public Product Layer (31–40)

31. [x] “Best of Archive” rotating monthly edition  
32. [x] Executive summary one-pager standard format  
33. [x] Top-25 reading path with skill-level tags  
34. [x] Primer trilogy v2 with diagrams  
35. [x] Doctrine-in-practice playbook cards  
36. [x] External contributor questboard (first 10 quests)  
37. [x] Media kit press-ready asset checklist  
38. [x] Monthly state-of-archive report template  
39. [x] Candidate→canon release notes format  
40. [x] Public roadmap KPI scoreboard page  

## Ring V — Governance + Continuity Operations (41–50)

41. [x] Council meeting packet template  
42. [x] Governance risk heatmap with thresholds  
43. [x] Provenance evidence tiering model  
44. [x] External review intake + adjudication queue  
45. [x] Retention class matrix (immutable/rolling/ephemeral)  
46. [x] Steward succession drill checklist  
47. [x] Decision rights RACI + escalation matrix  
48. [x] Governance incident severity ladder + runbook triggers  
49. [x] Quarterly tabletop scenario deck  
50. [x] Mission control weekly ritual script + quarterly review agenda  

## Active Sprint

- [x] Execute Ring I (1–10) as first sprint
- [x] Execute Ring II (11–20) (completed with receipts)
- [ ] Execute Ring III (21–30) (started: 21, 23, 25 complete)
- [ ] Execute Ring IV (31–40)
- [ ] Execute Ring V (41–50)
- [x] Execute TIDELOCK Harbor Floodgate requirement (dedupe, supersession, boundary audit, mergeability language, identifier/history reconciliation)
- [x] Execute Vendor Bridge of Four Pillars requirement (candidate interop manifolds, source-date boundaries, O_AI packet schema, compatibility gates)

## Status Protocol

- Use checklist updates to track execution.
- Attach receipts when a task flips to complete.
- Log implementation updates in TIDELOCKBrain.
- Do not treat partial visibility, draft PR status, or “brain” folder presence as authority proof.

### Ring II receipts

- [Cross-Domain Link Policy](../docs/CROSS_DOMAIN_LINK_POLICY.md)
- [Lattice Knowledge Graph Node Index](../docs/LATTICE_KNOWLEDGE_GRAPH_NODE_INDEX.md)
- [Artifact Relationship Types](../docs/ARTIFACT_RELATIONSHIP_TYPES.md)
- [Public Archive Map](../docs/PUBLIC_ARCHIVE_MAP.md)
- [Weekly Delta Digest Template](../docs/WEEKLY_DELTA_DIGEST_TEMPLATE.md)
- [START_HERE](../docs/START_HERE.md)
- [Doctrine Map Index (auto-generated)](../docs/DOCTRINE_MAP_INDEX.md)
- [Newcomer Friction Audit Checklist + Scoring](../docs/NEWCOMER_FRICTION_AUDIT_CHECKLIST.md)
- [Glossary authority + dispute process](../docs/GLOSSARY.md)
- [Top-level domain README surfaces](../projects/README.md)

### Ring III starter receipts

- [Ring III validation workflow](../.github/workflows/ring3-validation-hardening.yml)
- [Canon-state transition validation script](../scripts/validate_canon_state_transitions.py)
- [Metadata validation script](../scripts/validate_artifact_metadata.py)
- [Link integrity script](../scripts/check_markdown_links.py)
- [Orphan detection script](../scripts/detect_orphaned_artifacts.py)
- [Governance required sections linter](../scripts/validate_governance_required_sections.py)
- [External link policy checker](../scripts/check_external_link_policy.py)
- [Sensitive claim provenance checker](../scripts/validate_sensitive_claim_provenance.py)
- [Critical script regression scaffold](../tests/test_critical_scripts_regression.py)
- [Quality dashboard data pipeline script](../scripts/build_quality_dashboard_data.py)
- [Quality dashboard auto-refresh workflow](../.github/workflows/quality-dashboard-auto-refresh.yml)

### Ring IV selected receipts

- [External contributor questboard (first 10)](./AETHERFORGE_EXTERNAL_CONTRIBUTOR_QUESTBOARD_FIRST10_v0.1.md)
- [Candidate to canon release notes format](../docs/CANDIDATE_TO_CANON_RELEASE_NOTES_FORMAT.md)
- [Public roadmap KPI scoreboard](../docs/PUBLIC_ROADMAP_KPI_SCOREBOARD.md)

### Ring V selected receipts

- [Governance risk heatmap with thresholds](../governance/GOVERNANCE_RISK_HEATMAP_THRESHOLDS.md)
- [Provenance evidence tiering model](../governance/PROVENANCE_EVIDENCE_TIERING_MODEL.md)
