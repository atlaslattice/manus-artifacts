#!/usr/bin/env python3
"""
Planetarium Revival 12x12 task-matrix simulator.

Status: candidate / not canon / not deployed / no authority.
Purpose: validate and score a balanced 144-task simulation plan without
claiming implementation approval, partnership approval, or canon status.

Usage:
  python tools/simulate_planetarium_144_matrix.py --summary
  python tools/simulate_planetarium_144_matrix.py --json
  python tools/simulate_planetarium_144_matrix.py --csv
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import asdict, dataclass
from io import StringIO
from typing import Iterable


@dataclass(frozen=True)
class Task:
    task_id: str
    house: str
    task: str
    output: str
    status: str = "candidate"
    canon_status: str = "not_canon"
    deployment_status: str = "not_deployed"
    authority_scope: str = "none"


MATRIX: dict[str, list[str]] = {
    "H01 Strategy & Market": [
        'Define neutral-sector positioning statement',
        'Map primary customer segments',
        'Estimate planetarium venue tiers',
        'Draft buyer persona: small planetarium director',
        'Draft buyer persona: museum programmer',
        'Draft buyer persona: mobile dome operator',
        'Draft buyer persona: school district STEM lead',
        'Create pricing hypothesis table',
        'Define subscription versus license decision tree',
        'List first 50 discovery targets',
        'Draft market risk register',
        'Create go/no-go validation criteria',
    ],
    "H02 Customer Discovery": [
        'Draft interview script for planetarium directors',
        'Draft interview script for museum programmers',
        'Draft interview script for school districts',
        'Draft interview script for mobile dome operators',
        'Draft outreach email template',
        'Draft follow-up email template',
        'Define CRM fields',
        'Create scoring rubric for buying intent',
        'Define content-gap question set',
        'Define budget-validation question set',
        'Define decision-cycle question set',
        'Create discovery synthesis template',
    ],
    "H03 Product & Show Library": [
        'Define show format standard',
        'Define runtime bands',
        'Define audience age bands',
        'Create pilot one-page template',
        'Create show Bible template',
        'Create local module template',
        'Create sponsor-safe module template',
        'Define content rating rubric',
        'Define show refresh cadence',
        'Draft first 12 candidate show titles',
        'Define season packaging logic',
        'Define library subscription tiers',
    ],
    "H04 Pilot: Rainbow Bridge": [
        'Create lead pilot logline',
        'Draft 5-act structure',
        'Define emotional arc',
        'Define science anchors',
        'Define cultural collaboration placeholders',
        'Define visual motif list',
        'Define soundtrack direction',
        'Define dome moment set pieces',
        'Draft education companion outcomes',
        'Draft localization hooks',
        'Define minimum viable animatic',
        'Define pilot review gates',
    ],
    "H05 Cultural Participation": [
        'Rename partners as prospective until receipted',
        'Create cultural participation policy',
        'Draft MOU outline',
        'Draft compensation model',
        'Draft revenue-share model',
        'Create approval-rights matrix',
        'Define attribution rules',
        'Define sacred-knowledge exclusion rule',
        'Define no-impersonation AI narration rule',
        'Create partner review checklist',
        'Create benefit-sharing ledger template',
        'Create cultural-risk escalation path',
    ],
    "H06 Science & Education": [
        'Create science accuracy policy',
        'Create source citation standard',
        'Define NASA/ESA/public-domain asset rules',
        'Draft curriculum alignment map',
        'Create educator guide template',
        'Define assessment prompt bank',
        'Define student activity template',
        'Create glossary template',
        'Define expert review workflow',
        'Create misconception-risk register',
        'Define age-appropriate science bands',
        'Draft standards-alignment tracker',
    ],
    "H07 Technical Fulldome": [
        'Define 4K fulldome delivery spec',
        'Define 8K fulldome delivery spec',
        'Define audio delivery spec',
        'Define flat-screen derivative spec',
        'Define VR derivative spec',
        'Create asset folder taxonomy',
        'Create render pipeline checklist',
        'Create projection test checklist',
        'Create dome QC checklist',
        'Define file naming convention',
        'Define versioning convention',
        'Create minimal local preview harness',
    ],
    "H08 Open Source Simulation": [
        'Create task matrix data model',
        'Create scoring model for task readiness',
        'Create dependency model',
        'Create simulation CLI',
        'Create JSON export option',
        'Create CSV export option',
        'Create lane balance checker',
        'Create risk flag checker',
        'Create demo run documentation',
        'Create fixture dataset',
        'Create test plan',
        'Define future CI workflow',
    ],
    "H09 Business Operations": [
        'Create operating budget skeleton',
        'Create production budget skeleton',
        'Create licensing contract checklist',
        'Create sponsorship policy',
        'Create IP ownership policy',
        'Create participant rights checklist',
        'Create vendor list',
        'Create hiring plan',
        'Create advisory board profile list',
        'Create insurance/legal checklist',
        'Create sales pipeline stages',
        'Create quarterly operating cadence',
    ],
    "H10 Marketing & Sales": [
        'Create website landing page outline',
        'Draft one-line investor pitch',
        'Draft one-line buyer pitch',
        'Draft pitch deck outline',
        'Create demo trailer storyboard',
        'Create case study template',
        'Create press kit checklist',
        'Create school outreach package',
        'Create museum conference strategy',
        'Create sponsor pitch package',
        'Create social proof tracker',
        'Create launch event concept',
    ],
    "H11 Governance & Transparency": [
        'Add non-canon status header to all specs',
        'Create public/private release labels',
        'Create attribution ledger fields',
        'Create decision log template',
        'Create review gate checklist',
        'Create overclaim lint terms',
        'Create partnership-claim lint terms',
        'Create canon/deployment boundary note',
        'Create simulation-only badge',
        'Create audit trail template',
        'Create conflict-of-interest disclosure fields',
        'Create transparency report outline',
    ],
    "H12 Roadmap & Execution": [
        'Create 30-day roadmap',
        'Create 90-day roadmap',
        'Create 12-month roadmap',
        'Create first 10 tasks for GitHub issues',
        'Create milestone definitions',
        'Create blocked/on-hold rules',
        'Create MVP definition',
        'Create pilot launch criteria',
        'Create customer discovery completion criteria',
        'Create simulation completion criteria',
        'Create investor readiness criteria',
        'Create best-in-world benchmark checklist',
    ],
} 


REVIEW_TERMS = {
    "cultural": ["cultural", "Indigenous", "sacred", "knowledge", "partner", "MOU", "revenue-share"],
    "legal": ["IP", "contract", "legal", "rights", "approval", "insurance"],
    "sponsor": ["sponsor", "greenwashing"],
    "deployment": ["deployment", "launch", "contracted"],
}


def normalize_output(task: str) -> str:
    prefixes = ("Create ", "Draft ", "Define ", "Map ", "Estimate ", "List ", "Add ", "Rename ")
    for prefix in prefixes:
        if task.startswith(prefix):
            return task[len(prefix):]
    return task


def iter_tasks() -> Iterable[Task]:
    for house_index, (house, tasks) in enumerate(MATRIX.items(), start=1):
        for task_index, task in enumerate(tasks, start=1):
            yield Task(
                task_id=f"H{house_index:02d}-T{task_index:02d}",
                house=house,
                task=task,
                output=normalize_output(task),
            )


def validate(tasks: list[Task]) -> list[str]:
    errors: list[str] = []
    if len(MATRIX) != 12:
        errors.append(f"expected 12 houses; found {len(MATRIX)}")
    for house, house_tasks in MATRIX.items():
        if len(house_tasks) != 12:
            errors.append(f"{house}: expected 12 tasks; found {len(house_tasks)}")
    if len(tasks) != 144:
        errors.append(f"expected 144 tasks; found {len(tasks)}")
    for task in tasks:
        if task.canon_status != "not_canon":
            errors.append(f"{task.task_id}: canon_status must be not_canon")
        if task.deployment_status != "not_deployed":
            errors.append(f"{task.task_id}: deployment_status must be not_deployed")
        if task.authority_scope != "none":
            errors.append(f"{task.task_id}: authority_scope must be none")
    return errors


def review_flags(task: Task) -> list[str]:
    text = f"{task.task} {task.output}"
    flags = []
    for lane, terms in REVIEW_TERMS.items():
        if any(term.lower() in text.lower() for term in terms):
            flags.append(lane)
    return flags


def readiness_score(task: Task) -> int:
    """Simple simulation-only priority score, 0-100."""
    score = 50
    if task.house in {"H02 Customer Discovery", "H08 Open Source Simulation"}:
        score += 25
    if "template" in task.task.lower() or "checklist" in task.task.lower():
        score += 10
    if review_flags(task):
        score -= 5
    if "pilot" in task.task.lower() or "simulation" in task.task.lower():
        score += 5
    return max(0, min(100, score))


def summarize(tasks: list[Task]) -> str:
    lines = [
        "Planetarium Revival 12x12 Simulation Summary",
        "CANON: no | DEPLOYMENT: no | AUTHORITY: none",
        "",
        f"houses: {len(MATRIX)}",
        f"tasks: {len(tasks)}",
        "",
        "house counts:",
    ]
    for house, house_tasks in MATRIX.items():
        lines.append(f"  - {house}: {len(house_tasks)}")
    flagged = [(task, review_flags(task)) for task in tasks if review_flags(task)]
    lines.extend([
        "",
        f"review-flagged tasks: {len(flagged)}",
        "",
        "top 12 simulated priorities:",
    ])
    top = sorted(tasks, key=lambda task: (-readiness_score(task), task.task_id))[:12]
    for task in top:
        flags = ",".join(review_flags(task)) or "none"
        lines.append(f"  {task.task_id} [{readiness_score(task)}] {task.task} | flags={flags}")
    return "\n".join(lines)


def to_csv(tasks: list[Task]) -> str:
    buffer = StringIO()
    writer = csv.DictWriter(
        buffer,
        fieldnames=[
            "task_id",
            "house",
            "task",
            "output",
            "status",
            "canon_status",
            "deployment_status",
            "authority_scope",
            "review_flags",
            "readiness_score",
        ],
    )
    writer.writeheader()
    for task in tasks:
        row = asdict(task)
        row["review_flags"] = "|".join(review_flags(task))
        row["readiness_score"] = readiness_score(task)
        writer.writerow(row)
    return buffer.getvalue()


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", action="store_true", help="print human-readable summary")
    parser.add_argument("--json", action="store_true", help="print task matrix as JSON")
    parser.add_argument("--csv", action="store_true", help="print task matrix as CSV")
    args = parser.parse_args(argv)

    tasks = list(iter_tasks())
    errors = validate(tasks)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if args.json:
        payload = []
        for task in tasks:
            row = asdict(task)
            row["review_flags"] = review_flags(task)
            row["readiness_score"] = readiness_score(task)
            payload.append(row)
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    elif args.csv:
        print(to_csv(tasks), end="")
    else:
        print(summarize(tasks))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
