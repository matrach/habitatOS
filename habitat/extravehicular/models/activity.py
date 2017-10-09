from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDate


class Activity(HabitatModel, MissionDate):

    airlock_enter = models.TimeField(
        verbose_name=_('Airlock Enter'),
        blank=True,
        null=True,
        default=None)

    eva_start = models.TimeField(
        verbose_name=_('EVA Start'),
        blank=True,
        null=True,
        default=None)

    eva_end = models.TimeField(
        verbose_name=_('EVA End'),
        blank=True,
        null=True,
        default=None)

    airlock_exit = models.TimeField(
        verbose_name=_('Airlock Exit'),
        blank=True,
        null=True,
        default=None)

    location = models.ForeignKey(
        verbose_name=_('Location'),
        to='extravehicular.Location',
        help_text=_('Where the EVA took place'),
        default=None)

    objectives = models.TextField(
        verbose_name=_('Objectives'))

    tools = models.ManyToManyField(
        verbose_name=_('Tools'),
        to='inventory.Item',
        blank=True,
        default=None)

    contingencies = models.ManyToManyField(
        verbose_name=_('Contingencies'),
        to='extravehicular.Contingency',
        blank=True,
        default=None)

    remarks = models.TextField(
        verbose_name=_('Remarks'),
        blank=True,
        null=True,
        default=None)

    def __str__(self):
        return f'[{self.date}] (location: {self.location}) {self.objectives:.30}'

    class Meta:
        verbose_name = _('Extra-Vehicular Activity')
        verbose_name_plural = _('Extra-Vehicular Activities')
