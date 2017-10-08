from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Daily(HabitatModel, MissionDateTime, ReporterAstronaut):
    remarks = models.TextField(verbose_name=_('Remarks'))

    def __str__(self):
        return f'[{self.date}] {self.reporter}'

    class Meta:
        verbose_name = _('Daily Report')
        verbose_name_plural = _('Daily Reports')
