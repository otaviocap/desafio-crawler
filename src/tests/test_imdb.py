from lib.scrapper.driver import get_driver
from lib.sources.imdb import get_top_movies


def test_imdb():
    driver = get_driver()

    movies = get_top_movies(driver)

    driver.close()

    assert len(movies) == 250
