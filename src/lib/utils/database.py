import logging
import os

from psycopg_pool import ConnectionPool
from psycopg.connection import Connection

from lib.utils.env import is_running_on_container


def start_db() -> ConnectionPool:
    pool = ConnectionPool(
        conninfo=f"postgresql://root:root@{'db:5432' if is_running_on_container() else 'localhost:8001'}/postgres"
    )

    pool.open()

    logging.info("Connected to database!")

    return pool


def make_db(pool: ConnectionPool, force: bool = False):
    folder = os.path.join(os.getcwd(), 'sql')

    logging.info(f"Reading sql files from {folder}")
    files = os.listdir(folder)

    conn: Connection
    with pool.connection() as conn:
        with conn.cursor() as cur:

            if not force:
                cur.execute("SELECT EXISTS ( SELECT 1 FROM pg_tables WHERE tablename = 'movies' ) AS table_existence")

                if cur.fetchone()[0]:
                    logging.info("Table already exists. No need to recreate it")

                    return

            logging.info("Preparing database")
            for file in files:
                with open(os.path.join(folder, file), 'r') as sql:
                    cur.execute(sql.read())

    logging.info("Prepared database for app execution")

