django-tickets
==============

Reusable django application providing a generic support ticket system.

## Installation

If you want to install the latest stable release from PyPi:

    $ pip install django-tickets

If you want to install the latest development version from GitHub:

    $ pip install -e git://github.com/byteweaver/django-tickets#egg=django-tickets

Add `tickets` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'tickets',
        ...
    )

Hook this app into your ``urls.py``:

    urlpatterns = patterns('',
        ...
        url(r'^tickets/', include('tickets.urls', namespace='tickets')),
        ...
    )

## Tests

To run the test cases simply call:

    $ make tests

or use tox test runner:

    $ tox
