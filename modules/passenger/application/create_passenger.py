from uuid import UUID
from modules.passenger.domain import CreatePassengerService
from modules.passenger.domain import PassengerRepository
from modules.passenger.domain import PassengerExistException
from modules.shared.domain import EventPublisher


class CreatePassenger:
    """
    Class to create Passengers
    """

    def __init__(
        self,
        passenger_repository: PassengerRepository,
        event_publisher: EventPublisher,
    ):
        """
        Args:
            passenger_repository: repository for passenger database table operations
            event_publisher: element responsible for sending messages that have occurred
        """

        self.__passenger_repository = passenger_repository
        self.__event_publisher = event_publisher

    def __call__(self, id: UUID, name: str, last_name: str):
        if self.__passenger_repository.get(id=id):
            raise PassengerExistException(f"Passenger with id: {id} already exist")

        create_passenger_service = CreatePassengerService()
        passenger_entity = create_passenger_service.create_entity(
            id=id,
            name=name,
            last_name=last_name,
        )

        passenger_event = create_passenger_service.create_event_body(passenger_entity)

        self.__passenger_repository.create(passenger_entity)
        self.__event_publisher.publish(passenger_event)
