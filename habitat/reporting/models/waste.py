from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Waste(HabitatModel, MissionDateTime, ReporterAstronaut):
    TYPE_REGULAR = 'regular'
    TYPE_BIOHAZARD = 'biohazard'
    TYPE_CHEMICAL = 'chemical'
    TYPE_MEDICAL = 'medical'

    TYPE_CHOICES = [
        (TYPE_REGULAR, _('Regular')),
        (TYPE_BIOHAZARD, _('Biohazard')),
        (TYPE_CHEMICAL, _('Chemical')),
        (TYPE_MEDICAL, _('Medical')),
    ]

    type = models.CharField(
        verbose_name=_('Waste'),
        max_length=30,
        choices=TYPE_CHOICES,
        default=TYPE_REGULAR)

    weight = models.DecimalField(
        verbose_name=_('Weight'),
        help_text=_('kg'),
        max_digits=4,
        decimal_places=2)

    def __str__(self):
        return f'[{self.date}] {self.weight}kg'

    class Meta:
        verbose_name = _('Waste')
        verbose_name_plural = _('Waste')
