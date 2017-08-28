from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime


class Pressure(HabitatModel, MissionDateTime):

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.DecimalField(
        verbose_name=_('Pressure'),
        help_text=_('hPa'),
        max_digits=6,
        decimal_places=2,
        default=None,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(2000)])

    def __str__(self):
        return f'[{self.date} {self.time}] (location: {self.location}) {self.value} mmHg'

    class Meta:
        verbose_name = _('Pressure Measurement')
        verbose_name_plural = _('Pressure')
