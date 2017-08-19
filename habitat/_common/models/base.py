from django.db import models
from django.utils.translation import ugettext_lazy as _


class HabitatModel(models.Model):
    created = models.DateTimeField(
        verbose_name=_('Add Datetime'),
        db_index=True,
        auto_now_add=True)

    modified = models.DateTimeField(
        verbose_name=_('Modified Datetime'),
        db_index=True,
        auto_now=True)

    class Meta:
        abstract = True
