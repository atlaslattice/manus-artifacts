#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Shared helpers for lattice knowledge-graph campaign scripts."""

from __future__ import annotations

import csv
import hashlib
import ipaddress
import json
import re
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import yaml

CANDIDATE_STATUS = "CANDIDATE — NOT CANON"
AUTHORITY = "NONE"
DEPLOYMENT = "NONE"
ARTIFACT_ID_REGEX = r"^[A-Z0-9]+-[A-Z0-9_]+-[0-9]{8}-[a-z0-9-]+$"
FRONTMATTER_KEYS = [
    "status",
    "canon_status",
    "deployment_status",
    "authority",
    "artifact_id",
    "path",
    "domain",
    "lane",
    "generated_at_utc",
    "author",
    "version",
]
TRUST_STATES = {
    "candidate_unverified",
    "candidate_reviewed",
    "trusted_provisional",
    "trusted_ratified",
}
CANON_STATES = [
    "raw",
    "candidate",
    "under_review",
    "approved",
    "quarantined",
    "superseded",
    "ratified",
]
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
TOKEN_RE = re.compile(r"[a-z0-9]+")
DATE_PATTERNS = [re.compile(r"(20\d{2})-(\d{2})-(\d{2})"), re.compile(r"(20\d{2})(\d{2})(\d{2})")]
PRIVATE_HOSTS = {"localhost", "127.0.0.1", "0.0.0.0", "::1"}
EXCLUDE_PARTS = {".git", ".pytest_cache", "__pycache__", ".venv"}
DEFAULT_EXTENSIONS = {".md", ".yaml", ".yml"}
DOMAIN_MAP = {
    ".github": "governance",
    "archive": "archive",
    "docs": "docs",
    "scripts": "tools",
    "tests": "validation",
    "schemas": "schema",
    "fixtures": "data",
    "projects": "projects",
}
LANE_HINTS = {
    "knowledge_graph": "kg",
    "gptdream": "gptdream",
    "aetherforge": "aetherforge",
    "governance": "governance",
    "scripts": "tooling",
    "tests": "validation",
    "docs": "docs",
}


def utc_now() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _ordered_dump(data: Any) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True)


class DuplicateKeyLoader(yaml.SafeLoader):
    pass


def _construct_mapping(loader: DuplicateKeyLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"duplicate key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


DuplicateKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)


def load_yaml_strict(text: str) -> tuple[Any, str | None]:
    try:
        return yaml.load(text, Loader=DuplicateKeyLoader), None
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    data, error = load_yaml_strict(raw)
    return (data if isinstance(data, dict) else {}), text[end + 5 :]


def load_metadata(path: Path) -> dict[str, Any]:
    text = read_text(path)
    if path.suffix.lower() == ".md":
        meta, _ = split_frontmatter(text)
        return meta
    data, error = load_yaml_strict(text)
    if error or not isinstance(data, dict):
        return {}
    return data


def dump_frontmatter(metadata: dict[str, Any], body: str) -> str:
    return f"---\n{_ordered_dump(metadata).strip()}\n---\n\n{body.strip()}\n"


def slugify(value: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value.lower())).strip("-") or "artifact"


def path_tokens(path: str) -> list[str]:
    return TOKEN_RE.findall(path.lower().replace("/", " "))


def detect_domain(relative_path: str) -> str:
    parts = Path(relative_path).parts
    if not parts:
        return "root"
    root = parts[0]
    if root in DOMAIN_MAP:
        return DOMAIN_MAP[root]
    if "knowledge_graph" in parts:
        return "knowledge_graph"
    if "gptdream" in parts:
        return "gptdream"
    if "aetherforge" in parts:
        return "aetherforge"
    return root.replace("-", "_")


def detect_lane(relative_path: str) -> str:
    parts = [part.lower().replace("-", "_") for part in Path(relative_path).parts]
    for part in parts:
        if part in LANE_HINTS:
            return LANE_HINTS[part]
    if len(parts) > 1:
        return slugify(parts[1]).replace("-", "_").upper()
    return "GENERAL"


def infer_artifact_family(relative_path: str) -> str:
    path = Path(relative_path)
    if path.suffix == ".py":
        return "script"
    if path.suffix in {".yaml", ".yml"}:
        return "schema" if "schema" in relative_path else "data"
    if path.suffix == ".md":
        if "test" in path.name.lower() or "tests" in path.parts:
            return "test"
        if path.name.lower().startswith("readme"):
            return "doc"
        return "doc"
    if path.suffix == ".sh":
        return "script"
    if path.suffix == ".json":
        return "data"
    return "artifact"


def find_date_string(relative_path: str, fallback: datetime | None = None) -> str:
    for pattern in DATE_PATTERNS:
        match = pattern.search(relative_path)
        if match:
            groups = match.groups()
            return "".join(groups)
    stamp = fallback or datetime.now(UTC)
    return stamp.strftime("%Y%m%d")


