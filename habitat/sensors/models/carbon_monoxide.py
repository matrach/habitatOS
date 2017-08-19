from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from habitat._common.models import HabitatModel


class CarbonMonoxide(HabitatModel):

    location = models.ForeignKey(
        verbose_name=_('Sensor Location'),
        to='building.Module',
        null=True,
        blank=True,
        default=None)

    value = models.DecimalField(
        verbose_name=_('Concentration'),
        help_text=_('%'),
        max_digits=5,
        decimal_places=3,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)])

    def __str__(self):
        return f'[{self.datetime}] (location: {self.location}) {self.value}%'

    class Meta:
        verbose_name = _('Carbon Monoxide Concentration Measurement')
        verbose_name_plural = _('Carbon Monoxide')
