from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime


class Illuminance(HabitatModel, MissionDateTime):

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.PositiveSmallIntegerField(
        verbose_name=_('Illuminance'),
        help_text=_('Lux'),
        default=None)

    def __str__(self):
        return f'[{self.date} {self.time}] (location: {self.location}) {self.value} lumen'

    class Meta:
        verbose_name = _('Illuminance Measurement')
        verbose_name_plural = _('Illuminance')
