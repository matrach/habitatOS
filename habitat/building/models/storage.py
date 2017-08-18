from django.db import models
from django.utils.translation import ugettext_lazy as _


class Storage(models.Model):
    location = models.ForeignKey(
        verbose_name=_('location'),
        to='building.Module')

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=50)

    def __str__(self):
        return f'{self.location} -> {self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = _('Storage')
        verbose_name_plural = _('Storage')
