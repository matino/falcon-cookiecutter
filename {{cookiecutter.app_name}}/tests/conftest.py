def pytest_addoption(parser):
    parser.addoption(
        '--ini-file',
        action='store',
        type='string',
        default='{{ cookiecutter.package_name }}/confs/local.ini',
    )
