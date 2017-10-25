*********
habitatOS
*********

Operating System for analog extraterrestrial habitats.

.. image:: https://img.shields.io/pypi/l/habitatOS.svg?style=flat-square

.. image:: https://img.shields.io/pypi/pyversions/habitatOS.svg?style=flat-square

.. image:: https://img.shields.io/travis/AstroMatt/HabitatOS/master.svg?style=flat-square&label=Continuous%20Integration
   :target: http://travis-ci.org/AstroMatt/HabitatOS

.. image:: https://img.shields.io/pypi/v/habitatOS.svg?style=flat-square
   :target: https://pypi.org/project/habitatOS

.. image:: https://readthedocs.org/projects/habitatOS/badge/?version=latest
    :target: https://habitatOS.readthedocs.io


Contact
=======

**Author**
    :name: `Matt Harasymczuk <http://astromatt.space>`_
    :email: `habitatOS@astrotech.io <mailto:habtatOS@astrotech.io>`_
    :www: `http://www.astromatt.space <http://astromatt.space>`_
    :facebook: `https://facebook.com/astromatt.space <https://facebook.com/astromatt.space>`_
    :linkedin: `https://linkedin.com/in/mattharasymczuk <https://linkedin.com/in/mattharasymczuk>`_
    :slideshare: `https://www.slideshare.net/astromatt/presentations <https://www.slideshare.net/astromatt/presentations>`_

About the Lunares project
-------------------------

- http://lunares.space
- https://www.facebook.com/lunares.space/
- https://www.slideshare.net/astromatt/bioastronautics


Requirements
============

Minimal
-------
* Python >= 3.6
* Installed requirements from ``requirements.txt`` file

Recommended
-----------
* Python >= 3.6
* PostgreSQL >= 9.6
* Memcache
* Nginx


Install
=======

Download the project
--------------------

.. code-block:: console

    $ git clone https://github.com/AstroMatt/HabitatOS.git

Setup environment and install dependencies:

.. code-block:: console

    $ python -m venv .virtualenv
    $ source .virtualenv/bin/activate
    $ pip install -r requirements.txt

Create database and load data
-----------------------------

.. code-block:: console

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py loaddata fixtures/*

Verify
------

.. code-block:: console

    $ python manage.py test --verbosity 2

Run
---
.. code-block:: console

    $ gunicorn habitat.wsgi

Open browser and use:

.. code-block:: console

    $ open http://127.0.0.1:8000/

Cache
-----
In order to Memcache as a cache:

.. code-block::

    $ brew install memcached
    $ brew install libmemcached
    $ python -m pip install pylibmc
    $ memcached -d -s /tmp/memcached.sock

Database
--------

.. code-block:: console

    # linux (Debian/Ubuntu based)
    $ apt-get install postgresql

    # macOS
    $ brew install postgresql


Development
===========

API Documentation
-----------------
- http://localhost:8000/api/

Client
------
#. Go to http://localhost:8000/auth/user/ and add user
#. Remember to add permission to the user
#. Create ``config.json`` with the following content:

.. code-block:: json

    {
        "url": "http://test.habitatos.space",
        "username": "myuser",
        "password": "mypassword"
    }

#. Create python script with following content:

.. code-block:: python

    import datetime
    from HabitatOS.client import HabitatOSBasicAuth


    habitatOS = HabitatOSBasicAuth(config='config.json')

    response = habitatOS.post('/sensor/zwave/', data={
        'datetime': datetime.datetime.now(datetime.timezone.utc),
        'device': 'c1344062-2',
        'type': 'Temperature',
        'value': 21.5,
        'unit': 'Celsius',
     })

    if response.status_code == 200:
        print('updated')

    elif response.status_code == 201:
        print('created')

    else:
        print('error')


CI/CD
-----
.. image:: https://travis-ci.org/AstroMatt/HabitatOS.svg?branch=master
    :target: https://travis-ci.org/AstroMatt/HabitatOS

- `HabitatOS on SonarCloud.io <https://sonarcloud.io/dashboard?id=HabitatOS>`_
- `HabitatOS on Travis-CI.org <https://travis-ci.org/AstroMatt/HabitatOS.svg?branch=master>`_
- `HabitatOS on GitHub.com <https://github.com/AstroMatt/HabitatOS>`_

Pre-Commit Hook
---------------
.. code-block:: bash

    #!/bin/sh
    set -e

    pep8 habitat
    python manage.py check
    python manage.py makemigrations
    python manage.py migrate
    python manage.py test --verbosity 2

Authorization
-------------
- http://localhost:8000/oauth2/applications/
- http://localhost:8000/oauth2/token/


Timezone
--------
- http://localhost:8000/api/v1/timezone/lunar-standard-time/
- http://localhost:8000/api/v1/timezone/martian-standard-time/
