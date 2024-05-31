from uuid import UUID
from unittest.mock import Mock
import pytest
from modules.passenger.infraestructure import CreatePassengerController
from modules.passenger.infraestructure import FakePassengerRepository
from modules.passenger.domain import PassengerExistException
from modules.shared.infraestructure import FakeEventPublisher


def test_passenger_creator_controller():
    """
    test passenger creator without errors
    """

    fake_passenger_repository = FakePassengerRepository()
    fake_event_publisher = FakeEventPublisher()

    create_passenger_controller = CreatePassengerController(
        passenger_repository=fake_passenger_repository,
        event_publisher=fake_event_publisher,
    )

    create_passenger_controller(
        id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"),
        name="Pedro",
        last_name="Gonzalez",
    )


def test_id_already_exist_on_passenger_creator():
    """
    test passenger id already exist
    """

    fake_passenger_repository = FakePassengerRepository()
    fake_event_publisher = FakeEventPublisher()

    fake_passenger_repository.get = Mock(return_value=True)

    create_passenger_controller = CreatePassengerController(
        passenger_repository=fake_passenger_repository,
        event_publisher=fake_event_publisher,
    )

    with pytest.raises(PassengerExistException):
        create_passenger_controller(
            id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"),
            name="Pedro",
            last_name="Gonzalez",
        )
