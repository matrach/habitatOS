from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel


class Network(HabitatModel):

    location = models.ForeignKey(
        verbose_name=_('Sensor Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.DecimalField(
        verbose_name=_('Value'),
        help_text=_('Mbps'),
        max_digits=5,
        decimal_places=2,
        default=None)

    def __str__(self):
        return f'[{self.date} {self.time}] (location: {self.location}) {self.value} Mbps'

    class Meta:
        verbose_name = _('Network Performance Measurement')
        verbose_name_plural = _('Network Performance')
