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
