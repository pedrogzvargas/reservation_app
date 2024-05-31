from abc import ABC
from abc import abstractmethod


class DBEngineCreator(ABC):
    """
    Port to database engine creator
    """

    @abstractmethod
    def create(self):
        """function to crate database engine"""
        pass
