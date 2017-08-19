from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime


class Meteo(HabitatModel, MissionDateTime):

    location = models.ForeignKey(
        verbose_name=_('Sensor Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.PositiveSmallIntegerField(
        verbose_name=_('Value'),
        default=None)

    def __str__(self):
        return f'[{self.date} {self.time}] (location: {self.location}) {self.value}'

    class Meta:
        verbose_name = _('Meteo')
        verbose_name_plural = _('Meteo Measurements')
