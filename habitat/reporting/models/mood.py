from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from habitat._common.models import HabitatModel
from habitat._common.models import ReportAstronaut


class Mood(HabitatModel, ReportAstronaut):
    MOOD_CHOICES = [
        ('very-high', _('Very High')),
        ('high', _('High')),
        ('normal', _('Normal')),
        ('low', _('Low')),
        ('very-low', _('Very Low'))]

    QUALITY_CHOICES = [
        ('very-good', _('Very Good')),
        ('good', _('Good')),
        ('average', _('Average')),
        ('bad', _('Bad')),
        ('very-bad', _('Very Bad'))]

    day = models.DateField(verbose_name=_('Report About Day'), default=now)
    stress = models.CharField(verbose_name=_('Stress'), max_length=30, choices=MOOD_CHOICES, default=None)
    mood = models.CharField(verbose_name=_('Mood'), max_length=30, choices=MOOD_CHOICES, default=None)
    day_quality = models.CharField(verbose_name=_('Day Quality'), max_length=30, choices=QUALITY_CHOICES, default=None)
    productivity = models.CharField(verbose_name=_('Productivity'), max_length=30, choices=MOOD_CHOICES, default=None)
    remarks = models.TextField(verbose_name=_('Remarks'), blank=True, default=None)

    def __str__(self):
        return f'[{self.day:%Y-%m-%d}] {self.reporter}'

    class Meta:
        verbose_name = _('Mood Report')
        verbose_name_plural = _('Mood')
