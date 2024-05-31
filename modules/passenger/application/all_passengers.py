from modules.passenger.domain import PassengerRepository


class AllPassengers:
    """
    Class to get all Passengers
    """

    def __init__(self, passenger_repository: PassengerRepository):
        """
        Args:
            passenger_repository: repository for passenger database table operations
        """
        self.__passenger_repository = passenger_repository

    def __call__(self):
        return self.__passenger_repository.all()
