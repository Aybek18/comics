from typing import List

import pytest

from comics.models import Comics
from comics.tests.factories import ComicsFactory


@pytest.fixture
def list_comics(db) -> List[Comics]:
    list_comics = ComicsFactory.create_batch(size=5)
    return list_comics


@pytest.fixture
def comics(db, list_comics) -> Comics:
    return list_comics[0]

