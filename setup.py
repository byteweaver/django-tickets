import os
from setuptools import setup, find_packages

import tickets


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-tickets',
    version=tickets.__version__,
    description='Reusable django application providing a generic support ticket system',
    long_description=read('README.md'),
    license='MIT License',
    author='akuryou',
    author_email='contact@byteweaver.net',
    url='https://github.com/byteweaver/django-tickets',
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
        'factory_boy',
    ],
)
