import argparse
import logging

from lib.persistence import movies
from lib.scrapper.driver import get_driver
from lib.sources import imdb
from lib.utils import start_db, start_logger, make_db
from lib.utils.pandas import list_to_df, df_to_csv_file, df_to_json_file


def main():
    start_logger()

    parser = argparse.ArgumentParser(description="An web scrapper for imdb")
    parser.add_argument("--local", dest="local", help="Get the data from the database, not web", action="store_true")
    parser.add_argument("--csv", dest="csv", help="Export data to csv", action="store_true")
    parser.add_argument("--json", dest="json", help="Export data to json", action="store_true")
    parser.add_argument(
        "--prepare-database",
        dest="database",
        help="Only run all the sqls on the sql folder to prepare the database",
        action="store_true")
    args = parser.parse_args()

    logging.info("Starting app!")
    pool = start_db()
    driver = get_driver()
    try:
        if args.database:
            make_db(pool)
            return

        top_movies: list[movies]
        if args.local:
            top_movies = movies.get_all(pool)
        else:
            top_movies = imdb.get_top_movies(driver)
            movies.insert(pool, top_movies)

        top_movies_df = list_to_df(top_movies)

        if args.json:
            df_to_json_file(top_movies_df, 'Movies')

        if args.csv:
            df_to_csv_file(top_movies_df, 'Movies')

    except Exception as e:
        logging.exception(f'Something went wrong. Error: {e}')

    finally:
        driver.quit()
        pool.close()
        logging.info("Closed driver and database connection")


if __name__ == "__main__":
    main()
