from abc import ABC
from abc import abstractmethod


class EventPublisher(ABC):
    """
    Port to event publisher creator
    """

    @abstractmethod
    def publish(self, message):
        """function to publish on message service"""
        pass