def generate_artifact_id(relative_path: str, modified_at: datetime | None = None) -> str:
    domain = detect_domain(relative_path).replace("-", "_").upper()
    lane = detect_lane(relative_path).replace("-", "_").upper()
    date = find_date_string(relative_path, modified_at)
    slug = slugify(Path(relative_path).stem)
    return f"{domain}-{lane}-{date}-{slug}"


def extract_markdown_links(text: str) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for number, line in enumerate(text.splitlines(), start=1):
        for match in MARKDOWN_LINK_RE.finditer(line):
            results.append({"text": match.group(1), "target": match.group(2).strip(), "line": number})
    return results


def resolve_repo_link(repo_root: Path, source_rel: str, target: str) -> str | None:
    target = target.strip()
    if not target or target.startswith("#"):
        return None
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", target) or target.startswith("mailto:"):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0]
    source_parent = Path(source_rel).parent
    if target.startswith("/"):
        candidate = (repo_root / target.lstrip("/")).resolve()
    else:
        candidate = (repo_root / source_parent / target).resolve()
    try:
        return candidate.relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return None


def classify_external_link(target: str) -> str | None:
    parsed = urlparse(target)
    if parsed.scheme not in {"http", "https"}:
        return None
    host = (parsed.hostname or "").lower()
    if parsed.scheme == "http":
        return "non_https"
    if host in PRIVATE_HOSTS:
        return "private_host"
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return None
    if ip.is_private or ip.is_loopback or ip.is_link_local:
        return "private_host"
    return None


def iter_files(repo_root: Path, extensions: set[str] | None = None) -> list[Path]:
    wanted = extensions or DEFAULT_EXTENSIONS
    files: list[Path] = []
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(repo_root)
        if any(part in EXCLUDE_PARTS for part in rel.parts):
            continue
        if wanted and path.suffix.lower() not in wanted:
            continue
        files.append(path)
    return sorted(files)


def git_last_modified(repo_root: Path, relative_path: str) -> str:
    try:
        result = subprocess.run(
            ["git", "--no-pager", "log", "-1", "--format=%cI", "--", relative_path],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip().replace("+00:00", "Z")
    except Exception:  # noqa: BLE001
        pass
    timestamp = datetime.fromtimestamp((repo_root / relative_path).stat().st_mtime, tz=UTC)
    return timestamp.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def completeness_score(metadata: dict[str, Any], required_fields: list[str]) -> float:
    if not required_fields:
        return 1.0
    present = sum(1 for field in required_fields if metadata.get(field) not in (None, "", [], {}))
    return round(present / len(required_fields), 3)


def markdown_heading_anchors(text: str) -> set[str]:
    anchors: set[str] = set()
    for line in text.splitlines():
        if line.startswith("#"):
            heading = line.lstrip("#").strip().lower()
            anchor = re.sub(r"[^a-z0-9\s-]", "", heading)
            anchor = re.sub(r"\s+", "-", anchor).strip("-")
            if anchor:
                anchors.add(anchor)
    return anchors


def required_fields_by_family() -> dict[str, list[str]]:
    common = ["status", "authority", "deployment"]
    return {
        "doc": common + ["artifact_id", "path", "domain", "lane", "version"],
        "schema": common + ["artifact_id", "domain", "version"],
        "test": common + ["artifact_id", "path", "domain", "lane"],
        "script": common + ["artifact_id", "path", "domain", "lane"],
        "data": common + ["artifact_id", "path", "domain"],
        "project": common + ["artifact_id", "path", "domain", "lane"],
        "quest": common + ["artifact_id", "path", "domain", "lane", "version"],
        "governance": common + ["artifact_id", "path", "domain", "lane", "version"],
        "artifact": common,
    }


def emit_report(payload: Any, output_format: str, output_path: Path | None = None) -> str:
    if output_format == "json":
        rendered = json.dumps(payload, indent=2, sort_keys=False, default=str)
    elif output_format == "csv":
        rows = payload if isinstance(payload, list) else payload.get("rows", [])
        if not rows:
            rendered = ""
        else:
            fieldnames = sorted({key for row in rows for key in row})
            from io import StringIO
            buffer = StringIO()
            writer = csv.DictWriter(buffer, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
            rendered = buffer.getvalue()
    else:
        rendered = payload if isinstance(payload, str) else json.dumps(payload, indent=2)
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered + ("\n" if not rendered.endswith("\n") else ""), encoding="utf-8")
    return rendered


def validate_provenance_bit(provenance: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not provenance.get("source_receipt"):
        errors.append("missing source_receipt")
    sha = str(provenance.get("sha256", ""))
    if not re.fullmatch(r"[0-9a-f]{64}", sha):
        errors.append("invalid sha256")
    timestamp = provenance.get("generated_at_utc")
    try:
        datetime.fromisoformat(str(timestamp).replace("Z", "+00:00"))
    except Exception:  # noqa: BLE001
        errors.append("invalid generated_at_utc")
    if not provenance.get("tool_chain"):
        errors.append("missing tool_chain")
    return errors
