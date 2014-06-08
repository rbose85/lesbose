import os

from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """Return the value of an environment variable, or raise an exception."""
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = 'Set the {} env variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


#### PROJECT

PROJECT = 'lesbose'
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SITE_DOMAIN = None


#### DJANGO: https://docs.djangoproject.com/en/dev/ref/settings/

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
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# don't forget project apps ..
INSTALLED_APPS += (
    'authentication',
    'core',
    'profiles',
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

AUTH_USER_MODEL = 'authentication.user'


#### DJANGO REST FRAMEWORK: rest_framework.settings

INSTALLED_APPS += (
    'rest_framework',
)

REST_FRAMEWORK = {
    'DEFAULT_MODEL_SERIALIZER_CLASS': (
        'rest_framework.serializers.HyperlinkedModelSerializer'),

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}
