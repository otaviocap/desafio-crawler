from lib.scrapper.driver import get_driver


def test_driver_connectivity():
    driver = get_driver()

    driver.close()

