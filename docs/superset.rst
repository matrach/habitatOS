Superset Data Analytics
=======================

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



