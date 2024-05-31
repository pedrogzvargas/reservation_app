from uuid import UUID
from dataclasses import dataclass


@dataclass
class Reservation:
    """
    Reservation entity
    """
    id: UUID
    passenger_id: UUID
    seat: int
