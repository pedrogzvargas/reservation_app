from uuid import UUID
from modules.reservation.application import ReservationCreator
from modules.reservation.infraestructure import AlchemyReservationRepository
from modules.reservation.domain import ReservationRepository
from modules.passenger.infraestructure import AlchemyPassengerRepository
from modules.passenger.domain import PassengerRepository
from modules.shared.domain import EventPublisher
from modules.shared.infraestructure import RabbitEventPublisher


class ReservationCreatorController:
    """
    Class controller to create Reservation
    """

    def __init__(
            self,
            reservation_repository: ReservationRepository = None,
            passenger_repository: PassengerRepository = None,
            event_publisher: EventPublisher = None,
    ):
        """
        Args:
            reservation_repository: repository for reservation database table operations
            passenger_repository: repository for passenger database table operations
            event_publisher: element responsible for sending messages that have occurred
        """

        self.__alchemy_reservation_repository = reservation_repository or AlchemyReservationRepository()
        self.__alchemy_passenger_repository = passenger_repository or AlchemyPassengerRepository()
        self.__rabbit_event_publisher = event_publisher or RabbitEventPublisher()

    def __call__(self, id: UUID, passenger_id: UUID, seat: int):
        reservation_creator = ReservationCreator(
            reservation_repository=self.__alchemy_reservation_repository,
            passenger_repository=self.__alchemy_passenger_repository,
            event_publisher=self.__rabbit_event_publisher,
        )
        reservation_creator(
            id=id,
            passenger_id=passenger_id,
            seat=seat,
        )
