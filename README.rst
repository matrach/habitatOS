HabitatOS
=========

.. image:: https://travis-ci.org/AstroMatt/HabitatOS.svg?branch=master
    :target: https://travis-ci.org/AstroMatt/HabitatOS

Install
-------

Download the project:

.. code-block:: sh

    git clone https://github.com/AstroMatt/HabitatOS.git

Setup environment and install dependencies:

.. code-block:: sh

    python3 -m venv .virtualenv
    source .virtualenv/bin/activate
    pip install -r requirements.txt

Create database and run application:

.. code-block:: sh

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py loaddata fixtures/*
    python manage.py runserver

Open browser and use:

.. code-block:: sh

    open http://127.0.0.1:8000/
