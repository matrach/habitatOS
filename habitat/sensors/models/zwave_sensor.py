import datetime
import decimal
import logging
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat.timezone.models import MartianStandardTime


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

    DEVICE_ATRIUM = 'c1344062-2'
    DEVICE_ANALYTIC_LAB = 'c1344062-3'
    DEVICE_OPERATIONS = 'c1344062-4'
    DEVICE_TOILET = 'c1344062-5'
    DEVICE_DORMITORY = 'c1344062-6'
    DEVICE_STORAGE = 'c1344062-7'
    DEVICE_KITCHEN = 'c1344062-8'
    DEVICE_BIOLAB = 'c1344062-9'

    DEVICE_CHOICES = [
        (DEVICE_ATRIUM, _('Atrium')),
        (DEVICE_ANALYTIC_LAB, _('Analytic Lab')),
        (DEVICE_OPERATIONS, _('Operations')),
        (DEVICE_TOILET, _('Toilet')),
        (DEVICE_DORMITORY, _('Dormitory')),
        (DEVICE_STORAGE, _('Storage')),
        (DEVICE_KITCHEN, _('Kitchen')),
        (DEVICE_BIOLAB, _('Biolab')),
    ]

    datetime = models.DateTimeField(verbose_name=_('Datetime [UTC]'), db_index=True, editable=False)
    device = models.CharField(verbose_name=_('Device'), max_length=30, choices=DEVICE_CHOICES, db_index=True)
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
        dt = clean_datetime(datetime)

        # TODO: Change it to more generic solution
        mst = MartianStandardTime().get_time_dict(from_datetime=dt)

        return ZWaveSensor.objects.update_or_create(
            datetime=dt,
            defaults={
                'date': mst['date'],
                'time': mst['time'],
                'device': clean_device(device),
                'type': clean_type(type),
                'value': clean_value(value),
                'unit': clean_unit(unit),
            }
        )
