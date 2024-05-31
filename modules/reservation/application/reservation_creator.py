from uuid import UUID
from modules.reservation.domain import ReservationCreatorService
from modules.reservation.domain import ReservationRepository
from modules.reservation.domain import ReservationExistException
from modules.passenger.domain import PassengerRepository
from modules.passenger.domain import PassengerDoesNotExistException
from modules.shared.domain import EventPublisher


class ReservationCreator:
    """
    Class to create Passengers
    """

    def __init__(
        self,
        reservation_repository: ReservationRepository,
        passenger_repository: PassengerRepository,
        event_publisher: EventPublisher,
    ):
        """
        Args:
            reservation_repository: repository for reservation database table operations
            passenger_repository: repository for passenger database table operations
            event_publisher: element responsible for sending messages that have occurred
        """
        self.__reservation_repository = reservation_repository
        self.__passenger_repository = passenger_repository
        self.__event_publisher = event_publisher

    def __call__(self, id: UUID, passenger_id: UUID, seat: int):
        if self.__reservation_repository.get(id=id):
            raise ReservationExistException(f"Reservation with id: {id} already exist")

        if not self.__passenger_repository.get(id=passenger_id):
            raise PassengerDoesNotExistException(f"Passenger with id: {passenger_id} does not exist")

        reservation_creator_service = ReservationCreatorService()
        reservation_entity = reservation_creator_service.create_entity(
            id=id,
            passenger_id=passenger_id,
            seat=seat,
        )

        reservation_event = reservation_creator_service.create_event_body(reservation_entity)

        self.__reservation_repository.create(reservation_entity)
        self.__event_publisher.publish(reservation_event)
