import logging

from psycopg.connection import Connection
from psycopg.rows import class_row

from psycopg_pool import ConnectionPool

from lib.models.movie import Movie


def insert(pool: ConnectionPool, movies: list[Movie]):
    logging.info("Inserting movies at the database")

    conn: Connection
    with pool.connection() as conn:

        with conn.cursor() as cur:
            # If needs it can be translated to a Copy statement for better performance!

            cur.executemany(
                "INSERT INTO movies (name, rating, release_year, length, score, position) " +
                "VALUES (%(name)s, %(rating)s, %(release_year)s, %(length)s, %(score)s, %(position)s)",
                [i.__dict__ for i in movies]
            )


def get_all(pool: ConnectionPool) -> list[Movie]:
    logging.info("Getting all movies from database")

    movies: list[Movie] = []

    conn: Connection
    with pool.connection() as conn:
        with conn.cursor(row_factory=class_row(Movie)) as cur:
            cur.execute("SELECT name, length, position, rating, release_year, score FROM movies")

            record: Movie
            for record in cur:
                movies.append(record)

    return movies
