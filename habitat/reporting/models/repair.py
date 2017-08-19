from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from habitat._common.models import HabitatModel
from habitat._common.models import MissionDateTime
from habitat._common.models import ReporterAstronaut


class Repair(HabitatModel, MissionDateTime, ReporterAstronaut):
    SIZE_CHOICES = [
        ('small', _('Small')),
        ('medium', _('Medium')),
        ('huge', _('Huge'))]

    STATUS_CHOICES = [
        ('broken', _('Broken')),
        ('fixed', _('Fixed')),
        ('destroyed', _('Permanently Destroyed'))]

    size = models.CharField(verbose_name=_('Problem Size'), max_length=30, choices=SIZE_CHOICES, default=None)
    status = models.CharField(verbose_name=_('Current Status'), max_length=30, choices=STATUS_CHOICES, default=None)

    location = models.ForeignKey(verbose_name=_('Location'), to='building.Module', limit_choices_to={'status': 'nominal'}, default=1)
    object = models.ForeignKey(verbose_name=_('Object'), to='inventory.Item', help_text=_('Leave empty, if object is not on the list'), null=True, blank=True, default=None)
    what = models.CharField(verbose_name=_('What'), max_length=255, default=None)

    start = models.DateTimeField(verbose_name=_('Start'), null=True, blank=True, default=now)
    end = models.DateTimeField(verbose_name=_('End'), help_text=_('Leave empty if problem persists.'), null=True, blank=True, default=None)
    duration = models.DurationField(verbose_name=_('Duration'), null=True, blank=True, default=None)

    description = models.TextField(verbose_name=_('Description'), null=True, blank=True, default=None)
    solution = models.TextField(verbose_name=_('Solution'), null=True, blank=True, default=None)

    def clean(self):
        if self.end and self.start > self.end:
            raise forms.ValidationError({'end': 'End date need to be later than start date.'})

        if self.end and self.start:
            self.duration = self.end - self.start

    def __str__(self):
        return f'[{self.start:%Y-%m-%d}] ({self.status}) {self.what}'

    class Meta:
        verbose_name = _('Repair Log')
        verbose_name_plural = _('Repair')
