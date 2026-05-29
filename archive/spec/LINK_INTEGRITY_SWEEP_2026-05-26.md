# Markdown Link Integrity Sweep Report

```text
STATUS: CANDIDATE REPORT — NOT CANON
DATE: 2026-05-26
SCOPE: All *.md files in repository root and subdirectories
RUNNER: S7 / CopilotBrain / TIDELOCK
TASK: Aetherforge Taskboard #2 — markdown link integrity sweep
```

## Summary

Total broken internal links found: **16**  
Files affected: **3**  
Cause: missing files from legacy codebases; generated output stubs not committed.

---

## Findings

### `codebases/uws/` — 5 broken links across 3 files

These UWS codebase markdown files cross-reference files that were not migrated
from the source repository:

| File | Missing target |
|------|----------------|
| `UWS_AGENTS.md` | `README.md` |
| `UWS_AGENTS.md` | `ALUMINUM.md` |
| `UWS_ALUMINUM.md` | `CONTRIBUTING.md` |
| `UWS_CLAUDE.md` | `AGENTS.md` (×2), `ALUMINUM.md` (×2), `README.md` |

**Triage:** Legacy import gap. Files were present in the original UWS codebase
but not carried over into this repository. Options:
  1. Create stub files with a "not migrated" note.
  2. Remove the broken links and add a "source: external repo" note.
  3. Leave as known gap with a `<!-- BROKEN-LINK: external ref -->` comment.

**Recommended:** Option 2 or 3. Do not fabricate content for files not present in source.

---

### `codebases/sheldonbrain/sheldonbrain-omega-v1/core/grokbrain_v4/COMPLIANCE_REPORT.md` — 8 broken links

This compliance report references generated artifact files that are expected
outputs of running the GrokBrain v4 suite but were never committed:

| Missing file |
|---|
| `artifacts.json` |
| `parsed/mars_terraforming.json` |
| `parsed/by_god/icarus.json` |
| `logs/test_results.json` |
| `logs/twelve_step_validation.json` |

**Triage:** The Python source code (`grokbrain_v4.py`, `twelve_step_validation.py`,
`grok_parser.py`) is present. Running `python test_suite.py` would generate these files.
The COMPLIANCE_REPORT links to expected outputs that were never committed.

**Recommended:** Either run the test suite and commit the outputs, or annotate
the COMPLIANCE_REPORT links as `(generated — run test_suite.py to produce)`.

---

## Links that resolved correctly

All links in the following high-priority paths resolved successfully:

- `README.md` — all links valid ✓
- `projects/aetherforge-top10-taskboard-2026-05-26.md` — valid ✓
- `.github/CONTRIBUTING.md` — valid ✓
- `archive/boot/COUNCIL_BRAIN_INDEX.md` — all links valid ✓
- `archive/boot/gptbrain/` brain folders — valid ✓

---

## Action items

| Priority | Action | Owner |
|----------|--------|-------|
| Medium | Decide on UWS broken-link triage (stub/remove/comment) | @atlaslattice |
| Low | Run GrokBrain test suite and commit or annotate output refs | @atlaslattice / S3 |
| Done | Sweep completed and documented | S7 |

---

*Candidate artifact. Not ratified. Requires full council review.*
