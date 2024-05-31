import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    value = os.getenv("DATABASE_URL", "default")

    print(value)
