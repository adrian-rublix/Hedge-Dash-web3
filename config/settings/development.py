from .base import *


SECRET_KEY = '5pr8=^=iz-_ghb9ybc%6x1rlk!a@j5yu#^s&bg+y8s@ve&5v6k'

DEBUG = True
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
