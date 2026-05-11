#!/usr/bin/env python3
"""
AtlasBrain hard-gate validator.

STATUS: IMPLEMENTATION SCAFFOLD — NOT CANON
PURPOSE: enforce the AtlasBrain evidence chain before benchmark or public-claim artifacts
         can exist without a linked evidence packet, human-root flag, and authority gate.

Gate rules (from schemas/ATLASBRAIN_EVIDENCE_PACKET_SCHEMA_v0.1.yaml):
  - Any non-README file in benchmarks/ must declare an EVIDENCE PACKET link.
  - Any non-README file in public_claims/ must declare an EVIDENCE PACKET link.
  - Any non-README file in public_claims/ must declare authority_status of
    reviewed_claim or human_root_approved_public_claim.
  - Any quarantine-flagged claim must not appear in public_claims/.
  - Evidence packets must declare authority_status, benchmark_status, and
    human_root_required.

This module is intentionally simple and text-based so it can validate markdown
artifacts without requiring a YAML/JSON parser dependency beyond stdlib.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence


ATLASBRAIN_ROOT = Path(__file__).resolve().parents[2] / "atlasbrain"

# authority_status values that allow public-claim promotion
PUBLIC_CLAIM_ALLOWED_AUTHORITY = {
    "reviewed_claim",
    "human_root_approved_public_claim",
    "ratified_canon",
}

# authority_status values that block promotion entirely
BLOCKED_AUTHORITY = {"quarantined", "disputed"}

_EVIDENCE_PACKET_LINK_RE = re.compile(
    r"evidence[_\s-]?packet[s]?\s*[:=\|]\s*(archive/boot/atlasbrain/evidence_packets/\S+)",
    re.IGNORECASE,
)
_AUTHORITY_STATUS_RE = re.compile(
    r"authority[_\s-]?status\s*[:=\|]\s*(\S+)",
    re.IGNORECASE,
)
_HUMAN_ROOT_RE = re.compile(
    r"human[_\s-]?root[_\s-]?required\s*[:=\|]\s*(true|false)",
    re.IGNORECASE,
)
_BENCHMARK_STATUS_RE = re.compile(
    r"benchmark[_\s-]?status\s*[:=\|]\s*(\S+)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class GateViolation:
    file: str
    rule: str
    detail: str

    def __str__(self) -> str:
        return f"[VIOLATION] {self.file}\n  rule: {self.rule}\n  detail: {self.detail}"


@dataclass
class GateReport:
    checked: list[str] = field(default_factory=list)
    violations: list[GateViolation] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return len(self.violations) == 0

    def summary(self) -> str:
        lines = [
            f"AtlasBrain gate: {'PASS' if self.passed else 'FAIL'}",
            f"  checked: {len(self.checked)}",
            f"  violations: {len(self.violations)}",
            f"  skipped (READMEs): {len(self.skipped)}",
        ]
        for v in self.violations:
            lines.append(str(v))
        return "\n".join(lines)


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def _extract(pattern: re.Pattern[str], text: str) -> str | None:
    m = pattern.search(text)
    return m.group(1).strip().rstrip(".").lower() if m else None


def _non_readme_md_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return [
        f for f in folder.iterdir()
        if f.is_file() and f.suffix == ".md" and f.name.upper() != "README.MD"
    ]


def _rel(path: Path, root: Path) -> str:
    """Return path relative to root, falling back to str(path) if not a subpath."""
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def _check_evidence_packet_link(path: Path, text: str, report: GateReport, root: Path) -> None:
    """Rule: file must declare a link to an evidence packet."""
    link = _EVIDENCE_PACKET_LINK_RE.search(text)
    if not link:
        report.violations.append(GateViolation(
            file=_rel(path, root),
            rule="must_link_evidence_packet",
            detail=(
                "File does not declare an evidence_packet link "
                "(expected pattern: 'EVIDENCE PACKET: archive/boot/atlasbrain/evidence_packets/...')."
            ),
        ))


def _check_public_claim_authority(path: Path, text: str, report: GateReport, root: Path) -> None:
    """Rule: public_claims files must have reviewed_claim or human_root_approved_public_claim."""
    authority = _extract(_AUTHORITY_STATUS_RE, text)
    if authority is None:
        report.violations.append(GateViolation(
            file=_rel(path, root),
            rule="public_claim_must_declare_authority_status",
            detail="File does not declare authority_status.",
        ))
        return

    if authority in BLOCKED_AUTHORITY:
        report.violations.append(GateViolation(
            file=_rel(path, root),
            rule="quarantined_or_disputed_blocks_public_claim",
            detail=f"File has authority_status '{authority}' which blocks public claim routing.",
        ))
        return

    if authority not in PUBLIC_CLAIM_ALLOWED_AUTHORITY:
        report.violations.append(GateViolation(
            file=_rel(path, root),
            rule="public_claim_insufficient_authority_status",
            detail=(
                f"authority_status is '{authority}'. "
                f"Public claims require one of: {sorted(PUBLIC_CLAIM_ALLOWED_AUTHORITY)}."
            ),
        ))


def _check_evidence_packet_fields(path: Path, text: str, report: GateReport, root: Path) -> None:
    """Rule: evidence packets must declare required sentinel fields."""
    required_checks = [
        (_AUTHORITY_STATUS_RE, "authority_status"),
        (_BENCHMARK_STATUS_RE, "benchmark_status"),
        (_HUMAN_ROOT_RE, "human_root_required"),
    ]
    for pattern, field_name in required_checks:
        if not pattern.search(text):
            report.violations.append(GateViolation(
                file=_rel(path, root),
                rule=f"evidence_packet_missing_{field_name}",
                detail=f"Evidence packet does not declare '{field_name}'.",
            ))


def validate_benchmarks(root: Path = ATLASBRAIN_ROOT) -> GateReport:
    """Check all non-README files in benchmarks/."""
    report = GateReport()
    benchmarks_dir = root / "benchmarks"
    for path in _non_readme_md_files(benchmarks_dir):
        text = _read_text(path)
        report.checked.append(str(path))
        _check_evidence_packet_link(path, text, report, root)
    return report


def validate_public_claims(root: Path = ATLASBRAIN_ROOT) -> GateReport:
    """Check all non-README files in public_claims/."""
    report = GateReport()
    public_dir = root / "public_claims"
    for path in _non_readme_md_files(public_dir):
        text = _read_text(path)
        report.checked.append(str(path))
        _check_evidence_packet_link(path, text, report, root)
        _check_public_claim_authority(path, text, report, root)
    return report


def validate_evidence_packets(root: Path = ATLASBRAIN_ROOT) -> GateReport:
    """Check all non-README files in evidence_packets/ for required fields."""
    report = GateReport()
    ep_dir = root / "evidence_packets"
    for path in _non_readme_md_files(ep_dir):
        text = _read_text(path)
        report.checked.append(str(path))
        _check_evidence_packet_fields(path, text, report, root)
    return report


def validate_all(root: Path = ATLASBRAIN_ROOT) -> GateReport:
    """Run all gate checks and merge results into one report."""
    merged = GateReport()
    for sub_report in [
        validate_benchmarks(root),
        validate_public_claims(root),
        validate_evidence_packets(root),
    ]:
        merged.checked.extend(sub_report.checked)
        merged.violations.extend(sub_report.violations)
        merged.skipped.extend(sub_report.skipped)
    return merged


def list_non_readme_files(lane: str, root: Path = ATLASBRAIN_ROOT) -> list[Path]:
    """Utility: list non-README markdown files in a given lane subfolder."""
    return _non_readme_md_files(root / lane)


def main() -> int:
    report = validate_all()
    print(report.summary())
    return 0 if report.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
