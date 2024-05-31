import json
from uuid import UUID
from modules.passenger.domain import PatchPassengerService


def test_event_body_on_passenger_patch_service():
    """test event body"""

    passenger_id = "cc821472-19e6-4eef-b73f-7594b20e59f5"
    passenger_name = "Pedro"
    passenger_last_name = "Gonzalez"

    patch_passenger_service = PatchPassengerService()
    event_body = patch_passenger_service.create_event_body(
        passenger_id=UUID(passenger_id),
        passenger_data={
            "name": passenger_name,
            "last_name": passenger_last_name,
        }
    )

    event_body = json.loads(event_body)
    assert event_body.get("id") == passenger_id
    assert event_body.get("data", {}).get("name") == passenger_name
    assert event_body.get("data", {}).get("last_name") == passenger_last_name
