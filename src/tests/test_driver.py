import os.path

from selenium import webdriver

from lib.scrapper.driver import get_driver
from lib.sources.imdb import get_top_movies
from lib.utils.logger import get_file_location


class TestDriver:

    def test_connectivity(self):
        driver = get_driver()
        driver.quit()

    def test_imdb(self):
        driver = get_driver()
        movies = get_top_movies(driver, "Best Movies Test")

        assert len(movies) == 250
        driver.quit()

    def test_screenshot_log(self):
        location = get_file_location('images', "Best Movies Test", "png")

        assert os.path.exists(location)
        os.remove(location)



