from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel


class Location(HabitatModel):
    DIRECTIONS_NORTH = 'north'
    DIRECTIONS_NORTH_EAST = 'north-east'
    DIRECTIONS_NORTH_WEST = 'north-east'
    DIRECTIONS_SOUTH = 'south'
    DIRECTIONS_SOUTH_EAST = 'south-east'
    DIRECTIONS_SOUTH_WEST = 'south-east'
    DIRECTIONS_EAST = 'east'
    DIRECTIONS_WEST = 'west'

    DIRECTIONS_CHOICES = [
        (DIRECTIONS_NORTH, _('North')),
        (DIRECTIONS_SOUTH, _('South')),
        (DIRECTIONS_EAST, _('East')),
        (DIRECTIONS_WEST, _('West')),
        (DIRECTIONS_NORTH_EAST, _('North East')),
        (DIRECTIONS_NORTH_WEST, _('North West')),
        (DIRECTIONS_SOUTH_EAST, _('South East')),
        (DIRECTIONS_SOUTH_WEST, _('South West')),
    ]

    identifier = models.CharField(
        verbose_name=_('Identifier'),
        max_length=10,
        unique=True)

    direction = models.CharField(
        verbose_name=_('Direction from Habitat'),
        choices=DIRECTIONS_CHOICES,
        max_length=30)

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100,
        unique=True)

    description = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True,
        default=None)

    longitude = models.DecimalField(
        verbose_name=_('Longitude'),
        help_text=_('Decimal Degrees'),
        max_digits=9,
        decimal_places=7,
        null=True,
        blank=True,
        default=None)

    latitude = models.DecimalField(
        verbose_name=_('Latitude'),
        help_text=_('Decimal Degrees'),
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True,
        default=None)

    elevation = models.DecimalField(
        verbose_name=_('Elevation'),
        help_text=_('Meters AGSL'),
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        default=None)

    radius = models.DecimalField(
        verbose_name=_('Radius'),
        help_text=_('Meters'),
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        default=None)

    def __str__(self):
        return f'[{self.identifier}] {self.name}'

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')
