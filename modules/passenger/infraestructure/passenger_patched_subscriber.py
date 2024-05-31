from .patch_passenger_controller import PatchPassengerController
from modules.shared.infraestructure import FakeEventPublisher


class PassengerPatchedSubscriber:
    """
    Class to handle when a passenger was patched
    """

    def __init__(self, message):
        """
        Args:
            message: event message from message service
        """
        self.__message = message

    def __call__(self, body):
        try:
            fake_event_publisher = FakeEventPublisher()
            patch_passenger_controller = PatchPassengerController(
                event_publisher=fake_event_publisher,
            )
            patch_passenger_controller(
                passenger_id=body.get("id"),
                passenger_data=body.get("data"),
            )
        except Exception as e:
            print(f"PassengerPatchedSubscriber err: {e.__str__()}")
            self.__message.reject()
        else:
            self.__message.ack()
