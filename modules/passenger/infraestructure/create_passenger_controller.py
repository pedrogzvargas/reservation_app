from uuid import UUID
from modules.passenger.application import CreatePassenger
from modules.passenger.domain import PassengerRepository
from modules.shared.domain import EventPublisher
from modules.passenger.infraestructure import AlchemyPassengerRepository
from modules.shared.infraestructure import RabbitEventPublisher


class CreatePassengerController:
    """
    Class controller to create Passengers
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

    def __call__(self, id: UUID, name: str, last_name: str):
        create_passenger = CreatePassenger(
            passenger_repository=self.__alchemy_passenger_repository,
            event_publisher=self.__rabbit_event_publisher,
        )
        create_passenger(
            id=id,
            name=name,
            last_name=last_name,
        )
