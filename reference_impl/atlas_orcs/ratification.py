from datetime import datetime, timezone

from .state import Artifact, TrustState



def ratification_expired(artifact: Artifact, now_iso: str) -> bool:
    if not artifact.ratification_expires_at:
        return False
    now = datetime.fromisoformat(now_iso.replace("Z", "+00:00")).astimezone(timezone.utc)
    exp = datetime.fromisoformat(artifact.ratification_expires_at.replace("Z", "+00:00")).astimezone(timezone.utc)
    return now > exp


def enforce_ratification_expiry(artifact: Artifact, now_iso: str) -> bool:
    if artifact.trust_state in {TrustState.RATIFIED, TrustState.ACTIVE} and ratification_expired(artifact, now_iso):
        artifact.trust_state = TrustState.UNDER_REVIEW
        return True
    return False
