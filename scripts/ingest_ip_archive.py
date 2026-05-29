from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
HOUSE_REGISTRY_PATH = ROOT / "archive/knowledge_graph/HOUSE_SEED_REGISTRY.json"
DEFAULT_OUTPUT_PATH = ROOT / "archive/knowledge_graph/intake/INGESTED_IP_RECORDS.jsonl"


@dataclass(frozen=True)
class IngestedRecord:
    artifact_id: str
    source_path: str
    sha256: str
    hsn: str
    review_state: str
    route_gate: str
    provenance: dict

    def to_json(self) -> str:
        return json.dumps(
            {
                "record_type": "candidate_artifact",
                "artifact_id": self.artifact_id,
                "source_path": self.source_path,
                "sha256": self.sha256,
                "hsn": self.hsn,
                "review_state": self.review_state,
                "route_gate": self.route_gate,
                "provenance": self.provenance,
            },
            sort_keys=True,
        )


def _iter_files(source_dir: Path, max_files: int) -> Iterable[Path]:
    count = 0
    for path in sorted(source_dir.rglob("*")):
        if not path.is_file():
            continue
        count += 1
        if count > max_files:
            return
        yield path


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def _load_houses(path: Path = HOUSE_REGISTRY_PATH) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload.get("houses", [])


def _assign_hsn(seed: str, index: int) -> str:
    byte = hashlib.sha256(f"{seed}:{index}".encode("utf-8")).digest()
    h = (byte[0] % 12) + 1
    s = (byte[1] % 12) + 1
    n = (byte[2] % 12) + 1
    return f"H{h:02d}-S{s:02d}-N{n:02d}"


def ingest_archive(
    source_dir: Path,
    output_path: Path = DEFAULT_OUTPUT_PATH,
    max_files: int = 500,
) -> list[IngestedRecord]:
    source_dir = source_dir.resolve()
    houses = _load_houses(HOUSE_REGISTRY_PATH)
    records: list[IngestedRecord] = []
    for index, file_path in enumerate(_iter_files(source_dir, max_files), start=1):
        rel = file_path.relative_to(ROOT) if file_path.is_relative_to(ROOT) else file_path
        house = houses[(index - 1) % len(houses)]["house_id"] if houses else "H01"
        seed = f"{house}:{rel.as_posix()}"
        records.append(
            IngestedRecord(
                artifact_id=f"ip:{index:05d}",
                source_path=rel.as_posix(),
                sha256=_sha256(file_path),
                hsn=_assign_hsn(seed, index),
                review_state="candidate",
                route_gate="human-root-review",
                provenance={
                    "extractor": "scripts/ingest_ip_archive.py",
                    "source_root": str(source_dir),
                },
            )
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(record.to_json() for record in records) + "\n", encoding="utf-8")
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest candidate IP artifacts into lattice intake JSONL.")
    parser.add_argument("source_dir", help="Directory containing candidate source artifacts.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_PATH), help="JSONL output path.")
    parser.add_argument("--max-files", type=int, default=500, help="Maximum files to ingest.")
    args = parser.parse_args()

    records = ingest_archive(Path(args.source_dir), Path(args.output), max_files=args.max_files)
    print(f"ingested={len(records)} output={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
