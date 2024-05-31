from uuid import UUID
from unittest.mock import Mock
import pytest
from modules.passenger.infraestructure import DeletePassengerController
from modules.passenger.infraestructure import FakePassengerRepository
from modules.passenger.domain import PassengerDoesNotExistException


def test_delete_passenger_controller():
    """
    test delete passenger controller without errors
    """

    fake_passenger_repository = FakePassengerRepository()
    fake_passenger_repository.get = Mock(return_value=True)

    delete_passenger_controller = DeletePassengerController(
        passenger_repository=fake_passenger_repository,
    )

    delete_passenger_controller(id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"))


def test_id_does_not_exist_on_delete_passenger_creator_controller():
    """
    test passenger id does not exist
    """

    fake_passenger_repository = FakePassengerRepository()

    fake_passenger_repository.get = Mock(return_value=False)

    delete_passenger_controller = DeletePassengerController(
        passenger_repository=fake_passenger_repository,
    )

    with pytest.raises(PassengerDoesNotExistException):
        delete_passenger_controller(id=UUID("827cf2b2-64c3-4ccc-9800-edaf5d767a81"))
