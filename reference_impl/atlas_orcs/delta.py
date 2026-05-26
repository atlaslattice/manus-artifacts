from dataclasses import dataclass

@dataclass
class GovernanceDelta:
    governance_event: bool = False
    ratification_event: bool = False
    contradiction_record: dict | None = None
