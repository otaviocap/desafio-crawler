import logging

from lib.models.movie import Movie
from lib.persistence import movies
from lib.scrapper.driver import get_driver
from lib.sources import imdb
from lib.utils import start_db, start_logger
from lib.utils.pandas import list_to_df, df_to_csv_file, df_to_json_file


def main():
    start_logger()
    logging.info("Starting app!")
    pool = start_db()
    driver = get_driver()
    try:
        top_movies = imdb.get_top_movies(driver)
        movies.insert(pool, top_movies)

        top_movies = list_to_df(top_movies)

        df_to_json_file(top_movies, 'Movies')
        df_to_csv_file(top_movies, 'Movies')
    finally:
        driver.quit()
        pool.close()


if __name__ == "__main__":
    main()
