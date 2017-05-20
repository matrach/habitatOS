from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib import admin

"""
Sleep 1 (quality)
Sleep 1 (start)
Sleep 1 (end)
Sleep 1 (duration)
Sleep 1 (location)
Sleep 2 (start)
Sleep 2 (end)
Sleep 2 (duration)
Sleep 2 (quality)
Sleep 2 (location)
Sleep Total (duration)
"""


class Sleep(models.Model):
    QUALITY = [
        ('very bad', _('Very Bad')),
        ('bad', _('Bad')),
        ('average', _('Average')),
        ('good', _('Good')),
        ('very good', _('Very Good')),
    ]

    astronaut = models.ForeignKey(
        to='auth.User',
        limit_choices_to={'groups__name': 'Astronauts'})

    datetime_start = models.DateTimeField(
        verbose_name=_('Start'),
        default=now)

    datetime_end = models.DateTimeField(
        verbose_name=_('End'),
        default=now,
        blank=True,
        null=True)

    quality = models.CharField(
        verbose_name=_('Quality'),
        default='average',
        max_length=30,
        choices=QUALITY)

    def __str__(self):
        return f'[{self.datetime_start}] {self.astronaut} {self.quality}'

    class Meta:
        ordering = ['-datetime_start']

    class Admin(admin.ModelAdmin):
        list_display = ['datetime_start', 'datetime_end', 'astronaut', 'quality']
