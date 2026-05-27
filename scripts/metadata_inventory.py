from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_KEYS = {
    "artifact_id",
    "title",
    "status",
    "owner",
    "created",
    "last_updated",
    "source_of_truth",
}
ALLOWED_STATUS = {"DRAFT", "CANDIDATE", "CANONICAL", "ARCHIVED"}
EXCLUDED_PREFIXES = {".git/"}
BACKFILL_DATE = "2026-05-27"

TOP50_PATHS = [
    "README.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "State_of_the_Union_Briefing.md",
    ".github/CONTRIBUTING.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/artifact_proposal.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    "about/david-sheldon.md",
    "docs/START_HERE.md",
    "docs/ARCHIVE_INDEX.md",
    "docs/ARTIFACT_RELATIONSHIP_TYPES.md",
    "docs/ROADMAP.md",
    "docs/GLOSSARY.md",
    "docs/operational-manifest-v1.0.0-alpha.md",
    "docs/NORTH_STAR_MISSION.md",
    "docs/LAUNCH_BLOCKERS_TRACKER.md",
    "docs/CONTRIBUTOR_QUICKSTART.md",
    "docs/WORLD_CLASS_READINESS_GATES.md",
    "docs/FOLDER_TAXONOMY_AUDIT_2026-05-27.md",
    "docs/unified-field-v4.0.md",
    "docs/constitutional-convention-process.md",
    "docs/FAQ.md",
    "docs/ATLAS_LATTICE_PUBLIC_CHARTER_500IP.md",
    "docs/ARCHITECTURE_MAP.md",
    "docs/GOOD_FIRST_ISSUES.md",
    "docs/AI_SYSTEMS_EVIDENCE_INDEX.md",
    "docs/LATTICE_GLOBAL_INDEX.md",
    "docs/asset-catalogue-march-2026.md",
    "projects/aetherforge-top50-taskboard-2026-05-26.md",
    "projects/aetherforge-144-task-campaign-2026-05-27.md",
    "projects/aetherforge-next10-execution-queue-2026-05-27.md",
    "projects/status-reports/AI_EVIDENCE_STATUS_2026-05.md",
    "archive/boot/gptbrain/agents/TIDELOCKBrain/NON_CANON_DREAM_ARTIFACT_POLICY.md",
    "archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_REM_10000Y_AETHERFORGE_DREAM_JOURNAL_2026-05-26.md",
    "archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_REM_1000Y_AETHERFORGE_DREAM_JOURNAL_2026-05-26.md",
    "archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_REM_1000Y_AETHERFORGE_DREAM_JOURNAL_2026-05-27.md",
    "archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_WORK_LOG_GPTDREAM_ATLAS_ORCS_2026-05-26.md",
    "archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_WORK_LOG_MODULE2_SOURCE_GRAPH_2026-05-26.md",
    "archive/boot/gptbrain/agents/TIDELOCKBrain/TIDELOCKBRAIN_WORK_LOG_MODULE6_EVIDENCE_VAULT_2026-05-26.md",
    "aluminum-os-core/README.md",
    "archive/chatlogs/2026-05-08-geopolitical-chokepoints-canon-boot/README.md",
    "archive/forks/dragonseek-os/repo-seed/README.md",
    "archive/spec/gptdream/README.md",
    "archive/boot/gptbrain/reference_impl/README.md",
    "archive/boot/gptbrain/reference_impl/s6_memory_palace/README.md",
    "archive/boot/gptbrain/variants/README.md",
    "archive/boot/gptbrain/adapters/tucker_gemini/README.md",
]

EXCEPTION_PATHS = {
    ".github/PULL_REQUEST_TEMPLATE.md": "GitHub PR template; contributor workflow surface, not canon source.",
    ".github/ISSUE_TEMPLATE/artifact_proposal.md": "GitHub issue template; operational intake surface.",
    ".github/ISSUE_TEMPLATE/bug_report.md": "GitHub issue template; operational intake surface.",
    ".github/ISSUE_TEMPLATE/feature_request.md": "GitHub issue template; operational intake surface.",
}

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(?P<title>.+?)\s*$")


