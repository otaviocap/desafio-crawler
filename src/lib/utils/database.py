import logging
from typing import Optional

from psycopg_pool import ConnectionPool

from lib.utils.env import is_running_on_container


def start_db() -> ConnectionPool:
    pool = ConnectionPool(
        conninfo=f"postgresql://root:root@{'db:5432' if is_running_on_container() else 'localhost:8001'}/postgres"
    )

    pool.open()

    logging.info("Connected to database!")

    return pool

