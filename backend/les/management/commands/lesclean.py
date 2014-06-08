import fnmatch
import os
import logging
from optparse import make_option

from django.conf import settings
from django.core.management.base import CommandError, NoArgsCommand


logger = logging.getLogger(__name__)


class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        make_option('-n', '--dry-run',
                    action='store_true', dest='dry_run', default=False,
                    help='Do everything except delete files from project.'),)
    help = 'Remove intermediate and compiled files.'

    def __init__(self):
        super(Command, self).__init__()
        self.dry_run = None

    def set_options(self, **options):
        """
        Set instance variables based on an options dict.
        """
        self.dry_run = options['dry_run']

    @staticmethod
    def find_files(pattern=None):
        """
        Return list of files (including absolute path) matching extension.
        """
        if not pattern:
            return []

        matches = []
        for root, dirnames, filenames in os.walk(settings.PROJECT_DIR):
            for filename in fnmatch.filter(filenames, pattern):
                matches.append(os.path.join(root, filename))
        return matches

    def delete_file(self, filename):
        """
        Delete the file, filename, where 'filename' includes absolute path.
        """
        logger.info('deleting file: {}'.format(filename))
        try:
            if not self.dry_run:
                os.remove(filename)
        except OSError:
            raise CommandError('Unable to delete file, {}'.format(filename))

    def handle_noargs(self, **options):
        """
        Entry point for command. Add custom actions here.
        """
        logger.info('{} ...'.format(__name__))

        self.set_options(**options)

        # List filename patterns to be searched. Found files are deleted.
        patterns = ['*.pyc', ]

        delete_files = []
        for p in patterns:
            delete_files += self.find_files(p)

        for f in delete_files:
            self.delete_file(f)
