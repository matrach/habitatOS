from django.db import models
from django.utils.translation import ugettext_lazy as _


class Luminosity(models.Model):
    value = models.PositiveSmallIntegerField(verbose_name=_('Luminosity'), help_text=_('lumen'))

