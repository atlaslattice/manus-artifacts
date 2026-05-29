from __future__ import annotations

from reference_impl.atlas_orcs.ratification import enforce_ratification_freshness
from reference_impl.atlas_orcs.state import normalize_artifact
from reference_impl.atlas_orcs.transitions import validate_transition


def check_compatibility(artifact: dict, proposed_delta: dict) -> list[str]:
    before = normalize_artifact(artifact)
    after = normalize_artifact({**before, **proposed_delta})
    after = enforce_ratification_freshness(after)
    return validate_transition(before, after, proposed_delta)
