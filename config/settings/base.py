"""
Django settings for chopin project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import shutil
import os
import environ

ROOT_DIR = environ.Path(__file__) - 3
BASE_DIR = str(ROOT_DIR)
APPS_DIR = ROOT_DIR.path('apps')

if not os.path.isfile(str(ROOT_DIR('.env'))):
    shutil.copyfile(str(ROOT_DIR('.env.example')), str('.env'))

env = environ.Env()
env.read_env(str(ROOT_DIR('.env')))


# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]
LOCAL_APPS = [
    'apps.user',
    'apps.blueprints',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
SITE_ID = 1

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'resources/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# ------------------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'resources/static'),
]

# ALLAUTH CONFIGURATION
# https://docs.djangoproject.com/en/1.10/topics/auth/customizing/
# http://django-allauth.readthedocs.io/en/latest/configuration.html
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ACCOUNT_SIGNUP_FORM_CLASS = 'apps.user.forms.SignupForm'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGOUT_REDIRECT_URL = '/user/login/'
LOGIN_URL = '/user/login/'
LOGIN_REDIRECT_URL = '/blueprints/'

# TWILIO 
# ------------------------------------------------------------------------------
TWILIO_API_KEY = env('TWILIO_API_KEY')

# OAUTH SETTINGS - FACEBOOK
# ------------------------------------------------------------------------------
FB_OAUTH_CLIENT_ID = env('FB_OAUTH_CLIENT_ID')
FB_OAUTH_CLIENT_SECRET = env('FB_OAUTH_CLIENT_SECRET')

# OAUTH SETTINGS - GOOGLE
# https://developers.google.com/identity/sign-in/web/sign-in
# ------------------------------------------------------------------------------
GOOGLE_OAUTH_CLIENT_ID = env('GOOGLE_OAUTH_CLIENT_ID')

# EXPORT REQUIRED SETTINGS FOR USE IN TEMPLATES
# https://github.com/jakubroztocil/django-settings-export
# ------------------------------------------------------------------------------
SETTINGS_EXPORT = [
    'GOOGLE_OAUTH_CLIENT_ID',
]
