import os
from datetime import date
import logging


def start_logger():
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s]: %(message)s',
        level=logging.INFO,
        handlers=[
            logging.FileHandler(
                get_file_location('text', 'Log', 'log'),
                encoding='utf-8'),
            logging.StreamHandler()
        ]
    )


def get_log_folder() -> str:
    return os.path.join(os.getcwd(), 'logs')


def get_file_location(folder: str, file_name: str, ext: str) -> str:
    return os.path.join(
            get_log_folder(),
            folder,
            f"{date.today().strftime(f'{file_name} (%d-%m-%Y)')}.{ext}"
        )
