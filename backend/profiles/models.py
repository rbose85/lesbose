from django.conf import settings
from django.db import models

from core.models import TimeStampModel


class AccountHolder(TimeStampModel):
    """
    Define the owner of an account.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    first_name = models.CharField('Forename', max_length=30, blank=False,
                                  default='')
    last_name = models.CharField('Surname', max_length=30, blank=False,
                                 default='')
    birth_date = models.DateField('Date of Birth', null=True, blank=True,
                                  default=None)
