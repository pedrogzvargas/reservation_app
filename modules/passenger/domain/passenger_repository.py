from uuid import UUID
from abc import ABC
from abc import abstractmethod
from modules.passenger.domain.entity import Passenger


class PassengerRepository(ABC):
    """
    Repository for passenger database table operations
    """

    @abstractmethod
    def all(self):
        """list all passengers"""
        pass

    @abstractmethod
    def search(self):
        """search passengers"""
        pass

    @abstractmethod
    def get(self, id: UUID):
        """get passenger"""
        pass

    @abstractmethod
    def create(self, passenger: Passenger):
        """create passenger"""
        pass

    def patch(self, passenger_id: UUID, passenger_data: dict):
        """patch passenger"""

    @abstractmethod
    def delete(self, id: UUID):
        """delete passenger"""
        pass
