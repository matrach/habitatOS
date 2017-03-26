from django.db import models
from django.utils.translation import ugettext_lazy as _


class Humidity(models.Model):
    value = models.PositiveSmallIntegerField(verbose_name=_('Humidity'), help_text=_('%'))

