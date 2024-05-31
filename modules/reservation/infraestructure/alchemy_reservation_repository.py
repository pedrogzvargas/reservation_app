from uuid import UUID
from modules.reservation.domain import ReservationRepository
from modules.reservation.domain import Reservation as ReservationEntity
from modules.shared.infraestructure import AlchemySessionCreator
from models.reservation import Reservation


class AlchemyReservationRepository(ReservationRepository):
    """
    Alchemy repository for reservation database table operations
    """

    def __init__(self):
        alchemy_session_creator = AlchemySessionCreator()
        self.__session = alchemy_session_creator.create()

    def all(self):
        """list all reservations"""
        with self.__session as session:
            result = session.query(Reservation).all()
        return result

    def search(self):
        """search reservations"""
        pass

    def get(self, id: UUID):
        """get reservation"""
        with self.__session as session:
            reservation = session.get(Reservation, id)
        return reservation

    def create(self, reservation: ReservationEntity):
        """create reservation"""
        reservation = Reservation(
            id=reservation.id,
            passenger_id=reservation.passenger_id,
            seat=reservation.seat,
        )

        with self.__session as session:
            session.add(reservation)
            session.commit()

    def delete(self, id: UUID):
        """delete reservation"""
        with self.__session as session:
            reservation = self.__session.get(Reservation, id)
            session.delete(reservation)
            session.commit()
