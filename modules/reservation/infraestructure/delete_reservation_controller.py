from uuid import UUID
from modules.reservation.application.delete_reservation import DeleteReservation
from modules.reservation.domain import ReservationRepository
from modules.reservation.infraestructure import AlchemyReservationRepository


class DeleteReservationController:
    """
    Class to delete Reservation
    """

    def __init__(self, reservation_repository: ReservationRepository = None):
        """
        Args:
            reservation_repository: repository for reservation database table operations
        """

        self.__alchemy_reservation_repository = reservation_repository or AlchemyReservationRepository()

    def __call__(self, id: UUID):
        reservation_creator = DeleteReservation(reservation_repository=self.__alchemy_reservation_repository)
        return reservation_creator(id=id)
