from pydantic import BaseModel
from .passenger import PassengerModel


class ListResponseBody(BaseModel):
    message: str
    data: list[PassengerModel] = None


class CreateResponseBody(BaseModel):
    message: str


class DeleteResponseBody(BaseModel):
    message: str
