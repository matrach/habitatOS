import datetime
import decimal
import logging
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime


log = logging.getLogger('habitat.sensor')


def clean_unit(unit):
    try:
        return {
            'C': 'celsius',
            'F': 'fahrenheit',
            'dB': 'decibel',
            'lux': 'lux',
            '%': 'percent',
        }[unit]
    except KeyError:
        return None


def clean_type(type):
    return type.lower().replace(' ', '-')


def clean_value(value):
    try:
        return decimal.Decimal(value)
    except decimal.InvalidOperation:
        return decimal.Decimal(0)


def clean_device(device):
    return device


def clean_datetime(dt):

    try:
        return datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f+00:00').replace(tzinfo=datetime.timezone.utc)
    except ValueError:
        return datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S.%f')


class ZWaveSensor(HabitatModel, MissionDateTime):
    TYPE_BATTERY_LEVEL = 'battery-level'
    TYPE_POWER_LEVEL = 'powerlevel'
    TYPE_TEMPERATURE = 'temperature'
    TYPE_LUMINANCE = 'luminance'
    TYPE_RELATIVE_HUMIDITY = 'relative-humidity'
    TYPE_ULTRAVIOLET = 'ultraviolet'
    TYPE_BURGLAR = 'burglar'

    TYPE_CHOICES = [
        (TYPE_BATTERY_LEVEL, _('Battery Level')),
        (TYPE_POWER_LEVEL, _('Power Level')),
        (TYPE_TEMPERATURE, _('Temperature')),
        (TYPE_LUMINANCE, _('Luminance')),
        (TYPE_RELATIVE_HUMIDITY, _('Relative Humidity')),
        (TYPE_ULTRAVIOLET, _('Ultraviolet')),
        (TYPE_BURGLAR, _('Burglar')),
    ]

    UNIT_CELSIUS = 'celsius'
    UNIT_KELVIN = 'kelvin'
    UNIT_FAHRENHEIT = 'fahrenheit'
    UNIT_DECIBEL = 'decibel'
    UNIT_LUMINANCE = 'lux'
    UNIT_PERCENT = 'percent'
    UNIT_DIMENSIONLESS = None

    UNIT_CHOICES = [
        (UNIT_DIMENSIONLESS, _('n/a')),
        (UNIT_PERCENT, _('%')),
        (UNIT_LUMINANCE, _('Lux')),
        (UNIT_DECIBEL, _('dB')),
        (UNIT_CELSIUS, _('Celsius')),
        (UNIT_KELVIN, _('Kelvin')),
        (UNIT_FAHRENHEIT, _('Fahrenheit'))]

    datetime = models.DateTimeField(verbose_name=_('Datetime'), db_index=True, editable=False)
    device = models.CharField(verbose_name=_('Device'), max_length=30, db_index=True)
    type = models.CharField(verbose_name=_('Type'), max_length=30, choices=TYPE_CHOICES)
    value = models.DecimalField(verbose_name=_('Value'), max_digits=7, decimal_places=2, default=None)
    unit = models.CharField(verbose_name=_('Unit'), max_length=15, choices=UNIT_CHOICES, null=True, blank=True, default=None)

    def __str__(self):
        return f'[{self.date} {self.time}] (device: {self.device}) {self.type}: {self.value} {self.unit}'

    class Meta:
        verbose_name = _('Data')
        verbose_name_plural = _('Zwave Sensors')

    @staticmethod
    def add(datetime, device, type, value, unit):
        return ZWaveSensor.objects.update_or_create(
            datetime=clean_datetime(datetime),
            defaults={
                'device': clean_device(device),
                'type': clean_type(type),
                'value': clean_value(value),
                'unit': clean_unit(unit),
            }
        )
