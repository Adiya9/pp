import psycopg2
from config import load_conf

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to the postgresql server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    config = load_conf()
    connect(config)
    conn = psycopg2.connect("dbname=suppliers1 user=postgres password=87087214958diya")