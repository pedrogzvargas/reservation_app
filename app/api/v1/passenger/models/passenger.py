from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class PassengerModel(BaseModel):
    id: UUID
    name: str
    last_name: str


class PatchPassengerModel(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
