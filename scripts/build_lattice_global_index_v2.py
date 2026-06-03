#!/usr/bin/env python3
# STATUS: CANDIDATE — NOT CANON
# AUTHORITY: NONE
# DEPLOYMENT: NONE
"""Build the v2 lattice global index with metadata, links, freshness, and completeness scoring."""

from __future__ import annotations

if __package__ in {None, ''}:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).resolve().parents[1]))

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from scripts.lattice_kg_lib import (
    completeness_score,
    detect_domain,
    detect_lane,
    emit_report,
    extract_markdown_links,
    generate_artifact_id,
    git_last_modified,
    infer_artifact_family,
    iter_files,
    load_metadata,
    path_tokens,
    read_text,
    required_fields_by_family,
    resolve_repo_link,
    sha256_file,
    utc_now,
)


def build_index(repo_root: Path) -> dict:
    required = required_fields_by_family()
    artifacts: list[dict] = []
    inbound = Counter()
    edge_rows: list[dict] = []
    pending_outbound: dict[str, list[str]] = {}
    unresolved_map: dict[str, list[str]] = {}
    for path in iter_files(repo_root, extensions={".md", ".yaml", ".yml", ".py", ".sh", ".json"}):
        rel = path.relative_to(repo_root).as_posix()
        metadata = load_metadata(path) if path.suffix in {".md", ".yaml", ".yml"} else {}
        family = infer_artifact_family(rel)
        domain = detect_domain(rel)
        lane = detect_lane(rel)
        artifact_id = metadata.get("artifact_id") or generate_artifact_id(rel)
        record = {
            "artifact_id": artifact_id,
            "path": rel,
            "domain": domain,
            "lane": lane,
            "domain_tags": sorted({domain, domain + "_surface", path.parts[0].replace("-", "_")}),
            "artifact_family": family,
            "freshness_timestamp": git_last_modified(repo_root, rel),
            "last_modified": git_last_modified(repo_root, rel),
            "sha256": sha256_file(path),
            "completeness_score": completeness_score(metadata, required.get(family, [])),
            "metadata": metadata,
            "relationships": [],
        }
        outbound: list[str] = []
        unresolved: list[str] = []
        if path.suffix == ".md":
            text = read_text(path)
            for link in extract_markdown_links(text):
                target = resolve_repo_link(repo_root, rel, link["target"])
                if target is None:
                    continue
                if (repo_root / target).exists():
                    outbound.append(target)
                    inbound[target] += 1
                    relation = "links_to"
                    line_text = text.splitlines()[link["line"] - 1].lower()
                    for candidate in [
                        "derived_from",
                        "supports",
                        "contradicts",
                        "supersedes",
                        "patches",
                        "routes_to",
                        "reviews",
                        "blocks",
                        "extends",
                        "implements",
                        "cites",
                    ]:
                        if candidate.replace("_", " ") in line_text or candidate in line_text:
                            relation = candidate
                            break
                    edge_rows.append({
                        "from": artifact_id,
                        "to_path": target,
                        "relation": relation,
                        "source_path": rel,
                        "line": link["line"],
                    })
                else:
                    unresolved.append(target)
        pending_outbound[rel] = sorted(set(outbound))
        unresolved_map[rel] = sorted(set(unresolved))
        artifacts.append(record)
    path_to_artifact = {row["path"]: row["artifact_id"] for row in artifacts}
    for row in artifacts:
        rel = row["path"]
        row["outbound_repo_links"] = pending_outbound[rel]
        row["unresolved_repo_links"] = unresolved_map[rel]
        row["incoming_links"] = inbound[rel]
        row["relationship_inference"] = Counter(edge["relation"] for edge in edge_rows if edge["source_path"] == rel)
        row["relationship_inference"] = dict(row["relationship_inference"])
    edges = []
    for edge in edge_rows:
        target_id = path_to_artifact.get(edge["to_path"])
        if not target_id:
            continue
        edges.append({
            "edge_id": f"EDGE-{edge['relation'].upper()}-{len(edges)+1:05d}",
            "from_id": edge["from"],
            "to_id": target_id,
            "relation_type": edge["relation"],
            "source_path": edge["source_path"],
            "line": edge["line"],
        })
    domains = defaultdict(lambda: defaultdict(list))
    for row in artifacts:
        domains[row["domain"]][row["lane"]].append(row)
    coverage = {
        domain: {
            lane: {
                "artifact_count": len(rows),
                "avg_completeness": round(sum(r["completeness_score"] for r in rows) / len(rows), 3),
            }
            for lane, rows in lanes.items()
        }
        for domain, lanes in domains.items()
    }
    return {
        "STATUS": "CANDIDATE — NOT CANON",
        "AUTHORITY": "NONE",
        "DEPLOYMENT": "NONE",
        "index_version": "1.0",
        "index_generated_at_utc": utc_now(),
        "artifact_count": len(artifacts),
        "edge_count": len(edges),
        "average_completeness_score": round(sum(a["completeness_score"] for a in artifacts) / max(len(artifacts), 1), 3),
        "artifacts": artifacts,
        "edges": edges,
        "coverage": coverage,
    }


def is_index_stale(index_generated_at_utc: str, max_age_days: int) -> bool:
    from datetime import UTC, datetime, timedelta

    moment = datetime.fromisoformat(index_generated_at_utc.replace("Z", "+00:00"))
    return datetime.now(UTC) - moment > timedelta(days=max_age_days)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument(
        "--output",
        default="archive/knowledge_graph/lattice_kg/v1_0/lattice_global_index.v1.0.json",
    )
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    payload = build_index(repo_root)
    output_path = repo_root / args.output
    emit_report(payload, "json", output_path)
    print(json.dumps({"output": args.output, "artifact_count": payload["artifact_count"], "edge_count": payload["edge_count"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
