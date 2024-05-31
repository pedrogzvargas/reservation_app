import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from modules.shared.domain import DBEngineCreator

load_dotenv()


class AlchemyEngineCreator(DBEngineCreator):
    """
    Alchemy database engine creator
    """

    def __init__(self, db_url: str = None):
        self.__db_url = db_url or os.getenv('DATABASE_URL')

    def create(self):
        """function to crate alchemy database engine"""
        engine = create_engine(self.__db_url, echo=True)
        return engine
