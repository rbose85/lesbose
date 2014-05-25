from .base import *


#### PROJECT

PROJECT = 'lesbose-heroku'
SITE_DOMAIN = 'api.lesbose.com'
HEROKU_DOMAIN = 'lesbose.herokuapp.com'


#### DJANGO

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [HEROKU_DOMAIN, SITE_DOMAIN, ]


#### DJANGO: django.conf.global_settings

DATABASES['default'].update({
    'NAME': get_env_setting('DATABASE_NAME'),
    'USER': get_env_setting('DATABASE_USER'),
    'PASSWORD': get_env_setting('DATABASE_PASSWORD'),
    'HOST': get_env_setting('DATABASE_HOST'),
})

INSTALLED_APPS += (
    'gunicorn',
)


#### HEROKU

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
