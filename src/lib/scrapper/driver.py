import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from lib.utils.env import  is_running_on_container


def get_driver() -> webdriver.Remote:
    options = ChromeOptions()

    uri = f"http://{'hub' if is_running_on_container() else 'localhost'}:4444/wd/hub"

    logging.info(f"Trying to connect to Selenium Hub at {uri}")

    driver = webdriver.Remote(
        command_executor=uri,
        options=options
    )

    logging.info("Connected to Selenium Hub")

    return driver

