from modules.shared.domain import EventPublisher


class FakeEventPublisher(EventPublisher):
    """
    Fake event publisher creator
    """

    def __init__(self):
        self.__producer = None

    def publish(self, message: dict):
        """function to publish on RabbitMQ"""
        pass
