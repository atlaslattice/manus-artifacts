# Krakoa MCP — Historical source static deployment gate (2026-11-22)

**SOURCE-ONLY CANDIDATE / STATIC AUDIT / DEPLOYMENT: HOLD / CANON: NO / AUTHORITY: NONE**

This adds a *non-executing*, opt-in Python-stdlib AST review helper for the existing public historical Krakoa MCP source. The scanner does not import, run, connect, fetch secrets, or create host files from the inspected Python source. It emits only a SHA-256 checksum, byte count, line numbers and categorical findings. It never prints original source lines, file bodies, shell history, chat transcripts or credentials.

## Source evidence inspected

- Original source: `codebases/atlas-vault/krakoa_mcp_server.py` (Git blob `68ca281e8f64b0c1d43b94f31d3818e7dcdf80ff`; 286 lines as observed)
- Companion `codebases/atlas-vault/krakoa_keep_module.py` (Git blob `66732e48e7367c87471bcb687248180d29e9a358`; descriptive stub, not executable Keep integration)
- Parent readiness tracker: https://github.com/atlaslattice/manus-artifacts/issues/26

The original server contains filesystem writes and startup side effects, local shell-history/session metadata scanning, ADB/device control and CLI-driven cloud probing. In the original source these are concrete **review-requiring capabilities**, but a code scan alone cannot establish whether any instance is running, exposed or exploitably accessible. No private data was inspected.

## Reproduce without activating the server

From a local checkout:

```bash
python -m unittest discover -s tools/security -p 'test_krakoa_deployment_static_gate.py' -v
python tools/security/krakoa_deployment_static_gate.py codebases/atlas-vault/krakoa_mcp_server.py
```

The second command is expected to exit **2 / HOLD** on the unmodified historical source. It reads the file as text, parses its Python AST and reports only code/line indicators—not payloads or actual secrets. Never change that command to `python codebases/atlas-vault/krakoa_mcp_server.py` as a validation shortcut; that would execute legacy startup behavior.

The 23 synthetic tests were executed locally against byte-identical GitHub branch source:

- scanner Git blob `0909190e9b2b7c38ed0d50c284d03ecbd6db06b9`
- tests Git blob `a3b7626225dddf24ec632cf86eb2ecad0ad3886a`
- result: **23/23 passing**, Python compilation passing, no provider calls.

This work does **not** claim a full-repository checkout test against the original MCP source. A complete source-only checkout can run the baseline next and retain an actual redacted receipt under separate human review. No GitHub Actions passing run or authenticated source-rights decision has been demonstrated here.

## Fail-closed classifications

| Indicator | Result |
|---|---|
| A sensitive named tool (sphere_write, shadow_sweep, haptic_pulse, gcp_status) | HOLD |
| Import or call into subprocess / real MCP server / active server startup | HOLD |
| Filesystem write, dynamic open mode, known shell/session path reference | HOLD |
| Invalid/oversized/non-Python/absent source | HOLD |
| Syntactically ordinary, unflagged fixture | STATIC_REVIEW_ONLY — **never deploy authorized** |

The classifier is a **heuristic triage aid**, not a security analyzer that proves absence of arbitrary side effects, import aliasing, decorated wrappers, shell injection, data exfiltration or unsafe dependencies. The semantic distinction between trusted caller identity, access scope, consent and actual effect must be checked independently. Literal findings in comments are not automatically executable vulnerabilities; tests demonstrate that comments alone do not trigger executable AST findings.

## Required deployment boundary

Before any hosted Krakoa service is considered: remove or separately sandbox legacy haptic/ADB, history/session scanning and Google/GCP helper paths; authenticate the human principal and verify source consent at READ and RETURN; deny all writes by default; implement durable privacy-preserving audit receipts; test key rotation, permissions, revocation, data minimization, clean container boot, import behavior, live tool registration, network exposure and rollback; require independent security review plus explicit human-root site admission.

**This PR intentionally does not modify the original MCP server, create a deployment manifest, run an MCP service, export private bodies or close issue #26.**

*Keeper:* Source code can describe a tool. It cannot authorize the tool's actions.
