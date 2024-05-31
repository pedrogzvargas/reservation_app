from uuid import UUID
from dataclasses import dataclass


@dataclass
class Passenger:
    """
    Passenger entity
    """
    id: UUID
    name: str
    last_name: str
