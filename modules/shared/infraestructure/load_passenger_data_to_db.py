import pandas as pd

import os
import pathlib
import sys

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = str(pathlib.Path(CURRENT_PATH).parent.parent.parent)
sys.path.append(os.path.join(PROJECT_PATH))


from modules.shared.infraestructure.alchemy_engine_creator import AlchemyEngineCreator

engine_creator = AlchemyEngineCreator()
engine = engine_creator.create()


class LoadPassengerDataToDb:
    @staticmethod
    def load(file_name: str = "csv/passenger_file.csv"):
        data = pd.read_csv(file_name)
        data.to_sql("passengers", engine, index=False, if_exists="append", schema="public")


if __name__ == "__main__":
    LoadPassengerDataToDb.load()
