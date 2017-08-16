from django.db import models
from django.utils.translation import ugettext_lazy as _


class Plant(models.Model):
    latin_name = models.CharField(verbose_name=_('Latin Name'), max_length=255, default=None)
    species = models.CharField(verbose_name=_('Species'), max_length=255, default=None)
    image = models.ImageField(verbose_name=_('Image'), null=True, blank=True, default=None)
    wikipedia_url = models.URLField(verbose_name=_('Wikipedia URL'), null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.species} ({self.latin_name})'

    class Meta:
        ordering = ['-latin_name']
        verbose_name = _('Plant')
        verbose_name_plural = _('Plants')
