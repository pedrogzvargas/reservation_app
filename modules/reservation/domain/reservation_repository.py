from uuid import UUID
from abc import ABC
from abc import abstractmethod
from modules.reservation.domain.entity import Reservation


class ReservationRepository(ABC):
    """
    Repository for reservation database table operations
    """

    @abstractmethod
    def all(self):
        """list all reservations"""
        pass

    @abstractmethod
    def search(self):
        """search reservations"""
        pass

    @abstractmethod
    def get(self, id: UUID):
        """get reservation"""
        pass

    @abstractmethod
    def create(self, reservation: Reservation):
        """create reservation"""
        pass

    @abstractmethod
    def delete(self, id: UUID):
        """delete reservation"""
        pass
