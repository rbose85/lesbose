from django.db import models


class TimeStampModel(models.Model):
    """
    Abstract base class. Self-managed timestamp for db transactions on a record.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)
        abstract = True


# todo: if this pattern takes-off, remove this out into a proj of its own
class AbstractBaseFakes(object):
    """
    Abstract base class. Each concrete subtype will live in an app's 'fakes.py'.
    """

    class Meta:
        abstract = True

    def execute(self):
        """
        Override this func, it will be called to execute the fake.
        """
        raise NotImplementedError()
