from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel


class Location(HabitatModel):

    identifier = models.CharField(
        verbose_name=_('Identifier'),
        max_length=10,
        unique=True)

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100,
        unique=True)

    description = models.TextField(
        verbose_name=_('Description'))

    longitude = models.DecimalField(
        verbose_name=_('Longitude'),
        help_text=_('Decimal Degrees'),
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        default=None)

    latitude = models.DecimalField(
        verbose_name=_('Latitude'),
        help_text=_('Decimal Degrees'),
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        default=None)

    height = models.DecimalField(
        verbose_name=_('Height'),
        help_text=_('Meters'),
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
