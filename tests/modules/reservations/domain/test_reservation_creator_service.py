import json
from uuid import UUID
from modules.reservation.domain.reservation_creator_service import ReservationCreatorService
from modules.reservation.domain.entity import Reservation


def test_create_entity_on_reservation_creator_service():
    """test_create_entity_on_reservation_creator_service"""

    creator_service = ReservationCreatorService()
    entity = creator_service.create_entity(
        id=UUID("01ff116a-c3d4-4db3-9e0b-4d87063b1b24"),
        passenger_id=UUID("9eb265c5-d18f-4a3b-80bb-abc7a64fd7e6"),
        seat=34,

    )

    assert isinstance(entity, Reservation)


def test_event_body_on_reservation_creator_service():
    """test_event_body_on_reservation_creator_service"""

    creator_service = ReservationCreatorService()
    entity = creator_service.create_entity(
        id=UUID("01ff116a-c3d4-4db3-9e0b-4d87063b1b24"),
        passenger_id=UUID("9eb265c5-d18f-4a3b-80bb-abc7a64fd7e6"),
        seat=34,

    )

    event_body = creator_service.create_event_body(entity)
    event_body = json.loads(event_body)
    assert event_body.get("id") == str(entity.id)
    assert event_body.get("passenger_id") == str(entity.passenger_id)
    assert event_body.get("seat") == entity.seat
