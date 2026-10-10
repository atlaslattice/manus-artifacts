"""Additive simulator launcher; original simulator.py and baseline remain untouched."""
import argparse
import json
from pathlib import Path
from models.current_state import run as current_state
from nutrition.model import run

def compose(config):
    return {"baseline":current_state(), "candidate_extensions":{"NUT01":run(config)}}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NUT01 non-crediting sensitivity extension")
    parser.add_argument("scenario", type=Path)
    args = parser.parse_args()
    print(json.dumps(compose(json.loads(args.scenario.read_text())), indent=2, allow_nan=False))

