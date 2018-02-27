==========
{{ cookiecutter.app_name }}
==========

{{ cookiecutter.app_description }}


Testing
=======

Install packages required for testing:

.. code-block:: bash

   $ pip install -r requirements_test.txt

Run tests with pytest:

.. code-block:: bash

   $ py.test

Run tests with tox:

.. code-block:: bash

   $ tox
 

Running application
===================

.. code-block:: bash
   
   # Make sure that you have all requirements installed
   $ pip install -e .
   $ uwsgi --http :8000 --wsgi-file {{ cookiecutter.package_name }}/webapi/wsgi.py --pyargv={{ cookiecutter.package_name }}/confs/local.ini
   # curl 127.0.0.1:8000/v1/alert/ping


Generating documentation
========================

.. code-block:: bash

   # While executing the following lines you may expect a lot of
   # warnings. The command below goes through *.py files in project
   # directory and generates *.rst files in docs/src directory.

   $ sphinx-apidoc -fo docs {{ cookiecutter.package_name }}

   # The command below generates *.html in docs/build from *.rst in docs

   $ sphinx-build -b html docs docs/build
