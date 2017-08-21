from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDate


class Activity(HabitatModel, MissionDate):

    start = models.TimeField(
        verbose_name=_('Start'),
        blank=True,
        null=True)

    end = models.TimeField(
        verbose_name=_('End'),
        blank=True,
        null=True)

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='extravehicular.Location',
        default=None)

    objectives = models.TextField(
        verbose_name=_('Objectives'))

    tools = models.TextField(
        verbose_name=_('Tools'),
        null=True,
        blank=True,
        default=None)

    contingencies = models.ManyToManyField(
        verbose_name=_('Contingencies'),
        to='extravehicular.Contingency',
        blank=True,
        default=None)

    def __str__(self):
        return f'[{self.date}] (location: {self.location}) {self.objectives:.30}'

    class Meta:
        verbose_name = _('Extra-Vehicular Activity')
        verbose_name_plural = _('Extra-Vehicular Activities')
