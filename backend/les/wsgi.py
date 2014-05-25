"""
WSGI config for project.
"""

import os

from django.core.wsgi import get_wsgi_application


if os.environ.get('HOST_PLATFORM') in ['heroku', ]:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'les.settings.heroku')

application = get_wsgi_application()
