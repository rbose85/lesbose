import logging

from django.contrib.auth import hashers
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
        'is_active': True,
        'is_superuser': True,
    },
]


class Fakes(AbstractBaseFakes):
    """
    fakes for custom auth User
    """

    @staticmethod
    def is_unique_user(collection, obj):
        """return True if neither email nor username of obj are in collection"""
        return not bool([x for x in collection if (x.email == obj.email) or
                                                  (x.username == obj.username)])

    @staticmethod
    def random_fields():
        fake = Faker(locale='en_GB')
        return {
            'username': fake.user_name(),
            'email': fake.email(),
            'password': get_random_string(length=128),
            'is_active': bool(random.randint(0, 1)),
            'is_superuser': False,
        }

    def create_obj(self, fields=None):
        """
        Return an un-saved obj from provided dict.
        :param fields: a dict of fields for the new obj.
        :return: the newly create instance obj.
        """
        if not fields:
            fields = self.random_fields()
        fields['password'] = hashers.make_password(fields['password'])
        return User(**fields)

    def create_objs(self, count=500):
        """
        Return a list of new objs with random fields.
        :param count: total number of objs to be create.
        :return: a list of new objs.
        """
        users = []
        for i in range(0, count + 1):
            while i != len(users):  # equality after 'users.append()'
                user = self.create_obj()
                if self.is_unique_user(collection=users, obj=user):
                    users.append(user)
        return users

    def execute(self):
        users = []

        # create objs of known fields
        for daredev in DARING_DEVELOPERS:
            users.append(self.create_obj(fields=daredev))

        # create objs of random fields
        users.extend(self.create_objs())

        # persist objs to db
        for obj in users:
            obj.save()
