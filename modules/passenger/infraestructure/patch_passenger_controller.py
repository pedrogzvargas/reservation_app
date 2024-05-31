from uuid import UUID
from modules.passenger.application import PatchPassenger
from modules.passenger.domain import PassengerRepository
from modules.shared.domain import EventPublisher
from modules.passenger.infraestructure import AlchemyPassengerRepository
from modules.shared.infraestructure import RabbitEventPublisher


class PatchPassengerController:
    """
    Class controller to patch Passenger
    """

    def __init__(
            self,
            passenger_repository: PassengerRepository = None,
            event_publisher: EventPublisher = None,
    ):
        """
        Args:
            passenger_repository: repository for passenger database table operations
            event_publisher: element responsible for sending messages that have occurred
        """

        self.__alchemy_passenger_repository = passenger_repository or AlchemyPassengerRepository()
        self.__rabbit_event_publisher = event_publisher or RabbitEventPublisher()

    def __call__(self, passenger_id: UUID, passenger_data: dict):
        patch_passenger = PatchPassenger(
            passenger_repository=self.__alchemy_passenger_repository,
            event_publisher=self.__rabbit_event_publisher,
        )
        patch_passenger(
            passenger_id=passenger_id,
            passenger_data=passenger_data,
        )
