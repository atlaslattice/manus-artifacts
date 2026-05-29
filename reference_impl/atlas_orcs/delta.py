from dataclasses import dataclass
from typing import Optional


@dataclass
class TransitionDelta:
    to_state: str
    ratification_event_id: Optional[str] = None
    governance_event_id: Optional[str] = None
    contradiction_record: Optional[dict] = None
    replaces_source_with_summary: bool = False
