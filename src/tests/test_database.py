from lib.utils.database import start_db


def test_database_connection():
    pool = start_db()

    pool.close()
