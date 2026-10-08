"""Validation engine: assemble a bundle, run every gate, report the outcome."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from models.common import to_jsonable

from .gates import (
    FAIL,
    GATES,
    NOT_APPLICABLE,
    PASS,
    VETO,
    WARN,
    Bundle,
    GateResult,
)
from .ledger import RESOURCE_BOUNDS, CreditLedger, bound_violations

STATUS_ORDER = {FAIL: 0, VETO: 1, WARN: 2, PASS: 3, NOT_APPLICABLE: 4}


@dataclass
class ValidationReport:
    """Outcome of a full gate sweep."""

    generated_at: str
    gate_results: list[GateResult]
    ledger_entries: int
    ledger_violations: list[dict[str, Any]] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not any(r.failed for r in self.gate_results)

    @property
    def counts(self) -> dict[str, int]:
        out = {PASS: 0, WARN: 0, FAIL: 0, VETO: 0, NOT_APPLICABLE: 0}
        for r in self.gate_results:
            out[r.status] = out.get(r.status, 0) + 1
        return out

    @property
    def failures(self) -> list[GateResult]:
        return [r for r in self.gate_results if r.failed]

    @property
    def warnings(self) -> list[GateResult]:
        return [r for r in self.gate_results if r.status == WARN]

    def to_dict(self) -> dict[str, Any]:
        return to_jsonable({
            "artifact_id": "DJK-NODE-001-VALIDATION-REPORT",
            "status": "VALIDATION_PASSED" if self.passed else "VALIDATION_FAILED",
            "generated_at": self.generated_at,
            "gate_count": len(self.gate_results),
            "counts": self.counts,
            "ledger_entries": self.ledger_entries,
            "ledger_violations": self.ledger_violations,
            "gates": [
                {
                    "gate_id": r.gate_id,
                    "title": r.title,
                    "status": r.status,
                    "detail": r.detail,
                    "findings": r.findings,
                }
                for r in self.gate_results
            ],
        })

    def to_markdown(self) -> str:
        lines = [
            "# Node-001 Validator Report",
            "",
            f"Generated: {self.generated_at}",
            "",
            f"**Overall: {'PASSED' if self.passed else 'FAILED'}**",
            "",
            "| Status | Count |",
            "| --- | --- |",
        ]
        for status in (PASS, WARN, FAIL, VETO, NOT_APPLICABLE):
            lines.append(f"| {status} | {self.counts.get(status, 0)} |")
        lines += [
            "",
            f"Credit-ledger entries: {self.ledger_entries}",
            "",
            "| Gate | Invariant | Status | Detail |",
            "| --- | --- | --- | --- |",
        ]
        for r in sorted(self.gate_results, key=lambda x: (STATUS_ORDER.get(x.status, 9), x.gate_id)):
            detail = r.detail.replace("|", "\\|")
            lines.append(f"| {r.gate_id} | {r.title} | **{r.status}** | {detail} |")
        if self.ledger_violations:
            lines += ["", "## Ledger violations", ""]
            for v in self.ledger_violations:
                lines.append(f"- `{v['kind']}` on `{v['resource_id']}`: {v.get('detail', '')}")
        return "\n".join(lines) + "\n"


def build_bundle(
    artifacts: dict[str, Any],
    node_profile: dict[str, Any] | None = None,
    routing_policy: dict[str, Any] | None = None,
    **overrides: Any,
) -> Bundle:
    """Assemble a :class:`Bundle` from artifacts plus any explicit overrides.

    Overrides exist so that negative-control tests can inject a violation and
    prove the corresponding gate fires.
    """
    from .ledger import build_ledger_from_artifacts

    ledger: CreditLedger = overrides.pop("ledger", None) or build_ledger_from_artifacts(artifacts)

    bundle = Bundle(
        artifacts=artifacts,
        node_profile=node_profile or {},
        routing_policy=routing_policy or {},
        ledger=ledger,
        resource_bounds=dict(RESOURCE_BOUNDS),
    )
    for key, value in overrides.items():
        if not hasattr(bundle, key):
            raise AttributeError(f"Bundle has no field {key!r}")
        setattr(bundle, key, value)
    return bundle


def validate(bundle: Bundle) -> ValidationReport:
    """Run every gate against ``bundle`` and collect the report."""
    results: list[GateResult] = []
    for gate in GATES:
        try:
            results.append(gate.check(bundle))
        except Exception as exc:  # a gate that crashes is a gate that failed
            results.append(
                GateResult(
                    gate.gate_id,
                    gate.title,
                    FAIL,
                    f"Gate raised {type(exc).__name__}: {exc}",
                )
            )
    return ValidationReport(
        generated_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        gate_results=results,
        ledger_entries=len(bundle.ledger.entries),
        ledger_violations=bound_violations(bundle.ledger),
    )
