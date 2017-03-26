from django.db import models
from django.utils.translation import ugettext_lazy as _


class Plant(models.Model):
    spicies = models.CharField(verbose_name=_('Species'), help_text=_('Latin'), max_length=255)

