from uuid import UUID
from modules.passenger.application import DeletePassenger
from modules.passenger.domain import PassengerRepository
from modules.passenger.infraestructure import AlchemyPassengerRepository


class DeletePassengerController:
    """
    Class to delete Passenger
    """

    def __init__(self, passenger_repository: PassengerRepository = None):
        """
        Args:
            passenger_repository: repository for passenger database table operations
        """
        self.__alchemy_passenger_repository = passenger_repository or AlchemyPassengerRepository()

    def __call__(self, id: UUID):
        delete_passenger = DeletePassenger(passenger_repository=self.__alchemy_passenger_repository)
        return delete_passenger(id=id)
