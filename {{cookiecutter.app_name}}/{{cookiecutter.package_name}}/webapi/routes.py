import falcon

from {{ cookiecutter.package_name }}.webapi import containers
from {{ cookiecutter.package_name }}.webapi import resources


def add_routes(app: falcon.API, container: containers.Main) -> None:
    app.add_route('/v1/alert/ping', resources.monitoring.Ping())
