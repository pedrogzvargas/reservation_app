import uuid
from uuid import UUID
import json


class UUIDEncoder(json.JSONEncoder):
    """
    Class to encode UUID variable
    """
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)

        return json.JSONEncoder.default(self, obj)


class PatchPassengerService:
    """
    Class to create entity and event body
    """

    @staticmethod
    def create_event_body(passenger_id: UUID, passenger_data: dict):
        """
        function responsible to create a passanger event body
        """
        dict_body = dict(
            event_name="reservation_app.passenger_patched",
            id=passenger_id,
        )
        dict_body.update({"data": passenger_data})
        json_body = json.dumps(dict_body, cls=UUIDEncoder)
        return json_body
