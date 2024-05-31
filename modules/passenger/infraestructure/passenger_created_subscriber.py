from .create_passenger_controller import CreatePassengerController


class PassengerCreatedSubscriber:
    """
    Class to handle when a passenger was created
    """

    def __init__(self, message):
        """
        Args:
            message: event message from message service
        """
        self.__message = message

    def __call__(self, body):
        try:
            create_passenger_controller = CreatePassengerController()
            create_passenger_controller(
                id=body.get("id"),
                name=body.get("name"),
                last_name=body.get("last_name"),
            )
        except Exception as e:
            print(f"CreatePassengerController err: {e.__str__()}")
            self.__message.reject()
        else:
            self.__message.ack()
