#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
GOVERNANCE = ROOT / "governance"

HEADING_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)
STATUS_RE = re.compile(r"^Status:\s+", re.MULTILINE)
DATE_RE = re.compile(r"^Date:\s+", re.MULTILINE)

REQUIRED_SECTIONS = {
    "CANON_AUDIT_PROTOCOL.md": [
        "Audit scope",
        "Audit checklist",
        "Outputs",
    ],
    "COUNCIL_REVIEW_WORKFLOW.md": [
        "Workflow stages",
        "Decision record format",
    ],
    "PROVENANCE_REQUIREMENTS.md": [
        "When provenance requirements apply",
        "Citation format",
        "Failure rule",
    ],
    "RISK_REGISTER.md": [
        "| Risk ID | Domain | Description | Likelihood | Impact | Mitigation | Owner |",
    ],
    "WEBSITE_PUBLICATION_GATE.md": [
        "Entry criteria",
        "Publication checklist",
    ],
}

errors = []
files_checked = 0

for path in sorted(GOVERNANCE.glob("*.md")):
    files_checked += 1
    text = path.read_text(encoding="utf-8")

    if not STATUS_RE.search(text):
        errors.append(f"{path.name}: missing Status line")
    if not DATE_RE.search(text):
        errors.append(f"{path.name}: missing Date line")

    headings = {h.strip() for h in HEADING_RE.findall(text)}
    if not headings and path.name != "RISK_REGISTER.md":
        errors.append(f"{path.name}: missing level-2 sections")

    for required in REQUIRED_SECTIONS.get(path.name, []):
        if required.startswith("| "):
            if required not in text:
                errors.append(f"{path.name}: missing required table header: {required}")
            continue
        if required not in headings:
            errors.append(f"{path.name}: missing required section: {required}")

if errors:
    print("governance required sections validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"governance required sections validation passed ({files_checked} files)")
