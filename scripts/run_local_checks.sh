#!/usr/bin/env bash
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
set -euo pipefail
python3 scripts/build_lattice_global_index.py --repo-root .
python3 scripts/build_lattice_global_index_v2.py --repo-root .
python3 scripts/validate_markdown_links.py --repo-root .
python3 scripts/validate_edge_directions.py --repo-root .
python3 scripts/validate_no_self_promotion.py --repo-root .
python3 scripts/validate_trust_state.py --repo-root .
python3 scripts/validate_deployment_state.py --repo-root .
python3 -m pytest -q tests/
