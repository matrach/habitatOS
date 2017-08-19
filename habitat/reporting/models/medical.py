from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDate
from habitat._common.models import ReporterAstronaut


class Medical(HabitatModel, MissionDate, ReporterAstronaut):
    drugs_and_supplements = models.TextField(
        verbose_name=_('Remarks'),
        null=True,
        blank=True,
        default=None)

    medical_condition = models.TextField(
        verbose_name=_('Medical Condition'),
        null=True,
        blank=True,
        default=None)

    food = models.TextField(
        verbose_name=_('Food'),
        null=True,
        blank=True,
        default=None)

    EVA = models.TextField(
        verbose_name=_('EVA'),
        null=True,
        blank=True,
        default=None)

    medical_experiment = models.TextField(
        verbose_name=_('Medical Experiment'),
        null=True,
        blank=True,
        default=None)

    mood_and_morale = models.TextField(
        verbose_name=_('Mood and Morale'),
        null=True,
        blank=True,
        default=None)

    remarks = models.TextField(
        verbose_name=_('Remarks'),
        null=True,
        blank=True,
        default=None)

    def __str__(self):
        return f'[{self.date}] {self.reporter}'

    class Meta:
        verbose_name = _('Medical Report')
        verbose_name_plural = _('Medical')
