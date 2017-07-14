from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class Observation(models.Model):
    experiment = models.ForeignKey(
        verbose_name=_('Experiment'),
        to='biolab.experiment')

    datetime = models.DateTimeField(
        verbose_name=_('Observation date'),
        default=now)

    notes = models.TextField(
        verbose_name=_('Notes'),
        default=None,
        blank=True,
        null=True)

    image = models.ImageField(
        verbose_name=_('Image'),
        default=None,
        blank=True,
        null=True)

    def __str__(self):
        return f'[{self.datetime:%Y-%m-%d %H:%M}] {self.experiment} {self.notes:.30}'

    class Meta:
        ordering = ['-datetime']
        verbose_name = _('Observation')
        verbose_name_plural = _('Observations')

    class Admin(admin.ModelAdmin):
        list_display = ['datetime', 'experiment', 'image']
        search_fields = ['=experiment', '^datetime', 'notes']


class ObservationInline(admin.TabularInline):
    model = Observation
    extra = 1


class Experiment(models.Model):
    CULTIVATION_METHODS = [
        ('soil', _('Soil')),
        ('underwater', _('Underwater')),
        ('artificial', _('Artificial')),
        ('hydroponics', _('Hydroponics')),
        ('aeroponics', _('Aeroponics')),
        ('mixed', _('Mixed')),
        ('other', _('Other'))]

    plant = models.ForeignKey(
        verbose_name=_('Plant'),
        to='biolab.Plant')

    cultivation_method = models.CharField(
        verbose_name=_('Cultivation method'),
        choices=CULTIVATION_METHODS,
        default=None,
        max_length=30)

    planted_date = models.DateTimeField(
        verbose_name=_('Date Planted'),
        default=now)

    image = models.ImageField(
        verbose_name=_('Image'),
        default=None,
        blank=True,
        null=True)

    def __str__(self):
        return f'[{self.planted_date:%Y-%m-%d}] {self.plant} {self.cultivation_method}'

    class Meta:
        ordering = ['-planted_date']
        verbose_name = _('Experiment')
        verbose_name_plural = _('Experiments')

    class Admin(admin.ModelAdmin):
        inlines = [ObservationInline]
        list_display = ['planted_date', 'plant', 'planted_date']
        list_filter = ['cultivation_method']
        search_fields = ['=experiment', '^planted_date', 'plant']
