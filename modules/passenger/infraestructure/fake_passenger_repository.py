from uuid import UUID
from modules.passenger.domain import PassengerRepository
from modules.passenger.domain import Passenger as PassengerEntity


class FakePassengerRepository(PassengerRepository):
    """
    Fake repository for passenger database table operations
    """

    def __init__(self):
        pass

    def all(self):
        """list all passengers"""
        pass

    def search(self):
        """search passengers"""
        pass

    def get(self, id: UUID):
        """get passenger"""
        pass

    def create(self, passenger: PassengerEntity):
        """create passengers"""
        pass

    def delete(self, id: UUID):
        """delete passengers"""
        pass
