from django.db import models
from django.utils.translation import ugettext_lazy as _


class Experiment(models.Model):
    plant = models.ForeignKey(verbose_name=_('Plant'), to='greenhouse.Plant')
