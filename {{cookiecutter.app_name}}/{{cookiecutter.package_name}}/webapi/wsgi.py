import argparse

from {{ cookiecutter.package_name }}.webapi.configuration import create_app

parser = argparse.ArgumentParser()
parser.add_argument('config')
arguments = parser.parse_args()
application = create_app(arguments.config)
