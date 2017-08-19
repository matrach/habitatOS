from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Temperature(HabitatModel, MissionDateTime, ReporterAstronaut):

    temperature = models.DecimalField(
        verbose_name=_('Temperature'),
        help_text=_('Celsius'),
        max_digits=3,
        decimal_places=1,
        default=None,
        validators=[
            MaxValueValidator(42),
            MinValueValidator(30)])

    def __str__(self):
        return f'[{self.date} {self.time}] {self.reporter} Temp: {self.temperature}'

    class Meta:
        verbose_name = _('Temperature')
        verbose_name_plural = _('Temperature')
