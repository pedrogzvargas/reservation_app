from modules.passenger.application import AllPassengers
from modules.passenger.infraestructure import AlchemyPassengerRepository


class AllPassengerController:
    """
    Class controller to get all Passengers
    """

    def __init__(self):
        self.__alchemy_passenger_repository = AlchemyPassengerRepository()

    def __call__(self):
        all_passengers = AllPassengers(passenger_repository=self.__alchemy_passenger_repository)
        return all_passengers()
