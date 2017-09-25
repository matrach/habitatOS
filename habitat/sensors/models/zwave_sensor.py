from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime


class ZWaveSensor(HabitatModel, MissionDateTime):
    TYPE_BATTERY_LEVEL = 'battery-level'
    TYPE_POWER_LEVEL = 'powerlevel'
    TYPE_TEMPERATURE = 'temperature'
    TYPE_LUMINANCE = 'luminance'
    TYPE_RELATIVE_HUMIDITY = 'relative-humidity'
    TYPE_ULTRAVIOLET = 'ultraviolet'

    TYPE_CHOICES = [
        (TYPE_BATTERY_LEVEL, _('Battery Level')),
        (TYPE_POWER_LEVEL, _('Power Level')),
        (TYPE_TEMPERATURE, _('Temperature')),
        (TYPE_LUMINANCE, _('Luminance')),
        (TYPE_RELATIVE_HUMIDITY, _('Relative Humidity')),
        (TYPE_ULTRAVIOLET, _('Ultraviolet')),
    ]

    UNIT_CELSIUS = 'celsius'
    UNIT_KELVIN = 'kelvin'
    UNIT_FAHRENHEIT = 'fahrenheit'
    UNIT_DECIBEL = 'decibel'

    UNIT_CHOICES = [
        (UNIT_DECIBEL, _('dB')),
        (UNIT_CELSIUS, _('Celsius')),
        (UNIT_KELVIN, _('Kelvin')),
        (UNIT_FAHRENHEIT, _('Fahrenheit'))]

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        db_index=True,
        editable=False)

    device = models.CharField(
        verbose_name=_('Device'),
        max_length=30,
        db_index=True)

    type = models.CharField(
        verbose_name=_('Type'),
        max_length=30,
        choices=TYPE_CHOICES)

    value = models.DecimalField(
        verbose_name=_('Value'),
        max_digits=5,
        decimal_places=2,
        default=None)

    unit = models.CharField(
        verbose_name=_('Unit'),
        max_length=10,
        choices=UNIT_CHOICES,
        default=UNIT_CELSIUS)

    def __str__(self):
        return f'[{self.date} {self.time}] (device: {self.device}) {self.get_type_display()}: {self.value} {self.unit}'

    class Meta:
        verbose_name = _('ZWave Sensor Measurement')
        verbose_name_plural = _('Zwave Sensors')
