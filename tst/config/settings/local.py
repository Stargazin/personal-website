from .base import *

DEBUG = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'tst',
		'USER': 'tst',
		'PASSWORD': 'tst',
		'HOST': 'localhost',
		'PORT': '',
	}
}