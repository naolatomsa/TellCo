from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Function to create the engine
def get_engine(echo=False):

    return create_engine(DATABASE_URL, echo=echo)

# Function to test the connection
def test_connection():

    engine = get_engine()
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            for row in result:
                print(f"Database version: {row[0]}")
    except Exception as e:
        print(f"Error: {e}")
