from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class SpectralPoint:
    frequency: float
    amplitude: float


def riemann_s_score(point: SpectralPoint, sigma: float = 0.5) -> float:
    if point.frequency <= 0:
        raise ValueError("frequency must be > 0")
    harmonic = math.log(point.frequency)
    return float((point.amplitude ** sigma) * math.cos(harmonic))


def rank_spectrum(points: list[SpectralPoint], sigma: float = 0.5) -> list[dict]:
    ranked = [{"frequency": p.frequency, "amplitude": p.amplitude, "score": riemann_s_score(p, sigma)} for p in points]
    return sorted(ranked, key=lambda item: item["score"], reverse=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Candidate Riemann S operator over frequency/amplitude points.")
    parser.add_argument("pairs", nargs="+", help="Pairs in the form frequency:amplitude")
    parser.add_argument("--sigma", type=float, default=0.5)
    args = parser.parse_args()

    points = []
    for pair in args.pairs:
        frequency_text, amplitude_text = pair.split(":", maxsplit=1)
        points.append(SpectralPoint(float(frequency_text), float(amplitude_text)))
    print(json.dumps(rank_spectrum(points, sigma=args.sigma), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
