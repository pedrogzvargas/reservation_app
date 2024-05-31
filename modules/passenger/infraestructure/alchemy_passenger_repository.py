from uuid import UUID
from modules.passenger.domain import PassengerRepository
from modules.passenger.domain import Passenger as PassengerEntity
from modules.shared.infraestructure import AlchemySessionCreator
from models.passenger import Passenger

from sqlalchemy import update


class AlchemyPassengerRepository(PassengerRepository):
    """
    Alchemy repository for passenger database table operations
    """

    def __init__(self):
        alchemy_session_creator = AlchemySessionCreator()
        self.__session = alchemy_session_creator.create()

    def all(self):
        """list all passengers"""
        with self.__session as session:
            result = session.query(Passenger).all()
        return result

    def search(self):
        """search passengers"""
        pass

    def get(self, id: UUID):
        """get passenger"""
        with self.__session as session:
            passenger = session.get(Passenger, id)
        return passenger

    def create(self, passenger: PassengerEntity):
        """create passenger"""
        passenger = Passenger(
            id=passenger.id,
            name=passenger.name,
            last_name=passenger.last_name,
        )

        with self.__session as session:
            session.add(passenger)
            session.commit()

    def patch(self, passenger_id: UUID, passenger_data: dict):
        """patch passengers"""
        with self.__session as session:
            stmt = (update(Passenger).where(Passenger.id == passenger_id).values(**passenger_data))
            session.execute(stmt)
            session.commit()

    def delete(self, id: UUID):
        """delete passengers"""
        with self.__session as session:
            passenger = self.__session.get(Passenger, id)
            session.delete(passenger)
            session.commit()
