from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class DrinkingWater(HabitatModel, MissionDateTime, ReporterAstronaut):
    volume = models.DecimalField(verbose_name=_('Volume'), help_text=_('liters'), max_digits=3, decimal_places=2, default=None, validators=[MinValueValidator(0), MaxValueValidator(9.99)])

    def __str__(self):
        return f'[{self.date} {self.time}] {self.reporter} {self.volume}l'

    class Meta:
        verbose_name = _('Drinking Water Usage')
        verbose_name_plural = _('Drinking Water')
