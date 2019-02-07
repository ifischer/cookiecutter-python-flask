import pytest

from hello_service import hello_service


@pytest.fixture
def app():
    hello_service.app.debug = True
    return hello_service.app
