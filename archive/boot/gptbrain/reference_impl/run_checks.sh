#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

echo "== GPTBrain S1 reference implementation checks =="

echo "-- CLI: list C3 claims"
python gptbrain_memory.py claims --confidence C3 >/tmp/gptbrain_claims.json
python - <<'PY'
import json
from pathlib import Path
rows = json.loads(Path('/tmp/gptbrain_claims.json').read_text())
assert rows, 'expected at least one C3 claim'
print(f'claims: {len(rows)}')
PY

echo "-- CLI: trace seed claim"
python gptbrain_memory.py trace --claim-id S1-CLAIM-2026-0509-0001 >/tmp/gptbrain_trace.json
python - <<'PY'
import json
from pathlib import Path
trace = json.loads(Path('/tmp/gptbrain_trace.json').read_text())
assert trace['found'] is True
assert trace['evidence_refs']
print('trace: ok')
PY

echo "-- CLI: challenge seed claim"
python gptbrain_memory.py challenge --claim-id S1-CLAIM-2026-0509-0001 >/tmp/gptbrain_challenge.json
python - <<'PY'
import json
from pathlib import Path
report = json.loads(Path('/tmp/gptbrain_challenge.json').read_text())
assert report['status'] in {'needs_review', 'pass_with_boundaries'}
print(f"challenge: {report['status']}")
PY

echo "-- pytest (full suite)"
python -m pytest -q

echo "checks: pass"
