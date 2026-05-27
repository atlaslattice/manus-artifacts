from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/LATTICE_GLOBAL_INDEX.md"

EXCLUDED_PREFIXES = {
    ".git/",
}


def should_include(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return not any(rel.startswith(prefix) for prefix in EXCLUDED_PREFIXES)


def build_index() -> str:
    markdown_files = [
        p for p in ROOT.rglob("*.md") if p.is_file() and should_include(p)
    ]

    grouped: dict[str, list[str]] = defaultdict(list)
    for path in markdown_files:
        rel = path.relative_to(ROOT).as_posix()
        top = rel.split("/")[0] if "/" in rel else "(root)"
        grouped[top].append(rel)

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    lines = [
        "# Lattice Global Index",
        "",
        f"Generated at: `{now}`",
        "",
        "## Domain Summary",
        "",
        "| Domain | Markdown Artifacts |",
        "|---|---:|",
    ]

    for domain in sorted(grouped):
        lines.append(f"| `{domain}` | {len(grouped[domain])} |")

    lines.extend(
        [
            "",
            "## Domain Entry Points",
            "",
        ]
    )

    for domain in sorted(grouped):
        lines.append(f"### {domain}")
        for rel in sorted(grouped[domain])[:10]:
            lines.append(f"- `{rel}`")
        if len(grouped[domain]) > 10:
            lines.append(f"- ... {len(grouped[domain]) - 10} more")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    OUTPUT.write_text(build_index(), encoding="utf-8")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
