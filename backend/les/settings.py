import os

from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """
    Return an environment variable, or raise an exception.
    """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = 'Set the {} env variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = get_env_setting('SECRET_KEY')

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost', ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# don't forget project apps, too ...
INSTALLED_APPS += ()

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'les.urls'

WSGI_APPLICATION = 'les.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lesbose_db',
        'USER': 'lesbose_user',
        'PASSWORD': get_env_setting('DATABASE_LOCAL_PASSWORD')
    }
}

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
