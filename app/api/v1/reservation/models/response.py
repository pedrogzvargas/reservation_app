from pydantic import BaseModel
from .reservation import ReservationModel


class ListResponseBody(BaseModel):
    message: str
    data: list[ReservationModel] = None


class CreateResponseBody(BaseModel):
    message: str


class DeleteResponseBody(BaseModel):
    message: str
