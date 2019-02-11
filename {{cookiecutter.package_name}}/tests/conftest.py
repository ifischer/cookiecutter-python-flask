import pytest

from {{cookiecutter.module_name}} import example


@pytest.fixture
def app():
    {{cookiecutter.module_name}}.app.debug = True
    return {{cookiecutter.module_name}}.app
