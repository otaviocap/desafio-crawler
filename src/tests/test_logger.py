import logging
import os.path

from lib.utils.logger import start_logger, get_file_location

class TestLogger:

    def test_config(self):
        start_logger()

    def test_log(self):
        logging.debug("Test debug")
        logging.info("Test info")
        logging.warning("Test warning")
        logging.error("Test error")
        logging.critical("Test critical")

    def test_log_file_exists(self):
        os.path.exists(get_file_location("text", "Log", "log"))
