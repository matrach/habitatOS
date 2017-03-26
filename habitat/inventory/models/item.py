from django.db import models
from django.utils.translation import ugettext_lazy as _


class Item(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    code = models.CharField(verbose_name=_('Code'), max_length=7)
    quantity = models.PositiveSmallIntegerField(verbose_name=_('Quantity'))

    def __str__(self):
        return f'{self.name} [{self.code}]'
