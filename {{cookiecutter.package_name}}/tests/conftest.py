import pytest

from {{cookiecutter.module_name}} import hello_service


@pytest.fixture
def app():
    {{cookiecutter.module_name}}.app.debug = True
    return {{cookiecutter.module_name}}.app
