from uuid import UUID
from unittest.mock import Mock
import pytest
from modules.reservation.infraestructure import DeleteReservationController
from modules.reservation.infraestructure import FakeReservationRepository
from modules.reservation.domain import ReservationDoesNotExistException


def test_delete_reservation_controller():
    """
    test delete reservation controller without errors
    """

    fake_reservation_repository = FakeReservationRepository()
    fake_reservation_repository.get = Mock(return_value=True)

    delete_reservation_controller = DeleteReservationController(
        reservation_repository=fake_reservation_repository,
    )

    delete_reservation_controller(id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"))


def test_id_does_not_exist_on_delete_reservation_creator_controller():
    """
    test reservation id does not exist
    """

    fake_reservation_repository = FakeReservationRepository()

    fake_reservation_repository.get = Mock(return_value=False)

    delete_reservation_controller = DeleteReservationController(
        reservation_repository=fake_reservation_repository,
    )

    with pytest.raises(ReservationDoesNotExistException):
        delete_reservation_controller(id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"))
