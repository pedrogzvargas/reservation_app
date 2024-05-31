from modules.reservation.application.all_reservations import AllReservations
from modules.reservation.infraestructure import AlchemyReservationRepository


class AllReservationController:
    """
    Class controller to get all Reservations
    """

    def __init__(self):
        self.__alchemy_reservation_repository = AlchemyReservationRepository()

    def __call__(self):
        all_reservations = AllReservations(reservation_repository=self.__alchemy_reservation_repository)
        return all_reservations()
