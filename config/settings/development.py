import os
from .base import *


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True

# SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
# ------------------------------------------------------------------------------
SECRET_KEY = '5pr8=^=iz-_ghb9ybc%6x1rlk!a@j5yu#^s&bg+y8s@ve&5v6k'

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': 5432,
        'NAME': env('POSTGRES_DBNAME'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
    }
}

# EMAIL CONFIGURATION
# Set MailHog as the local mail server
# ------------------------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
