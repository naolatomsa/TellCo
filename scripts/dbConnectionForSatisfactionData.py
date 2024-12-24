
from sqlalchemy import create_engine, text
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def connection_for_data(table_name):
    engine = create_engine(DATABASE_URL)
    query_result = pd.read_sql(f'SELECT * FROM {table_name}', con=engine)
    return query_result