from uuid import UUID
import json
from dataclasses import asdict
import uuid
from .entity import Reservation


class UUIDEncoder(json.JSONEncoder):
    """
    Class to encode UUID variable
    """
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)

        return json.JSONEncoder.default(self, obj)


class ReservationCreatorService:
    """
    Class to create entity and event body
    """

    @staticmethod
    def create_entity(id: UUID, passenger_id: UUID, seat: int):
        """
        function responsible to create a reservation entity
        """
        reservation = Reservation(
            id=id,
            passenger_id=passenger_id,
            seat=seat,
        )
        return reservation

    @staticmethod
    def create_event_body(reservation: Reservation):
        """
        function responsible to create a reservation event body
        """
        dict_body = dict(event_name="reservation_app.reservation_created")
        dict_body.update(asdict(reservation))
        json_body = json.dumps(dict_body, cls=UUIDEncoder)
        return json_body
