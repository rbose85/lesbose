import string
import logging

from django.conf import settings
from django.contrib.auth import hashers
from django.core.exceptions import ImproperlyConfigured
from django.utils.crypto import get_random_string, random
from faker import Faker

from core.models import AbstractBaseFakes
from .models import User


logger = logging.getLogger(__name__)

DARING_DEVELOPERS = [
    {
        'username': 'admin',
        'email': 'admin@dev.lesbose.com',
        'password': 'password',
        'isActive': True,
        'isAdmin': True,
    },
]


class Fakes(AbstractBaseFakes):
    """
    fakes for custom auth.User
    """

    @staticmethod
    def random_passwd():
        size = 128
        chrs = string.letters + string.digits
        return get_random_string(length=size, allowed_chars=chrs)

    @staticmethod
    def random_bool():
        return bool(random.randint(0, 1))

    @staticmethod
    def random_deets():
        details = Faker(locale='en_GB').simple_profile()
        details['email'] = details['mail']
        del details['mail']
        return details

    @staticmethod
    def is_unique_user(collection, obj):
        """return True if neither email nor username of obj are in collection"""
        return not bool([x for x in collection if (x.email == obj.email) or
                                                  (x.username == obj.username)])

    def create_user(self, deets=None):
        """
        Return an un-saved User obj from provided details dict.
        :param deets: a dict of details for the User.
        :return User: the newly create instance obj.
        """
        if not deets:
            deets = self.random_deets()

        u = deets['username']
        e = deets['email']
        p = deets['password'] if deets.get('password') else self.random_passwd()

        # create new User instance
        obj = User(username=u, email=e, password=hashers.make_password(p))

        # activate new User ?
        obj.is_active = self.random_bool()
        if deets.get('isActive'):
            obj.is_active = bool(deets['isActive'])

        # upgrade new User ?
        if 'isAdmin' in deets and deets['isAdmin']:
            obj.is_superuser = True

        return obj

    def create_users(self, count=None):
        """
        Return a list of new User objs with random details.
        :param count: total number of User objs to be create.
        :return: a list of new User obj.
        """
        if not count:
            count = 500

        users = []
        for i in range(0, count + 1):
            while i != len(users):  # equality after 'users.append()'
                user = self.create_user()
                if self.is_unique_user(collection=users, obj=user):
                    users.append(user)
        return users

    def execute(self):
        if not settings.DEBUG:
            logger.error('Cannot run fakes, {}.'.format(__file__))
            raise ImproperlyConfigured

        users = []

        # create objs of known deets
        for i in DARING_DEVELOPERS:
            users.append(self.create_user(deets=i))

        # create objs of random deets
        users += self.create_users()

        # persist objs to db
        for obj in users:
            obj.save()
