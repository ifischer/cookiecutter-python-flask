import pytest

from example import example


@pytest.fixture
def app():
    example.app.debug = True
    return example.app
