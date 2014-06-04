import dj_database_url

from .base import *


#### PROJECT

PROJECT = 'lesbose-heroku'
SITE_DOMAIN = 'lesbose.herokuapp.com'


#### DJANGO

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [SITE_DOMAIN, ]


#### DJANGO: django.conf.global_settings

DATABASES['default'] = dj_database_url.config()

INSTALLED_APPS += (
    'gunicorn',
)


#### HEROKU

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
