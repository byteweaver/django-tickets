VIRTUALENV_DIRECTORY?=env
VIRTUALENV_BINARY?=virtualenv
VIRTUALENV_PYTHON_BINARY?=python

PYTHON_BINARY=$(VIRTUALENV_DIRECTORY)/bin/python
PIP_BINARY=$(VIRTUALENV_DIRECTORY)/bin/pip
DJANGO_ADMIN_BINARY=$(VIRTUALENV_DIRECTORY)/bin/django-admin

all: environment requirements

environment:
	test -d "$(VIRTUALENV_DIRECTORY)" || virtualenv --no-site-packages $(VIRTUALENV_DIRECTORY)

requirements:
	$(PIP_BINARY) install -r requirements.txt

test: requirements
	$(DJANGO_ADMIN_BINARY) test --settings=tickets.tests.settings

coverage: requirements
	$(COVERAGE_BINARY) erase
	$(COVERAGE_BINARY) run --branch --source=tickets env/bin/django-admin.py test --settings=tickets.tests.settings
	$(COVERAGE_BINARY) html
