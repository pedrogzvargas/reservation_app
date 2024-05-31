from uuid import UUID
from unittest.mock import Mock
import pytest
from modules.passenger.infraestructure import PatchPassengerController
from modules.passenger.infraestructure import FakePassengerRepository
from modules.passenger.domain import PassengerDoesNotExistException
from modules.shared.infraestructure import FakeEventPublisher


def test_passenger_creator_controller():
    """
    test passenger creator without errors
    """

    fake_passenger_repository = FakePassengerRepository()
    fake_event_publisher = FakeEventPublisher()

    fake_passenger_repository.get = Mock(return_value=True)

    patch_passenger_controller = PatchPassengerController(
        passenger_repository=fake_passenger_repository,
        event_publisher=fake_event_publisher,
    )

    patch_passenger_controller(
        passenger_id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"),
        passenger_data={
            "name": "Pedro",
        }
    )


def test_passenger_does_not_exist_on_passenger_creator():
    """
    test passenger id does not exist
    """

    fake_passenger_repository = FakePassengerRepository()
    fake_event_publisher = FakeEventPublisher()

    fake_passenger_repository.get = Mock(return_value=False)

    patch_passenger_controller = PatchPassengerController(
        passenger_repository=fake_passenger_repository,
        event_publisher=fake_event_publisher,
    )

    with pytest.raises(PassengerDoesNotExistException):
        patch_passenger_controller(
            passenger_id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"),
            passenger_data={
                "name": "Pedro",
            }
        )
