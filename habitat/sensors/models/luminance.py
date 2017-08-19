from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel


class Luminance(HabitatModel):

    location = models.ForeignKey(
        verbose_name=_('Sensor Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.PositiveSmallIntegerField(
        verbose_name=_('Luminance'),
        help_text=_('lumen'),
        default=None)

    def __str__(self):
        return f'[{self.date} {self.time}] (location: {self.location}) {self.value} lumen'

    class Meta:
        verbose_name = _('Luminance Measurement')
        verbose_name_plural = _('Luminance')
