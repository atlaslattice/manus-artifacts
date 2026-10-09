"""Dependency-free guardrail checker for Maui *research* manifest.
Not integrated with Dongjiakou simulator runtime. Run:
python3 research/localities/maui_lahaina_node_001/validate_maui_manifest.py
"""
import json
from pathlib import Path

p = Path(__file__).with_name("maui_node_v0_1.json")
d = json.loads(p.read_text(encoding="utf-8"))
assert d["status"] == "PROPOSED_NON_CANON"
assert d["realized_credit"] == 0
assert d["authority"] == "NONE"
assert not d["geography"]["parcel_selected"]
assert not d["geography"]["private_residence_recorded"]
assert all(v == "UNRESOLVED" for v in d["gates"].values())
assert all(v is None for v in d["measured_inputs"].values())
assert all(m["id"] for m in d["modules"])
print("Maui research manifest guards PASS; physical locality clearance NOT ESTABLISHED")
