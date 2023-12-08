from typing import List

import pytest

from ratings.models import Rating
from ratings.tests.factories import RatingFactory


@pytest.fixture
def ratings(db) -> List[Rating]:
    ratings = RatingFactory.create_batch(size=5)
    return ratings


@pytest.fixture
def rating(db, ratings) -> Rating:
    return ratings[0]

