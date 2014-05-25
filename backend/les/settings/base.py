import os

from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """Return the value of an environment variable, or raise an exception."""
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = 'Set the {} env variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


#### DJANGO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

ROOT_URLCONF = 'les.urls'


#### DJANGO: django.conf.global_settings

TIME_ZONE = 'UTC'

USE_TZ = True

LANGUAGE_CODE = 'en-gb'

USE_I18N = True

USE_L10N = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2'
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

SECRET_KEY = get_env_setting('SECRET_KEY')

STATIC_URL = '/static/'

WSGI_APPLICATION = 'les.wsgi.application'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
