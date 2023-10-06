import json
from dataclasses import dataclass


@dataclass
class Movie:
    name: str
    rating: str
    score: float
    release_year: int
    length: str
    position: int

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)


