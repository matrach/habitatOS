from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class TechnicalWater(HabitatModel, MissionDateTime, ReporterAstronaut):
    location = models.ForeignKey(verbose_name=_('Usage Location'), to='building.Module', null=True, blank=True, default=None)
    volume = models.DecimalField(verbose_name=_('Volume'), help_text=_('liters'), max_digits=5, decimal_places=2, default=None, validators=[MinValueValidator(0), MaxValueValidator(9.99)])
    usage_description = models.TextField(verbose_name=_('Usage Description'), null=True, blank=True, default=None)

    def __str__(self):
        return f'[{self.date} {self.time}] {self.reporter} {self.volume}l'

    class Meta:
        verbose_name = _('Technical Water Usage')
        verbose_name_plural = _('Technical Water')
