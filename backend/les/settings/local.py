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

# don't forget project apps ..
INSTALLED_APPS += (
    'les',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'verbose': {
            'format': "%(levelname)s [%(name)s:%(lineno)s] %(message)s"
        },
    },

    'handlers': {
        'console-simple': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'console-verbose': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },

    'loggers': {

        #### D J A N G O ####
        'django': {
            'handlers': ['console-verbose'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console-verbose', ],
            'level': 'INFO',
            'propagate': False,
        },

        #### P R O J E C T ####
        '': {
            'handlers': ['console-simple'],
            'level': 'INFO',
            'propagate': False,
        },
        'les.management.commands': {
            'handlers': ['console-simple'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
