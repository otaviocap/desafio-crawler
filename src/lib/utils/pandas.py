import logging

import pandas as pd

from lib.utils.logger import get_file_location


def list_to_df(items: list) -> pd.DataFrame:
    df = pd.DataFrame(items)

    return df


def df_to_json_file(df: pd.DataFrame, file_name: str):
    logging.info("Converting df to json")

    df.to_json(
        get_file_location('data', file_name, "json"),
        orient='records'
    )


def df_to_csv_file(df: pd.DataFrame, file_name: str):
    logging.info("Converting df to CSV")

    df.to_csv(
        get_file_location('data', file_name, "csv"),
        index=False
    )
