"""Aetherforge Simulation Sandbox.

Dependency-free local simulator for the non-canon 12x12 task matrix.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import random
import sys
from pathlib import Path
from typing import Any, Iterable

MATRIX_PATH = Path(__file__).with_name("task-matrix-12x12.json")


class SimulationError(ValueError):
    """Raised when matrix or simulation input is invalid."""


@dataclasses.dataclass(frozen=True)
class MatrixReport:
    domain_count: int
    tasks_per_domain: int
    task_count: int
    unique_task_ids: int
    boundary_ok: bool

    @property
    def ok(self) -> bool:
        return (
            self.domain_count == 12
            and self.tasks_per_domain == 12
            and self.task_count == 144
            and self.unique_task_ids == 144
            and self.boundary_ok
        )

    def to_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self) | {"ok": self.ok}


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def load_matrix(path: Path = MATRIX_PATH) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SimulationError(f"Matrix file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SimulationError(f"Matrix file is not valid JSON: {exc}") from exc


def expand_tasks(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    tasks: list[dict[str, Any]] = []
    domains = matrix.get("domains", [])
    if not isinstance(domains, list):
        raise SimulationError("Matrix must contain a domains list.")

    values = ["reproducibility", "validation", "usability", "safety", "interoperability"]
    for domain_index, domain in enumerate(domains, start=1):
        if not isinstance(domain, dict):
            raise SimulationError("Every domain must be an object.")
        domain_id = domain.get("id")
        domain_name = domain.get("name")
        titles = domain.get("tasks")
        if not isinstance(domain_id, str) or not isinstance(domain_name, str):
            raise SimulationError("Every domain must have string id and name fields.")
        if not isinstance(titles, list):
            raise SimulationError(f"Domain {domain_id} must contain a tasks list.")
        for task_index, title in enumerate(titles, start=1):
            if not isinstance(title, str) or not title:
                raise SimulationError(f"Domain {domain_id} task {task_index} must be a title string.")
            tasks.append(
                {
                    "id": f"{domain_id}-T{task_index:02d}",
                    "domain": domain_name,
                    "domain_index": domain_index,
                    "task_index": task_index,
                    "title": title,
                    "status": "candidate",
                    "boundary": "non-canon simulation infrastructure",
                    "simulation_value": values[(domain_index + task_index) % len(values)],
                }
            )
    return tasks


def validate_matrix(matrix: dict[str, Any]) -> MatrixReport:
    domains = matrix.get("domains", [])
    tasks = expand_tasks(matrix)
    counts: dict[str, int] = {}
    for task in tasks:
        counts[task["domain"]] = counts.get(task["domain"], 0) + 1
        if task["boundary"] != "non-canon simulation infrastructure":
            raise SimulationError(f"Task {task['id']} has an invalid boundary field.")

    per_domain_values = set(counts.values())
    tasks_per_domain = per_domain_values.pop() if len(per_domain_values) == 1 else -1
    boundary = matrix.get("boundary", {})
    boundary_ok = (
        isinstance(boundary, dict)
        and boundary.get("canon_adjustments") is False
        and boundary.get("runtime_claims") is False
        and boundary.get("authority_claims") is False
        and boundary.get("runtime_scope") == "local deterministic simulation"
    )

    return MatrixReport(
        domain_count=len(domains),
        tasks_per_domain=tasks_per_domain,
        task_count=len(tasks),
        unique_task_ids=len({task["id"] for task in tasks}),
        boundary_ok=boundary_ok,
    )


def simulate(matrix: dict[str, Any], *, steps: int = 12, seed: int = 144) -> dict[str, Any]:
    if steps < 1:
        raise SimulationError("steps must be at least 1.")

    report = validate_matrix(matrix)
    if not report.ok:
        raise SimulationError(f"Matrix failed validation: {report.to_dict()}")

    tasks = sorted(expand_tasks(matrix), key=lambda task: task["id"])
    rng = random.Random(seed)
    head = sha256_text(canonical_json({"seed": seed, "boundary": matrix["boundary"]}))
    receipts: list[dict[str, Any]] = []
    selected_ids: set[str] = set()

    for step in range(1, steps + 1):
        available = [task for task in tasks if task["id"] not in selected_ids] or tasks
        task = available[rng.randrange(len(available))]
        selected_ids.add(task["id"])
        previous_head = head
        event = canonical_json({"step": step, "task_id": task["id"], "domain": task["domain"], "status": task["status"], "simulation_value": task["simulation_value"]})
        head = sha256_text(previous_head + event)
        receipts.append({"step": step, "task_id": task["id"], "domain": task["domain"], "previous_head": previous_head, "event": event, "head": head})

    domain_counts: dict[str, int] = {}
    for receipt in receipts:
        domain_counts[receipt["domain"]] = domain_counts.get(receipt["domain"], 0) + 1

    return {
        "schema_version": "aetherforge.simulation_result.v1",
        "boundary": matrix["boundary"],
        "seed": seed,
        "steps": steps,
        "matrix_fingerprint": sha256_text(canonical_json(matrix)),
        "receipt_head": head,
        "domain_counts": dict(sorted(domain_counts.items())),
        "receipts": receipts,
        "validation": report.to_dict(),
    }


def render_text(result: dict[str, Any]) -> str:
    lines = ["Aetherforge Simulation Sandbox", f"seed: {result['seed']}", f"steps: {result['steps']}", f"receipt_head: {result['receipt_head']}", f"matrix_fingerprint: {result['matrix_fingerprint']}", "domain_counts:"]
    for domain, count in result["domain_counts"].items():
        lines.append(f"  - {domain}: {count}")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the Aetherforge simulation sandbox.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--matrix-path", default=str(MATRIX_PATH), help="Path to matrix JSON.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="Validate the 12x12 matrix.")
    subparsers.add_parser("matrix", help="Print the matrix summary.")
    simulate_parser = subparsers.add_parser("simulate", help="Run a deterministic simulation.")
    simulate_parser.add_argument("--steps", type=int, default=12)
    simulate_parser.add_argument("--seed", type=int, default=144)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        matrix = load_matrix(Path(args.matrix_path))
        report = validate_matrix(matrix)
        if args.command == "validate":
            payload = report.to_dict()
            print(json.dumps(payload, indent=2, sort_keys=True) if args.json else ("OK" if report.ok else "FAILED"))
            return 0 if report.ok else 1
        if args.command == "matrix":
            payload = {"name": matrix.get("name"), "dimensions": matrix.get("dimensions"), "domains": [{"id": d["id"], "name": d["name"], "task_count": len(d["tasks"])} for d in matrix["domains"]], "validation": report.to_dict()}
            if args.json:
                print(json.dumps(payload, indent=2, sort_keys=True))
            else:
                print(f"{payload['name']}: {payload['dimensions']}")
                for domain in payload["domains"]:
                    print(f"- {domain['id']}: {domain['name']} ({domain['task_count']})")
            return 0
        if args.command == "simulate":
            result = simulate(matrix, steps=args.steps, seed=args.seed)
            print(json.dumps(result, indent=2, sort_keys=True) if args.json else render_text(result))
            return 0
        parser.error(f"Unknown command: {args.command}")
        return 2
    except SimulationError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
