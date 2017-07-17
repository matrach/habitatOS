*********
HabitatOS
*********

.. image:: https://travis-ci.org/AstroMatt/HabitatOS.svg?branch=master
    :target: https://travis-ci.org/AstroMatt/HabitatOS

Install
=======

Download the project:

.. code-block:: console

    $ git clone https://github.com/AstroMatt/HabitatOS.git

Setup environment and install dependencies:

.. code-block:: console

    $ python3 -m venv .virtualenv
    $ source .virtualenv/bin/activate
    $ pip install -r requirements.txt

Create database and run application:

.. code-block:: console

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py loaddata fixtures/*
    $ python manage.py test --verbosity 0
    $ python manage.py runserver

Open browser and use:

.. code-block:: console

    $ open http://127.0.0.1:8000/

Cache
=====
In order to Memcache as a cache:

.. code-block::

    $ brew install memcached
    $ brew install libmemcached
    $ pip install pylibmc
    $ memcached -d -s /tmp/memcached.sock

Database
========

.. code-block:: console

    $ brew install postgresql
