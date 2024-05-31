from uuid import UUID
from modules.passenger.domain import PatchPassengerService
from modules.passenger.domain import PassengerRepository
from modules.passenger.domain import PassengerDoesNotExistException
from modules.shared.domain import EventPublisher


class PatchPassenger:
    """
    Class to patch Passengers
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

    def __call__(self, passenger_id: UUID, passenger_data: dict):
        if not self.__passenger_repository.get(id=passenger_id):
            raise PassengerDoesNotExistException(f"Passenger with id: {id} does not exist")

        patch_passenger_service = PatchPassengerService()
        passenger_event = patch_passenger_service.create_event_body(
            passenger_id=passenger_id,
            passenger_data=passenger_data,
        )

        self.__passenger_repository.patch(passenger_id=passenger_id, passenger_data=passenger_data)
        self.__event_publisher.publish(passenger_event)
