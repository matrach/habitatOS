from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime


class Humidity(HabitatModel, MissionDateTime):

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.DecimalField(
        verbose_name=_('Humidity'),
        help_text=_('%'),
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])

    def __str__(self):
        return f'[{self.date} {self.time}] (location: {self.location}) {self.value}%'

    class Meta:
        verbose_name = _('Humidity Measurement')
        verbose_name_plural = _('Humidity')
