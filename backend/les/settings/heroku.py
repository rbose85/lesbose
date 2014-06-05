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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },

    'loggers': {

        #### D J A N G O ####
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False,
        },

        #### P R O J E C T ####
        'les.management.commands': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True


#### HEROKU

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
