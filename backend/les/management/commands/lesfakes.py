import imp
import os
import logging

from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import NoArgsCommand
from django.utils.importlib import import_module


logger = logging.getLogger(__name__)


def execute_fakes(app_name):
    """
    Run the execute() of the fakes module
    """
    module = import_module('{}.fakes'.format(app_name))
    logger.debug('running execute() for module: {}'.format(module))
    module.Fakes().execute()


def find_fakes_module(app_name):
    """
    Return the path to 'fakes' module for 'app_name', without importing app.
    Raises ImportError if 'fakes' cannot be found, for any reason.
    """
    parts = app_name.split('.')
    parts.append('fakes')
    parts.reverse()
    part = parts.pop()
    path = None

    try:
        f, path, descr = imp.find_module(part, path)
    except ImportError as e:
        if os.path.basename(os.getcwd()) != part:
            raise e
    else:
        if f:
            f.close()

    while parts:
        part = parts.pop()
        f, path, descr = imp.find_module(part, [path] if path else None)
        if f:
            f.close()

    return app_name + '.' + 'fakes'


def get_installed_apps():
    """
    Return list of installed apps.
    """

    from django.conf import settings

    try:
        apps = settings.INSTALLED_APPS
    except ImproperlyConfigured:
        logger.error('Cannot locate settings.INSTALLED_APPS')
    else:
        return apps


class Command(NoArgsCommand):
    help = "Populate db with models listed in each app's 'fakes.py' file."

    def __init__(self):
        super(Command, self).__init__()
        self._fakes = {}

    def handle_noargs(self, **options):
        """
        Entry point for command. Add custom actions here.
        """

        logger.info('{} ...'.format(__name__))

        apps = get_installed_apps()

        # Find and load the management module for each installed app.
        for app_name in apps:
            try:
                self._fakes[app_name] = find_fakes_module(app_name)
            except ImportError:
                logger.debug("Missing 'fakes.py' file in: {} ".format(app_name))
                pass  # No management module - ignore this app

        for fakes in self._fakes:
            logger.info("Executing 'fakes.py' for: {} ".format(fakes))
            execute_fakes(app_name=fakes)
            logger.debug('fakes: {}'.format(fakes))
