#!/usr/bin/env python3
"""Validate lattice global index completeness, freshness, and retrieval behavior."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import UTC, datetime
from pathlib import Path

EXCLUDE_PARTS = {".git", ".pytest_cache", "__pycache__"}
EXCLUDE_PATHS = {"archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json"}
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
GPTDREAMPP_FIXTURE_PATHS = {
    "fixtures/gptdreampp_openai/artifact_contract_records.valid.candidate.json",
    "fixtures/gptdreampp_openai/notion_cargo_queue.valid.candidate.json",
    "fixtures/gptdreampp_openai/bullshit_olympics_review.valid.candidate.json",
}
REQUIRED_SURFACE_PATHS = {
    "README.md",
    "projects/README.md",
    "projects/aetherforge-world-class-authoritative-roadmap-v0.1.md",
    "projects/aetherforge-144-task-campaign-2026-05-27.md",
    "projects/aetherforge-top10-taskboard-2026-05-28.md",
    "projects/aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md",
    "archive/spec/gptdream/GPTDREAM_PLUSPLUS_PUBLIC_RELEASE_PROTOCOL_v0.1.md",
}
REQUIRED_LINK_RELATIONSHIPS = {
    ("README.md", "projects/aetherforge-world-class-authoritative-roadmap-v0.1.md"),
    ("README.md", "projects/aetherforge-144-task-campaign-2026-05-27.md"),
    ("README.md", "projects/aetherforge-top10-taskboard-2026-05-28.md"),
    ("projects/README.md", "projects/aetherforge-world-class-authoritative-roadmap-v0.1.md"),
    ("projects/README.md", "projects/aetherforge-144-task-campaign-2026-05-27.md"),
    ("projects/README.md", "projects/aetherforge-top10-taskboard-2026-05-28.md"),
    ("projects/aetherforge-top10-taskboard-2026-05-28.md", "projects/aetherforge-144-task-campaign-2026-05-27.md"),
    ("projects/aetherforge-top10-taskboard-2026-05-28.md", "projects/aetherforge-world-class-authoritative-roadmap-v0.1.md"),
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_repo_files(repo_root: Path) -> list[str]:
    files = []
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(repo_root)
        if any(part in EXCLUDE_PARTS for part in rel.parts):
            continue
        rel_posix = rel.as_posix()
        if rel_posix in EXCLUDE_PATHS:
            continue
        files.append(rel_posix)
    return sorted(files)


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def compute_fingerprint(repo_root: Path, files: list[str]) -> str:
    lines = []
    for rel in files:
        digest = file_sha256(repo_root / rel)
        lines.append(f"{rel}:{digest}")
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def _extract_repo_links(repo_root: Path, relative_path: str) -> tuple[set[str], set[str]]:
    if not relative_path.endswith(".md"):
        return set(), set()

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

        if target.startswith("/"):
            normalized = Path(target.lstrip("/"))
        else:
            candidate_abs = (repo_root / source_parent / target).resolve()
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

    return resolved, unresolved


def validate_candidate_governance_state(indexed_artifacts: list[dict]) -> list[str]:
    errors: list[str] = []
    for item in indexed_artifacts:
        if item.get("canon_status") != "not_canon":
            errors.append(f"governance check failed: {item.get('path')} has canon_status drift")
        if item.get("deployment_status") != "not_deployable":
            errors.append(f"governance check failed: {item.get('path')} has deployment_status drift")
        if item.get("trust_state") != "candidate_unverified":
            errors.append(f"governance check failed: {item.get('path')} has trust_state drift")
    return errors


def validate_cross_reference_contract(index: dict) -> list[str]:
    errors: list[str] = []
    artifacts = index.get("artifacts", [])
    markdown_rows = [row for row in artifacts if str(row.get("path", "")).endswith(".md")]

    unresolved_count = 0
    underlinked_count = 0
    for row in markdown_rows:
        for field in ("outbound_repo_links", "unresolved_repo_links", "inbound_repo_links"):
            if field not in row:
                errors.append(
                    f"cross-reference check failed: markdown artifact missing '{field}' field: {row.get('path')}"
                )
                continue
            if not isinstance(row[field], list):
                errors.append(
                    f"cross-reference check failed: markdown artifact field '{field}' must be a list: {row.get('path')}"
                )

        outbound = row.get("outbound_repo_links", [])
        unresolved = row.get("unresolved_repo_links", [])
        if isinstance(outbound, list) and len(outbound) == 0:
            underlinked_count += 1
        if isinstance(unresolved, list):
            unresolved_count += len(unresolved)

    health = index.get("link_health", {})
    if health.get("markdown_artifacts_total") != len(markdown_rows):
        errors.append("cross-reference check failed: markdown_artifacts_total does not match indexed markdown count")
    if health.get("underlinked_markdown_artifacts") != underlinked_count:
        errors.append("cross-reference check failed: underlinked_markdown_artifacts mismatch")
    if health.get("unresolved_repo_links") != unresolved_count:
        errors.append("cross-reference check failed: unresolved_repo_links mismatch")

    return errors


def validate_surface_link_integrity(repo_root: Path) -> list[str]:
    errors: list[str] = []
    links_by_source: dict[str, set[str]] = {}
    unresolved_by_source: dict[str, set[str]] = {}

    for rel in REQUIRED_SURFACE_PATHS:
        if not (repo_root / rel).exists():
            errors.append(f"link integrity check failed: required surface missing: {rel}")
            continue
        resolved, unresolved = _extract_repo_links(repo_root, rel)
        links_by_source[rel] = resolved
        unresolved_by_source[rel] = unresolved
        if unresolved:
            errors.append(
                f"link integrity check failed: {rel} contains unresolved repo links: {sorted(unresolved)}"
            )

    for source, target in sorted(REQUIRED_LINK_RELATIONSHIPS):
        if source not in links_by_source:
            continue
        if target not in links_by_source[source]:
            errors.append(f"link integrity check failed: missing required link {source} -> {target}")

    return errors


def validate_metadata_consistency(repo_root: Path) -> list[str]:
    errors: list[str] = []
    files = {
        "projects/aetherforge-world-class-authoritative-roadmap-v0.1.md": ("AUTHORITY: NONE", "NOT CANON"),
        "projects/aetherforge-144-task-campaign-2026-05-27.md": ("AUTHORITY: NONE", "NOT CANON"),
        "projects/aetherforge-top10-taskboard-2026-05-28.md": ("AUTHORITY: NONE", "NOT CANON"),
        "archive/spec/gptdream/GPTDREAM_PLUSPLUS_PUBLIC_RELEASE_PROTOCOL_v0.1.md": ("AUTHORITY: NONE", "NOT CANON"),
    }
    for rel, required_tokens in files.items():
        target = repo_root / rel
        if not target.exists():
            errors.append(f"metadata check failed: required file missing: {rel}")
            continue
        text = target.read_text(encoding="utf-8", errors="ignore")
        for token in required_tokens:
            if token not in text:
                errors.append(f"metadata check failed: {rel} missing token '{token}'")
    return errors


def validate_index(repo_root: Path, index_path: Path, max_age_days: int) -> list[str]:
    errors: list[str] = []
    index = load_json(index_path)
    repo_files = iter_repo_files(repo_root)

    indexed_artifacts = index.get("artifacts", [])
    indexed_paths = sorted(item["path"] for item in indexed_artifacts)

    missing = sorted(set(repo_files) - set(indexed_paths))
    extra = sorted(set(indexed_paths) - set(repo_files))

    if missing:
        errors.append(f"completeness check failed: {len(missing)} repository files missing from index")
    if extra:
        errors.append(f"stale-index check failed: {len(extra)} indexed paths not present in repository")

    for item in indexed_artifacts:
        candidate_path = repo_root / item["path"]
        if not candidate_path.exists():
            errors.append(f"broken-link check failed: indexed path does not exist: {item['path']}")
            break

    expected_fingerprint = compute_fingerprint(repo_root, repo_files)
    if index.get("snapshot_fingerprint") != expected_fingerprint:
        errors.append("stale-index check failed: snapshot_fingerprint mismatch")

    generated = datetime.fromisoformat(index["generated_at_utc"].replace("Z", "+00:00"))
    age_days = (datetime.now(UTC) - generated).days
    if age_days > max_age_days:
        errors.append(f"stale-index check failed: index is {age_days} days old (max {max_age_days})")

    required_paths = {
        "README.md",
        "projects/README.md",
        "projects/aetherforge-world-class-authoritative-roadmap-v0.1.md",
        "projects/aetherforge-144-task-campaign-2026-05-27.md",
        "projects/aetherforge-top10-taskboard-2026-05-28.md",
        "projects/aetherforge-metatrons-cube-top50-taskboard-2026-05-26.md",
        "archive/knowledge_graph/lattice_kg/v0_5/LATTICE_AETHERFORGE_GPTDREAM_UNIFIED_MISSION_CHARTER_v0.1.md",
        "archive/knowledge_graph/lattice_kg/v0_5/lattice_hypercube_144_scoreboard.v0.1.json",
        "archive/knowledge_graph/lattice_kg/v0_5/LATTICE_WORLD_CLASS_CONTRIBUTOR_START_HERE_v0.1.md",
        "archive/knowledge_graph/lattice_kg/v0_5/LATTICE_KG_GLOSSARY_v0.1.md",
        "archive/knowledge_graph/lattice_kg/v0_5/LATTICE_KG_QUERY_COOKBOOK_v0.1.md",
        "archive/knowledge_graph/lattice_kg/v0_5/LATTICE_STATE_OF_GRAPH_WEEKLY_REPORT_2026-05-27.md",
    }
    index_by_path = {item["path"]: item for item in indexed_artifacts}
    index_by_id = {item["artifact_id"]: item for item in indexed_artifacts}

    for required in required_paths:
        record = index_by_path.get(required)
        if record is None:
            errors.append(f"retrieval check failed: required path not indexed: {required}")
            continue
        if record["artifact_id"] not in index_by_id:
            errors.append(f"retrieval check failed: artifact_id lookup missing for {required}")

    errors.extend(validate_candidate_governance_state(indexed_artifacts))
    errors.extend(validate_cross_reference_contract(index))
    errors.extend(validate_metadata_consistency(repo_root))
    errors.extend(validate_surface_link_integrity(repo_root))
    errors.extend(validate_gptdreampp_staging_fixtures(repo_root))

    return errors


def validate_gptdreampp_staging_fixtures(repo_root: Path) -> list[str]:
    errors: list[str] = []
    for rel in sorted(GPTDREAMPP_FIXTURE_PATHS):
        if not (repo_root / rel).exists():
            errors.append(f"fixture check failed: required GPTDream++ fixture missing: {rel}")

    if errors:
        return errors

    artifact_fixture = load_json(
        repo_root / "fixtures/gptdreampp_openai/artifact_contract_records.valid.candidate.json"
    )
    record_required = {
        "artifact_id",
        "artifact_path",
        "source_pointer",
        "lineage_parent_ids",
        "provenance_receipt_path",
        "content_hash_sha256",
        "hash_status",
        "claim_class",
        "review_state",
        "lifecycle_state",
        "promotion_eligibility",
        "contamination_flags",
        "contradiction_links",
        "supersedes_links",
        "tests_required",
        "tests_run",
        "blockers",
        "next_safest_action",
    }
    records = artifact_fixture.get("records", [])
    if not records:
        errors.append("fixture check failed: artifact contract fixture has no records")
    else:
        record_ids = [record.get("artifact_id") for record in records]
        if len(record_ids) != len(set(record_ids)):
            errors.append("fixture check failed: artifact contract records contain duplicate artifact_id values")

        allowed_lifecycle_states = {
            "intake",
            "in_review",
            "blocked",
            "ready_for_adjudication",
        }

        for idx, record in enumerate(records):
            missing = sorted(record_required - set(record))
            if missing:
                errors.append(
                    f"fixture check failed: artifact contract record {idx} missing required fields: {missing}"
                )
            if record.get("promotion_eligibility") == "ratified":
                errors.append(
                    f"fixture check failed: artifact contract record {idx} cannot be ratified in candidate fixture"
                )
            if record.get("lifecycle_state") not in allowed_lifecycle_states:
                errors.append(
                    f"fixture check failed: artifact contract record {idx} has invalid lifecycle_state"
                )

            relationship_fields = ("lineage_parent_ids", "contradiction_links", "supersedes_links")
            for field in relationship_fields:
                value = record.get(field)
                if not isinstance(value, list):
                    errors.append(
                        f"fixture check failed: artifact contract record {idx} field '{field}' must be a list"
                    )
                    continue
                non_str = [entry for entry in value if not isinstance(entry, str)]
                if non_str:
                    errors.append(
                        f"fixture check failed: artifact contract record {idx} field '{field}' must contain only strings"
                    )

            supersedes = record.get("supersedes_links", [])
            if isinstance(supersedes, list) and record.get("artifact_id") in supersedes:
                errors.append(
                    f"fixture check failed: artifact contract record {idx} cannot supersede itself"
                )
            for target in supersedes:
                if isinstance(target, str) and target not in record_ids:
                    errors.append(
                        f"fixture check failed: artifact contract record {idx} supersedes unknown artifact_id '{target}'"
                    )

            if record.get("lifecycle_state") == "blocked" and not record.get("blockers"):
                errors.append(
                    f"fixture check failed: artifact contract record {idx} is blocked but has no blockers"
                )

    notion_fixture = load_json(repo_root / "fixtures/gptdreampp_openai/notion_cargo_queue.valid.candidate.json")
    notion_queue = notion_fixture.get("queue", [])
    if not notion_queue:
        errors.append("fixture check failed: notion cargo queue fixture has no queue rows")
    else:
        blocked_rows = [row for row in notion_queue if row.get("blocked") is True]
        if not blocked_rows:
            errors.append("fixture check failed: notion cargo queue fixture must include at least one blocked row")
        for idx, row in enumerate(notion_queue):
            if row.get("blocked") is True and row.get("route") != "intake":
                errors.append(
                    f"fixture check failed: notion cargo queue row {idx} blocked entries must route to intake"
                )

    review_fixture = load_json(
        repo_root / "fixtures/gptdreampp_openai/bullshit_olympics_review.valid.candidate.json"
    )
    required_checks = {
        "overclaim_detector",
        "false_authority_detector",
        "canon_drift_detector",
        "contradiction_link_completeness",
        "source_to_claim_traceability",
    }
    checks = review_fixture.get("checks", [])
    observed_checks = {row.get("check_id") for row in checks}
    missing_checks = sorted(required_checks - observed_checks)
    if missing_checks:
        errors.append(f"fixture check failed: bullshit olympics fixture missing checks: {missing_checks}")
    if review_fixture.get("promotion_outcome") == "ratified":
        errors.append("fixture check failed: bullshit olympics fixture cannot declare ratified outcome")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".", help="Repository root directory")
    parser.add_argument(
        "--index",
        default="archive/knowledge_graph/lattice_kg/v0_5/lattice_global_index.v0.1.json",
        help="Path to index JSON",
    )
    parser.add_argument("--max-age-days", type=int, default=7)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    index_path = (repo_root / args.index).resolve() if not Path(args.index).is_absolute() else Path(args.index)

    errors = validate_index(repo_root, index_path, max_age_days=args.max_age_days)
    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    print("All lattice quality gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
