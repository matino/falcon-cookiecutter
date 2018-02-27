import os
import re

from setuptools import find_packages
from setuptools import setup


def get_version():
    """Extract and return version number from the packages '__init__.py'."""
    init_path = os.path.join('{{ cookiecutter.package_name }}', '__init__.py')
    content = read_file(init_path)
    match = re.search(r"__version__ = '([^']+)'", content, re.M)
    version = match.group(1)
    return version


def read_requirements(filename):
    """Open a requirements file and return list of its lines."""
    content = read_file(filename)
    return content.strip('\n').split('\n')


def read_file(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path) as f:
        return f.read()


setup(
    name='{{ cookiecutter.app_name }}',
    description='{{cookiecutter.app_description}}',
    version=get_version(),
    packages=find_packages(include=('{{ cookiecutter.package_name }}*',)),
    include_package_data=True,
    classifiers = [
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT',
    ],
    install_requires=read_requirements('requirements.txt'),
    tests_require=read_requirements('requirements_test.txt'),
    zip_safe=False,
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_mail}}',
    url='{{cookiecutter.app_url}}',
)
