import logging
import os.path
from datetime import date

from selenium.webdriver.common.by import By
from selenium import webdriver

from lib.models.movie import Movie
from lib.utils.logger import get_file_location


def get_top_movies(driver: webdriver.Remote) -> list[Movie]:
    logging.info("Starting scrapping imdb for the best 250 movies")

    driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

    results = driver.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

    movies: list[Movie] = []

    logging.info("Ended scrapping imdb for the best 250 movies")

    for result in results:
        splitted_result = result.text.split('\n')

        logging.info(f"Converting scrapped movie: {splitted_result}")

        movie = Movie(
            position=int(splitted_result[0][:splitted_result[0].find('.')]),
            name=splitted_result[0][splitted_result[0].find(' '):],
            release_year=int(splitted_result[1]),
            length=splitted_result[2],
            rating=splitted_result[3] if len(splitted_result) == 7 else "Rating not found",
            score=float(splitted_result[4 if len(splitted_result) == 7 else 3]),
        )

        movies.append(movie)

    driver.get_screenshot_as_file(get_file_location('images', "Best Movies", "png"))

    return movies
