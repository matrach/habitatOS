from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime


class Temperature(HabitatModel, MissionDateTime):
    UNIT_CELSIUS = 'celsius'
    UNIT_KELVIN = 'kelvin'
    UNIT_FAHRENHEIT = 'fahrenheit'

    UNIT_CHOICES = [
        (UNIT_CELSIUS, _('Celsius')),
        (UNIT_KELVIN, _('Kelvin')),
        (UNIT_FAHRENHEIT, _('Fahrenheit'))]

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.DecimalField(
        verbose_name=_('Temperature'),
        max_digits=5,
        decimal_places=2,
        default=None)

    unit = models.CharField(
        verbose_name=_('Unit'),
        max_length=10,
        choices=UNIT_CHOICES,
        default=UNIT_CELSIUS)

    def __str__(self):
        return f'[{self.date} {self.time}] (location: {self.location}) {self.value} {self.unit.upper():.1}'

    class Meta:
        verbose_name = _('Temperature Measurement')
        verbose_name_plural = _('Temperature')
