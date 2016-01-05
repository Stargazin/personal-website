from .base import *

DEBUG = True

##EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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

INSTALLED_APPS += ()