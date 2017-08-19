from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Disease(HabitatModel, MissionDateTime, ReporterAstronaut):

    datetime_start = models.DateTimeField(
        verbose_name=_('Start Datetime'),
        default=now)

    datetime_end = models.DateTimeField(
        verbose_name=_('End Datetime'),
        default=None,
        blank=False,
        null=False)

    icd10 = models.CharField(
        verbose_name=_('ICD-10'),
        max_length=50,
        default=None)

    symptoms = models.TextField(
        verbose_name=_('Sympthoms'),
        default=None,
        blank=False,
        null=False)

    def __str__(self):
        return f'[{self.date} {self.time}] {self.reporter} ICD-10: {self.icd10}, Sympthoms: {self.symptoms:.30}'

    class Meta:
        verbose_name = _('Disease')
        verbose_name_plural = _('Disease')
