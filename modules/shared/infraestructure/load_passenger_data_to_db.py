import pandas as pd
from modules.shared.infraestructure import AlchemyEngineCreator


engine_creator = AlchemyEngineCreator()
engine = engine_creator.create()


class LoadPassengerDataToDb:
    @staticmethod
    def load(file_name: str = "passenger_file.csv"):
        data = pd.read_csv(file_name)
        data.to_sql("passengers", engine, index=False, if_exists="append", schema="public")


if __name__ == "__main__":
    LoadPassengerDataToDb.load()
