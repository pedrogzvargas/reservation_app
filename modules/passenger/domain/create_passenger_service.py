import uuid
from uuid import UUID
import json
from dataclasses import asdict
from .entity import Passenger


class UUIDEncoder(json.JSONEncoder):
    """
    Class to encode UUID variable
    """
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)

        return json.JSONEncoder.default(self, obj)


class CreatePassengerService:
    """
    Class to create entity and event body
    """

    @staticmethod
    def create_entity(id: UUID, name: str, last_name: str):
        """
        function responsible to create a passanger entity
        """
        passenger = Passenger(
            id=id,
            name=name,
            last_name=last_name,
        )
        return passenger

    @staticmethod
    def create_event_body(passenger: Passenger):
        """
        function responsible to create a passanger event body
        """
        dict_body = dict(event_name="reservation_app.passenger_created")
        dict_body.update(asdict(passenger))
        json_body = json.dumps(dict_body, cls=UUIDEncoder)
        return json_body
