from os import environ

from .base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tst',
        'USER': environ['DB_USERNAME'],
        'PASSWORD': environ['DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}