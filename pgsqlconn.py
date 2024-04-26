import os
import psycopg
import pandas as pd

def fetch_data(table):
    
    #connection = {"sslmode": "verify-full", "target_session_attrs": "read-write"}
    connection = {"sslmode": "require", "target_session_attrs": "read-write"}
    
    postgres_credentials = {
        "host": os.getenv("DB_DESTINATION_HOST"),
        "port": os.getenv("DB_DESTINATION_PORT"),
        "dbname": os.getenv("DB_DESTINATION_NAME"),
        "user": os.getenv("DB_DESTINATION_USER"),
        "password": os.getenv("DB_DESTINATION_PASSWORD"),
        }
    
    connection.update(postgres_credentials)
    
    with psycopg.connect(**connection) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {table}")
            data = cur.fetchall()
            columns = [col[0] for col in cur.description]
    
    return pd.DataFrame(data, columns=columns)