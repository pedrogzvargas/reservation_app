from uuid import UUID
from modules.passenger.domain import PassengerRepository
from modules.passenger.domain import PassengerDoesNotExistException


class DeletePassenger:
    """
    Class to get delete Passenger
    """

    def __init__(self, passenger_repository: PassengerRepository):
        """
        Args:
            passenger_repository: repository for passenger database table operations
        """
        self.__passenger_repository = passenger_repository

    def __call__(self, id: UUID):
        if not self.__passenger_repository.get(id=id):
            raise PassengerDoesNotExistException(f"Passenger with id: {id} does not exist")
        self.__passenger_repository.delete(id)
