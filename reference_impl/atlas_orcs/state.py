from enum import Enum


class TrustState(str, Enum):
    RAW = "raw"
    PARSED = "parsed"
    CANDIDATE = "candidate"
    REVIEWED = "reviewed"
    RATIFIED = "ratified"
    ACTIVE = "active"
    UNDER_REVIEW = "under_review"
    SUPERSEDED = "superseded"
    REVOKED = "revoked"
    QUARANTINED = "quarantined"
    REJECTED = "rejected"
