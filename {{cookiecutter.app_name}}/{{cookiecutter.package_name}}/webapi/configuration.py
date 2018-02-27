from configparser import ConfigParser
from logging.config import fileConfig

import falcon

from {{ cookiecutter.package_name }}.webapi import containers
from {{ cookiecutter.package_name }}.webapi.routes import add_routes


def create_app(container: containers.Main) -> falcon.API:
    app = falcon.API()
    add_routes(app, container)
    return app


def parse_config(config_path: str) -> dict:
    fileConfig(config_path)
    parser = ConfigParser()
    parser.read(config_path)
    return dict(parser['DEFAULT'])


def create_container(settings: dict) -> containers.Main:
    return containers.Main(settings)
