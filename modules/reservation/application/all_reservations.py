from modules.reservation.domain import ReservationRepository


class AllReservations:
    """
    Class to get all Passengers
    """

    def __init__(self, reservation_repository: ReservationRepository):
        self.__reservation_repository = reservation_repository

    def __call__(self, *args, **kwargs):
        return self.__reservation_repository.all()
