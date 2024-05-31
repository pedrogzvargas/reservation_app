import json
from uuid import UUID
from modules.passenger.domain.create_passenger_service import CreatePassengerService
from modules.passenger.domain.entity import Passenger


def test_create_entity_on_passenger_creator_service():
    """test_create_entity_on_passenger_creator_service"""

    create_passenger_service = CreatePassengerService()
    entity = create_passenger_service.create_entity(
        id=UUID("01ff116a-c3d4-4db3-9e0b-4d87063b1b24"),
        name="Pedro",
        last_name="Gonzalez",
    )

    assert isinstance(entity, Passenger)


def test_event_body_on_passenger_creator_service():
    """test_event_body_on_passenger_creator_service"""

    create_passenger_service = CreatePassengerService()
    entity = create_passenger_service.create_entity(
        id=UUID("01ff116a-c3d4-4db3-9e0b-4d87063b1b24"),
        name="Pedro",
        last_name="Gonzalez",
    )

    event_body = create_passenger_service.create_event_body(entity)
    event_body = json.loads(event_body)
    assert event_body.get("id") == str(entity.id)
    assert event_body.get("name") == entity.name
    assert event_body.get("last_name") == entity.last_name
