from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime


class Radiation(HabitatModel, MissionDateTime):

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.DecimalField(
        verbose_name=_('Radiation'),
        help_text=_('Sievert'),
        max_digits=6,
        decimal_places=5,
        default=None)

    def __str__(self):
        return f'[{self.date} {self.time}] (location: {self.location}) {self.value}Sv'

    class Meta:
        verbose_name = _('Radiation Measurement')
        verbose_name_plural = _('Radiation')
