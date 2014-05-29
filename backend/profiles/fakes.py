import datetime
import logging

from faker import Faker

from authentication.models import User
from core.models import AbstractBaseFakes
from .models import AccountHolder


logger = logging.getLogger(__name__)

DARING_DEVELOPERS = [
    {
        'username': 'admin',
        'first_name': 'Donald',
        'last_name': 'Duck',
        'birth_date': {'year': 1938, 'month': 1, 'day': 10},
    },
]


class Fakes(AbstractBaseFakes):
    """
    fakes for profiles.AccountHolder
    """

    @staticmethod
    def random_fields():
        fake = Faker(locale='en_GB')
        dob = fake.date_time_between(start_date='-80y', end_date='-18y')
        return {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'birth_date': {'year': dob.year, 'month': dob.month, 'day': dob.day}
        }

    @staticmethod
    def create_obj(fields):
        """
        Return an un-saved obj from provided dict.
        :param fields: a dict of details for the new obj.
        :return: the newly create instance obj.
        """
        fields['birth_date'] = datetime.datetime(**fields['birth_date'])
        return AccountHolder(**fields)

    def create_objs(self, qs_users):
        """
        Return a list of new objs with random fields.
        :param qs_users: a QuerySet instances to build objs.
        :return: a list of new objs.
        """
        holders = []
        for u in qs_users:
            fields = self.random_fields()
            fields['user'] = u
            holders.append(self.create_obj(fields=fields))
        return holders

    def execute(self):
        dev_usernames = [x.get('username') for x in DARING_DEVELOPERS]
        users = User.objects.exclude(username__in=dev_usernames)

        holders = []

        # create objs of known fields
        for daredev in DARING_DEVELOPERS:
            daredev['user'] = User.objects.get(username=daredev.pop('username'))
            holders.append(self.create_obj(fields=daredev))

        # create objs of random fields
        holders.extend(self.create_objs(qs_users=users))

        # persist objs to db
        for obj in holders:
            obj.save()
