
from sqlalchemy import create_engine, text
import pandas as pd

# Database URL
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/xdr_data"


def connection_for_data(table_name):
    engine = create_engine(DATABASE_URL)
    query_result = pd.read_sql(f'SELECT * FROM {table_name}', con=engine)
    return query_result