**FAQ**:

**What would I use this template for?**


Whenever you want to create an new falcon based API and don't want to
repeat all the annoying setup stuff.


**Why would I use this template?**


It was created to reduce the boilerplate that every new project introduces.


**How do I use this template?**


.. code-block:: bash

   $ pip install cookiecutter
   $ cookiecutter git@github.com:matino/falcon-cookiecutter.git


**What choices have been made for me?**


* Python 3.6+
* Falcon with Cython as http framework
* Monitoring view under '/alert/ping' route
* Logging to syslog
* Logging errors to Sentry
* Running with uwsgi
* Testing with py.test
* Documentation using sphinx
* Configuration using .ini files


**Why do you store config files in the main package?**


If they were outside the main package, they wouldn't be included in the
wheel package, so you wouldn't have them on production machine.
