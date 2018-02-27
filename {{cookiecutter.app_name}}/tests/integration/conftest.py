import pytest
import webtest

from {{ cookiecutter.package_name }}.webapi.configuration import create_app
from {{ cookiecutter.package_name }}.webapi.configuration import create_container
from {{ cookiecutter.package_name }}.webapi.configuration import parse_config


@pytest.fixture(scope='session')
def webapi(container):
    app = create_app(container)
    return webtest.TestApp(app)


@pytest.fixture(autouse=True, scope='session')
def container(pytestconfig):
    settings = parse_config(pytestconfig.option.ini_file)
    container = create_container(settings)
    container.configure()
    return container
