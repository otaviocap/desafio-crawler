from psycopg_pool import ConnectionPool

from lib.models.movie import Movie
from lib.utils.database import start_db
from lib.persistence import movies


test_movie = Movie(
    position=-1,
    name='Test Movie',
    release_year=2023,
    length='2h 10m',
    rating='PG',
    score=10,
)


class TestDatabase:

    def test_connection(self):
        pool = start_db()
        pool.close()

    def test_movies_insert(self):
        pool = start_db()
        movies.insert(pool, [test_movie])
        pool.close()

    def test_movies_get(self):
        pool = start_db()
        top_movies = movies.get_all(pool)

        assert len(top_movies) > 0
        pool.close()

    def test_movies_remove(self):
        pool = start_db()
        movies.remove(pool, test_movie)
        pool.close()
