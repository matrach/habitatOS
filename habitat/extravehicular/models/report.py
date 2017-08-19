from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Report(HabitatModel, MissionDateTime, ReporterAstronaut):

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='extravehicular.Location',
        null=True,
        blank=True,
        default=None)

    start = models.TimeField(
        verbose_name=_('Start'),
        blank=True,
        null=True,
        default=True)

    end = models.TimeField(
        verbose_name=_('End'),
        blank=True,
        null=True,
        default=True)

    objectives = models.TextField(
        verbose_name=_('Contingencies'))

    description = models.TextField(
        verbose_name=_('Description'))

    contingencies = models.TextField(
        verbose_name=_('Contingencies'))

    def __str__(self):
        return f'[{self.date}] (location: {self.location}) {self.objectives:.30}'

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')
