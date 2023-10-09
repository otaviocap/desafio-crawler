import logging
import os.path

from lib.models.movie import Movie
from lib.utils.logger import start_logger, get_file_location
from lib.utils.pandas import df_to_json_file, df_to_csv_file, list_to_df


class TestExport:

    def test_export_to_json(self):
        file_name = "Test"

        movie_df = list_to_df([Movie(
            position=1,
            name='Test Movie',
            release_year=2023,
            length='2h 10m',
            rating='PG',
            score=10,
        )])

        df_to_json_file(movie_df, file_name)

        location = get_file_location('data', file_name, "json")

        assert os.path.exists(location)
        os.remove(location)

    def test_export_to_csv(self):
        file_name = "Test"

        movie_df = list_to_df([Movie(
            position=1,
            name='Test Movie',
            release_year=2023,
            length='2h 10m',
            rating='PG',
            score=10,
        )])

        df_to_csv_file(movie_df, file_name)

        location = get_file_location('data', file_name, "csv")

        assert os.path.exists(location)
        os.remove(location)
