from lib.models.movie import Movie

def test_movie_json():
    movie = Movie(
        position=1,
        name='Test Movie',
        release_year=2023,
        length='2h 10m',
        rating='PG',
        score=10,
    )

    assert movie.to_json() == """{
  "length": "2h 10m",
  "name": "Test Movie",
  "position": 1,
  "rating": "PG",
  "release_year": 2023,
  "score": 10
}"""