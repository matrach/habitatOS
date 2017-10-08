from django.db import models
from django.utils.translation import ugettext_lazy as _
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Mood(HabitatModel, MissionDateTime, ReporterAstronaut):

    stress = models.TextField(verbose_name=_('Right now are you stressed...'))
    stress_remarks = models.TextField(verbose_name=_('Because...'), null=True, blank=True, default=None)

    mood = models.TextField(verbose_name=_('Right now I feel...'))
    mood_remarks = models.TextField(verbose_name=_('Because...'), null=True, blank=True, default=None)

    day_quality = models.TextField(verbose_name=_('During the day I felt...'))
    day_quality_remarks = models.TextField(verbose_name=_('Because...'), null=True, blank=True, default=None)

    productivity = models.TextField(verbose_name=_('My Productivity was...'))
    productivity_remarks = models.TextField(verbose_name=_('Because...'), null=True, blank=True, default=None)

    positives = models.TextField(verbose_name=_('Please name positive moments you have experienced today'))
    negatives = models.TextField(verbose_name=_('Please name negative moments you have experienced today'))

    def __str__(self):
        return f'[{self.date}] {self.reporter}'

    class Meta:
        verbose_name = _('Mood Report')
        verbose_name_plural = _('Mood')
