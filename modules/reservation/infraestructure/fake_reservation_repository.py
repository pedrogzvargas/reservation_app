from uuid import UUID
from modules.reservation.domain import ReservationRepository
from modules.reservation.domain import Reservation as ReservationEntity


class FakeReservationRepository(ReservationRepository):
    """
    Fake repository for reservation database table operations
    """

    def __init__(self):
        pass

    def all(self):
        """list all reservations"""
        pass

    def search(self):
        """search reservations"""
        pass

    def get(self, id: UUID):
        """get reservation"""
        pass

    def create(self, passenger: ReservationEntity):
        """create reservation"""
        pass

    def delete(self, id: UUID):
        """delete reservation"""
        pass
