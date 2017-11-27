Superset Data Analytics
=======================

Installation
------------

.. code-block:: console

        # Install superset
        pip install superset

        # Create an admin user (you will be prompted to set username, first and last name before setting a password)
        fabmanager create-admin --app superset

        # Initialize the database
        superset db upgrade

        # Create default roles and permissions
        superset init

        # To start a development web server, use the -d switch
        # superset runserver -d -p 8080


Using
-----
W trybie wyklikania można tworzyć wykresy, a te później umieszczać na dashboardach i będą się automatycznie odświeżały.
Narzędzie zaciąga dane na bieżąco z habitatOS.
Trzeba jeszcze trochę popracować nad raportami, ale już można się bawić na danych które mamy.

W trybie SQL Lab możesz pisać takie zapytania.

.. code-block:: sql

        SELECT *
        FROM sensors_zwavesensor
        WHERE
            device='c1344062-6'
            AND type='temperature'


Urządzenia
----------

.. code-block:: txt

        DEVICE_ATRIUM = 'c1344062-2'
        DEVICE_ANALYTIC_LAB = 'c1344062-3'
        DEVICE_OPERATIONS = 'c1344062-4'
        DEVICE_TOILET = 'c1344062-5'
        DEVICE_DORMITORY = 'c1344062-6'
        DEVICE_STORAGE = 'c1344062-7'
        DEVICE_KITCHEN = 'c1344062-8'
        DEVICE_BIOLAB = 'c1344062-9'

