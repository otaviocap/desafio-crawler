import logging
import os.path

from lib.utils.logger import start_logger, get_file_location

class TestLogger:

    def test_config(self):
        start_logger("Log Test")

    def test_log(self):
        start_logger("Log Test")
        logging.debug("Test debug")
        logging.info("Test info")
        logging.warning("Test warning")
        logging.error("Test error")
        logging.critical("Test critical")

    def test_log_file_exists(self):
        location = get_file_location("text", "Log Test", "log")

        assert os.path.exists(location)
        os.remove(location)
