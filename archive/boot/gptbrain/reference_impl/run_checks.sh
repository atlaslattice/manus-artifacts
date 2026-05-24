#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

tmp_dir="$(mktemp -d /tmp/gptbrain_checks.XXXXXX)"
trap 'rm -rf "$tmp_dir"' EXIT

echo "== GPTBrain S1 reference implementation checks =="

echo "-- preflight: pytest available"
python - <<'PY'
import importlib.util
import sys

if importlib.util.find_spec("pytest") is None:
    raise SystemExit("pytest is required for run_checks.sh. Install it with `python -m pip install pytest`.")

print("pytest: ok")
PY

echo "-- CLI: list C3 claims"
claims_json="$tmp_dir/gptbrain_claims.json"
python gptbrain_memory.py claims --confidence C3 >"$claims_json"
export CLAIMS_JSON="$claims_json"
python - <<'PY'
import json
import os
from pathlib import Path

rows = json.loads(Path(os.environ["CLAIMS_JSON"]).read_text())
assert rows, 'expected at least one C3 claim'
print(f'claims: {len(rows)}')
PY

echo "-- CLI: trace seed claim"
trace_json="$tmp_dir/gptbrain_trace.json"
python gptbrain_memory.py trace --claim-id S1-CLAIM-2026-0509-0001 >"$trace_json"
export TRACE_JSON="$trace_json"
python - <<'PY'
import json
import os
from pathlib import Path

trace = json.loads(Path(os.environ["TRACE_JSON"]).read_text())
assert trace['found'] is True
assert trace['evidence_refs']
print('trace: ok')
PY

echo "-- CLI: challenge seed claim"
challenge_json="$tmp_dir/gptbrain_challenge.json"
python gptbrain_memory.py challenge --claim-id S1-CLAIM-2026-0509-0001 >"$challenge_json"
export CHALLENGE_JSON="$challenge_json"
python - <<'PY'
import json
import os
from pathlib import Path

report = json.loads(Path(os.environ["CHALLENGE_JSON"]).read_text())
assert report['status'] in {'needs_review', 'pass_with_boundaries'}
print(f"challenge: {report['status']}")
PY

echo "-- pytest (full suite)"
python -m pytest -q

echo "checks: pass"
