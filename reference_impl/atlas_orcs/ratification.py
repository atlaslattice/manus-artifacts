from datetime import datetime


def has_valid_ratification(expires_at: datetime | None, now: datetime) -> bool:
    return bool(expires_at and now < expires_at)
