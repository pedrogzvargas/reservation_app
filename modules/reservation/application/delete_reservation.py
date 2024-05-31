from uuid import UUID
from modules.reservation.domain import ReservationRepository
from modules.reservation.domain import ReservationDoesNotExistException


class DeleteReservation:
    """
    Class to delete Passenger
    """

    def __init__(self, reservation_repository: ReservationRepository):
        """
        Args:
            reservation_repository: repository for reservation database table operations
        """
        self.__reservation_repository = reservation_repository

    def __call__(self, id: UUID):
        if not self.__reservation_repository.get(id=id):
            raise ReservationDoesNotExistException(f"Reservation with id: {id} does not exist")
        self.__reservation_repository.delete(id)
