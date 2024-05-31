from sqlalchemy.orm import Session
from dotenv import load_dotenv
from modules.shared.domain import DBSessionCreator
from .alchemy_engine_creator import AlchemyEngineCreator

load_dotenv()


class AlchemySessionCreator(DBSessionCreator):
    """
    Alchemy database session creator
    """

    def __init__(self, engine=None):
        self.__engine = engine or AlchemyEngineCreator()

    def create(self):
        """function to crate alchemy database session"""
        session = Session(bind=self.__engine.create())
        return session
