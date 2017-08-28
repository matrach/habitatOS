*********
HabitatOS
*********

Operating System for analog extraterrestrial habitats.

Contact
=======

.. image:: https://travis-ci.org/AstroMatt/HabitatOS.svg?branch=master
    :target: https://travis-ci.org/AstroMatt/HabitatOS


- `HabitatOS on SonarCloud.io <https://sonarcloud.io/dashboard?id=HabitatOS>`_
- `HabitatOS on Travis-CI.org <https://travis-ci.org/AstroMatt/HabitatOS.svg?branch=master>`_
- `HabitatOS on GitHub.com <https://github.com/AstroMatt/HabitatOS>`_


**Author**
    :name: `Matt Harasymczuk <http://astromatt.space>`_
    :email: `HabitatOS@astrotech.io <mailto:HabtatOS@astrotech.io>`_
    :www: `http://www.astromatt.space <http://astromatt.space>`_
    :facebook: `https://facebook.com/astromatt.space <https://facebook.com/astromatt.space>`_
    :linkedin: `https://linkedin.com/in/mattharasymczuk <https://linkedin.com/in/mattharasymczuk>`_
    :slideshare: `https://www.slideshare.net/astrotech/presentations <https://www.slideshare.net/astrotech/presentations>`_





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

    $ python3 -m venv .virtualenv
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
    $ pip install pylibmc
    $ memcached -d -s /tmp/memcached.sock

Database
--------

.. code-block:: console

    $ brew install postgresql

Contributing
============

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

