#!/usr/bin/env python3
"""
check_ai_evidence_integrity.py

Axis #120 AI evidence integrity checker:
- verifies required AI evidence schema/readme/template files exist
- verifies template files contain an artifact_type + canon_status YAML envelope
- verifies artifact_type values are unique across templates

Exit codes:
  0 — integrity checks pass
  1 — one or more integrity checks fail
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AI_ROOT = REPO_ROOT / "docs" / "ai-evidence"
TEMPLATES_DIR = AI_ROOT / "templates"
README_FILE = AI_ROOT / "README.md"
SCHEMA_FILE = AI_ROOT / "AI_EVIDENCE_SCHEMA_v0.1.md"

REQUIRED_FILES = [
    "docs/ai-evidence/README.md",
    "docs/ai-evidence/AI_EVIDENCE_SCHEMA_v0.1.md",
    "docs/ai-evidence/templates/AI_BUILD_LOG_TEMPLATE.md",
    "docs/ai-evidence/templates/MODEL_EVAL_LOG_TEMPLATE.md",
    "docs/ai-evidence/templates/ARCHITECTURE_DECISION_LOG_TEMPLATE.md",
    "docs/ai-evidence/templates/TRAINING_DATA_PROVENANCE_LOG_TEMPLATE.md",
    "docs/ai-evidence/templates/SAFETY_INCIDENT_LOG_TEMPLATE.md",
    "docs/ai-evidence/templates/DRIFT_PERFORMANCE_LOG_TEMPLATE.md",
    "docs/ai-evidence/templates/REPRODUCIBILITY_RECEIPT_TEMPLATE.md",
    "docs/ai-evidence/templates/AI_CLAIMS_TO_EVIDENCE_MATRIX_TEMPLATE.md",
    "docs/ai-evidence/templates/THIRD_PARTY_VALIDATION_LOG_TEMPLATE.md",
    "docs/ai-evidence/templates/AI_EVIDENCE_INDEX_TEMPLATE.md",
]

FENCED_YAML_RE = re.compile(r"```yaml\s*(.*?)```", re.DOTALL | re.IGNORECASE)
ARTIFACT_TYPE_RE = re.compile(r"artifact_type:\s*([a-zA-Z0-9_]+)")
CANON_STATUS_RE = re.compile(r"canon_status:\s*([A-Z_]+)")


def parse_yaml_envelope(md_text: str) -> tuple[str | None, str | None]:
    match = FENCED_YAML_RE.search(md_text)
    if not match:
        return None, None
    yaml_block = match.group(1)
    artifact_match = ARTIFACT_TYPE_RE.search(yaml_block)
    status_match = CANON_STATUS_RE.search(yaml_block)
    artifact_type = artifact_match.group(1) if artifact_match else None
    canon_status = status_match.group(1) if status_match else None
    return artifact_type, canon_status


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED_FILES:
        if not (REPO_ROOT / rel).exists():
            failures.append(f"missing required AI evidence file: {rel}")

    if README_FILE.exists():
        readme_text = README_FILE.read_text(encoding="utf-8", errors="replace")
        if "109-120" not in readme_text:
            failures.append(
                "docs/ai-evidence/README.md should reflect Axis 10 scope 109-120"
            )
    else:
        failures.append("missing docs/ai-evidence/README.md")

    if SCHEMA_FILE.exists():
        schema_text = SCHEMA_FILE.read_text(encoding="utf-8", errors="replace")
        for required_field in (
            "artifact_id",
            "artifact_type",
            "source_lineage",
            "review_lane",
            "confidence",
            "overclaim_risk",
        ):
            if required_field not in schema_text:
                failures.append(
                    f"schema missing expected field token '{required_field}'"
                )
    else:
        failures.append("missing docs/ai-evidence/AI_EVIDENCE_SCHEMA_v0.1.md")

    artifact_types: dict[str, Path] = {}
    template_files = sorted(TEMPLATES_DIR.glob("*.md")) if TEMPLATES_DIR.exists() else []

    if not template_files:
        failures.append("no templates found in docs/ai-evidence/templates/")

    for template in template_files:
        text = template.read_text(encoding="utf-8", errors="replace")
        artifact_type, canon_status = parse_yaml_envelope(text)
        rel = template.relative_to(REPO_ROOT)

        if not artifact_type:
            failures.append(f"{rel} missing artifact_type in YAML envelope")
            continue
        if not canon_status:
            failures.append(f"{rel} missing canon_status in YAML envelope")
        elif canon_status != "NOT_CANON":
            failures.append(f"{rel} uses unexpected canon_status '{canon_status}'")

        if artifact_type in artifact_types:
            failures.append(
                f"duplicate artifact_type '{artifact_type}' in {rel} and "
                f"{artifact_types[artifact_type].relative_to(REPO_ROOT)}"
            )
        else:
            artifact_types[artifact_type] = template

    print(f"AI evidence integrity: {len(template_files)} template file(s) scanned")
    if failures:
        print(f"  FAILURES: {len(failures)}\n")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print(
        "  PASS: schema/templates are present and template metadata envelopes are valid."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
