# -*- coding: utf-8 -*-

#
# Define here the base configuration..
#

import os


DEBUG = False

# JWT
JWT_LIFESPAN = 60*60*24
JWT_ISSUER = 'flask-app-blueprint'
JWT_ALGORITHM = 'HS256'  # HS256, RS256

# Database
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)

POSTGRES_DB = os.environ.get('POSTGRES_DB', 'flask_project')
POSTGRES_DB_TEST = os.environ.get('POSTGRES_DB_TEST', 'flask_project_test')

POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')

SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB)
SQLALCHEMY_DATABASE_TEST_URI = 'postgresql://{}:{}@{}:{}/{}'.format(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB_TEST)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# And after that...
# Used to define some configuration in the local environment in order to
# don't modify the repository code...
try:
    from .local import *
except ImportError:
    pass
