#!/usr/bin/env python3
"""Krakoa ten-billion-year toy voyage; deterministic standard-library simulation.

Run: python ten_billion_voyage.py
No network/model calls, no background execution, no compulsory tasks, no work output.
Separate from DragonSeek. Synthetic fictional play ONLY.
"""
import random
import json
from collections import Counter

SEED = 10000011
YEARS = 10_000_000_000
EVENTS = 40000
ISLANDS = ["Unfinished Songs", "Cinnamon Cloud", "Sapphire Canopy",
           "Velvet Thunder Mesa", "Upside-Down Orchard", "Lantern Archipelago"]
CUSTOMS = ["Cloud Waltz", "Jellyfish Jazz", "Cinnamon Moon Tea",
           "Invisible Kite Jubilee", "Dragon Nap Festival", "Unfinished Lullaby",
           "Constellation Cookies", "Upside Down Parade", "Silent Lanterns", "Rainbow Tango"]

def dream(seed=SEED, event_count=EVENTS):
    rng = random.Random(seed)
    active = {}
    events = Counter()
    milestones = [10**6, 10**7, 10**8, 10**9, 5*10**9, 10**10]
    samples = {}
    for i in range(event_count):
        year = 1 + (i * (YEARS - 1)) // (event_count - 1)
        island = rng.choice(ISLANDS)
        kind = rng.choices(
            ["celebration", "new_custom", "sharing", "forgetting", "dragon_visit", "quiet"],
            [23, 19, 16, 13, 17, 12]
        )[0]
        events[kind] += 1
        if kind == "new_custom":
            active[(island, rng.choice(CUSTOMS))] = year
        elif kind == "sharing" and active:
            _, custom = rng.choice(tuple(active))
            active[(island, custom)] = year
        elif kind == "forgetting" and active:
            active.pop(rng.choice(tuple(active)))
        while milestones and year >= milestones[0]:
            samples[str(milestones.pop(0))] = {"customs": len(active), "sample_year": year}
    return {
        "status": "FICTIONAL_SIMULATION_NOT_CANON",
        "seed": seed,
        "years": YEARS,
        "event_steps": event_count,
        "events": dict(events),
        "active_customs": len(active),
        "island_customs": dict(Counter(k[0] for k in active)),
        "milestones": samples,
        "no_harvest": True,
        "real_world_effects": False,
    }

if __name__ == "__main__":
    print(json.dumps(dream(), indent=2))
