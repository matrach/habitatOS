from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.contrib import admin


class Sleep(models.Model):
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

    location = models.CharField(
        verbose_name=_('Location'),
        max_length=255,
        default=None,
        blank=True,
        null=True)

    quality = models.CharField(
        verbose_name=_('Quality'),
        max_length=30,
        choices=QUALITY,
        default=None,
        blank=True,
        null=True)

    datetime_start = models.DateTimeField(
        verbose_name=_('Start'),
        default=now)

    datetime_end = models.DateTimeField(
        verbose_name=_('End'),
        default=None,
        blank=True,
        null=True)

    duration = models.DurationField(
        verbose_name=_('Duration'),
        default=None,
        blank=True,
        null=True)

    def save(self, **kwargs):
        if self.datetime_end:
            self.duration = self.datetime_end - self.datetime_start
            return super().save(**kwargs)

    def __str__(self):
        return f'[{self.datetime_start:%Y-%m-%d %H:%M}-{self.datetime_end:%Y-%m-%d %H:%M}] {self.astronaut} Quality: {self.quality}, Location: {self.location}'

    class Meta:
        ordering = ['-datetime_start']
        verbose_name = _('Sleep Log')
        verbose_name_plural = _('Sleep Logbook')

    class Admin(admin.ModelAdmin):
        list_display = ['astronaut', 'quality', 'location', 'duration', 'datetime_start', 'datetime_end']
        list_filter = ['astronaut', 'quality']
        readonly_fields = ['duration']