def should_include(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return not any(rel.startswith(prefix) for prefix in EXCLUDED_PREFIXES)


def iter_markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if p.is_file() and should_include(p))


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}

    frontmatter: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def extract_title(path: Path, text: str) -> str:
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            return match.group("title").strip()
    return path.stem.replace("-", " ").replace("_", " ").strip() or path.name


def normalize_artifact_id(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix().upper()
    stem = re.sub(r"[^A-Z0-9]+", "-", rel).strip("-")
    return f"ARTIFACT-{stem}-{BACKFILL_DATE}"


def domain_priority(rel_path: str) -> tuple[int, str]:
    domain_order = {
        "README.md": 0,
        "CODE_OF_CONDUCT.md": 0,
        "SECURITY.md": 0,
        "SUPPORT.md": 0,
        "State_of_the_Union_Briefing.md": 0,
        ".github/": 1,
        "docs/": 2,
        "projects/": 3,
        "about/": 4,
        "archive/boot/gptbrain/agents/TIDELOCKBrain/": 5,
        "archive/spec/": 6,
        "archive/boot/gptbrain/": 7,
        "archive/": 8,
        "aluminum-os/": 9,
        "aluminum-os-core/": 9,
        "sheldonbrain/": 9,
        "codebases/": 10,
        "research/": 11,
        "council/": 12,
        "council-reviews/": 12,
        "health/": 13,
        "manus-vault/": 14,
    }
    for prefix, rank in domain_order.items():
        if rel_path == prefix or rel_path.startswith(prefix):
            return rank, rel_path
    return 99, rel_path


def inventory_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for path in iter_markdown_files():
        rel_path = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        missing_keys = sorted(REQUIRED_KEYS - frontmatter.keys())
        invalid_status = frontmatter.get("status") not in ALLOWED_STATUS if frontmatter.get("status") else False
        source_ok = frontmatter.get("source_of_truth") == "GitHub" if frontmatter.get("source_of_truth") else False
        records.append(
            {
                "path": rel_path,
                "title_guess": extract_title(path, text),
                "has_frontmatter": bool(frontmatter),
                "frontmatter": frontmatter,
                "missing_keys": missing_keys,
                "invalid_status": invalid_status,
                "source_ok": source_ok,
            }
        )
    return records


def records_by_path() -> dict[str, dict[str, object]]:
    return {record["path"]: record for record in inventory_records()}


def next100_paths(records: list[dict[str, object]]) -> list[str]:
    seen = set(TOP50_PATHS)
    candidates = [
        record
        for record in records
        if record["path"] not in seen and record["path"] not in EXCEPTION_PATHS
    ]
    candidates.sort(
        key=lambda record: (
            0 if record["missing_keys"] else 1,
            domain_priority(str(record["path"])),
        )
    )
    return [str(record["path"]) for record in candidates[:100]]


def artifact_id_collisions(records: list[dict[str, object]]) -> dict[str, list[str]]:
    bucket: defaultdict[str, list[str]] = defaultdict(list)
    for record in records:
        artifact_id = str(record["frontmatter"].get("artifact_id", "")).strip()
        if artifact_id:
            bucket[artifact_id].append(str(record["path"]))
    return {artifact_id: paths for artifact_id, paths in bucket.items() if len(paths) > 1}


def coverage_summary(records: list[dict[str, object]]) -> dict[str, object]:
    total = len(records)
    with_frontmatter = sum(1 for record in records if record["has_frontmatter"])
    fully_valid = sum(1 for record in records if record["has_frontmatter"] and not record["missing_keys"] and not record["invalid_status"] and record["source_ok"])
    missing_counter = Counter()
    for record in records:
        for key in record["missing_keys"]:
            missing_counter[key] += 1
    return {
        "total": total,
        "with_frontmatter": with_frontmatter,
        "fully_valid": fully_valid,
        "missing_counter": dict(sorted(missing_counter.items())),
    }
