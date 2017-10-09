from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Daily(HabitatModel, MissionDateTime, ReporterAstronaut):
    done = models.TextField(verbose_name=_('Scheduled and Done Activities'), blank=True, null=True, default=True)
    unfinished = models.TextField(verbose_name=_('Problems or Unfinished Activities'), blank=True, null=True, default=True)
    unsheduled = models.TextField(verbose_name=_('Additional Activities'), blank=True, null=True, default=True)
    remarks = models.TextField(verbose_name=_('Additional Remarks'), blank=True, null=True, default=True)

    def __str__(self):
        return f'[{self.date}] {self.reporter}'

    class Meta:
        verbose_name = _('Daily Report')
        verbose_name_plural = _('Daily Reports')
