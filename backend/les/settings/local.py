from .base import *


#### PROJECT

PROJECT = 'lesbose-local'
SITE_DOMAIN = 'localhost'


#### DJANGO

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [SITE_DOMAIN, ]


#### DJANGO: django.conf.global_settings

DATABASES['default'].update({
    'NAME': 'lesbose_db',
    'USER': 'lesbose_user',
    'PASSWORD': get_env_setting('DATABASE_PASSWORD')
})
