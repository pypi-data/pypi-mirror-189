#Chedid

Chedid is a Django app to make easily create and manage data handlers for common JSON data,
and JWT data.

Detailed documentation is in the "docs" directory.

##Quick start


1. Add "chedid" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'chedid',
    ]


3. Run ``python manage.py makemigrations`` and ``python manage.py migrate`` to create the TokenPair models models.
