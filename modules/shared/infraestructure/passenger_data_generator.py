import csv
from faker import Faker
from uuid import uuid4


class PassengerDataGenerator:
    @staticmethod
    def genetate(file_name: str = "csv/passenger_file.csv") -> None:
        faker = Faker()
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["id", "name", "last_name", "created_at", "updated_at"]

            writer.writerow(field)

            for user in range(0, 7000):
                writer.writerow(
                    [
                        uuid4(),
                        faker.first_name(),
                        faker.last_name(),
                        faker.date_time(),
                        faker.date_time(),
                    ]
                )


if __name__ == "__main__":
    PassengerDataGenerator.genetate()
