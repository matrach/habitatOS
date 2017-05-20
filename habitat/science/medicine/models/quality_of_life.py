from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib import admin


class QualityOfLife(models.Model):
    QUALITY = [
        ('very bad', _('Very Bad')),
        ('bad', _('Bad')),
        ('average', _('Average')),
        ('good', _('Good')),
        ('very good', _('Very Good'))]

    astronaut = models.ForeignKey(
        verbose_name=_('Astronaut'),
        to='auth.User',
        limit_choices_to={'groups__name': 'Astronauts'})

    datetime = models.DateTimeField(
        verbose_name=_('Datetime'),
        default=now)

    morning_stress = models.CharField(
        verbose_name=_('Morning Stress'),
        max_length=30,
        choices=QUALITY,
        default=None,
        blank=True,
        null=True)

    morning_mood = models.CharField(
        verbose_name=_('Morning Mood'),
        max_length=30,
        choices=QUALITY,
        default=None,
        blank=True,
        null=True)

    space_work = models.CharField(
        verbose_name=_('Space Work'),
        max_length=30,
        choices=QUALITY,
        default=None,
        blank=True,
        null=True)

    day_quality = models.CharField(
        verbose_name=_('Space Work'),
        max_length=30,
        choices=QUALITY,
        default=None,
        blank=True,
        null=True)

    productivity = models.CharField(
        verbose_name=_('Productivity'),
        max_length=30,
        choices=QUALITY,
        default=None,
        blank=True,
        null=True)

    evening_stress = models.CharField(
        verbose_name=_('Evening Stress'),
        max_length=30,
        choices=QUALITY,
        default=None,
        blank=True,
        null=True)

    evening_mood = models.CharField(
        verbose_name=_('Evening Mood'),
        max_length=30,
        choices=QUALITY,
        default=None,
        blank=True,
        null=True)

    day_summary = models.TextField(
        verbose_name=_('Day Summary'),
        default=None,
        blank=True,
        null=True)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] {self.astronaut}'

    class Meta:
        ordering = ['-datetime']

    class Admin(admin.ModelAdmin):
        list_display = ['datetime', 'astronaut']
        list_filter = ['astronaut']
