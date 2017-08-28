from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime


class Voltage(HabitatModel, MissionDateTime):

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.DecimalField(
        verbose_name=_('Value'),
        help_text=_('Volts'),
        max_digits=6,
        decimal_places=3,
        default=None)

    def __str__(self):
        return f'[{self.date} {self.time}] (location: {self.location}) {self.value} V'

    class Meta:
        verbose_name = _('Voltage Measurement')
        verbose_name_plural = _('Voltage')
