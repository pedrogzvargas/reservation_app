from pydantic import BaseModel
from uuid import UUID


class ReservationModel(BaseModel):
    id: UUID
    passenger_id: UUID
    seat: int
