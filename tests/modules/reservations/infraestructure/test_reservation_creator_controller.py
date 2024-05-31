from uuid import UUID
from unittest.mock import Mock
import pytest
from modules.reservation.infraestructure import ReservationCreatorController
from modules.reservation.infraestructure import FakeReservationRepository
from modules.reservation.domain import ReservationExistException
from modules.passenger.domain import PassengerDoesNotExistException
from modules.passenger.infraestructure import FakePassengerRepository
from modules.shared.infraestructure import FakeEventPublisher


def test_reservation_creator_controller():
    """
    test reservation creator without errors
    """

    fake_passenger_repository = FakePassengerRepository()
    fake_reservation_repository = FakeReservationRepository()
    fake_event_publisher = FakeEventPublisher()

    fake_passenger_repository.get = Mock(return_value=True)

    reservation_creator_controller = ReservationCreatorController(
        passenger_repository=fake_passenger_repository,
        reservation_repository=fake_reservation_repository,
        event_publisher=fake_event_publisher,
    )

    reservation_creator_controller(
        id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"),
        passenger_id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"),
        seat=1,
    )


def test_id_already_exist_on_passenger_creator():
    """
    test passenger id already exist
    """

    fake_passenger_repository = FakePassengerRepository()
    fake_reservation_repository = FakeReservationRepository()
    fake_event_publisher = FakeEventPublisher()

    fake_reservation_repository.get = Mock(return_value=True)

    reservation_creator_controller = ReservationCreatorController(
        passenger_repository=fake_passenger_repository,
        reservation_repository=fake_reservation_repository,
        event_publisher=fake_event_publisher,
    )

    with pytest.raises(ReservationExistException):
        reservation_creator_controller(
            id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"),
            passenger_id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"),
            seat=1,
        )


def test_passenger_does_not_exist_on_passenger_creator():
    """
    test passenger id does not exist
    """

    fake_passenger_repository = FakePassengerRepository()
    fake_reservation_repository = FakeReservationRepository()
    fake_event_publisher = FakeEventPublisher()

    reservation_creator_controller = ReservationCreatorController(
        passenger_repository=fake_passenger_repository,
        reservation_repository=fake_reservation_repository,
        event_publisher=fake_event_publisher,
    )

    with pytest.raises(PassengerDoesNotExistException):
        reservation_creator_controller(
            id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"),
            passenger_id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"),
            seat=1,
        )
