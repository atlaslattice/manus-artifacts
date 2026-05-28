#!/usr/bin/env python3
"""Build a deterministic machine-readable global index for repo artifacts and logs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

EXCLUDE_PARTS = {".git", ".pytest_cache", "__pycache__"}
EXCLUDE_PATHS = {"archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json"}
LOG_MARKERS = ("log", "journal", "wake_report", "delta_extraction", "receipt")
LANE_MAP = {
    "archive": "archive_ops",
    "archives": "archive_ops",
    "projects": "project_execution",
    "schemas": "schema_validation",
    "tests": "validation",
    "scripts": "tooling",
    "docs": "public_navigation",
    ".github": "ci_governance",
}
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


@dataclass(frozen=True)
class ArtifactRecord:
    artifact_id: str
    path: str
    domain: str
    lane: str
    is_log: bool
    size_bytes: int
    sha256: str
    last_modified_utc: str
    canon_status: str = "not_canon"
    deployment_status: str = "not_deployable"
    trust_state: str = "candidate_unverified"
    outbound_repo_links: list[str] | None = None
    unresolved_repo_links: list[str] | None = None
    inbound_repo_links: list[str] | None = None

    def as_dict(self) -> dict[str, object]:
        payload = self.__dict__.copy()
        payload["source_receipt"] = self.path
        payload["outbound_repo_links"] = payload.get("outbound_repo_links") or []
        payload["unresolved_repo_links"] = payload.get("unresolved_repo_links") or []
        payload["inbound_repo_links"] = payload.get("inbound_repo_links") or []
        return payload


def _should_include(path: Path) -> bool:
    if any(part in EXCLUDE_PARTS for part in path.parts):
        return False
    return path.as_posix() not in EXCLUDE_PATHS


def _iter_files(repo_root: Path) -> list[Path]:
    files = [
        path
        for path in repo_root.rglob("*")
        if path.is_file() and _should_include(path.relative_to(repo_root))
    ]
    return sorted(files, key=lambda path: path.relative_to(repo_root).as_posix())


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _artifact_id(relative_path: str) -> str:
    digest = hashlib.sha1(relative_path.encode("utf-8")).hexdigest()[:16]
    return f"ATLAS-KG-{digest}"


def _domain_and_lane(relative_path: str) -> tuple[str, str]:
    domain = relative_path.split("/", 1)[0] if "/" in relative_path else "_root"
    lane = LANE_MAP.get(domain, "general")
    return domain, lane


def _is_log(relative_path: str) -> bool:
    lowered = relative_path.lower()
    return any(marker in lowered for marker in LOG_MARKERS)


def _extract_repo_links(repo_root: Path, relative_path: str) -> tuple[list[str], list[str]]:
    if not relative_path.lower().endswith(".md"):
        return [], []

    source = repo_root / relative_path
    text = source.read_text(encoding="utf-8", errors="ignore")
    source_parent = Path(relative_path).parent
    resolved: set[str] = set()
    unresolved: set[str] = set()

    for match in MARKDOWN_LINK_RE.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith("#"):
            continue
        if "://" in target or target.startswith("mailto:"):
            continue
        target = target.split("#", 1)[0].strip()
        if not target:
            continue

        candidate = Path(target)
        if target.startswith("/"):
            normalized = Path(target.lstrip("/"))
        else:
            candidate_abs = (repo_root / source_parent / candidate).resolve()
            try:
                normalized = candidate_abs.relative_to(repo_root.resolve())
            except ValueError:
                unresolved.add(target)
                continue

        normalized_posix = normalized.as_posix()
        if (repo_root / normalized_posix).exists():
            resolved.add(normalized_posix)
        else:
            unresolved.add(normalized_posix)

    return sorted(resolved), sorted(unresolved)


def build_index(repo_root: Path) -> dict[str, object]:
    files = _iter_files(repo_root)
    records: list[ArtifactRecord] = []
    route_counter: dict[tuple[str, str], dict[str, int]] = defaultdict(lambda: {"artifacts": 0, "logs": 0})
    fingerprint_parts: list[str] = []
    inbound_link_map: dict[str, set[str]] = defaultdict(set)
    unresolved_link_count = 0

    for path in files:
        rel = path.relative_to(repo_root).as_posix()
        digest = _sha256(path)
        domain, lane = _domain_and_lane(rel)
        log_flag = _is_log(rel)
        modified = datetime.fromtimestamp(path.stat().st_mtime, tz=UTC).isoformat().replace("+00:00", "Z")
        outbound_links, unresolved_links = _extract_repo_links(repo_root, rel)

        record = ArtifactRecord(
            artifact_id=_artifact_id(rel),
            path=rel,
            domain=domain,
            lane=lane,
            is_log=log_flag,
            size_bytes=path.stat().st_size,
            sha256=digest,
            last_modified_utc=modified,
            outbound_repo_links=outbound_links,
            unresolved_repo_links=unresolved_links,
        )
        records.append(record)

        route_counter[(domain, lane)]["artifacts"] += 1
        if log_flag:
            route_counter[(domain, lane)]["logs"] += 1
        unresolved_link_count += len(unresolved_links)
        for linked in outbound_links:
            inbound_link_map[linked].add(rel)

        fingerprint_parts.append(f"{rel}:{digest}")

    fingerprint = hashlib.sha256("\n".join(fingerprint_parts).encode("utf-8")).hexdigest()
    generated_at = datetime.now(UTC).isoformat().replace("+00:00", "Z")

    routes = [
        {
            "route_id": f"ROUTE-{domain.upper()}-{lane.upper()}",
            "domain": domain,
            "lane": lane,
            "artifact_count": counts["artifacts"],
            "log_count": counts["logs"],
        }
        for (domain, lane), counts in sorted(route_counter.items(), key=lambda item: (item[0][0], item[0][1]))
    ]

    artifact_payload = [record.as_dict() for record in records]
    underlinked_markdown = 0
    for payload in artifact_payload:
        inbound = sorted(inbound_link_map.get(payload["path"], set()))
        payload["inbound_repo_links"] = inbound
        if payload["path"].endswith(".md") and not payload["outbound_repo_links"]:
            underlinked_markdown += 1

    return {
        "schema_id": "lattice_global_index.v0.1",
        "generated_at_utc": generated_at,
        "repository_root": repo_root.resolve().as_posix(),
        "snapshot_fingerprint": fingerprint,
        "routes": routes,
        "link_health": {
            "markdown_artifacts_total": sum(1 for payload in artifact_payload if payload["path"].endswith(".md")),
            "underlinked_markdown_artifacts": underlinked_markdown,
            "unresolved_repo_links": unresolved_link_count,
        },
        "artifacts": artifact_payload,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    parser.add_argument(
        "--output",
        default="archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json",
        help="Output JSON path",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    output = (repo_root / args.output).resolve() if not Path(args.output).is_absolute() else Path(args.output)

    index = build_index(repo_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
