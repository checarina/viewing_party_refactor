import pytest
from viewing_party.movie import *

def test_movie_creation():
    # Arrange

    # Act
    new_movie = Movie("Top Gun: Maverick", "Action", 4.8, "Hulu", "16+")

    # Assert
    assert new_movie.title == "Top Gun: Maverick"
    assert new_movie.genre == "Action"
    assert new_movie.rating == 4.8
    assert new_movie.host == "Hulu"
    assert new_movie.audience == "16+"