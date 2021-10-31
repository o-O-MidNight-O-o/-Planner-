


import psycopg2
import os

def conn():

    host = os.environ.get("POSTGRES_HOST")
    port = os.environ.get('POSTGRES_PORT')
    username = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASS')
    database = os.environ.get('POSTGRES_DB')

    con = psycopg2.connect(user = username,
                                password = password,
                                host = host,
                                port = port,
                                database = database)
    return con