from django.db import models
from django.utils.translation import ugettext_lazy as _


class Temperature(models.Model):
    value = models.PositiveSmallIntegerField(verbose_name=_('Temperature'), help_text=_('K'))
